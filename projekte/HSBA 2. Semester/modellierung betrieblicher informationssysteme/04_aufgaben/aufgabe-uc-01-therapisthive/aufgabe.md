# Aufgabe 1 — Online-Therapie „TherapistHive“ (UML-Use-Case-Diagramm)

- **Quelle:** `UML Use Case Vertiefungsübungen.pptx`, Folie 4 (Aeneas Christodoulou, Kea Knoll)
- **Modul:** Modellierung betrieblicher Informationssysteme, HSBA, 2. Semester
- **Datum der Bearbeitung:** 2026-09-02
- **Empfohlenes Werkzeug laut Folie 2:** Visual Paradigm Online
  (<https://online.visual-paradigm.com/de/diagrams/features/use-case-diagram-software/>)

## Aufgabenstellung (wörtlich)

Die Firma „TherapistHive“ betreibt eine Online-Plattform zur Vermittlung und
Durchführung psychologischer Therapien. Über die Plattform können verschiedene
Nutzendengruppen miteinander interagieren und diverse digitale Dienstleistungen
in Anspruch nehmen.

Jede*r **Patient*in** muss zu Beginn ein **Benutzerkonto** in TherapistHive
anlegen. Bei der Registrierung müssen die persönlichen Daten **Vor- und
Nachname**, **Geburtsdatum**, **Adresse**, **Krankenversicherung** und
**E-Mail-Adresse** angegeben werden und ein **Passwort** muss festgelegt werden.

Nach diesen Schritten kann sich die nutzende Person normal **anmelden**, indem
die **E-Mail-Adresse** als Nutzername und das **Passwort** korrekt eingegeben
werden.

**Patient*innen** können auf der Plattform nach geeigneten **Therapeut*innen**
suchen. Dafür können sie **optional** die Suchkriterien **Fachgebiet**,
**Sprache**, **Verfügbarkeit** oder **Behandlungsform** nutzen, müssen dies aber
nicht, um Suchergebnisse zu erhalten. Jeder Therapiesuchende kann sich nach
erfolgreicher Suche das **Profil** jedes oder jeder Therapeut*in ansehen, jedoch
nicht andersherum.

Über die Plattform können Patient*innen nach **Suche** und **Auswahl** eines
oder einer geeigneten Therapeut*in **Terminanfragen schicken**. Wenn Termine
angefragt wurden, kann die therapierende Person diese **öffnen**. Diese können
dann entscheiden, ob sie die **Anfrage annehmen** oder **ablehnen**. Wird der
Termin angenommen, erhält der/die Patient*in eine **Terminbestätigung**. Wird er
abgelehnt, so wird eine **Absage** verschickt.

Zum vereinbarten Zeitpunkt können Therapeut*in und Patient*in
**Online-Sitzungen** im Videocallsystem „**TheraZoom**“ durchführen. Hierfür
können **Video**-, **Audio**- und **optional Chatfunktionen** genutzt werden.
Außerdem hat der/die Therapeut*in die Möglichkeit, **Notizen anzulegen**. Diese
stehen allerdings nur dem/der Therapeut*in zur Verfügung.

Außerdem erhalten Therapiesuchende nach der Sitzung von dem/der Therapeut*in
eine **Bescheinigung**, die sie bei ihrer Krankenkasse im
**Krankenkassenportal** **einreichen** können. Diese muss die **Bescheinigung**
abrufen und übernimmt nach vollständiger **Prüfung der Personaldaten** die
**Kosten** für den/die Patient*in.

## Verbindliche Sprachkonstrukte (Folie 3)

| Konstrukt | Bedeutung | Merkregel |
|---|---|---|
| Akteur | Person, Rolle, Organisation oder externes System | steht **außerhalb** der Systemgrenze |
| Use Case | konkretes Ziel eines Akteurs, keine technische Funktion | liegt **innerhalb** der Systemgrenze |
| Assoziation | Nutzung einer Systemfunktion | Linie Akteur ↔ Use Case |
| Generalisierung | „ist-ein“ zwischen zwei Akteuren **oder** zwei Use Cases | Pfeil zum allgemeineren Element |
| «include» | Basis-Use-Case bezieht anderen **zwingend** ein | Pfeil zeigt **zum eingebundenen** Use Case |
| «extend» | Use Case erweitert anderen **optional** | Pfeil zeigt **zum Basis-Use-Case** |

## Offene Punkte / Annahmen

Werden in `arbeitsstand/loesung.md` dokumentiert.
