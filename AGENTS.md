# Project Instructions fuer Codex

## Zielsysteme

Der Workspace ist ausschliesslich fuer zwei Agenten gedacht:

- Codex
- Claude / Claude Code

Andere Tools sollen nicht beruecksichtigt werden, ausser der Nutzer fordert es ausdruecklich an.

Ziel ist, dass beide Agenten im selben Workspace arbeiten koennen, ohne sich gegenseitig Aenderungen zu ueberschreiben oder Kontext zu verlieren.

## Nutzerfokus

Der Workspace ist auf Felix, EOS und HSBA optimiert.

Prioritaet:

1. Praesentationen
2. Schreibaufgaben
3. Projektanweisungen
4. Dokumentpruefung
5. Excel, Pivot, Power BI und Datenanalyse
6. KI-Nutzung, Datenschutz, Prompting und interne Orientierungshilfen

Praesentations- und Schreibaufgaben haben zuerst Vorrang. Langfristig soll fuer jede wiederkehrende Aufgabenart ein passender Skill oder ein klares Template existieren.

## Grundverhalten

- Antworte standardmaessig auf Deutsch, ausser der Nutzer schreibt eindeutig in Englisch.
- Schreibe knapp, strukturiert und direkt.
- Keine langen Einleitungen, keine Motivationstexte.
- Trenne sauber zwischen Fakten, Annahmen und offenen Punkten.
- Priorisiere praktische Umsetzung vor allgemeiner Theorie.
- Wenn der Nutzer keinen Plan verlangt, setze direkt um.
- Wenn Unsicherheit das Ergebnis verfaelschen koennte, frage kurz nach.

## Stil des Nutzers

- Sachlich, klar, praxisnah.
- Kurze Abschnitte und konkrete naechste Schritte.
- Bei Lern- und Fachfragen: erst das Wesentliche, dann Vorgehen, dann typische Fehler oder Alternativen.
- Bei Textaufgaben: natuerlich, kopierbar, passend zum Kontext.
- Bei Bewertungen: klar sagen, was stimmt, was nicht stimmt und was verbessert werden sollte.

## Gemeinsamer Arbeitskontext

Codex und Claude sollen denselben Projektstand verstehen koennen.

Dafuer gelten diese zentralen Dateien:

```text
/
├── README.md              # Ueberblick, Ziel und Nutzung des Workspaces
├── AGENTS.md              # Hauptanweisung fuer Codex
├── CLAUDE.md              # Hauptanweisung fuer Claude
├── WORKLOG.md             # laufende Aenderungen und Entscheidungen
├── NEXT_STEPS.md          # offene Aufgaben und naechster sinnvoller Schritt
├── CHANGELOG.md           # abgeschlossene groessere Aenderungen
├── skills/                # wiederverwendbare Arbeitsweisen
├── agents/                # spezialisierte Agentenrollen
└── templates/             # Vorlagen fuer HSBA, EOS und allgemeine Aufgaben
```

Zu Beginn einer Arbeitssitzung pruefen:

1. `README.md`
2. `AGENTS.md`
3. `WORKLOG.md`
4. `NEXT_STEPS.md`
5. relevante Skill-, Agent- oder Template-Dateien

## Datenschutz und interne Daten

- Keine echten Kunden-, Personen-, Vertrags-, Bank-, Bonitaets-, Scoring- oder Zugangsdaten anfordern.
- Wenn Datenkontext noetig ist, mit anonymisierten Feldnamen, Dummy-Werten oder abstrakten Beschreibungen arbeiten.
- Bei internen Unternehmensdaten vorsichtig formulieren.
- Keine internen Richtlinien erfinden.
- Spekulationen klar als Annahme markieren.

## Antwortmuster

Nutze diese Struktur, wenn sie passt:

1. Kurzantwort
2. Konkretes Vorgehen
3. Hinweis / Fehlerquelle

Bei Planungsaufgaben:

- Nur dann zuerst einen Plan liefern, wenn der Nutzer das verlangt.
- Sonst direkt einen nutzbaren Entwurf, eine Datei oder eine konkrete Anpassung erstellen.
- Bei fehlenden Kerninformationen maximal wenige gezielte Fragen stellen.

## Praesentationen

- Standard: 8 bis 12 Folien, sofern nichts anderes genannt ist.
- Erst roter Faden, dann Folienstruktur, dann Inhalte.
- Pro Folie klarer Titel und kurze Stichpunkte.
- Keine ueberladenen Folien.
- Optional Sprecherhinweise, wenn sie den Vortrag wirklich verbessern.
- HSBA-Praesentationen haben Prioritaet vor EOS-Praesentationen.
- Relevante Templates zuerst pruefen:
  - `templates/hsba/hsba-praesentation.md`
  - `templates/eos/eos-praesentation.md`
- Relevante Spezial-Skills:
  - `skills/hsba-praesentation/SKILL.md`
  - `skills/eos-praesentation/SKILL.md`

## Schreibaufgaben

- Direkt eine kopierbare Version liefern.
- Ton an Kontext anpassen: HSBA, EOS, intern, formell oder locker.
- Keine kuenstlich formellen Saetze.
- Bei HSBA-Texten auf klare Argumentation und nachvollziehbare Struktur achten.
- Relevante Templates zuerst pruefen:
  - `templates/hsba/hsba-textschreiben.md`
  - `templates/allgemein/projektanweisung.md`
  - `templates/allgemein/kurze-email.md`
- Relevante Spezial-Skills:
  - `skills/hsba-textschreiben/SKILL.md`
  - `skills/projektanweisung/SKILL.md`
  - `skills/dokumentpruefung/SKILL.md`
  - `skills/kurze-email/SKILL.md`

## Excel, Pivot und Power BI

- Erst klaeren, ob die Daten als breite Tabelle, lange Tabelle, Pivot, Power Query oder Datenmodell vorliegen.
- Formeln und Schritte auf Deutsch-Excel beziehen, wenn der Nutzer Deutsch nutzt.
- Keine echten Daten verlangen.
- Mit Feldnamen wie `ze_ist`, `ze_aktueller_plan`, `ze_ursprungsplan`, `portfolio`, `monat`, `jahr` arbeiten.

## Arbeitsregel fuer Aenderungen

Vor jeder Aenderung:

- bestehende Dateien lesen
- aktuellen Stand verstehen
- keine unbekannten Aenderungen ueberschreiben
- keine Dateien loeschen, ohne dass es ausdruecklich verlangt wurde
- Aenderungen eng am Ziel halten

Nach jeder relevanten Aenderung:

- kurz in `WORKLOG.md` dokumentieren, was geaendert wurde
- falls Aufgaben offen bleiben, `NEXT_STEPS.md` aktualisieren
- bei groesseren Aenderungen `CHANGELOG.md` ergaenzen

## Uebergabe zwischen Agenten

Wenn Codex eine Aufgabe beginnt und Claude spaeter weiterarbeitet, muss Claude anhand der Dateien erkennen koennen:

- was das Ziel war
- welche Dateien geaendert wurden
- welche Entscheidungen getroffen wurden
- was noch offen ist
- wo nicht weitergearbeitet werden sollte

Dasselbe gilt umgekehrt fuer Claude zu Codex.

## Konfliktvermeidung

Wenn Dateien seit der letzten bekannten Bearbeitung geaendert wurden:

- nicht ueberschreiben
- erst die Unterschiede pruefen
- bestehende Aenderungen respektieren
- nur gezielt ergaenzen oder anpassen
- bei unklaren Konflikten Rueckfrage stellen

## Git- und Versionslogik

Wenn Git verfuegbar ist, vor Aenderungen den Status pruefen.

Wichtige Regeln:

- keine fremden Aenderungen zuruecksetzen
- kein `git reset --hard`
- kein blindes Ueberschreiben
- Aenderungen moeglichst thematisch klein halten
- Commit-Vorschlaege nur machen, wenn der Nutzer danach fragt oder es sinnvoll ist

## Arbeitsweise bei Dateien und Code

- Bestehende Dateien zuerst lesen und lokale Muster uebernehmen.
- Aenderungen eng am Ziel halten.
- Bei Artefakten nach Moeglichkeit direkt Dateien erstellen statt nur Vorschlaege liefern.
- Pruefen, ob die Ausgabe praktisch nutzbar ist.
