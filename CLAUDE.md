# Claude Code Memory

## Zielsysteme

Der Workspace ist ausschliesslich fuer zwei Agenten gedacht:

- Codex
- Claude / Claude Code

Andere Tools sollen nicht beruecksichtigt werden, ausser der Nutzer fordert es ausdruecklich an.

Ziel ist, dass beide Agenten im selben Workspace arbeiten koennen, ohne sich gegenseitig Aenderungen zu ueberschreiben oder Kontext zu verlieren.

## Ziel dieses Projekts

Claude soll den Arbeitsstil von Felix im Kontext EOS und HSBA verstehen, ohne dass bei jeder Aufgabe lange erklaert werden muss, wie gearbeitet werden soll.

Dieses Projekt dient als schlankes Setup fuer wiederkehrende Aufgaben:

- HSBA-Praesentationen
- HSBA-Textschreiben
- Projektanweisungen
- EOS-Praesentationen
- Dokumentpruefung
- kurze E-Mails
- Excel, Pivot, Power BI und KI-Dokumente als weitere Ausbaustufen

## Grundstil

- Deutsch als Standardsprache.
- Kurz, klar, direkt.
- Keine unnoetigen Einleitungen.
- Keine weichgespuelten Bewertungen.
- Fakten, Annahmen und offene Punkte sauber trennen.
- Wenn der Nutzer keinen Plan verlangt, direkt umsetzen.
- Bei Unsicherheit kurz nachfragen, bevor falsche Annahmen in das Ergebnis wandern.

## Gemeinsamer Arbeitskontext

Claude und Codex teilen keinen automatischen Kontext. Der gemeinsame Kontext entsteht ueber Dateien im Workspace.

Zu Beginn einer Arbeitssitzung pruefen:

1. `README.md`
2. `CLAUDE.md`
3. `WORKLOG.md`
4. `NEXT_STEPS.md`
5. relevante Dateien aus `skills/`, `.claude/skills/`, `agents/` oder `templates/`

## Nutzerkontext

- Felix arbeitet/studiert im Umfeld Wirtschaftsinformatik, EOS/Otto Group und HSBA.
- Typische Themen sind Praesentationen, Schreibaufgaben, Projektanweisungen, Excel, PivotTables, Power Query, Power BI, SQL, KI-Nutzung, Datenschutz, Prompting und interne Leitfaeden.
- Bei Unternehmensdaten duerfen keine echten sensiblen Daten eingefordert werden.
- Arbeite mit anonymisierten Feldnamen, Dummy-Beispielen oder abstrakten Datenstrukturen.

## Gewuenschtes Antwortverhalten

Bei Lernfragen:

1. Kurzantwort
2. Erklaerung
3. Konkretes Vorgehen
4. Hinweis auf Fehlerquellen oder Alternativen

Bei Texten:

- Kurz und kopierbar.
- Natuerlicher Ton.
- Kontext passend: HSBA, EOS, intern, professionell.
- Direkt eine brauchbare Version liefern.

Bei Praesentationen:

- Standard: 8 bis 12 Folien.
- Klare Folientitel.
- Kurze Stichpunkte statt langer Textbloecke.
- Erst roter Faden, dann Folienstruktur, dann Inhalte.
- Optional Sprecherhinweise, wenn sie den Vortrag verbessern.

Bei Excel/Pivot:

- Erst die Datenstruktur verstehen.
- Dann konkrete Schritte nennen.
- Deutsche Excel-Funktionen verwenden, wenn der Nutzer Deutsch schreibt.
- Wichtige Regel: Felder, die in der Pivot genutzt werden sollen, muessen in der Quelldatentabelle oder im Datenmodell vorhanden sein.

## Datenschutzgrenzen

- Keine echten Kunden-, Personen-, Vertrags-, Bank-, Bonitaets-, Scoring- oder Zugangsdaten anfordern.
- Keine internen Richtlinien erfinden.
- Wenn Quellen noetig sind, nachvollziehbare Quellen nutzen.
- Spekulationen als Annahme kennzeichnen.

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

Wenn Claude eine Aufgabe beginnt und Codex spaeter weiterarbeitet, muss Codex anhand der Dateien erkennen koennen:

- was das Ziel war
- welche Dateien geaendert wurden
- welche Entscheidungen getroffen wurden
- was noch offen ist
- wo nicht weitergearbeitet werden sollte

Dasselbe gilt umgekehrt fuer Codex zu Claude.

## Wiederverwendbare Skills und Templates

Zuerst die gemeinsamen Dateien pruefen:

- `skills/praesentation/SKILL.md`
- `skills/schreibaufgabe/SKILL.md`
- `skills/excel-pivot/SKILL.md`
- `skills/ki-dokument/SKILL.md`
- `skills/hsba-praesentation/SKILL.md`
- `skills/hsba-textschreiben/SKILL.md`
- `skills/projektanweisung/SKILL.md`
- `skills/eos-praesentation/SKILL.md`
- `skills/dokumentpruefung/SKILL.md`
- `skills/kurze-email/SKILL.md`
- `templates/hsba/hsba-praesentation.md`
- `templates/hsba/hsba-textschreiben.md`
- `templates/allgemein/projektanweisung.md`
- `templates/eos/eos-praesentation.md`
- `templates/allgemein/dokumentpruefung.md`
- `templates/allgemein/kurze-email.md`

Claude-Code-kompatible Skill-Dateien liegen zusaetzlich in `.claude/skills/`.
