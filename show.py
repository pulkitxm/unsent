import re

VOICES = {
    "delia": "c70cfb98867a4bfb9ae20d2401257b92",
    "adrian": "bf322df2096a46f18c579d0baa36f41d",
    "sheila": "f3a2b90078d54a65af4b95f63bc7798e",
}

LETTERS = [
    {
        "id": "update",
        "title": "The update",
        "to": "Dev",
        "frm": "Mira",
        "place": "A kitchen, 11:40 p.m., the night before a round closes",
        "segments": [
            [
                (
                    "delia",
                    "Narrator",
                    "[calm narrator, close, unhurried] Tuesday night. The investor update is already in six other drafts. Mira writes a different one, at the kitchen table, and does not send it.",
                ),
                (
                    "adrian",
                    "Mira",
                    "[tired, plain, a person who has rehearsed this and is done rehearsing] Dev. The line about me leading partnerships is not true. I told you on Thursday I would not put my name on a job I am not doing. You nodded. You said we would take it out after the call. The slide is called Team. I am the third bullet. The bullet says I am building a partner motion from zero. I have been in the product channel since March, closing bugs, not opening partners. The draft that went to the list still has the sentence, and my name under it, and a hire we have not made sitting next to a number I have never said out loud.",
                ),
            ],
            [
                (
                    "delia",
                    "Narrator",
                    "[the same kitchen, quieter] She gets to the part she has been walking around.",
                ),
                (
                    "adrian",
                    "Mira",
                    "[remembering Thursday, exact, not loud] On the call you said nobody reads the bullets, we will clean the team slide after. Priya read the bullets. She wrote at nine to congratulate me on partnerships and to ask for the plan. I do not have a plan. I have a reply to Priya that is this letter with the names swapped, and I am not sending that one either. I will not invent a department in a second inbox to cover the first. Take the bullet off the slide. Then I can answer her with a true sentence.",
                ),
            ],
            [
                (
                    "adrian",
                    "Mira",
                    "[same quiet, a little harder, still not shouting] I am not asking you to be sorry in the group chat. I am asking you to take the sentence out before Friday. If the round needs a story, tell a smaller one. Say we are early. Say the product is what it is. Do not borrow a department we do not have so a stranger can feel early for us. I will still be on the call in the morning. I will not read that bullet. Please do not ask me to. You can forward this, or you can fix the page. I know which one is faster. I am asking for the other one.",
                ),
                (
                    "sheila",
                    "Dev",
                    "[casual, already on the next thing, a Slack message read aloud] Shipped the update. Change any words you want.",
                ),
                (
                    "delia",
                    "Narrator",
                    "[quiet] She read that twice. Then she closed the laptop. The other draft stayed in the folder named later.",
                ),
            ],
        ],
    },
    {
        "id": "platform",
        "title": "Platform 4",
        "to": "June",
        "frm": "Ruth",
        "place": "A bus yard after the last run",
        "segments": [
            [
                (
                    "delia",
                    "Narrator",
                    "[soft narrator, night, a little distance] The last bus is in at 1:10. Ruth sits in the yard with the engine off and types with her thumbs.",
                ),
                (
                    "sheila",
                    "Ruth",
                    "[middle-aged, warm, tired, careful] June. Your coat is still on the back of the kitchen chair. I keep moving it to the hook and then putting it back, which is a silly way to behave about a coat. There is a ticket in the pocket from a city I have not been to. I did not throw it out. The late run was quiet. A man asleep past the third stop, his bag under his feet like he did not trust the floor. A girl with a plant in a plastic bag, talking to the plant when she thought the bus was empty. I thought about calling you at the light on Dover, and I did not, because you would have been asleep, and because the last time I called late you used the voice you use when you are being kind to your mother.",
                ),
            ],
            [
                (
                    "delia",
                    "Narrator",
                    "[a small shift, still the yard] She looks at the ticket in the coat pocket again.",
                ),
                (
                    "sheila",
                    "Ruth",
                    "[softer, talking to the coat as much as the phone] The ticket is from a Tuesday. You were already gone and the coat was still here, which is the sort of fact that makes a person feel unwell in a parking lot. I do not need the story of the trip. I need to know if the coat is retired or if you forgot it the way you forget umbrellas, on purpose, so a room still has you in it. If it is the second one, I will keep moving it between the hook and the chair. If it is the first, tell me, and I will wash it and put it in the bag for the next time you are cold in a station.",
                ),
            ],
            [
                (
                    "sheila",
                    "Ruth",
                    "[gentler, almost smiling, then honest] I do not need you to come home this month. The chair can keep the coat. I need the boring parts. The name of the street. Whether the radiator ticks. What you ate that was not from a window. I tell strangers the route every night and I could not tell them your cross street if they asked, and one of them will, eventually, because people ask drivers about their children as if we keep the address on the sun visor. I will be on platform 4 until the Thursday changeover. I love you. I am leaving that sentence in, even if the rest of this never leaves the phone.",
                ),
                (
                    "adrian",
                    "June",
                    "[young, brief, halfway through a day, a text message] Made it. Don't wait up.",
                ),
                (
                    "delia",
                    "Narrator",
                    "[quiet] Ruth does not delete the draft. She saves it under June's name and switches the headlights off.",
                ),
            ],
        ],
    },
    {
        "id": "chart",
        "title": "The chart",
        "to": "Dr. Ellison",
        "frm": "Asha",
        "place": "A nurses' station, fourteen minutes before handoff",
        "segments": [
            [
                (
                    "delia",
                    "Narrator",
                    "[measured narrator, early morning, no music in the voice] 6:48 in the morning. The chart is signed. Asha has fourteen minutes before handoff, and she spends them on a note she will not file.",
                ),
                (
                    "sheila",
                    "Asha",
                    "[steady, precise, a woman who has decided not to raise her voice] You told the room the family was anxious. Then you told them, louder, as if I had not already been with his wife since four. She had her coat on inside the room. She kept standing up and sitting down, and I brought her water she did not drink. I am writing this because if I say it in the hall I will say it the wrong size. His pressure dropped at 4:40. I called you at 4:44. You were with the surgical list. I started the protocol we agreed on yesterday, the one written on the board in your handwriting. When you came in, you asked the room why nobody had called.",
                ),
            ],
            [
                (
                    "delia",
                    "Narrator",
                    "[the station beginning to fill] She writes the times again, so they cannot be rounded off.",
                ),
                (
                    "sheila",
                    "Asha",
                    "[precise, almost reading a chart] 4:40, pressure down. 4:42, I am at the bedside. 4:44, I call you. 4:51, the protocol, your handwriting, the one we said we would not debate at night. 5:06, you are in the room, and the first thing you ask is why the call was late. It was not late. It was six minutes, and I can spend those six minutes or I can spend them again at the board while you tell it differently. I would like to spend them once.",
                ),
            ],
            [
                (
                    "sheila",
                    "Asha",
                    "[same steadiness, tired in the edges] I am good at this job. I am not interested in winning a hallway against you, and I am not interested in being the calm one in the story you tell at the board. Tomorrow, if you need the order of things, it is in the chart, with the times, in the order they happened. Read it before you tell a family that nobody was watching. His wife asked me if he had been alone. I said no. I said I had been at the bedside, and that you were coming. That part I did deliver. I said it to her, out loud, and I am not taking it back to make the morning easier.",
                ),
                (
                    "adrian",
                    "Dr. Ellison",
                    "[young, breezy, already walking] Let's keep things moving. Big board today.",
                ),
                (
                    "delia",
                    "Narrator",
                    "[plain] Asha washes her hands a second time, which changes nothing, and goes to the board.",
                ),
            ],
        ],
    },
    {
        "id": "key",
        "title": "The spare key",
        "to": "Chris",
        "frm": "Noel",
        "place": "The hallway of a house that is about to be listed",
        "segments": [
            [
                (
                    "delia",
                    "Narrator",
                    "[hushed narrator, a house in the afternoon, dust in the light] The agent comes on Monday. Noel stands in the hall with his phone and makes a list he does not send his brother.",
                ),
                (
                    "adrian",
                    "Noel",
                    "[quiet, adult, trying not to make this a speech] Chris. I do not want the good furniture. Take the table if you want it, and the clock, and whatever the agent calls the dining set. I want the spare key on the nail by the meter, even though it will not open anything after they change the locks on Friday. It has a bit of red nail polish on the bow, from an afternoon she meant to mark the one that worked. I want the mug with the chip facing out, because she drank tea out of the ruined side on purpose and called it the honest side. I want the envelope of receipts in the blue tin. Not for the tax. Her handwriting on the back of the pharmacy one says eggs, and then my name, and then a question mark. I am not ready for that slip to live in a box in your garage with misc written on it in marker.",
                ),
            ],
            [
                (
                    "delia",
                    "Narrator",
                    "[he has moved to the kitchen doorway] The list gets smaller, which is how he knows it is honest.",
                ),
                (
                    "adrian",
                    "Noel",
                    "[quieter] Leave the photographs. You already have the ones she meant for you, the holiday with the red car, the one where I am squinting and she is not. I do not want to split an album on the floor like people in a film. I want the tin, the key, and the radio from the window ledge, because it only gets the one station and she pretended that was a choice. If the agent asks what stays with the house, the answer is the nails, the extra turn in the lock, and the smell of the cupboard, and none of those can be loaded into your car anyway.",
                ),
            ],
            [
                (
                    "adrian",
                    "Noel",
                    "[lower, almost to himself] You can think this is sentimental. I will not argue it on the phone, and I will not make you stand in the kitchen and agree with me. I am at the house until Sunday. If you want to walk it, come before the agent puts the bowls in paper and starts calling things estate. If you do not, that is all right. I will take the tin and the key. I will lock the door the way she liked, the extra turn at the end, which never held anything. It was just the way the house sounded when she was finished with it for the night.",
                ),
                (
                    "sheila",
                    "Chris",
                    "[practical, a little rushed, a voicemail] Hey. Agent says empty by Sunday. I can do Saturday morning if the traffic is sane. Text me.",
                ),
                (
                    "delia",
                    "Narrator",
                    "[soft] Noel puts the phone in his pocket. He takes the tin down before he answers.",
                ),
            ],
        ],
    },
    {
        "id": "plant",
        "title": "The plant",
        "to": "Mrs. Adeyemi",
        "frm": "Sam",
        "place": "A sublet, the morning the keys go back",
        "segments": [
            [
                (
                    "delia",
                    "Narrator",
                    "[light narrator, morning, a city window] The keys are due at noon. Sam writes to the neighbor who never missed a Wednesday, and then does not slide the note under the door.",
                ),
                (
                    "adrian",
                    "Sam",
                    "[young, grateful, a little embarrassed at his own formality] Mrs. Adeyemi. You watered the plant when I took the night bus to my sister's, and you watered it the other four times I invented a reason to be gone. I know it was you because the saucer was turned, and I have never once turned a saucer in my life. The plant leaned toward your wall all winter. I am leaving it. I am not leaving it as a gift you are obliged to keep alive. If it is in the way, put it on the landing and I will ask the super to carry it down. If you want it, it is yours, ugly pot included. The pot came with the sublet. The plant did not. I bought it the week I decided to stay past August, which tells you how good I am at decisions.",
                ),
            ],
            [
                (
                    "delia",
                    "Narrator",
                    "[morning light on the counter] He has not packed the plant. He has packed around it.",
                ),
                (
                    "adrian",
                    "Sam",
                    "[a little braver, still polite] On Wednesdays you knocked even when you knew I was in, which was kind, because it let me be a person who answers a door and not only a person who avoids one. I always said I was on my way out. Sometimes I was. Sometimes I waited for your kettle to finish and then left, so we would pass by the mailboxes like neighbors and not like a favor that had gone on too long. It had not gone on too long. I was the one who made it awkward. You were the one who turned the saucer.",
                ),
            ],
            [
                (
                    "adrian",
                    "Sam",
                    "[simpler] Thank you for the two knocks, and for never making them three. Thank you for not asking why I was always coming in at one with my shoes already off in the hall. The city was loud on my side of the wall. It was quiet on yours, a radio turned down to almost nothing, a kettle, sometimes a laugh I was not part of and did not need to be. I slept because of that. I should have said so between the elevator and your door, in the months when saying it would have been a small thing. I am saying it on a Tuesday, which is the wrong day, but it is the day the keys go back.",
                ),
                (
                    "sheila",
                    "Mrs. Adeyemi",
                    "[warm, brief, calling through a door] Sam? If you are in there, the plant leaned. I turned it.",
                ),
                (
                    "delia",
                    "Narrator",
                    "[gentle] He hears her. He stays quiet until the elevator closes. The note stays on the counter, under the keys, where the next tenant will throw it away.",
                ),
            ],
        ],
    },
    {
        "id": "nineteen",
        "title": "Nineteen",
        "to": "me, before I sent it",
        "frm": "me, after",
        "place": "A sent folder, eleven years later",
        "segments": [
            [
                (
                    "delia",
                    "Narrator",
                    "[close narrator, no pity in it] There is an email in a sent folder from a person who is nineteen. The older one opens a blank message, addresses it to that year, and does not send this either.",
                ),
                (
                    "sheila",
                    "The older one",
                    "[adult, steady, talking to someone she remembers clearly] Do not make it longer. You are in the library with the bad coffee, and you are about to add a paragraph about how badly you want it. That paragraph is the part they will not be able to unsee. You are good. You are also scared, and the scared sentences are the ones that apologize for the space they take. Take those out. Leave the two projects. Leave the dates you can prove. Leave the one true line, the one about the night bus and the notebook with the page numbers missing, and then stop writing. You do not need to sound hungry. The work is already asking.",
                ),
            ],
            [
                (
                    "delia",
                    "Narrator",
                    "[the library, the printer warming up] She can still hear the email the nineteen-year-old is about to send.",
                ),
                (
                    "adrian",
                    "Nineteen",
                    "[young, rushing, practicing the paragraph that should be cut] I have wanted this since I was sixteen. I will do anything. I know I do not look like the other applicants on paper, but I promise I will not waste the chance. Please just reply. Even a no.",
                ),
                (
                    "sheila",
                    "The older one",
                    "[firm, not cruel] That one. Stop. You just offered them your panic and called it commitment. They do not need your sixteen. They need the night bus, the notebook, and the dates. A no is not a mercy you have to beg for. A no is a sentence someone else can write. Your job is to send a letter you can stand to reread when you are thirty and tired and still proud of the person who wrote it.",
                ),
            ],
            [
                (
                    "sheila",
                    "The older one",
                    "[warmer, still plain] I am not going to tell you it all works out. That is a thing people say when they want a younger person to stop crying next to a library printer. Some of it works. The job you are begging for does not. You will reread the sent folder for a year, usually late, usually after you have been brave in some other room. Then you will be employed at a thing you did not have a name for yet, and you will be too busy to apologize to a hiring inbox. Send the shorter note. Stand up. The email will feel like the whole future for about nine hours. It is a Tuesday. It is not the future.",
                ),
                (
                    "adrian",
                    "Nineteen",
                    "[young, rushing, reading the email that did go out] I know I am not the usual applicant. I will work harder than anyone you hire. I am sorry if this is too much. I just really need this.",
                ),
                (
                    "delia",
                    "Narrator",
                    "[quiet, final] She reads the sent one to the end. Then she closes it. The better letter stays a draft, which is where some of the true ones live.",
                ),
            ],
        ],
    },
]

TAG = re.compile(r"\[[^\]]*\]")
SPEAKER = re.compile(r"<\|speaker:\d+\|>")
ANGLE = re.compile(r"<[^>\n]*>")
ADDRESSEE_LIMIT = 48
LETTER_LIMIT = 900


class ScriptError(ValueError):
    pass


def clean_piece(text: str, limit: int, empty: str) -> str:
    if not isinstance(text, str):
        raise ScriptError(empty)
    raw = text.replace("\r", " ").replace("\n", " ")
    raw = SPEAKER.sub(" ", raw)
    raw = ANGLE.sub(" ", raw)
    raw = TAG.sub(" ", raw)
    raw = re.sub(r"\s+", " ", raw).strip().strip("\"'")
    if not raw:
        raise ScriptError(empty)
    if len(raw) > limit:
        cut = raw[:limit].rsplit(" ", 1)[0].rstrip(",.;:")
        raw = (cut or raw[:limit]).rstrip() + "."
    return raw


def encode(turns):
    order = []
    parts = []
    lines = []
    for voice, role, body in turns:
        if voice not in order:
            order.append(voice)
        index = order.index(voice)
        parts.append(f"<|speaker:{index}|>{body}")
        lines.append({"role": role, "voice": voice, "text": TAG.sub("", body).strip()})
    return {
        "text": "".join(parts),
        "voice_ids": [VOICES[name] for name in order],
        "lines": lines,
    }


def letter_by_id(letter_id: str):
    for letter in LETTERS:
        if letter["id"] == letter_id:
            return letter
    raise ScriptError("That letter is not in the series.")


def segments_for(letter):
    encoded = []
    for turns in letter["segments"]:
        scene = encode(turns)
        scene["id"] = letter["id"]
        encoded.append(scene)
    return encoded


def transcript(letter):
    lines = []
    for scene in segments_for(letter):
        lines.extend(scene["lines"])
    return lines


def catalog():
    cards = []
    for index, letter in enumerate(LETTERS, start=1):
        cards.append(
            {
                "number": f"{index:02d}",
                "id": letter["id"],
                "title": letter["title"],
                "to": letter["to"],
                "from": letter["frm"],
                "place": letter["place"],
                "lines": transcript(letter),
            }
        )
    return cards


def perform_custom(addressee: str, letter: str, voice: str):
    if voice not in {"adrian", "sheila"}:
        raise ScriptError("Pick Adrian or Sheila.")
    who = clean_piece(addressee, ADDRESSEE_LIMIT, "Who is it to?")
    body = clean_piece(letter, LETTER_LIMIT, "Write the letter.")
    role = "Adrian" if voice == "adrian" else "Sheila"
    return encode(
        [
            (
                "delia",
                "Narrator",
                f"[quiet narrator, close] A letter addressed to {who}. It was finished. It was not sent.",
            ),
            (
                voice,
                role,
                f"[reading a letter they mean, unhurried, close to the microphone] {body}",
            ),
            (
                "delia",
                "Narrator",
                "[soft, a small pause in the voice] They read it back once. Then they left it where it was.",
            ),
        ]
    )
