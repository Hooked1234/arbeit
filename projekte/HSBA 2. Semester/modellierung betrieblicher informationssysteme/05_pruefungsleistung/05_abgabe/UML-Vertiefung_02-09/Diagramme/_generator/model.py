# -*- coding: utf-8 -*-
"""Layoutmodell der Vertiefungsdiagramme, Termin 02.09.2026.

Notation strikt nach dem belegten Katalog: keine Sichtbarkeiten, keine
Datentypen, keine Methodensignaturen, keine abstrakten Klassen, keine
Enumerationen, keine Assoziationsklassen. Belege siehe
`03_entwurf/Szenarien_vertiefung.md`.
"""

NAVY = "#2E4A6B"      # Kanten und Titelbalken
INK = "#12263F"       # Text in den Klassen
ACCENT = "#8A6A2F"

# Kopfzeilenfarbe und Rahmenfarbe je Zustand, Hausstil der Runde vom 12.08.
TONE = {
    None: ("#DAE8FC", "#4A6FA5"),          # unveraendert, hellblau
    "neu": ("#D5E8D4", "#5E9B4A"),         # neu in Aufgabe 2, gruen
    "geaendert": ("#FFF2CC", "#C0A24A"),   # umgebaut, gelb
}

FILES = {
    "stufe_1": "Stufe_1_Ist-Modell",
    "stufe_2": "Stufe_2_Endmodell",
    "stufe_2_diff": "Stufe_2_Differenz",
    "aufgabe_2_ki": "Aufgabe_2_KI-Entwurf",
}

HDR = 30      # Kopfzeile Klassenname
PAD = 7       # Innenabstand je Fach
LINE = 16     # Zeilenhoehe


class C:
    """Klasse im Diagramm."""

    def __init__(self, key, name, x, y, w, attrs=(), ops=(), abstract=False,
                 stereotype=None, literals=None, tone=None):
        self.key, self.name, self.x, self.y, self.w = key, name, x, y, w
        self.attrs, self.ops = list(attrs), list(ops)
        self.abstract, self.stereotype = abstract, stereotype
        self.literals = list(literals) if literals else None
        self.tone = tone

    @property
    def h(self):
        if self.literals is not None:
            head = HDR + (LINE if self.stereotype else 0)
            return head + 2 * PAD + LINE * len(self.literals)
        head = HDR
        body = 2 * PAD + LINE * len(self.attrs)
        tail = 2 * PAD + LINE * len(self.ops)
        return head + body + tail

    @property
    def label(self):
        return self.name + (" {abstract}" if self.abstract else "")

    def box(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)


class E:
    """Beziehung. kind: assoc | compo | aggr | gener | navassoc | dashed"""

    def __init__(self, kind, src, dst, points, name=None, m_src=None, m_dst=None,
                 r_src=None, r_dst=None, name_at=None, m_src_at=None,
                 m_dst_at=None, r_src_at=None, r_dst_at=None):
        self.kind, self.src, self.dst, self.points = kind, src, dst, points
        self.name, self.m_src, self.m_dst = name, m_src, m_dst
        self.r_src, self.r_dst = r_src, r_dst
        self.name_at, self.m_src_at, self.m_dst_at = name_at, m_src_at, m_dst_at
        self.r_src_at, self.r_dst_at = r_src_at, r_dst_at


class N:
    """Notiz."""

    def __init__(self, x, y, w, lines, h=None, plain=False):
        self.x, self.y, self.w, self.lines = x, y, w, list(lines)
        self.plain = plain
        self.h = h or (2 * PAD + LINE * len(self.lines) + 6)


def toned(classes, tones):
    """Kopiert eine Klassenliste und faerbt sie fuer die Differenzansicht."""
    out = []
    for c in classes:
        d = C(c.key, c.name, c.x, c.y, c.w, c.attrs, c.ops)
        d.tone = tones.get(c.key)
        out.append(d)
    return out


# ==========================================================================
# Stufe 1 - Ist-Modell der Pruefungsverwaltung
# ==========================================================================
S1_W, S1_H = 1540, 1200
S1 = [
    C("studiengang", "Studiengang", 60, 110, 250,
      ["kürzel", "bezeichnung", "regelstudienzeit"],
      ["modulAufnehmen()", "studienplanDrucken()"]),
    C("modul", "Modul", 470, 110, 250,
      ["modulnummer", "titel", "credits"],
      ["prüfungAnsetzen()"]),
    C("dozent", "Dozent", 900, 110, 250,
      ["personalnummer", "name"],
      ["noteEintragen()"]),
    C("student", "Student", 60, 380, 250,
      ["matrikelnummer", "name", "e-mail"],
      ["zuPrüfungAnmelden()", "notenspiegelAbrufen()"]),
    C("pruefung", "Prüfung", 470, 380, 250,
      ["prüfungsnummer", "datum", "raum"],
      ["anmeldungÖffnen()", "prüfungAbsagen()"]),
    C("versuch", "Prüfungsversuch", 60, 640, 260,
      ["versuchsnummer", "datum", "note"],
      ["alsBestandenVerbuchen()", "versuchZurücktreten()"]),
    C("klausur", "Klausur", 430, 830, 230,
      ["bearbeitungsdauer"],
      ["aufsichtEinteilen()"]),
    C("muendlich", "MündlichePrüfung", 720, 830, 250,
      ["dauer", "beisitzer"],
      ["protokollAnlegen()"]),
    C("praesentation", "Präsentation", 1030, 830, 230,
      ["vortragsdauer"],
      ["technikPrüfen()"]),
    C("einzel", "Einzelpräsentation", 900, 1040, 250,
      ["vortragstermin"],
      ["terminVerschieben()"]),
    C("gruppe", "Gruppenpräsentation", 1210, 1040, 260,
      ["mitgliederzahl"],
      ["gruppeEinteilen()"]),
]
S1_E = [
    E("aggr", "studiengang", "modul", [(310, 160), (470, 160)],
      name="fasst zusammen", m_src="0..*", m_dst="1..*"),
    E("compo", "modul", "pruefung", [(595, 232), (595, 380)],
      name="setzt an", m_src="1", m_dst="1..*"),
    E("assoc", "dozent", "modul", [(900, 160), (720, 160)],
      name="lehrt", m_src="1..*", m_dst="0..*"),
    E("assoc", "dozent", "pruefung", [(1025, 216), (1025, 450), (720, 450)],
      name="beaufsichtigt", m_src="0..1", m_dst="0..*"),
    E("assoc", "student", "studiengang", [(185, 380), (185, 248)],
      name="ist eingeschrieben in", m_src="0..*", m_dst="1"),
    E("compo", "student", "versuch", [(185, 518), (185, 640)],
      name="unternimmt", m_src="1", m_dst="0..*"),
    E("aggr", "versuch", "pruefung",
      [(320, 700), (400, 700), (400, 490), (470, 490)],
      name="bezieht sich auf", m_src="0..*", m_dst="1"),
    E("gener", "klausur", "pruefung",
      [(545, 830), (545, 770), (645, 770), (645, 518)]),
    E("gener", "muendlich", "pruefung",
      [(845, 830), (845, 770), (645, 770), (645, 518)]),
    E("gener", "praesentation", "pruefung",
      [(1145, 830), (1145, 770), (645, 770), (645, 518)]),
    E("gener", "einzel", "praesentation",
      [(1025, 1040), (1025, 980), (1145, 980), (1145, 920)]),
    E("gener", "gruppe", "praesentation",
      [(1340, 1040), (1340, 980), (1145, 980), (1145, 920)]),
]
S1_N = []


# ==========================================================================
# Stufe 2 - Endmodell nach der neuen Pruefungsordnung
# ==========================================================================
S2_W, S2_H = 1900, 1120
S2 = [
    C("studiengang", "Studiengang", 60, 110, 250,
      ["kürzel", "bezeichnung", "regelstudienzeit"],
      ["modulAufnehmen()", "studienplanDrucken()"]),
    C("modulzuordnung", "Modulzuordnung", 430, 120, 250,
      ["art", "fachsemester"],
      ["artÄndern()"]),
    C("modul", "Modul", 800, 110, 250,
      ["modulnummer", "titel", "credits"],
      ["prüfungAnsetzen()"]),
    C("dozent", "Dozent", 1300, 110, 250,
      ["personalnummer", "name"],
      ["noteEintragen()"]),
    C("student", "Student", 60, 380, 250,
      ["matrikelnummer", "name", "e-mail"],
      ["zuPrüfungAnmelden()", "notenspiegelAbrufen()"]),
    C("pruefung", "Prüfung", 800, 380, 250,
      ["prüfungsnummer", "datum", "raum"],
      ["anmeldungÖffnen()", "prüfungAbsagen()"]),
    C("leistung", "Leistung", 60, 660, 280,
      ["datum", "note"],
      ["angerechnetesModulErmitteln()", "alsBestandenVerbuchen()"]),
    C("anerkannt", "AnerkannteLeistung", 60, 940, 270,
      ["hochschule", "externerTitel"],
      ["nachweisPrüfen()"]),
    C("versuch", "Prüfungsversuch", 420, 940, 250,
      ["versuchsnummer"],
      ["versuchZurücktreten()"]),
    C("klausur", "Klausur", 760, 700, 230,
      ["bearbeitungsdauer"],
      ["aufsichtEinteilen()"]),
    C("muendlich", "MündlichePrüfung", 1060, 700, 250,
      ["dauer", "beisitzer"],
      ["protokollAnlegen()"]),
    C("praesentation", "Präsentation", 1400, 700, 230,
      ["vortragsdauer"],
      ["technikPrüfen()"]),
    C("einzel", "Einzelpräsentation", 1280, 950, 250,
      ["vortragstermin"],
      ["terminVerschieben()"]),
    C("gruppe", "Gruppenpräsentation", 1590, 950, 260,
      ["mitgliederzahl"],
      ["gruppeEinteilen()"]),
]
S2_E = [
    E("compo", "studiengang", "modulzuordnung", [(310, 175), (430, 175)],
      name="ordnet zu", m_src="1", m_dst="1..*"),
    E("aggr", "modulzuordnung", "modul", [(680, 175), (800, 175)],
      name="betrifft", m_src="0..*", m_dst="1"),
    E("assoc", "dozent", "modul", [(1300, 160), (1050, 160)],
      name="lehrt", m_src="1..*", m_dst="0..*"),
    E("assoc", "dozent", "pruefung", [(1425, 216), (1425, 450), (1050, 450)],
      name="beaufsichtigt", m_src="0..1", m_dst="0..*"),
    E("compo", "modul", "pruefung", [(925, 232), (925, 380)],
      name="setzt an", m_src="1", m_dst="1..*"),
    E("assoc", "student", "studiengang", [(185, 380), (185, 248)],
      name="ist eingeschrieben in", m_src="0..*", m_dst="1"),
    E("compo", "student", "leistung", [(185, 518), (185, 660)],
      name="erbringt", m_src="1", m_dst="0..*"),
    E("gener", "anerkannt", "leistung", [(195, 940), (195, 782)]),
    E("gener", "versuch", "leistung",
      [(545, 940), (545, 870), (195, 870), (195, 782)]),
    E("aggr", "versuch", "pruefung",
      [(670, 985), (720, 985), (720, 480), (800, 480)],
      name="bezieht sich auf", m_src="0..*", m_dst="1",
      name_at=(706, 590, "end"), m_src_at=(688, 972, "end")),
    E("aggr", "anerkannt", "modul",
      [(330, 993), (375, 993), (375, 90), (925, 90), (925, 110)],
      name="wird angerechnet auf", m_src="0..*", m_dst="1",
      name_at=(390, 640, "start"), m_dst_at=(910, 104, "end")),
    E("gener", "klausur", "pruefung",
      [(875, 700), (875, 620), (925, 620), (925, 518)]),
    E("gener", "muendlich", "pruefung",
      [(1185, 700), (1185, 620), (925, 620), (925, 518)]),
    E("gener", "praesentation", "pruefung",
      [(1515, 700), (1515, 620), (925, 620), (925, 518)]),
    E("gener", "einzel", "praesentation",
      [(1405, 950), (1405, 870), (1515, 870), (1515, 790)]),
    E("gener", "gruppe", "praesentation",
      [(1720, 950), (1720, 870), (1515, 870), (1515, 790)]),
]
S2_N = [
    N(700, 860, 560,
      ["Zielkonflikt Gruppenpräsentation, Variante B:",
       "je Mitglied eine eigene Leistung, alle beziehen sich",
       "auf dieselbe Gruppenpräsentation. Die Komposition",
       "zu Student bleibt damit unverändert."]),
]


# ==========================================================================
# Stufe 2 - Differenzansicht
# ==========================================================================
S3_TONES = {
    "modulzuordnung": "neu",
    "leistung": "neu",
    "anerkannt": "neu",
    "einzel": "neu",
    "gruppe": "neu",
    "studiengang": "geaendert",
    "modul": "geaendert",
    "student": "geaendert",
    "versuch": "geaendert",
    "praesentation": "geaendert",
}
S3_W, S3_H = S2_W, S2_H
S3 = toned(S2, S3_TONES)
S3_E = S2_E
S3_N = S2_N + [
    N(700, 990, 560,
      ["Blau  unverändert aus Aufgabe 1",
       "Grün  neu in Aufgabe 2",
       "Gelb  gegenüber Aufgabe 1 umgebaut"]),
    N(400, 262, 480,
      ["Entfallen: die Aggregation Studiengang - Modul",
       "aus Aufgabe 1. Sie kann Art und Fachsemester",
       "nicht tragen und weicht der Modulzuordnung."]),
]


# ==========================================================================
# Aufgabe 2 - KI-Entwurf zum Szenario aus Aufgabe 1
# --------------------------------------------------------------------------
# Bewusst fehlerhaft. Acht echte Fehler und zwei zulaessige Abweichungen,
# gesetzt nach den typischen Ausfallmustern eines Sprachmodells bei UML aus
# Fliesstext. Fundliste und Begruendungen: 03_entwurf/Szenarien_vertiefung.md
# ==========================================================================
K_W, K_H = 1540, 1200
K = [
    C("studiengang", "Studiengang", 60, 110, 250,
      ["kürzel", "bezeichnung", "regelstudienzeit"],
      ["modulAufnehmen()", "studienplanDrucken()"]),
    C("modul", "Modul", 470, 110, 250,
      ["modulnummer", "titel", "credits", "beschreibung"],
      ["prüfungAnsetzen()"]),
    C("dozent", "Dozent", 900, 110, 250,
      ["personalnummer", "name"],
      ["noteEintragen()"]),
    C("student", "Student", 60, 380, 250,
      ["matrikelnummer", "name", "e-mail", "status"],
      ["zuPrüfungAnmelden()", "notenspiegelAbrufen()"]),
    C("pruefung", "Prüfungstermin", 470, 380, 250,
      ["prüfungsnummer", "datum", "raum", "status"],
      ["anmeldungÖffnen()", "prüfungAbsagen()"]),
    C("versuch", "Prüfungsversuch", 60, 660, 260,
      ["id", "datum", "note"],
      ["alsBestandenVerbuchen()", "versuchZurücktreten()"]),
    C("klausur", "Klausur", 430, 830, 230,
      ["bearbeitungsdauer"],
      ["aufsichtEinteilen()"]),
    C("muendlich", "MündlichePrüfung", 720, 830, 250,
      ["dauer", "beisitzer"],
      ["protokollAnlegen()"]),
    C("praesentation", "Präsentation", 1030, 830, 230,
      ["vortragsdauer"],
      ["technikPrüfen()"]),
    C("einzel", "Einzelpräsentation", 60, 1040, 250,
      ["vortragstermin"],
      ["terminVerschieben()"]),
    C("gruppe", "Gruppenpräsentation", 370, 1040, 260,
      ["mitgliederzahl"],
      ["gruppeEinteilen()"]),
]
K_E = [
    # F1 schwarze statt weisser Raute
    E("compo", "studiengang", "modul", [(310, 160), (470, 160)],
      name="fasst zusammen", m_src="0..*", m_dst="1..*"),
    # F2 Assoziation statt Komposition
    E("assoc", "modul", "pruefung", [(595, 248), (595, 380)],
      name="setzt an", m_src="1", m_dst="1..*"),
    # F5 Assoziation Dozent-Modul fehlt vollstaendig
    # F3 Kardinalitaet 1 statt 0..1
    E("assoc", "dozent", "pruefung", [(1025, 216), (1025, 450), (720, 450)],
      name="beaufsichtigt", m_src="1", m_dst="0..*"),
    # F4 Kardinalitaeten vertauscht
    E("assoc", "student", "studiengang", [(185, 380), (185, 248)],
      name="ist eingeschrieben in", m_src="1", m_dst="0..*"),
    E("compo", "student", "versuch", [(185, 534), (185, 660)],
      name="unternimmt", m_src="1", m_dst="0..*"),
    # A1 Assoziation statt Aggregation - zulaessig, nicht falsch
    E("assoc", "versuch", "pruefung",
      [(320, 720), (400, 720), (400, 490), (470, 490)],
      name="bezieht sich auf", m_src="0..*", m_dst="1"),
    E("gener", "klausur", "pruefung",
      [(545, 830), (545, 770), (645, 770), (645, 534)]),
    E("gener", "muendlich", "pruefung",
      [(845, 830), (845, 770), (645, 770), (645, 534)]),
    E("gener", "praesentation", "pruefung",
      [(1145, 830), (1145, 770), (645, 770), (645, 534)]),
    # F6 zweite Vererbungsebene geplaettet
    E("gener", "einzel", "pruefung",
      [(185, 1040), (185, 980), (690, 980), (690, 534)]),
    E("gener", "gruppe", "pruefung",
      [(500, 1040), (500, 980), (690, 980), (690, 534)]),
]
K_N = []


PAGES = [
    ("stufe_1", "Stufe 1 - Prüfungsverwaltung einer Hochschule",
     S1_W, S1_H, S1, S1_E, S1_N),
    ("stufe_2", "Stufe 2 - Die neue Prüfungsordnung",
     S2_W, S2_H, S2, S2_E, S2_N),
    ("stufe_2_diff", "Stufe 2 - Differenzansicht zu Stufe 1",
     S3_W, S3_H, S3, S3_E, S3_N),
    ("aufgabe_2_ki", "Modellentwurf eines KI-Werkzeugs zum Szenario",
     K_W, K_H, K, K_E, K_N),
]
