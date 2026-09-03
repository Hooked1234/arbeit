# -*- coding: utf-8 -*-
"""Layoutmodell der drei UML-Klassendiagramme (Auflage 3)."""

NAVY = "#173B57"
ACCENT = "#8A6A2F"

HDR = 30      # Kopfzeile Klassenname
PAD = 7       # Innenabstand je Fach
LINE = 16     # Zeilenhoehe


class C:
    """Klasse im Diagramm."""

    def __init__(self, key, name, x, y, w, attrs=(), ops=(), abstract=False,
                 stereotype=None, literals=None):
        self.key, self.name, self.x, self.y, self.w = key, name, x, y, w
        self.attrs, self.ops = list(attrs), list(ops)
        self.abstract, self.stereotype = abstract, stereotype
        self.literals = list(literals) if literals else None

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


# --------------------------------------------------------------------------
# Aufgabe 1 - Bestellsystem eines Onlineshops
# --------------------------------------------------------------------------
A1_W, A1_H = 1280, 700
A1 = [
    C("kunde", "Kunde", 60, 110, 270,
      ["-kundennummer: String", "-name: String", "-eMailAdresse: String"],
      ["+eMailAdresseÄndern(neu: String): void"]),
    C("bestellung", "Bestellung", 480, 110, 300,
      ["-bestellnummer: String", "-bestelldatum: Date",
       '-status: String = "offen"'],
      ["+stornieren(): void"]),
    C("position", "Bestellposition", 480, 380, 300,
      ["-menge: Integer", "-einzelpreis: Decimal"],
      ["+positionsbetragBerechnen(): Decimal"]),
    C("produkt", "Produkt", 930, 380, 280,
      ["-produktnummer: String", "-bezeichnung: String",
       "-aktuellerPreis: Decimal"],
      ["+preisÄndern(neu: Decimal): void"]),
    C("sortiment", "Sortiment", 930, 110, 300,
      ["-name: String"],
      ["+produktAufnehmen(p: Produkt): void",
       "+produktEntfernen(p: Produkt): void"]),
]
A1_E = [
    E("assoc", "kunde", "bestellung", [(330, 171), (480, 171)],
      name="gibt auf", m_src="1", m_dst="0..*"),
    E("compo", "bestellung", "position", [(630, 232), (630, 380)],
      name="besteht aus", m_src="1", m_dst="1..*"),
    E("assoc", "position", "produkt", [(780, 433), (930, 433)],
      name="bezieht sich auf", m_src="0..*", m_dst="1"),
    E("aggr", "sortiment", "produkt", [(1080, 216), (1080, 380)],
      name="führt", m_src="0..*", m_dst="0..*"),
]
A1_N = [
    N(60, 560, 700,
      ["{menge >= 1}",
       "Bestellposition.einzelpreis bleibt bei späteren",
       "Preisänderungen am Produkt unverändert."]),
]

# --------------------------------------------------------------------------
# Aufgabe 2 - Hotelverwaltung
# --------------------------------------------------------------------------
A2_W, A2_H = 1700, 1020
A2 = [
    C("gast", "Gast", 60, 110, 320,
      ["-gastnummer: String", "-name: String", "-eMailAdresse: String"],
      ["+reservierungAnlegen(von: Date, bis: Date): Reservierung"]),
    C("reservierung", "Reservierung", 530, 110, 300,
      ["-reservierungsnummer: String", "-anreise: Date", "-abreise: Date",
       "-status: Reservierungsstatus", "/gesamtpreis: Money",
       "mehrwertsteuersatz: Decimal"],
      ["+bestätigen(): void", "+stornieren(): void"]),
    C("bposition", "Buchungsposition", 530, 400, 280,
      ["-positionsnummer: Integer", "-anzahl: Integer", "-einzelpreis: Money"],
      ["+positionspreisErmitteln(): Money"]),
    C("leistung", "BuchbareLeistung", 960, 400, 340,
      ["-leistungsnummer: String", "-bezeichnung: String", "-grundpreis: Money"],
      ["+istVerfügbar(von: Date, bis: Date): Boolean {abstract}",
       "+preisBerechnen(von: Date, bis: Date): Money {abstract}"],
      abstract=True),
    C("zimmer", "Zimmer", 880, 660, 340,
      ["-zimmernummer: String", "-etage: Integer"],
      ["+istVerfügbar(von: Date, bis: Date): Boolean",
       "+preisBerechnen(von: Date, bis: Date): Money"]),
    C("zusatz", "Zusatzleistung", 1290, 660, 340,
      ["-kategorie: String"],
      ["+istVerfügbar(von: Date, bis: Date): Boolean",
       "+preisBerechnen(von: Date, bis: Date): Money"]),
    C("standard", "Standardzimmer", 830, 880, 210, ["-anzahlBetten: Integer"], []),
    C("suite", "Suite", 1100, 880, 210, ["-wohnflächeQm: Decimal"], []),
    C("enum", "Reservierungsstatus", 60, 400, 260, stereotype="enumeration",
      literals=["ANGELEGT", "BESTÄTIGT", "EINGECHECKT", "ABGESCHLOSSEN",
                "STORNIERT"]),
]
A2_E = [
    E("assoc", "gast", "reservierung", [(380, 171), (530, 171)],
      name="tätigt", m_src="1", m_dst="0..*"),
    E("compo", "reservierung", "bposition", [(670, 296), (670, 400)],
      name="besteht aus", m_src="1", m_dst="1..*"),
    E("navassoc", "bposition", "leistung", [(810, 461), (960, 461)],
      name="bezieht sich auf", m_src="0..*", m_dst="1"),
    E("gener", "zimmer", "leistung", [(1050, 660), (1050, 600), (1130, 600),
                                      (1130, 538)]),
    E("gener", "zusatz", "leistung", [(1460, 660), (1460, 600), (1130, 600),
                                      (1130, 538)]),
    E("gener", "standard", "zimmer", [(935, 880), (935, 830), (1050, 830),
                                      (1050, 782)]),
    E("gener", "suite", "zimmer", [(1205, 880), (1205, 830), (1050, 830),
                                   (1050, 782)]),
]
A2_N = [
    N(60, 620, 620,
      ["Ein Zimmer ist in einem Zeitraum nur verfügbar, wenn keine",
       "bestätigte oder eingecheckte Reservierung den Zeitraum",
       "[anreise, abreise) überlappt.",
       "{Leistung ist Zimmer  =>  anzahl = 1}"]),
]

# --------------------------------------------------------------------------
# Aufgabe 3 - Veranstaltungsmanagement
# --------------------------------------------------------------------------
A3_W, A3_H = 1800, 1010
A3 = [
    C("veranstalter", "Veranstalter", 140, 110, 300,
      ["-veranstalterId: String", "-name: String"],
      ["+mitarbeiterAufnehmen(m: Mitarbeiter): void",
       "+mitarbeiterAbgeben(m: Mitarbeiter): void"]),
    C("mitarbeiter", "Mitarbeiter", 140, 420, 300,
      ["-personalnummer: String", "-name: String"],
      ["+veranstaltungÜbernehmen(v: Veranstaltung): void"]),
    C("veranstaltung", "Veranstaltung", 680, 110, 300,
      ["-titel: String", "-zeitraum: Zeitraum", "-ticketpreis: Money"],
      ["+absagen(grund: String): void"], abstract=True),
    C("praesenz", "Präsenzveranstaltung", 620, 580, 250,
      ["-einlassAb: DateTime"], ["+freiePlätzeErmitteln(): Integer"]),
    C("online", "Onlineveranstaltung", 960, 580, 250,
      ["-plattform: String", "-zugangsUrl: URL"], []),
    C("ort", "Veranstaltungsort", 500, 790, 300,
      ["-name: String", "-adresse: String", "-kapazität: Integer"],
      ["+istVerfügbar(zeitraum: Zeitraum): Boolean"]),
    C("teilnehmer", "Teilnehmer", 1310, 110, 320,
      ["-teilnehmerId: String", "-name: String"],
      ["+buchen(v: Veranstaltung, plätze: Integer): Buchung"]),
    C("buchung", "Buchung", 1310, 420, 280,
      ["-buchungsId: String", "-anzahlPlätze: Integer",
       "-status: Buchungsstatus", "/betrag: Money"],
      ["+bestätigen(): void", "+stornieren(): void"]),
    C("betreuung", "Betreuung", 460, 280, 220,
      ["-rolle: String", "-einsatzzeitraum: Zeitraum"], []),
    C("enum3", "Buchungsstatus", 1310, 680, 220, stereotype="enumeration",
      literals=["ANGELEGT", "BESTÄTIGT", "STORNIERT"]),
]
A3_E = [
    E("aggr", "veranstalter", "mitarbeiter", [(290, 232), (290, 420)],
      name="beschäftigt", m_src="1", m_dst="0..*"),
    E("assoc", "veranstalter", "veranstaltung", [(440, 169), (680, 169)],
      name="organisiert", m_src="1", m_dst="0..*"),
    E("assoc", "mitarbeiter", "veranstaltung",
      [(440, 471), (760, 471), (760, 232)],
      name="betreut", m_src="0..*", m_dst="0..*",
      name_at=(600, 460), m_src_at=(455, 460), m_dst_at=(770, 250)),
    E("dashed", "betreuung", None, [(570, 370), (570, 471)]),
    E("gener", "praesenz", "veranstaltung",
      [(745, 580), (745, 530), (900, 530), (900, 232)]),
    E("gener", "online", "veranstaltung",
      [(1085, 580), (1085, 530), (900, 530), (900, 232)]),
    E("assoc", "praesenz", "ort",
      [(745, 670), (745, 730), (650, 730), (650, 790)],
      name="findet statt an", m_src="0..*", m_dst="1",
      name_at=(700, 745), m_src_at=(762, 700), m_dst_at=(665, 778)),
    E("assoc", "teilnehmer", "buchung", [(1460, 216), (1460, 420)],
      name="tätigt", m_src="1", m_dst="0..*"),
    E("assoc", "buchung", "veranstaltung",
      [(1310, 495), (1250, 495), (1250, 169), (980, 169)],
      name="bezieht sich auf", m_src="0..*", m_dst="1",
      name_at=(1262, 340), m_src_at=(1295, 483), m_dst_at=(995, 157)),
    E("assoc", "mitarbeiter", "mitarbeiter",
      [(140, 430), (30, 430), (30, 520), (140, 520)],
      name="berichtet an", r_src="vorgesetzter", r_dst="unterstellte",
      m_src="0..1", m_dst="0..*",
      name_at=(85, 479, "middle"), m_src_at=(130, 417, "end"),
      m_dst_at=(130, 537, "end"), r_src_at=(130, 449, "end"),
      r_dst_at=(130, 509, "end")),
]
A3_N = [
    N(915, 492, 260, ["{disjoint, complete}",
                      "Generalisierungsmenge Durchführungsform"], plain=True),
    N(940, 800, 700,
      ["{Onlineveranstaltung hat keine Beziehung zu Veranstaltungsort}",
       "{Summe der Plätze bestätigter Buchungen einer",
       " Präsenzveranstaltung <= Veranstaltungsort.kapazität}",
       "/betrag = anzahlPlätze * Veranstaltung.ticketpreis"]),
]

PAGES = [
    ("aufgabe_1", "Aufgabe 1 - Bestellsystem eines Onlineshops", A1_W, A1_H,
     A1, A1_E, A1_N),
    ("aufgabe_2", "Aufgabe 2 - Hotelverwaltung", A2_W, A2_H, A2, A2_E, A2_N),
    ("aufgabe_3", "Aufgabe 3 - Veranstaltungsmanagement", A3_W, A3_H, A3, A3_E,
     A3_N),
]
