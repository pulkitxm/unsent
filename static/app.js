const programEl = document.querySelector("#program");
const now = document.querySelector("#now");
const stamp = document.querySelector("#stamp");
const place = document.querySelector("#place");
const titleEl = document.querySelector("#title");
const address = document.querySelector("#address");
const player = document.querySelector("#player");
const scriptEl = document.querySelector("#script");
const download = document.querySelector("#download");
const copyButton = document.querySelector("#copy");
const playAll = document.querySelector("#play-all");
const totalEl = document.querySelector("#total");
const form = document.querySelector("#own");
const statusEl = document.querySelector("#status");

let letters = [];
let index = 0;
let chain = false;
let voice = "adrian";
let objectUrl = null;

function clock(seconds) {
  if (!seconds && seconds !== 0) return "";
  const whole = Math.round(seconds);
  const minutes = Math.floor(whole / 60);
  const remain = String(whole % 60).padStart(2, "0");
  return `${minutes}:${remain}`;
}

function setStatus(text) {
  statusEl.textContent = text || "";
}

function show(letter) {
  stamp.textContent = `Letter ${letter.number}`;
  place.textContent = letter.place;
  titleEl.textContent = letter.title;
  address.textContent = `${letter.from} to ${letter.to}`;
  scriptEl.replaceChildren();
  for (const line of letter.lines) {
    const item = document.createElement("li");
    const role = document.createElement("span");
    role.className = "role";
    role.textContent = line.role;
    const said = document.createElement("span");
    said.textContent = line.text;
    item.append(role, said);
    scriptEl.append(item);
  }
  if (letter.audio) {
    if (objectUrl) {
      URL.revokeObjectURL(objectUrl);
      objectUrl = null;
    }
    player.src = letter.audio;
    download.href = letter.audio;
    download.download = `${letter.id}.mp3`;
    download.hidden = false;
  }
  now.hidden = false;
  for (const button of programEl.querySelectorAll("button")) {
    button.setAttribute("aria-current", String(button.dataset.id === letter.id));
  }
}

function play(nextIndex, continueAfter) {
  const letter = letters[nextIndex];
  if (!letter || !letter.audio) {
    setStatus("This letter has no audio yet.");
    chain = false;
    playAll.textContent = "Play the series";
    return;
  }
  index = nextIndex;
  chain = continueAfter;
  show(letter);
  player.play().catch(() => {});
  playAll.textContent = chain ? "Playing the series" : "Play the series";
}

function renderProgram() {
  programEl.replaceChildren();
  let total = 0;
  letters.forEach((letter, letterIndex) => {
    if (letter.seconds) total += letter.seconds;
    const item = document.createElement("li");
    const button = document.createElement("button");
    button.type = "button";
    button.dataset.id = letter.id;
    const num = document.createElement("span");
    num.className = "num";
    num.textContent = letter.number;
    const name = document.createElement("span");
    const strong = document.createElement("strong");
    strong.textContent = letter.title;
    const meta = document.createElement("span");
    meta.className = "meta";
    meta.textContent = `${letter.from} to ${letter.to}`;
    name.append(strong, meta);
    const time = document.createElement("span");
    time.className = "num";
    time.textContent = clock(letter.seconds);
    button.append(num, name, time);
    button.addEventListener("click", () => play(letterIndex, false));
    item.append(button);
    programEl.append(item);
  });
  totalEl.textContent = total ? `${clock(total)} in all` : "";
  if (letters[0]) show(letters[0]);
}

player.addEventListener("ended", () => {
  if (!chain) return;
  if (index + 1 < letters.length) play(index + 1, true);
  else {
    chain = false;
    playAll.textContent = "Play the series";
  }
});

playAll.addEventListener("click", () => {
  if (chain) {
    chain = false;
    player.pause();
    playAll.textContent = "Play the series";
    return;
  }
  play(0, true);
});

copyButton.addEventListener("click", async () => {
  const letter = letters[index];
  if (!letter) return;
  const post = [
    "a letter that was finished and never sent",
    "",
    `${letter.title}. ${letter.from} to ${letter.to}.`,
    "",
    "https://github.com/pulkitxm/unsent",
  ].join("\n");
  try {
    await navigator.clipboard.writeText(post);
    setStatus("Copied.");
  } catch (error) {
    setStatus("Copy failed.");
  }
});

for (const button of document.querySelectorAll(".voices button")) {
  button.addEventListener("click", () => {
    voice = button.dataset.voice;
    for (const other of document.querySelectorAll(".voices button")) {
      other.setAttribute("aria-pressed", String(other === button));
    }
  });
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const perform = document.querySelector("#perform");
  perform.disabled = true;
  setStatus("The take is being read.");
  chain = false;
  playAll.textContent = "Play the series";
  try {
    const response = await fetch("/api/perform", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        to: document.querySelector("#to").value,
        letter: document.querySelector("#letter").value,
        voice,
      }),
    });
    const payload = await response.json();
    if (!response.ok) {
      setStatus(payload.error || "The take failed.");
      return;
    }
    const bytes = Uint8Array.from(atob(payload.audio_base64), (char) => char.charCodeAt(0));
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    objectUrl = URL.createObjectURL(new Blob([bytes], { type: payload.mime || "audio/mpeg" }));
    const custom = {
      id: "custom",
      number: "00",
      title: `To ${document.querySelector("#to").value.trim()}`,
      from: voice === "sheila" ? "Sheila" : "Adrian",
      to: document.querySelector("#to").value.trim(),
      place: "Just now, and not sent",
      lines: payload.lines,
      audio: objectUrl,
    };
    show(custom);
    player.play().catch(() => {});
    setStatus("");
  } catch (error) {
    setStatus("The take failed.");
  } finally {
    perform.disabled = false;
  }
});

fetch("/api/letters")
  .then((response) => response.json())
  .then((payload) => {
    letters = payload.letters;
    renderProgram();
  })
  .catch(() => {
    setStatus("The series did not load.");
  });
