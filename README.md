# Claude/Codex Workspace

Dieser Workspace ist fuer zwei Agenten gedacht:

- Codex
- Claude / Claude Code

Andere Tools werden nur beruecksichtigt, wenn der Nutzer sie ausdruecklich fordert.

Ziel: Beide Agenten sollen denselben Projektstand verstehen und weiterbearbeiten koennen, ohne Arbeit zu doppeln, zu ueberschreiben oder ohne Kontext fortzusetzen.

## Struktur

```text
/
├── README.md              # Ueberblick, Ziel und Nutzung des Workspaces
├── AGENTS.md              # Hauptanweisung fuer Codex
├── CLAUDE.md              # Hauptanweisung fuer Claude
├── WORKLOG.md             # laufende Aenderungen und Entscheidungen
├── NEXT_STEPS.md          # offene Aufgaben und naechster sinnvoller Schritt
├── CHANGELOG.md           # abgeschlossene groessere Aenderungen
├── skills/                # gemeinsame wiederverwendbare Arbeitsweisen
├── agents/                # spezialisierte Agentenrollen
├── templates/             # Vorlagen fuer HSBA, EOS und allgemeine Aufgaben
└── .claude/               # Claude-Code-kompatible Spiegelung wichtiger Skills
```

## Arbeitskontext

Der Workspace ist auf Felix, EOS und HSBA optimiert.

Aktuelle Prioritaet:

1. HSBA-Praesentationen
2. HSBA-Textschreiben
3. Projektanweisungen
4. EOS-Praesentationen
5. Dokumentpruefung
6. kurze E-Mails

Praesentationen und Schreibaufgaben werden zuerst praezisiert. Danach soll fuer jede wiederkehrende Aufgabenart ein eigener, passender Skill oder ein klares Template existieren.

Aktuell angelegte Spezial-Skills:

- `skills/hsba-praesentation/`
- `skills/hsba-textschreiben/`
- `skills/projektanweisung/`
- `skills/eos-praesentation/`
- `skills/dokumentpruefung/`
- `skills/kurze-email/`

## Nutzung

Zu Beginn einer Arbeitssitzung soll der Agent diese Dateien pruefen:

1. `README.md`
2. eigene Hauptanweisung:
   - Codex: `AGENTS.md`
   - Claude: `CLAUDE.md`
3. `WORKLOG.md`
4. `NEXT_STEPS.md`
5. relevante Dateien aus `skills/`, `agents/` oder `templates/`

## Grundprinzip

Der gemeinsame Kontext entsteht ueber Dateien im Workspace, nicht ueber automatisch geteiltes Chat-Gedaechtnis.

Vor Aenderungen:

- bestehende Dateien lesen
- aktuellen Stand verstehen
- keine unbekannten Aenderungen ueberschreiben
- keine Dateien loeschen, ohne dass es ausdruecklich verlangt wurde
- Aenderungen eng am Ziel halten

Nach relevanten Aenderungen:

- `WORKLOG.md` kurz aktualisieren
- offene Punkte in `NEXT_STEPS.md` eintragen
- groessere abgeschlossene Aenderungen in `CHANGELOG.md` dokumentieren

## Standard-Arbeitsmodus

Wenn der Nutzer keinen Plan verlangt, soll direkt umgesetzt werden.

Bei Unsicherheiten soll kurz nachgefragt werden, bevor falsche Annahmen zu unstimmigen Ergebnissen fuehren.

## Rollen

Codex eignet sich besonders fuer:

- Dateien und Ordnerstrukturen anlegen
- Skills technisch vorbereiten
- README, AGENTS.md und CLAUDE.md pflegen
- Projektstruktur umsetzen
- Arbeitslogik versionierbar machen

Claude eignet sich besonders fuer:

- laengere Textarbeit
- Stil- und Praesentationslogik
- konzeptionelle Ausarbeitung
- Skill-Inhalte formulieren
- Schreib- und Praesentationsvorlagen verbessern

Diese Rollen sind Orientierung, keine harte Grenze.
