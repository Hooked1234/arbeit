# Arbeitsstand — Aufgabe 1 „TherapistHive“

**Stand: 2026-09-02 — Zwischenstand, noch keine Lösung.**

## Was vorliegt

`entwuerfe.json` enthält das Rohmaterial eines Mehr-Agenten-Laufs:

- **5 unabhängige Modellentwürfe** aus fünf Perspektiven
  (`lehrbuch`, `purist`, `granular`, `akteure`, `fallen`) — je mit Akteuren,
  Use Cases, Assoziationen, `include`/`extend`/Generalisierungen, Begründung
  je Element und einer Textabdeckungstabelle gegen den Aufgabentext.
- **15 Kritiken** — je Entwurf eine Prüfung auf Texttreue, auf UML-Korrektheit
  und auf Eignung als Hochschul-Musterlösung.

Größenordnung der Entwürfe: 5–6 Akteure, 17–30 Use Cases.

## Was fehlt

Die drei letzten Stufen des Laufs sind **nicht** ausgeführt worden (Session-Limit):

1. **Synthese** der fünf Entwürfe zu einem kanonischen Modell
2. **Kritik** des Synthesemodells (Vollständigkeit, Regel-Audit, Advocatus
   Diaboli, Layoutplanung)
3. **Finalisierung**

Damit gibt es **noch kein abgestimmtes Modell und kein Diagramm**. Die Entwürfe
in `entwuerfe.json` sind ungeprüftes Rohmaterial und widersprechen sich an
mehreren Stellen — sie sind ausdrücklich **keine** Musterlösung.

## Bekannte Streitpunkte zwischen den Entwürfen

- Verlauf der Systemgrenze rund um **Krankenkasse** und **Krankenkassenportal**:
  eigener Akteur je, ein Akteur, oder Vorgänge außerhalb der Systemgrenze
- Granularität bei **Registrierung** und **Anmeldung** (Dateneingabe als eigene
  Use Cases oder als Teil des Anwendungsfalls)
- Abbildung der vier **optionalen Suchkriterien** (vier `extend`, ein `extend`
  mit Generalisierungen, oder gar nicht)
- Einordnung von **„Profil ansehen“** (eigener Use Case am Akteur oder `extend`
  der Suche)
- Struktur der **Terminbearbeitung** (öffnen / entscheiden / annehmen /
  ablehnen) und der **Video-, Audio- und Chatfunktionen**

## Nächster Schritt

Lauf ab der Synthesestufe fortsetzen, danach Diagramm bauen
(`abgabe/` ist noch leer). Werkzeugfrage offen: Folie 2 der Aufgabenstellung
empfiehlt Visual Paradigm Online; das Repo nutzt für die bisherigen
UML-Lösungen `.drawio`.
