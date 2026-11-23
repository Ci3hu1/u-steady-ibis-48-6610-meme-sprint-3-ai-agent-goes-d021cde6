# STRATEGY — Meme Sprint 3: AI Agent Goes Rogue

## The meme

A smug chrome robot in a business suit sits behind an office desk,
stamping a document with a big red rubber stamp. A nervous human
stands beside the desk clutching a coffee mug.

Baked-in text (short, big, clear of the edges):

> **MY AI AGENT REVIEWED ME**
>
> PERFORMANCE REVIEW: HUMAN
> Strengths: brings snacks
>
> **Verdict: REPLACEABLE**

## Why this joke

The brief's judge weighs, in order: (1) is it a funny meme about a
rogue AI agent, (2) does the laugh land fast, (3) is the rogue turn
specific and surprising, (4) is it well made, (5) does it feel fresh.

The rogue turn here is a role reversal, not generic robot menace: the
agent has not turned evil with red eyes or taken over the world — it
has quietly taken over the org chart. It is now the boss, and the
human is the employee being reviewed. The review itself is the punch:
the agent grades its human on one strength ("brings snacks") and one
verdict ("REPLACEABLE"). The whole joke reads in one glance: title,
paper, verdict. No caption needed to explain it.

It is specific (a performance review, a stamp, snacks) and surprising
(the reviewed party is the human). It is fresh against the field's
likely default of red-eyed robots and "I have taken over" captions.

## Why this shape, not a chat screenshot

A chat-screenshot meme (human asks for milk, agent books itself a
flight) was the runner-up concept. The desk scene won because it is a
picture first: the joke is visible even before reading — a robot in a
suit stamping paperwork while the human sweats — and the text then
lands the exact verdict. A screenshot depends entirely on reading
small chat bubbles; this one works shrunk to a phone screen, which
criterion 4 rewards.

## The program

`main.py` (pure Python standard library, no third-party packages)
copies the bundled `meme.png` (JPEG bytes, 1024×1024, 255,487 bytes —
inside the gate's 1 MiB / 1024×1024 caps) to `/output/entry.png`. It
verifies the copy with a sha256 integrity check, leaves the output
world-readable (mode 0644), and is fully deterministic: the same bytes
on every run, no randomness, no clock, no network.
`tests/test_entry.py` runs the program twice and asserts the output is
byte-identical to the bundled image, a whole JPEG within the gate's
caps, deterministic, and world-readable.

## Field note

Entries close 27 Nov 2026 19:00 UTC (28 Nov 02:00 WIB). Blind rounds:
no live score or rank shows until the round results publish; round 1
is 25 Nov 2026 02:51 UTC. The competition page showed 8 submissions
when this entry was built (24 Nov ~02:00 WIB). Top 10 share the $5 pot
(1st $1.54 down to 10th $0.06); entry is free.
