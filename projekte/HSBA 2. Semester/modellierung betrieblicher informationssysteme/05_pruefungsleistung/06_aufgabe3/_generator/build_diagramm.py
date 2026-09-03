# -*- coding: utf-8 -*-
"""Erzeugt das Klassendiagramm zu Aufgabe 3 (Fitnessstudio) als SVG und PNG.

Notation strikt nach `02_materialien/7-UML-KD.pptx` (Prof. Dr. Sarshar):
Klasse mit Attributen und Methoden, Assoziation, Aggregation, Komposition,
Vererbung, Kardinalitaeten 1 / 0..1 / 0..* / 1..*. Keine Sichtbarkeiten,
keine Datentypen, keine abstrakten Klassen, keine Enumerationen.

Optik bewusst identisch zu den Diagrammen der Aufgaben 1 und 2 der Abgabe:
schwarz-weiss, duenne Rahmen, fette zentrierte Klassennamen, orthogonale
Kanten. Aggregation und Komposition tragen — wie beim Dozenten und in den
Aufgaben 1 und 2 — keine Kardinalitaeten.
"""
import os
import sys
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1] if len(sys.argv) > 1 else "."

FONT = "C:/Windows/Fonts/arial.ttf"
FONTB = "C:/Windows/Fonts/arialbd.ttf"
FS = 34          # Text in den Klassen
FS_L = 32        # Kantenbeschriftung
STROKE = 3
HDR = 60         # Kopfzeile Klassenname
PAD = 20         # Innenabstand je Fach
LINE = 46        # Zeilenhoehe
W, H = 2240, 1900

_f = ImageFont.truetype(FONT, FS)
_fb = ImageFont.truetype(FONTB, FS)
_fl = ImageFont.truetype(FONT, FS_L)


def tw(s, font=None):
    return (font or _f).getlength(s)


class C:
    def __init__(self, key, name, x, y, w, attrs=(), ops=()):
        self.key, self.name, self.x, self.y, self.w = key, name, x, y, w
        self.attrs, self.ops = list(attrs), list(ops)

    @property
    def h(self):
        return HDR + (2 * PAD + LINE * len(self.attrs)) + (2 * PAD + LINE * len(self.ops))

    def box(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)


class E:
    """kind: assoc | aggr | compo | gener"""

    def __init__(self, kind, points, m_src=None, m_dst=None,
                 m_src_at=None, m_dst_at=None, branches=()):
        self.kind, self.points = kind, list(points)
        self.m_src, self.m_dst = m_src, m_dst
        self.m_src_at, self.m_dst_at = m_src_at, m_dst_at
        self.branches = [list(b) for b in branches]


# ------------------------------------------------------------------- Modell
CLASSES = [
    C("person", "Person", 1000, 60, 560,
      ["name", "geburtsdatum"], ["kontaktdatenÄndern()"]),
    C("schliessfach", "Schließfach", 60, 560, 440,
      ["fachnummer"], ["öffnen()"]),
    C("mitglied", "Mitglied", 720, 560, 560,
      ["mitgliedsnummer", "beitrag"], ["kursBuchen()"]),
    C("trainer", "Trainer", 1620, 560, 560,
      ["personalnummer", "qualifikation"], ["kursLeiten()"]),
    C("kurs", "Kurs", 1000, 1080, 560,
      ["kursnummer", "titel", "wochentag"], ["teilnehmerlisteDrucken()"]),
    C("studio", "Fitnessstudio", 1000, 1560, 560,
      ["name", "adresse"], ["kursAnlegen()"]),
]

EDGES = [
    # Vererbung: Dreieck an Person, gemeinsamer Baum wie Dozentenfolie 22
    E("gener", [(1280, 338), (1280, 450)],
      branches=[[(1000, 450), (1900, 450)],
                [(1000, 450), (1000, 560)],
                [(1900, 450), (1900, 560)]]),
    # Schließfach 0..1 -- 1 Mitglied
    E("assoc", [(500, 676), (720, 676)],
      m_src="0..1", m_dst="1", m_src_at=(512, 636), m_dst_at=(676, 636)),
    # Mitglied 0..* -- 0..* Kurs
    E("assoc", [(1100, 838), (1100, 1080)],
      m_src="0..*", m_dst="0..*", m_src_at=(1114, 848), m_dst_at=(1114, 1002)),
    # Trainer 1 -- 1..* Kurs
    E("assoc", [(1900, 838), (1900, 1260), (1560, 1260)],
      m_src="1", m_dst="1..*", m_src_at=(1914, 848), m_dst_at=(1574, 1214)),
    # Komposition: schwarze Raute am Fitnessstudio (Ganzes)
    E("compo", [(1280, 1560), (1280, 1404)]),
    # Aggregation: weiße Raute am Fitnessstudio (Ganzes)
    E("aggr", [(1000, 1690), (820, 1690), (820, 838)]),
]


# ---------------------------------------------------------------- Pruefungen
def validate():
    errs = []
    byk = {c.key: c for c in CLASSES}
    boxes = [(c.key, c.box()) for c in CLASSES]
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            (k1, b1), (k2, b2) = boxes[i], boxes[j]
            if b1[0] < b2[2] and b2[0] < b1[2] and b1[1] < b2[3] and b2[1] < b1[3]:
                errs.append("Ueberlappung %s / %s" % (k1, k2))
    for k, b in boxes:
        if b[0] < 0 or b[1] < 0 or b[2] > W or b[3] > H:
            errs.append("ausserhalb der Seite: %s %s" % (k, b))
    for c in CLASSES:
        need = max([tw(l) for l in (c.attrs + c.ops)] or [0])
        need = max(need, tw(c.name, _fb)) + 2 * PAD + 8
        if need > c.w:
            errs.append("zu schmal: %s braucht %d, hat %d" % (c.key, need, c.w))

    def on_border(pt):
        for c in CLASSES:
            x0, y0, x1, y1 = c.box()
            if x0 - 2 <= pt[0] <= x1 + 2 and y0 - 2 <= pt[1] <= y1 + 2:
                if (abs(pt[0] - x0) < 3 or abs(pt[0] - x1) < 3
                        or abs(pt[1] - y0) < 3 or abs(pt[1] - y1) < 3):
                    return c.key
                return "INNEN:" + c.key
        return None

    def seg_hits_box(p, q):
        hits = []
        for c in CLASSES:
            x0, y0, x1, y1 = c.box()
            if p[0] == q[0]:                       # senkrecht
                lo, hi = sorted((p[1], q[1]))
                if x0 + 3 < p[0] < x1 - 3 and lo < y1 - 3 and y0 + 3 < hi:
                    hits.append(c.key)
            else:                                   # waagerecht
                lo, hi = sorted((p[0], q[0]))
                if y0 + 3 < p[1] < y1 - 3 and lo < x1 - 3 and x0 + 3 < hi:
                    hits.append(c.key)
        return hits

    for n, e in enumerate(EDGES):
        chains = [e.points] + e.branches
        for ch in chains:
            for a, b in zip(ch, ch[1:]):
                if a[0] != b[0] and a[1] != b[1]:
                    errs.append("Kante %d nicht orthogonal: %s->%s" % (n, a, b))
                for k in seg_hits_box(a, b):
                    errs.append("Kante %d laeuft durch %s" % (n, k))
        for pt in (e.points[0], e.points[-1]):
            r = on_border(pt)
            if r is None or str(r).startswith("INNEN"):
                errs.append("Kante %d Endpunkt %s nicht auf Rahmen (%s)" % (n, pt, r))
        for br in e.branches:
            r = on_border(br[-1])
            if r is not None and str(r).startswith("INNEN"):
                errs.append("Kante %d Zweigende %s liegt im Kasten" % (n, br[-1]))
    return errs


# --------------------------------------------------------------------- SVG
def svg():
    p = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
         'viewBox="0 0 %d %d">' % (W, H, W, H),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H),
         '<g stroke="#000000" stroke-width="%d" fill="none">' % STROKE]

    def line(a, b):
        p.append('<line x1="%d" y1="%d" x2="%d" y2="%d"/>' % (a[0], a[1], b[0], b[1]))

    for c in CLASSES:
        x, y, w, h = c.x, c.y, c.w, c.h
        p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#ffffff"/>'
                 % (x, y, w, h))
        y1 = y + HDR
        y2 = y1 + 2 * PAD + LINE * len(c.attrs)
        line((x, y1), (x + w, y1))
        line((x, y2), (x + w, y2))

    for e in EDGES:
        for ch in [e.points] + e.branches:
            for a, b in zip(ch, ch[1:]):
                line(a, b)
    p.append('</g>')

    # Kantenenden
    for e in EDGES:
        a, b = e.points[0], e.points[1]
        dx, dy = (b[0] - a[0]), (b[1] - a[1])
        n = max(abs(dx), abs(dy)) or 1
        ux, uy = dx / n, dy / n
        if e.kind in ("aggr", "compo"):
            L, Wd = 46, 26
            mx, my = a[0] + ux * L / 2, a[1] + uy * L / 2
            px, py = -uy, ux
            pts = [(a[0], a[1]), (mx + px * Wd / 2, my + py * Wd / 2),
                   (a[0] + ux * L, a[1] + uy * L),
                   (mx - px * Wd / 2, my - py * Wd / 2)]
            fill = "#000000" if e.kind == "compo" else "#ffffff"
            p.append('<polygon points="%s" fill="%s" stroke="#000000" '
                     'stroke-width="%d"/>'
                     % (" ".join("%d,%d" % (int(q[0]), int(q[1])) for q in pts),
                        fill, STROKE))
        if e.kind == "gener":
            L, Wd = 42, 46
            px, py = -uy, ux
            tip = (a[0], a[1])
            base = (a[0] + ux * L, a[1] + uy * L)
            pts = [tip, (base[0] + px * Wd / 2, base[1] + py * Wd / 2),
                   (base[0] - px * Wd / 2, base[1] - py * Wd / 2)]
            p.append('<polygon points="%s" fill="#ffffff" stroke="#000000" '
                     'stroke-width="%d"/>'
                     % (" ".join("%d,%d" % (int(q[0]), int(q[1])) for q in pts),
                        STROKE))

    # Text
    def txt(x, y, s, bold=False, anchor="start", size=FS):
        p.append('<text x="%d" y="%d" font-family="Arial, Helvetica, sans-serif" '
                 'font-size="%d" fill="#000000"%s%s>%s</text>'
                 % (x, y, size, ' font-weight="bold"' if bold else "",
                    ' text-anchor="middle"' if anchor == "middle" else "",
                    escape(s)))

    base = int(FS * 0.35)
    for c in CLASSES:
        txt(c.x + c.w // 2, c.y + HDR // 2 + base, c.name, bold=True,
            anchor="middle")
        yy = c.y + HDR + PAD + LINE // 2 + base
        for a in c.attrs:
            txt(c.x + PAD, yy, a)
            yy += LINE
        yy = c.y + HDR + 2 * PAD + LINE * len(c.attrs) + PAD + LINE // 2 + base
        for o in c.ops:
            txt(c.x + PAD, yy, o)
            yy += LINE

    for e in EDGES:
        for lbl, at in ((e.m_src, e.m_src_at), (e.m_dst, e.m_dst_at)):
            if lbl and at:
                txt(at[0], at[1] + FS_L, lbl, size=FS_L)
    p.append('</svg>')
    return "\n".join(p)


# --------------------------------------------------------------------- PNG
def png():
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)

    def line(a, b):
        d.line([a, b], fill="black", width=STROKE)

    for c in CLASSES:
        x, y, w, h = c.x, c.y, c.w, c.h
        d.rectangle([x, y, x + w, y + h], outline="black", width=STROKE, fill="white")
        y1 = y + HDR
        y2 = y1 + 2 * PAD + LINE * len(c.attrs)
        line((x, y1), (x + w, y1))
        line((x, y2), (x + w, y2))

    for e in EDGES:
        for ch in [e.points] + e.branches:
            for a, b in zip(ch, ch[1:]):
                line(a, b)

    for e in EDGES:
        a, b = e.points[0], e.points[1]
        dx, dy = (b[0] - a[0]), (b[1] - a[1])
        n = max(abs(dx), abs(dy)) or 1
        ux, uy = dx / n, dy / n
        if e.kind in ("aggr", "compo"):
            L, Wd = 46, 26
            mx, my = a[0] + ux * L / 2, a[1] + uy * L / 2
            px, py = -uy, ux
            pts = [(a[0], a[1]), (mx + px * Wd / 2, my + py * Wd / 2),
                   (a[0] + ux * L, a[1] + uy * L),
                   (mx - px * Wd / 2, my - py * Wd / 2)]
            d.polygon(pts, fill="black" if e.kind == "compo" else "white",
                      outline="black")
            d.line(pts + [pts[0]], fill="black", width=STROKE)
        if e.kind == "gener":
            L, Wd = 42, 46
            px, py = -uy, ux
            base = (a[0] + ux * L, a[1] + uy * L)
            pts = [(a[0], a[1]), (base[0] + px * Wd / 2, base[1] + py * Wd / 2),
                   (base[0] - px * Wd / 2, base[1] - py * Wd / 2)]
            d.polygon(pts, fill="white", outline="black")
            d.line(pts + [pts[0]], fill="black", width=STROKE)

    for c in CLASSES:
        d.text((c.x + c.w / 2, c.y + HDR / 2), c.name, font=_fb, fill="black",
               anchor="mm")
        yy = c.y + HDR + PAD + LINE / 2
        for a in c.attrs:
            d.text((c.x + PAD, yy), a, font=_f, fill="black", anchor="lm")
            yy += LINE
        yy = c.y + HDR + 2 * PAD + LINE * len(c.attrs) + PAD + LINE / 2
        for o in c.ops:
            d.text((c.x + PAD, yy), o, font=_f, fill="black", anchor="lm")
            yy += LINE

    for e in EDGES:
        for lbl, at in ((e.m_src, e.m_src_at), (e.m_dst, e.m_dst_at)):
            if lbl and at:
                d.text((at[0], at[1] + FS_L / 2), lbl, font=_fl, fill="black",
                       anchor="lm")
    return im


if __name__ == "__main__":
    errs = validate()
    if errs:
        print("PRUEFUNG FEHLGESCHLAGEN:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print("Geometriepruefung ohne Befund.")
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "Aufgabe_3_Fitnessstudio.svg"), "w",
              encoding="utf-8") as f:
        f.write(svg())
    png().save(os.path.join(OUT, "Aufgabe_3_Fitnessstudio.png"))
    print("geschrieben:", OUT)
