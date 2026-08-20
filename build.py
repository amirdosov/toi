# -*- coding: utf-8 -*-
"""Артефакт-нұсқадан дербес сайт файлын жинайды (doctype, charset, viewport қосады)."""
import io
import os
import re
import sys

SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")

HEAD = u"""<!doctype html>
<html lang="kk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="%(theme)s">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="Гүлмираның ұзату тойына шақыру — 18 қыркүйек 2026, Ақтөбе">
<meta property="og:title" content="Гүлмираның ұзату тойы">
<meta property="og:description" content="18 қыркүйек 2026, 18:00 · Ақтөбе, Қарасай батыр к-сі 142">
<meta property="og:type" content="website">
%(headbits)s
</head>
<body>
"""

TAIL = u"""
</body>
</html>
"""


def build(src_name, out_path, theme):
    src = io.open(os.path.join(SRC_DIR, src_name), encoding="utf-8").read()
    # <title> мен қаріп сілтемелерін <head> ішіне көшіреміз
    m = re.match(r'(<title>.*?display=swap">)\n', src, re.S)
    headbits, body = m.group(1), src[m.end():]
    page = (HEAD % {"theme": theme, "headbits": headbits}) + body + TAIL
    io.open(out_path, "w", encoding="utf-8").write(page)
    print("built %s (%d bytes)" % (out_path, len(page.encode("utf-8"))))


here = os.path.dirname(os.path.abspath(__file__))
build("uzatu.html", os.path.join(here, "index.html"), "#08181E")
build("uzatu-light.html", os.path.join(here, "index-light.html"), "#FBF7F0")
