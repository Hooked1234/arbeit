# Claude/Codex Workspace

Dieser Workspace ist fuer zwei Agenten gedacht:

- Codex
- Claude / Claude Code

Ziel ist, dass beide Agenten denselben Projektstand verstehen, ohne automatisch denselben Chatkontext vorauszusetzen. Der gemeinsame Kontext entsteht ueber Dateien in diesem Workspace.

## Zentrale Dateien

```text
/
|-- README.md              # Ueberblick, Ziel und Nutzung des Workspaces
|-- AGENTS.md              # Hauptanweisung fuer Codex
|-- CLAUDE.md              # Hauptanweisung fuer Claude / Claude Code
|-- WORKLOG.md             # laufende Aenderungen und Entscheidungen
|-- NEXT_STEPS.md          # offene Aufgaben und naechster sinnvoller Schritt
|-- CHANGELOG.md           # abgeschlossene groessere Aenderungen
|-- skills/                # agentenuebergreifende Arbeitsweisen
|-- agents/                # spezialisierte Agentenrollen
`-- templates/             # Vorlagen fuer EOS, HSBA und allgemeine Aufgaben
```

Zusaetzlich gibt es aktuell Claude-spezifische Dateien unter `.claude/`. Diese bleiben bestehen, damit Claude Code sie direkt nutzen kann.

## Nutzung

Starte Codex oder Claude Code aus diesem Ordner.

Zu Beginn einer Arbeitssitzung soll der Agent diese Dateien lesen:

1. `README.md`
2. eigene Hauptanweisung:
   - Codex: `AGENTS.md`
   - Claude: `CLAUDE.md`
3. `WORKLOG.md`
4. `NEXT_STEPS.md`
5. relevante Dateien aus `skills/`, `agents/` oder `templates/`

## Git

Die Umgebung blockiert das normale `.git`-Verzeichnis. Deshalb liegt die lokale Git-Verwaltung in `/workspace/_git`.

Nutze fuer alle Git-Befehle den Wrapper `./gitw`:

```bash
./gitw status
./gitw add .
./gitw commit -m "Nachricht"
./gitw switch -c feature/kurzer-name
./gitw branch
```

Das Remote ist als `origin` auf `https://github.com/Hooked1234/arbeit.git` gesetzt. Pull/Push kann nur funktionieren, wenn die Umgebung GitHub-Zugriff erlaubt.

### Branch- und Commit-Workflow

- Vor jeder Aenderung: `./gitw status` ausfuehren.
- Fuer groessere Aufgaben einen eigenen Branch anlegen: `./gitw switch -c feature/kurzer-name`.
- Aenderungen thematisch klein halten.
- Nur gelesene und bewusst geaenderte Dateien committen.
- Nach relevanten Aenderungen `WORKLOG.md` und bei offenen Punkten `NEXT_STEPS.md` aktualisieren.
- Commit-Nachrichten kurz und konkret formulieren, z. B. `Add presentation templates`.
- Keine fremden Aenderungen zuruecksetzen.
- Kein `git reset --hard`.

## Arbeitsprinzip

- Bestehende Dateien zuerst lesen.
- Keine unbekannten Aenderungen ueberschreiben.
- Keine Dateien loeschen, ausser es wurde ausdruecklich verlangt.
- Aenderungen eng am Ziel halten.
- Relevante Aenderungen in `WORKLOG.md` dokumentieren.
- Offene Aufgaben in `NEXT_STEPS.md` aktualisieren.
- Groessere abgeschlossene Schritte in `CHANGELOG.md` ergaenzen.

## Ziel

Der Workspace soll verhindern, dass Arbeit doppelt gemacht, ueberschrieben oder ohne Kontext fortgesetzt wird. Codex und Claude sollen anhand der Dateien erkennen koennen:

- was das Ziel war
- welche Dateien geaendert wurden
- welche Entscheidungen getroffen wurden
- was noch offen ist
- wo nicht weitergearbeitet werden sollte
