# -*- coding: utf-8 -*-
"""Prueft, dass Stufe 2 das Modell aus Stufe 1 enthaelt.

Stufe 2 ist seit dem 30.08. Reserve: Block 2 ist die KI-Kritik, nicht mehr der
Aenderungsauftrag. Die Pruefung bleibt, damit die Reserve gueltig bleibt, falls
das KI-Werkzeug im Raum ausfaellt.

Erlaubt sind ausschliesslich die im Aenderungsauftrag angekuendigten Umbauten.
Jede andere Abweichung ist ein Fehler: Die Gruppen bekommen die Loesung zu
Stufe 1 zu Beginn von Block 2 ausgehaendigt und bauen darauf auf.

Aufruf:  python _generator/check_konsistenz.py
"""
from model import S1, S1_E, S2, S2_E

# --------------------------------------------------------------- Sollzustand
# einzel und gruppe stehen seit dem 30.08. bereits in Stufe 1: sie tragen die
# mehrstufige Vererbung und damit Kriterium 9, das sonst ungedeckt bliebe.
NEUE_KLASSEN = {"modulzuordnung", "leistung", "anerkannt"}

# Klasse -> (Attribute die weggehen, Methoden die weggehen), mit Ziel
UMZUG = {
    "versuch": {
        "attrs": {"datum", "note"},
        "ops": {"alsBestandenVerbuchen()"},
        "ziel": "leistung",
        "grund": "Datum und Note sind ab Aufgabe 2 gemeinsame Merkmale",
    },
}

ENTFALLENE_KANTEN = {
    ("aggr", "studiengang", "modul"),
}

ERSETZTE_KANTEN = {
    ("compo", "student", "versuch"): ("compo", "student", "leistung"),
}

NEUE_KANTEN = {
    ("compo", "studiengang", "modulzuordnung"),
    ("aggr", "modulzuordnung", "modul"),
    ("gener", "anerkannt", "leistung"),
    ("gener", "versuch", "leistung"),
    ("aggr", "anerkannt", "modul"),
}


def sig(e):
    return (e.kind, e.src, e.dst)


def mult(e):
    return (e.m_src, e.m_dst, e.name)


def main():
    errs, notes = [], []
    c1 = {c.key: c for c in S1}
    c2 = {c.key: c for c in S2}

    # 1 Keine Klasse aus Stufe 1 darf verschwinden
    for k in c1:
        if k not in c2:
            errs.append("Klasse aus Stufe 1 fehlt in Stufe 2: %s" % k)

    # 2 Neue Klassen muessen genau die angekuendigten sein
    neu = set(c2) - set(c1)
    if neu != NEUE_KLASSEN:
        errs.append("neue Klassen weichen ab: %s statt %s"
                    % (sorted(neu), sorted(NEUE_KLASSEN)))

    # 3 Inhalte uebernommener Klassen: nur angekuendigte Umzuege
    for k, a in c1.items():
        if k not in c2:
            continue
        b = c2[k]
        if a.name != b.name:
            errs.append("Klassenname geaendert: %s -> %s" % (a.name, b.name))
        weg_a = set(a.attrs) - set(b.attrs)
        weg_o = set(a.ops) - set(b.ops)
        soll = UMZUG.get(k, {})
        if weg_a != set(soll.get("attrs", ())):
            errs.append("%s: unerwartet entfernte Attribute %s"
                        % (k, sorted(weg_a - set(soll.get("attrs", ())))))
        if weg_o != set(soll.get("ops", ())):
            errs.append("%s: unerwartet entfernte Methoden %s"
                        % (k, sorted(weg_o - set(soll.get("ops", ())))))
        if soll:
            ziel = c2[soll["ziel"]]
            fehlt = (soll["attrs"] - set(ziel.attrs)) | \
                    (soll["ops"] - set(ziel.ops))
            if fehlt:
                errs.append("%s: umgezogene Elemente fehlen in %s: %s"
                            % (k, soll["ziel"], sorted(fehlt)))
            else:
                notes.append("%s -> %s: %s (%s)"
                             % (k, soll["ziel"],
                                ", ".join(sorted(soll["attrs"] | soll["ops"])),
                                soll["grund"]))

    # 4 Kanten
    e1 = {sig(e): e for e in S1_E}
    e2 = {sig(e): e for e in S2_E}
    for s, e in e1.items():
        if s in e2:
            if mult(e) != mult(e2[s]):
                errs.append("Kardinalitaet oder Name geaendert bei %s: %s -> %s"
                            % (str(s), mult(e), mult(e2[s])))
            continue
        if s in ENTFALLENE_KANTEN:
            notes.append("entfallen wie angekuendigt: %s" % str(s))
        elif s in ERSETZTE_KANTEN:
            neu_s = ERSETZTE_KANTEN[s]
            if neu_s in e2:
                notes.append("ersetzt wie angekuendigt: %s -> %s"
                             % (str(s), str(neu_s)))
            else:
                errs.append("Ersatzkante fehlt: %s" % str(neu_s))
        else:
            errs.append("Kante aus Stufe 1 fehlt unangekuendigt: %s" % str(s))

    zusatz = set(e2) - set(e1) - set(ERSETZTE_KANTEN.values())
    if zusatz != NEUE_KANTEN:
        errs.append("neue Kanten weichen ab: %s statt %s"
                    % (sorted(map(str, zusatz)), sorted(map(str, NEUE_KANTEN))))

    # 5 Jede Klasse ist verbunden
    for cs, es, tag in ((S1, S1_E, "Stufe 1"), (S2, S2_E, "Stufe 2")):
        verbunden = set()
        for e in es:
            verbunden.add(e.src)
            verbunden.add(e.dst)
        for c in cs:
            if c.key not in verbunden:
                errs.append("%s: Klasse ohne Beziehung: %s" % (tag, c.key))

    print("Konsistenzpruefung Stufe 1 -> Stufe 2")
    print("  Stufe 1: %d Klassen, %d Kanten" % (len(S1), len(S1_E)))
    print("  Stufe 2: %d Klassen, %d Kanten" % (len(S2), len(S2_E)))
    for n in notes:
        print("  angekuendigt:", n)
    if errs:
        print("FEHLER:")
        for e in errs:
            print("   -", e)
        return 1
    print("BESTANDEN: Stufe 1 ist bis auf die angekuendigten Umbauten "
          "vollstaendig in Stufe 2 enthalten.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
