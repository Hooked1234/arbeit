# -*- coding: utf-8 -*-
"""Erzeugt drawio, SVG und PNG-Kontrollbild aus model.py."""
import io, os, sys, math
from xml.sax.saxutils import escape
from model import PAGES, NAVY, ACCENT, HDR, PAD, LINE

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
FONT = "C:/Windows/Fonts/arial.ttf"
FONTB = "C:/Windows/Fonts/arialbd.ttf"
FONTI = "C:/Windows/Fonts/ariali.ttf"
FS = 11          # Textgroesse in den Klassen
FS_T = 20        # Titel
FS_L = 11        # Kantenbeschriftung

from PIL import Image, ImageDraw, ImageFont
_f = ImageFont.truetype(FONT, FS)
_fb = ImageFont.truetype(FONTB, FS)


def tw(s, font=None):
    return (font or _f).getlength(s)


# ---------------------------------------------------------------- Pruefungen
def validate(key, w, h, cs, es, ns):
    errs = []
    byk = {c.key: c for c in cs}
    boxes = [(c.key, c.box()) for c in cs] + \
            [("note%d" % i, (n.x, n.y, n.x + n.w, n.y + n.h))
             for i, n in enumerate(ns) if not getattr(n, "plain", False)]
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            (k1, b1), (k2, b2) = boxes[i], boxes[j]
            if b1[0] < b2[2] and b2[0] < b1[2] and b1[1] < b2[3] and b2[1] < b1[3]:
                errs.append("Ueberlappung %s / %s" % (k1, k2))
    for k, b in boxes:
        if b[0] < 0 or b[1] < 0 or b[2] > w or b[3] > h:
            errs.append("ausserhalb der Seite: %s %s" % (k, b))
    for c in cs:
        need = max([tw(l) for l in (c.attrs + c.ops + (c.literals or []))] or [0])
        need = max(need, tw(c.label, _fb)) + 2 * PAD + 6
        if need > c.w:
            errs.append("zu schmal: %s braucht %d, hat %d" % (c.key, need, c.w))
    for n in ns:
        need = max([tw(l) for l in n.lines] or [0]) + 2 * PAD +             (0 if getattr(n, "plain", False) else 14)
        if need > n.w:
            errs.append("Notiz zu schmal: braucht %d, hat %d" % (need, n.w))
    for e in es:
        for k in (e.src, e.dst):
            if k is not None and k not in byk:
                errs.append("unbekannte Klasse in Kante: %s" % k)
        # Endpunkte muessen den jeweiligen Rahmen beruehren
        for k, pt in ((e.src, e.points[0]), (e.dst, e.points[-1])):
            if k is None or k not in byk:
                continue
            x0, y0, x1, y1 = byk[k].box()
            on = (abs(pt[0] - x0) < 2 or abs(pt[0] - x1) < 2 or
                  abs(pt[1] - y0) < 2 or abs(pt[1] - y1) < 2)
            inside = x0 - 2 <= pt[0] <= x1 + 2 and y0 - 2 <= pt[1] <= y1 + 2
            if not (on and inside):
                errs.append("Endpunkt %s liegt nicht am Rahmen von %s" % (pt, k))
    return errs


# ------------------------------------------------------------------- Geometrie
def comp_tops(c):
    """y-Grenzen der Faecher."""
    y1 = c.y + HDR
    y2 = y1 + 2 * PAD + LINE * len(c.attrs)
    return y1, y2


def unit(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    d = math.hypot(dx, dy) or 1
    return dx / d, dy / d



def _at(v, default_anchor="middle"):
    if v is None:
        return None
    return (v[0], v[1], v[2] if len(v) > 2 else default_anchor)


def edge_labels(e):
    """[(text, x, y, anchor, italic)] fuer Name, Multiplizitaeten, Rollen."""
    pts = e.points
    out = []

    def horiz(a, b):
        return abs(a[1] - b[1]) < abs(a[0] - b[0])

    if e.name:
        a = _at(e.name_at)
        if a:
            out.append((e.name, a[0], a[1], a[2], True))
        else:
            p, q = pts[0], pts[-1]
            mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
            if horiz(p, q):
                out.append((e.name, mx, my - 11, "middle", True))
            else:
                out.append((e.name, mx + 12, my + 4, "start", True))
    for m, at, p0, p1 in ((e.m_src, e.m_src_at, pts[0], pts[1]),
                          (e.m_dst, e.m_dst_at, pts[-1], pts[-2])):
        if not m:
            continue
        a = _at(at)
        if a:
            out.append((m, a[0], a[1], a[2], False))
        elif horiz(p0, p1):
            sx = 1 if p1[0] > p0[0] else -1
            out.append((m, p0[0] + sx * 26, p0[1] + 18, "middle", False))
        else:
            sy = 1 if p1[1] > p0[1] else -1
            out.append((m, p0[0] - 9, p0[1] + sy * 24, "end", False))
    for r, at, p0, p1 in ((e.r_src, e.r_src_at, pts[0], pts[1]),
                          (e.r_dst, e.r_dst_at, pts[-1], pts[-2])):
        if not r:
            continue
        a = _at(at)
        if a:
            out.append((r, a[0], a[1], a[2], False))
        elif horiz(p0, p1):
            sx = 1 if p1[0] > p0[0] else -1
            out.append((r, p0[0] + sx * 30, p0[1] - 9, "middle", False))
        else:
            sy = 1 if p1[1] > p0[1] else -1
            out.append((r, p0[0] - 9, p0[1] + sy * 42, "end", False))
    return out


# ----------------------------------------------------------------------- SVG
def svg_marker(kind, tip, prev):
    """Markierung am Endpunkt tip, Richtung aus prev."""
    ux, uy = unit(prev, tip)
    px, py = -uy, ux
    out = []
    if kind in ("compo", "aggr"):
        L, W = 16, 6
        a = (tip[0], tip[1])
        b = (tip[0] - ux * L / 2 + px * W, tip[1] - uy * L / 2 + py * W)
        c = (tip[0] - ux * L, tip[1] - uy * L)
        d = (tip[0] - ux * L / 2 - px * W, tip[1] - uy * L / 2 - py * W)
        pts = " ".join("%.1f,%.1f" % p for p in (a, b, c, d))
        fill = NAVY if kind == "compo" else "#FFFFFF"
        out.append('<polygon points="%s" fill="%s" stroke="%s" '
                   'stroke-width="1.6"/>' % (pts, fill, NAVY))
    elif kind == "gener":
        L, W = 16, 8
        a = (tip[0], tip[1])
        b = (tip[0] - ux * L + px * W, tip[1] - uy * L + py * W)
        c = (tip[0] - ux * L - px * W, tip[1] - uy * L - py * W)
        pts = " ".join("%.1f,%.1f" % p for p in (a, b, c))
        out.append('<polygon points="%s" fill="#FFFFFF" stroke="%s" '
                   'stroke-width="1.6"/>' % (pts, NAVY))
    elif kind == "nav":
        L, W = 12, 5
        b = (tip[0] - ux * L + px * W, tip[1] - uy * L + py * W)
        c = (tip[0] - ux * L - px * W, tip[1] - uy * L - py * W)
        out.append('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" fill="none" '
                   'stroke="%s" stroke-width="1.6"/>'
                   % (b[0], b[1], tip[0], tip[1], c[0], c[1], NAVY))
    return out


def render_svg(key, title, w, h, cs, es, ns):
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
         'viewBox="0 0 %d %d" font-family="Arial, Helvetica, sans-serif">'
         % (w, h, w, h),
         '<rect width="%d" height="%d" fill="#FFFFFF"/>' % (w, h),
         '<rect x="0" y="0" width="%d" height="46" fill="%s"/>' % (w, NAVY),
         '<text x="16" y="30" fill="#FFFFFF" font-size="%d" font-weight="bold">%s'
         '</text>' % (FS_T, escape(title))]

    for e in es:
        pts = e.points
        dash = ' stroke-dasharray="6 4"' if e.kind == "dashed" else ""
        d = " ".join(("M" if i == 0 else "L") + "%.1f,%.1f" % p
                     for i, p in enumerate(pts))
        o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.6"%s/>'
                 % (d, NAVY, dash))
        if e.kind in ("compo", "aggr"):
            o += svg_marker(e.kind, pts[0], pts[1])
        elif e.kind == "gener":
            o += svg_marker("gener", pts[-1], pts[-2])
        elif e.kind == "navassoc":
            o += svg_marker("nav", pts[-1], pts[-2])

        for txt, lx, ly, anc, it in edge_labels(e):
            o.append('<text x="%.0f" y="%.0f" font-size="%d" fill="%s" '
                     'text-anchor="%s"%s>%s</text>'
                     % (lx, ly, FS_L, NAVY, anc,
                        ' font-style="italic"' if it else '', escape(txt)))

    for c in cs:
        x, y, wdt, hgt = c.x, c.y, c.w, c.h
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#FFFFFF" '
                 'stroke="%s" stroke-width="1.6"/>' % (x, y, wdt, hgt, NAVY))
        ty = y + 20
        if c.stereotype:
            o.append('<text x="%d" y="%d" font-size="%d" fill="%s" '
                     'text-anchor="middle">&#171;%s&#187;</text>'
                     % (x + wdt / 2, ty, FS, NAVY, c.stereotype))
            ty += LINE
        style = ' font-style="italic"' if c.abstract else ""
        o.append('<text x="%d" y="%d" font-size="%d" font-weight="bold" '
                 'fill="%s" text-anchor="middle"%s>%s</text>'
                 % (x + wdt / 2, ty, FS + 1, NAVY, style, escape(c.label)))
        if c.literals is not None:
            sep = y + HDR + (LINE if c.stereotype else 0)
            o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                     'stroke-width="1.2"/>' % (x, sep, x + wdt, sep, NAVY))
            ly = sep + PAD + 12
            for l in c.literals:
                o.append('<text x="%d" y="%d" font-size="%d" fill="%s">%s</text>'
                         % (x + PAD, ly, FS, NAVY, escape(l)))
                ly += LINE
            continue
        y1, y2 = comp_tops(c)
        for sep in (y1, y2):
            o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                     'stroke-width="1.2"/>' % (x, sep, x + wdt, sep, NAVY))
        ly = y1 + PAD + 12
        for a in c.attrs:
            und = ' text-decoration="underline"' if not a[:1] in "+-#/" else ""
            o.append('<text x="%d" y="%d" font-size="%d" fill="%s"%s>%s</text>'
                     % (x + PAD, ly, FS, NAVY, und, escape(a)))
            ly += LINE
        ly = y2 + PAD + 12
        for op in c.ops:
            it = ' font-style="italic"' if op.endswith("{abstract}") else ""
            o.append('<text x="%d" y="%d" font-size="%d" fill="%s"%s>%s</text>'
                     % (x + PAD, ly, FS, NAVY, it, escape(op)))
            ly += LINE

    for n in ns:
        if getattr(n, "plain", False):
            ly = n.y + 12
            for l in n.lines:
                o.append('<text x="%d" y="%d" font-size="%d" fill="%s">%s'
                         '</text>' % (n.x, ly, FS, NAVY, escape(l)))
                ly += LINE
            continue
        f = 14
        o.append('<path d="M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#FFFFFF" '
                 'stroke="%s" stroke-width="1.4"/>'
                 % (n.x, n.y, n.x + n.w - f, n.y, n.x + n.w, n.y + f,
                    n.x + n.w, n.y + n.h, n.x, n.y + n.h, NAVY))
        o.append('<path d="M%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" '
                 'stroke-width="1.4"/>'
                 % (n.x + n.w - f, n.y, n.x + n.w - f, n.y + f, n.x + n.w,
                    n.y + f, NAVY))
        ly = n.y + PAD + 12
        for l in n.lines:
            o.append('<text x="%d" y="%d" font-size="%d" fill="%s">%s</text>'
                     % (n.x + PAD, ly, FS, NAVY, escape(l)))
            ly += LINE
    o.append('</svg>')
    return "\n".join(o)


# --------------------------------------------------------------------- drawio
def html_box(c):
    p = ['<div style="text-align:center">']
    if c.stereotype:
        p.append("&#171;%s&#187;<br>" % c.stereotype)
    nm = escape(c.name)
    p.append("<i><b>%s</b></i>" % nm if c.abstract else "<b>%s</b>" % nm)
    if c.abstract:
        p.append("<br>{abstract}")
    p.append("</div><hr>")
    if c.literals is not None:
        p.append("<div>" + "<br>".join(escape(l) for l in c.literals) + "</div>")
        return "".join(p)
    body = "<br>".join(("<u>%s</u>" % escape(a)) if a[:1] not in "+-#/"
                       else escape(a) for a in c.attrs)
    p.append("<div>%s</div><hr>" % body)
    ops = "<br>".join(("<i>%s</i>" % escape(o)) if o.endswith("{abstract}")
                      else escape(o) for o in c.ops)
    p.append("<div>%s</div>" % ops)
    return "".join(p)


EDGE_BASE = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;"
             "strokeColor=%s;strokeWidth=1.6;endArrow=none;startArrow=none;"
             % NAVY)
EDGE_STYLE = {
    "assoc": EDGE_BASE,
    "navassoc": EDGE_BASE + "endArrow=open;endFill=0;endSize=10;",
    "compo": EDGE_BASE + "startArrow=diamondThin;startFill=1;startSize=14;",
    "aggr": EDGE_BASE + "startArrow=diamondThin;startFill=0;startSize=14;",
    "gener": EDGE_BASE + "endArrow=block;endFill=0;endSize=14;",
    "dashed": EDGE_BASE + "dashed=1;",
}


def render_drawio(pages):
    o = ["<?xml version='1.0' encoding='utf-8'?>",
         '<mxfile host="app.diagrams.net" agent="MOBIS aufl.3" pages="%d">'
         % len(pages)]
    for idx, (key, title, w, h, cs, es, ns) in enumerate(pages):
        o.append('  <diagram id="%s" name="Aufgabe %d">' % (key, idx + 1))
        o.append('    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" '
                 'guides="1" tooltips="1" connect="1" arrows="1" fold="1" '
                 'page="1" pageScale="1" pageWidth="%d" pageHeight="%d" '
                 'background="#FFFFFF"><root>' % (w, h))
        o.append('      <mxCell id="0"/><mxCell id="1" parent="0"/>')
        o.append('      <mxCell id="%s_title" value="%s" style="text;html=1;'
                 'strokeColor=none;fillColor=%s;fontColor=#FFFFFF;'
                 'fontFamily=Arial;fontSize=18;fontStyle=1;align=left;'
                 'verticalAlign=middle;spacingLeft=14;" vertex="1" parent="1">'
                 '<mxGeometry x="0" y="0" width="%d" height="46" as="geometry"/>'
                 '</mxCell>' % (key, escape(title), NAVY, w))
        for c in cs:
            o.append('      <mxCell id="%s_%s" value="%s" style="rounded=0;'
                     'whiteSpace=wrap;html=1;align=left;verticalAlign=top;'
                     'spacing=6;fontFamily=Arial;fontSize=10;fillColor=#FFFFFF;'
                     'strokeColor=%s;strokeWidth=1.6;" vertex="1" parent="1">'
                     '<mxGeometry x="%d" y="%d" width="%d" height="%d" '
                     'as="geometry"/></mxCell>'
                     % (key, c.key, escape(html_box(c), {'"': "&quot;"}), NAVY,
                        c.x, c.y, c.w, c.h))
        for i, e in enumerate(es):
            src = '%s_%s' % (key, e.src) if e.src else None
            dst = '%s_%s' % (key, e.dst) if e.dst else None
            att = ''
            if src:
                att += ' source="%s"' % src
            if dst:
                att += ' target="%s"' % dst
            wp = "".join('<mxPoint x="%d" y="%d" as="point"/>' % p
                         for p in e.points[1:-1])
            o.append('      <mxCell id="%s_e%d" value="%s" style="%s" edge="1" '
                     'parent="1"%s><mxGeometry relative="1" as="geometry">'
                     '<mxPoint x="%d" y="%d" as="sourcePoint"/>'
                     '<mxPoint x="%d" y="%d" as="targetPoint"/>'
                     '%s</mxGeometry></mxCell>'
                     % (key, i, escape(e.name or ""), EDGE_STYLE[e.kind], att,
                        e.points[0][0], e.points[0][1], e.points[-1][0],
                        e.points[-1][1],
                        ('<Array as="points">%s</Array>' % wp) if wp else ''))
            for m, frac in ((e.m_src, -1), (e.m_dst, 1)):
                if not m:
                    continue
                o.append('      <mxCell id="%s_e%d_m%d" value="%s" '
                         'style="edgeLabel;html=1;align=center;fontFamily=Arial;'
                         'fontSize=10;fontColor=%s;labelBackgroundColor=#FFFFFF;'
                         '" vertex="1" connectable="0" parent="%s_e%d">'
                         '<mxGeometry x="%d" relative="1" as="geometry">'
                         '<mxPoint as="offset"/></mxGeometry></mxCell>'
                         % (key, i, frac, escape(m), NAVY, key, i, frac))
            for r, frac in ((e.r_src, -1), (e.r_dst, 1)):
                if not r:
                    continue
                o.append('      <mxCell id="%s_e%d_r%d" value="%s" '
                         'style="edgeLabel;html=1;align=center;fontFamily=Arial;'
                         'fontSize=10;fontColor=%s;labelBackgroundColor=#FFFFFF;'
                         '" vertex="1" connectable="0" parent="%s_e%d">'
                         '<mxGeometry x="%d" y="16" relative="1" as="geometry">'
                         '<mxPoint as="offset"/></mxGeometry></mxCell>'
                         % (key, i, frac, escape(r), NAVY, key, i, frac))
        for j, n in enumerate(ns):
            if getattr(n, "plain", False):
                o.append('      <mxCell id="%s_n%d" value="%s" style="text;'
                         'html=1;strokeColor=none;fillColor=none;align=left;'
                         'verticalAlign=top;fontFamily=Arial;fontSize=10;'
                         'fontColor=%s;" vertex="1" parent="1"><mxGeometry '
                         'x="%d" y="%d" width="%d" height="%d" as="geometry"/>'
                         '</mxCell>' % (key, j, escape("<br>".join(n.lines)),
                                        NAVY, n.x, n.y, n.w, n.h))
                continue
            o.append('      <mxCell id="%s_n%d" value="%s" style="shape=note;'
                     'whiteSpace=wrap;html=1;size=14;align=left;'
                     'verticalAlign=top;spacing=6;fontFamily=Arial;fontSize=10;'
                     'fillColor=#FFFFFF;strokeColor=%s;fontColor=%s;" '
                     'vertex="1" parent="1"><mxGeometry x="%d" y="%d" '
                     'width="%d" height="%d" as="geometry"/></mxCell>'
                     % (key, j, escape("<br>".join(n.lines)), NAVY, NAVY,
                        n.x, n.y, n.w, n.h))
        o.append('    </root></mxGraphModel>')
        o.append('  </diagram>')
    o.append('</mxfile>')
    return "\n".join(o)


# ------------------------------------------------------------------------ PNG
def render_png(key, title, w, h, cs, es, ns, scale=1):
    img = Image.new("RGB", (int(w * scale), int(h * scale)), "white")
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT, int(FS * scale))
    fb = ImageFont.truetype(FONTB, int((FS + 1) * scale))
    fi = ImageFont.truetype(FONTI, int((FS + 1) * scale))
    fim = ImageFont.truetype(FONTI, int(FS * scale))
    ft = ImageFont.truetype(FONTB, int(FS_T * scale))
    S = lambda v: v * scale
    d.rectangle([0, 0, w * scale, 46 * scale], fill=NAVY)
    d.text((S(16), S(12)), title, font=ft, fill="white")

    for e in es:
        pts = [(S(p[0]), S(p[1])) for p in e.points]
        for i in range(len(pts) - 1):
            d.line([pts[i], pts[i + 1]], fill=NAVY, width=max(1, int(1.6 * scale)))
        if e.kind in ("compo", "aggr"):
            tip, prev = pts[0], pts[1]
            ux, uy = unit(prev, tip)
            ux, uy = -ux, -uy
            px, py = -uy, ux
            L, W = S(16), S(6)
            poly = [tip, (tip[0] + ux * L / 2 + px * W, tip[1] + uy * L / 2 + py * W),
                    (tip[0] + ux * L, tip[1] + uy * L),
                    (tip[0] + ux * L / 2 - px * W, tip[1] + uy * L / 2 - py * W)]
            d.polygon(poly, fill=NAVY if e.kind == "compo" else "white",
                      outline=NAVY)
        if e.kind == "gener":
            tip, prev = pts[-1], pts[-2]
            ux, uy = unit(prev, tip)
            px, py = -uy, ux
            L, W = S(16), S(8)
            d.polygon([tip, (tip[0] - ux * L + px * W, tip[1] - uy * L + py * W),
                       (tip[0] - ux * L - px * W, tip[1] - uy * L - py * W)],
                      fill="white", outline=NAVY)
        if e.kind == "navassoc":
            tip, prev = pts[-1], pts[-2]
            ux, uy = unit(prev, tip)
            px, py = -uy, ux
            L, W = S(12), S(5)
            d.line([(tip[0] - ux * L + px * W, tip[1] - uy * L + py * W), tip],
                   fill=NAVY, width=2)
            d.line([(tip[0] - ux * L - px * W, tip[1] - uy * L - py * W), tip],
                   fill=NAVY, width=2)

        _anc = {"middle": "mm", "start": "lm", "end": "rm"}
        for txt, lx, ly, anc, it in edge_labels(e):
            d.text((S(lx), S(ly)), txt, font=fim if it else f, fill=NAVY,
                   anchor=_anc[anc])

    for c in cs:
        d.rectangle([S(c.x), S(c.y), S(c.x + c.w), S(c.y + c.h)], fill="white",
                    outline=NAVY, width=max(1, int(1.6 * scale)))
        ty = c.y + 10
        if c.stereotype:
            d.text((S(c.x + c.w / 2), S(ty)), "\u00ab%s\u00bb" % c.stereotype,
                   font=f, fill=NAVY, anchor="ma")
            ty += LINE
        d.text((S(c.x + c.w / 2), S(ty)), c.label, font=fi if c.abstract else fb,
               fill=NAVY, anchor="ma")
        if c.literals is not None:
            sep = c.y + HDR + (LINE if c.stereotype else 0)
            d.line([(S(c.x), S(sep)), (S(c.x + c.w), S(sep))], fill=NAVY)
            ly = sep + PAD
            for l in c.literals:
                d.text((S(c.x + PAD), S(ly)), l, font=f, fill=NAVY)
                ly += LINE
            continue
        y1, y2 = comp_tops(c)
        for sep in (y1, y2):
            d.line([(S(c.x), S(sep)), (S(c.x + c.w), S(sep))], fill=NAVY)
        ly = y1 + PAD
        for a in c.attrs:
            d.text((S(c.x + PAD), S(ly)), a, font=f, fill=NAVY)
            if a[:1] not in "+-#/":
                wpx = f.getlength(a)
                d.line([(S(c.x + PAD), S(ly) + f.size + 2),
                        (S(c.x + PAD) + wpx, S(ly) + f.size + 2)], fill=NAVY)
            ly += LINE
        ly = y2 + PAD
        for op in c.ops:
            d.text((S(c.x + PAD), S(ly)), op,
                   font=fim if op.endswith("{abstract}") else f, fill=NAVY)
            ly += LINE

    for n in ns:
        if getattr(n, "plain", False):
            ly = n.y
            for l in n.lines:
                d.text((S(n.x), S(ly)), l, font=f, fill=NAVY)
                ly += LINE
            continue
        fold = 14
        d.polygon([(S(n.x), S(n.y)), (S(n.x + n.w - fold), S(n.y)),
                   (S(n.x + n.w), S(n.y + fold)), (S(n.x + n.w), S(n.y + n.h)),
                   (S(n.x), S(n.y + n.h))], fill="white", outline=NAVY)
        ly = n.y + PAD
        for l in n.lines:
            d.text((S(n.x + PAD), S(ly)), l, font=f, fill=NAVY)
            ly += LINE
    return img


# ----------------------------------------------------------------------- main
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    ok = True
    names = {"aufgabe_1": "Aufgabe_1_Bestellsystem_eines_Onlineshops",
             "aufgabe_2": "Aufgabe_2_Hotelverwaltung",
             "aufgabe_3": "Aufgabe_3_Veranstaltungsmanagement"}
    for page in PAGES:
        key, title, w, h, cs, es, ns = page
        errs = validate(key, w, h, cs, es, ns)
        if errs:
            ok = False
            print("FEHLER %s:" % key)
            for e in errs:
                print("   -", e)
        else:
            print("OK %s (%dx%d, %d Klassen, %d Kanten)"
                  % (key, w, h, len(cs), len(es)))
        io.open(os.path.join(OUT, names[key] + ".svg"), "w",
                encoding="utf-8").write(render_svg(*page))
        render_png(*page, scale=1).save(
            os.path.join(OUT, "preview_" + key + ".png"))
        img = render_png(*page, scale=3)
        img.save(os.path.join(OUT, names[key] + ".png"), dpi=(288, 288))
    io.open(os.path.join(OUT, "MOBIS_UML_Loesungen.drawio"), "w",
            encoding="utf-8").write(render_drawio(PAGES))
    print("fertig" if ok else "MIT FEHLERN")
