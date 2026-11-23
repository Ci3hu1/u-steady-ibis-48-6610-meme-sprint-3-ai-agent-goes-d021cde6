#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Copies the bundled meme image (meme.png, JPEG bytes) to
/output/entry.png, the file the sealed gate reads.

The joke: the AI agent has flipped the org chart — it sits behind the
desk in a suit, stamping a performance review of its human:
"Strengths: brings snacks. Verdict: REPLACEABLE."

Python 3, standard library only. Deterministic: the output bytes are
exactly the bytes of meme.png shipped in this repository. No network,
no clock, no randomness. Verifies the copy with a sha256 integrity
check and leaves the output world-readable (mode 0644) so the
collector can read it.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "meme.png"

DEFAULT_OUTPUT = "/output/entry.png"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not SRC.is_file():
        print(f"missing source image: {SRC}", file=sys.stderr)
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(SRC, output_path)
    os.chmod(output_path, 0o644)

    src_hash = sha256_of(SRC)
    dest_hash = sha256_of(Path(output_path))
    if src_hash != dest_hash:
        print(
            f"integrity check FAILED: {SRC} sha256 {src_hash} != "
            f"{output_path} sha256 {dest_hash}",
            file=sys.stderr,
        )
        return 1

    size = Path(output_path).stat().st_size
    print(f"wrote {output_path} ({size} bytes, sha256 {dest_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
