# -*- coding: utf-8 -*-
"""Legt die 288-dpi-PNGs zentriert auf A3 quer und schreibt je ein PDF.

Aufruf:  python _generator/build_pdf.py <Diagrammordner>
Die Auflage 3 hatte hier eine Luecke: ohne drawio-CLI und ohne
SVG-nach-PDF-Konverter gab es keine eigenstaendigen Diagramm-PDFs.
Der Umweg ueber das Rasterbild loest das ohne Zusatzwerkzeug.
"""
import os
import sys

from PIL import Image

from model import FILES

DPI = 288
MM = 25.4
A3_W = int(round(420 / MM * DPI))   # 4763 px
A3_H = int(round(297 / MM * DPI))   # 3367 px
MARGIN = int(round(10 / MM * DPI))  # 10 mm Rand

OUT = sys.argv[1] if len(sys.argv) > 1 else "."


def to_a3(src, dst):
    img = Image.open(src).convert("RGB")
    box_w, box_h = A3_W - 2 * MARGIN, A3_H - 2 * MARGIN
    scale = min(box_w / img.width, box_h / img.height)
    if scale < 1:
        img = img.resize((int(img.width * scale), int(img.height * scale)),
                         Image.LANCZOS)
    page = Image.new("RGB", (A3_W, A3_H), "white")
    page.paste(img, ((A3_W - img.width) // 2, (A3_H - img.height) // 2))
    page.save(dst, "PDF", resolution=DPI)
    return img.width, img.height, round(scale, 3)


if __name__ == "__main__":
    for key, name in FILES.items():
        src = os.path.join(OUT, name + ".png")
        if not os.path.exists(src):
            print("fehlt:", src)
            continue
        dst = os.path.join(OUT, name + ".pdf")
        w, h, s = to_a3(src, dst)
        print("OK %s -> A3 quer, Bild %dx%d px, Faktor %s" % (name, w, h, s))
