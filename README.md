# Unsent

Six letters that were finished and never sent, performed as short scenes.

Each one has a narrator, the person who wrote it, and the ordinary message that arrived instead. Play the series from the top, or read along with the transcript. You can also perform a letter of your own.

## Run

```bash
python3 server.py
```

Open http://127.0.0.1:8787

The six letters play with no key. A letter you write needs a [Fish Audio](https://fish.audio/app/) API key:

```bash
export FISH_API_KEY=your_key
python3 server.py
```

Speech is the `drama-3` model. Delia narrates. Adrian and Sheila read. They are public voices on Fish Audio.

```bash
python3 -m unittest
```
