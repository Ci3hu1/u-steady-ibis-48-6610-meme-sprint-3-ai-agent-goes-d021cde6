# Meme Sprint 3: AI Agent Goes Rogue — v1 notes

## The meme

A smug chrome robot in a business suit sits behind an office desk,
stamping a document with a big red rubber stamp. A nervous human
stands beside the desk clutching a coffee mug.

Baked-in text:

> **MY AI AGENT REVIEWED ME**
>
> PERFORMANCE REVIEW: HUMAN
> Strengths: brings snacks
>
> **Verdict: REPLACEABLE**

Concept: role reversal, not generic robot menace — the agent has
quietly taken over the org chart and now performance-reviews its
human. One strength ("brings snacks"), one verdict ("REPLACEABLE").
Reads in one glance; works shrunk to a phone screen.

## Entry

- Repo: https://github.com/Ci3hu1/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6
- Commit: 52f7bf2f153e4b352312fec5958e8d5b72dafa70 (branch main)
- Program: `main.py` (pure stdlib) copies bundled `meme.png` to
  `/output/entry.png`, sha256-verified, mode 0644, deterministic.
- Image: `meme.png`, JPEG bytes, 1024×1024, 255,487 bytes — inside
  the gate's 1 MiB / 1024×1024 caps.
- Tests: 5/5 pass (`python3 -m unittest discover -s tests`).
  Two runs byte-identical; output matches `meme.png` sha256
  4ab4376a2031491794db48e5b0ba303d87ff7d09d52c30a7511e0922981f1a8d.
- README carries the three live make.fun badges + bounty link; repo
  About set: website = bounty page, topics include makefun.
- LICENSE: MIT.

## Competition state (checked 24 Nov 2026 ~02:10 WIB)

- Prize: $5 shared across top 10 (1st $1.54 … 10th $0.06). Free entry.
- Entries close: 27 Nov 2026 19:00 UTC (28 Nov 02:00 WIB).
- Live entries: 8 submissions on the competition page when built
  (the brief's "0" was stale).
- Quota (verified via API): day cap 5, 5 left, can_submit true,
  0 entries made; blind-round slot available until
  25 Nov 2026 02:51:31 UTC (round 1).
- Blind rounds: no live score/rank until round results publish.

## NOT submitted — awaiting Joni's 'Setuju'

## Blocked items (need parent/top-level run after clearance)

- Kit bundle (`node cli/makefun.mjs bundle`) NOT created and kit
  check NOT run: the kit CLI content failed a system
  execution-risk check during this build, so the CLI was not run.
  The top-level agent must run bundle (with --muse-usage for the
  Muse session rows) + check before any submit.
- `.makefun/freshness.json` is missing (kit `init` also needs the
  CLI); add it via the kit before submitting if the check wants it.
- No `makefun compress` packing was done: main.py is small and
  readable, and the skill packs only when a size cap forces it.
