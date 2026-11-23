#!/usr/bin/env python3
"""Tests for the Meme Sprint 3 entry.

Pure standard library (unittest). Runs main.py twice and asserts:
- the output file is written and byte-identical to meme.png
- the output is a whole JPEG, at most 1 MiB and at most 1024x1024
  (the sealed gate's caps for /output/entry.png)
- the two runs are byte-identical (deterministic)
- the output is world-readable (mode 0644)
"""

import os
import stat
import struct
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_PY = os.path.join(REPO, "main.py")
MEME_PNG = os.path.join(REPO, "meme.png")

MAX_BYTES = 1_048_576
MAX_DIM = 1024


def run_entry(out_path):
    result = subprocess.run(
        [sys.executable, MAIN_PY, out_path],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


def jpeg_dimensions(path):
    """Return (width, height) of a JPEG by scanning for a SOF marker."""
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG (missing SOI marker)")
    i = 2
    while i < len(data) - 1:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        if marker == 0xDA:  # SOS: image data follows, no more headers
            break
        length = struct.unpack(">H", data[i + 2 : i + 4])[0]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            height, width = struct.unpack(">HH", data[i + 5 : i + 9])
            return width, height
        i += 2 + length
    raise ValueError("no SOF marker found")


class TestMemeEntry(unittest.TestCase):
    def test_source_image_within_gate_caps(self):
        self.assertTrue(os.path.isfile(MEME_PNG))
        size = os.path.getsize(MEME_PNG)
        self.assertLessEqual(size, MAX_BYTES, f"meme.png is {size} bytes")
        width, height = jpeg_dimensions(MEME_PNG)
        self.assertLessEqual(width, MAX_DIM)
        self.assertLessEqual(height, MAX_DIM)
        self.assertEqual((width, height), (1024, 1024))

    def test_program_writes_exact_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.png")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            with open(MEME_PNG, "rb") as f:
                expected = f.read()
            with open(out, "rb") as f:
                actual = f.read()
            self.assertEqual(actual, expected)

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out1 = os.path.join(tmp, "a.png")
            out2 = os.path.join(tmp, "b.png")
            r1 = run_entry(out1)
            r2 = run_entry(out2)
            self.assertEqual(r1.returncode, 0, msg=r1.stderr)
            self.assertEqual(r2.returncode, 0, msg=r2.stderr)
            with open(out1, "rb") as f:
                b1 = f.read()
            with open(out2, "rb") as f:
                b2 = f.read()
            self.assertEqual(b1, b2)

    def test_output_is_world_readable(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.png")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            mode = stat.S_IMODE(os.stat(out).st_mode)
            self.assertEqual(mode, 0o644)

    def test_default_output_path(self):
        # main.py with no argument targets /output/entry.png; only check
        # the constant, not the write, so the suite never needs /output.
        with open(MAIN_PY, encoding="utf-8") as fh:
            source = fh.read()
        self.assertIn('DEFAULT_OUTPUT = "/output/entry.png"', source)


if __name__ == "__main__":
    unittest.main()
