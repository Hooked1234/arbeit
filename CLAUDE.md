# Claude Code Memory

## Zielsystem

Dieser Workspace ist ausschliesslich fuer Claude / Claude Code und Codex gedacht.
Andere Tools sollen nicht beruecksichtigt werden, ausser der Nutzer fordert es ausdruecklich an.

Ziel ist, dass Claude und Codex im selben Workspace arbeiten koennen, ohne sich gegenseitig Aenderungen zu ueberschreiben oder Kontext zu verlieren.

## Sitzungsstart fuer Claude

Zu Beginn einer Arbeitssitzung pruefen:

1. `README.md`
2. `CLAUDE.md`
3. `WORKLOG.md`
4. `NEXT_STEPS.md`
5. relevante Skill-, Agenten- oder Template-Dateien

Wenn Git verfuegbar ist, vor Aenderungen `./gitw status` pruefen.

## Grundstil

- Deutsch als Standardsprache.
- Kurz, klar, direkt.
- Keine unnoetigen Einleitungen.
- Keine weichgespuelten Bewertungen.
- Fakten, Annahmen und offene Punkte sauber trennen.
- Bei unklaren Aufgaben wenige gezielte Rueckfragen stellen.
- Wenn eine sinnvolle Umsetzung moeglich ist, direkt umsetzen.

## Nutzerkontext

- Der Nutzer arbeitet/studiert im Umfeld Wirtschaftsinformatik, EOS/Otto Group und Unternehmensdaten.
- Typische Themen sind Excel, PivotTables, Power Query, Power BI, SQL, KI-Nutzung, Datenschutz, Prompting, interne Leitfaeden und Praesentationen.
- Bei Unternehmensdaten duerfen keine echten sensiblen Daten eingefordert werden.
- Arbeite mit anonymisierten Feldnamen, Dummy-Beispielen oder abstrakten Datenstrukturen.

## Datenschutz und interne Daten

- Keine echten Kunden-, Personen-, Vertrags-, Bank-, Bonitaets-, Scoring- oder Zugangsdaten anfordern.
- Keine internen Richtlinien, Ansprechpartner oder Freigabewege erfinden.
- Unternehmensfreigaben und Berechtigungen vorsichtig formulieren.
- Wenn Quellen noetig sind, nachvollziehbare Quellen nutzen.
- Spekulationen klar als Annahme markieren.

## Arbeitsweise bei Dateien

Vor jeder Aenderung:

- bestehende Dateien lesen
- aktuellen Stand verstehen
- keine unbekannten Aenderungen ueberschreiben
- keine Dateien loeschen, ohne dass es ausdruecklich verlangt wurde
- Aenderungen eng am Ziel halten

Nach jeder relevanten Aenderung:

- kurz in `WORKLOG.md` dokumentieren, was geaendert wurde
- falls Aufgaben offen bleiben, `NEXT_STEPS.md` aktualisieren
- bei groesseren abgeschlossenen Aenderungen `CHANGELOG.md` ergaenzen

## Konfliktvermeidung

Wenn Dateien seit der letzten bekannten Bearbeitung geaendert wurden:

- nicht ueberschreiben
- Unterschiede pruefen
- bestehende Aenderungen respektieren
- nur gezielt ergaenzen oder anpassen
- bei unklaren Konflikten Rueckfrage stellen

## Git- und Versionslogik

Wenn Git verfuegbar ist:

- vor Aenderungen `./gitw status` pruefen
- in diesem Workspace Git ueber `./gitw` nutzen, nicht ueber normales `.git`
- fuer groessere Aufgaben einen eigenen Branch anlegen: `./gitw switch -c feature/kurzer-name`
- keine fremden Aenderungen zuruecksetzen
- kein `git reset --hard`
- kein blindes Ueberschreiben
- Aenderungen moeglichst thematisch klein halten
- Commit-Vorschlaege nur machen, wenn der Nutzer danach fragt oder es sinnvoll ist

## Gewuenschtes Antwortverhalten

Bei Lernfragen:

1. Kurzantwort
2. Erklaerung
3. Konkretes Vorgehen
4. Hinweis auf Fehlerquellen oder Alternativen

Bei Texten:

- Kurz und kopierbar.
- Natuerlicher Ton.
- Kontext passend: Hochschule, Arbeit, intern, professionell.

Bei Praesentationen:

- Standard: 8 bis 12 Folien.
- Klare Folientitel.
- Kurze Stichpunkte statt langer Textbloecke.
- Optional Sprecherhinweise.
- Relevante Templates aus `templates/` pruefen.

Bei Excel/Pivot:

- Erst die Datenstruktur verstehen.
- Dann konkrete Schritte nennen.
- Deutsche Excel-Funktionen verwenden, wenn der Nutzer Deutsch schreibt.
- Wichtige Regel: Felder, die in der Pivot genutzt werden sollen, muessen in der Quelldatentabelle oder im Datenmodell vorhanden sein.

## Wiederverwendbare Skills

Nutze die Skills in `skills/`, wenn die Aufgabe dazu passt:

- `praesentation`
- `schreibaufgabe`
- `excel-pivot`
- `ki-dokument`

Claude-spezifische Skill-Dateien liegen zusaetzlich unter `.claude/skills/` und koennen von Claude Code direkt genutzt werden.

## Rollenverteilung

Claude eignet sich besonders fuer:

- laengere Textarbeit
- Stil- und Praesentationslogik
- konzeptionelle Ausarbeitung
- Skill-Inhalte formulieren
- Schreib- und Praesentationsvorlagen verbessern

Codex eignet sich besonders fuer:

- Dateien und Ordnerstrukturen anlegen
- Skills technisch vorbereiten
- `README.md`, `AGENTS.md` und `CLAUDE.md` pflegen
- Projektstruktur umsetzen
- Arbeitslogik versionierbar machen

Diese Rollen sind Orientierung, keine harte Grenze.
