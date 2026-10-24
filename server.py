#!/usr/bin/env python3
import base64
import json
import os
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from show import ScriptError, catalog, perform_custom

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
AUDIO = ROOT / "audio"
HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "8787"))
FISH_URL = "https://api.fish.audio/v1/tts"


def load_env():
    path = ROOT / ".env"
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def durations():
    path = AUDIO / "manifest.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def letters_payload():
    timing = durations()
    cards = []
    for card in catalog():
        meta = timing.get(card["id"], {})
        file_name = meta.get("file")
        audio = f"/audio/{file_name}" if file_name and (AUDIO / file_name).is_file() else None
        cards.append({**card, "audio": audio, "seconds": meta.get("seconds")})
    return cards


def speak(scene):
    key = os.environ.get("FISH_API_KEY", "").strip()
    if not key:
        raise RuntimeError("Set FISH_API_KEY to perform a new letter. The six in the series already play.")
    payload = json.dumps(
        {
            "text": scene["text"],
            "reference_id": scene["voice_ids"],
            "format": "mp3",
            "mp3_bitrate": 128,
            "latency": "normal",
        }
    ).encode()
    request = urllib.request.Request(
        FISH_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "model": "drama-3",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            audio = response.read()
            mime = response.headers.get("Content-Type", "audio/mpeg")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")[:300]
        raise RuntimeError(f"Fish Audio returned {error.code}. {detail}") from error
    if not audio:
        raise RuntimeError("Fish Audio returned empty audio.")
    return audio, mime.split(";")[0]


class App(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print("%s %s" % (self.command, self.path))

    def _json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _bytes(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _file(self, path: Path, content_type: str):
        if not path.is_file():
            self._json(404, {"error": "Missing."})
            return
        self._bytes(200, path.read_bytes(), content_type)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self._file(STATIC / "index.html", "text/html; charset=utf-8")
            return
        if path == "/api/letters":
            self._json(200, {"letters": letters_payload()})
            return
        if path.startswith("/static/"):
            name = Path(path).name
            target = STATIC / name
            types = {
                ".css": "text/css; charset=utf-8",
                ".js": "text/javascript; charset=utf-8",
                ".svg": "image/svg+xml",
            }
            self._file(target, types.get(target.suffix, "application/octet-stream"))
            return
        if path.startswith("/audio/"):
            name = Path(path).name
            if name.endswith(".mp3"):
                self._file(AUDIO / name, "audio/mpeg")
                return
        self._json(404, {"error": "Missing."})

    def do_POST(self):
        if urlparse(self.path).path != "/api/perform":
            self._json(404, {"error": "Missing."})
            return
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length > 20_000:
            self._json(413, {"error": "That letter is too long for one take."})
            return
        try:
            payload = json.loads(self.rfile.read(length).decode() or "{}")
            scene = perform_custom(
                str(payload.get("to", "")),
                str(payload.get("letter", "")),
                str(payload.get("voice", "adrian")),
            )
            audio, mime = speak(scene)
        except ScriptError as error:
            self._json(400, {"error": str(error)})
            return
        except RuntimeError as error:
            self._json(503, {"error": str(error)})
            return
        except (json.JSONDecodeError, UnicodeDecodeError):
            self._json(400, {"error": "Send the letter as JSON."})
            return
        self._json(
            200,
            {
                "title": "Unsent",
                "lines": scene["lines"],
                "audio_base64": base64.b64encode(audio).decode(),
                "mime": mime,
            },
        )


def main():
    load_env()
    AUDIO.mkdir(exist_ok=True)
    server = ThreadingHTTPServer((HOST, PORT), App)
    print(f"http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
