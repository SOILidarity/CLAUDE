#!/usr/bin/env python3
"""Inline fonts and images into deck.src.html so the deck is one offline file.

Usage: python3 build.py
Writes Susulung-king-Pyalung-Final-Defense.html next to this script.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "deck.src.html"
OUT = ROOT / "Susulung-king-Pyalung-Final-Defense.html"
ASSETS = ROOT / "assets"

MIME = {".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml"}


def data_uri(name: str) -> str:
    path = ASSETS / name
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{MIME[path.suffix]};base64,{b64}"


html = SRC.read_text(encoding="utf-8")
html, n = re.subn(r"\{\{asset:([\w.\-]+)\}\}", lambda m: data_uri(m.group(1)), html)
OUT.write_text(html, encoding="utf-8")
print(f"Inlined {n} asset references -> {OUT.name} ({OUT.stat().st_size / 1024:.0f} KB)")
