# Changelog

Groessere abgeschlossene Aenderungen werden hier dokumentiert.

## 2026-06-30

### Added

- Gemeinsame Workspace-Struktur fuer Codex und Claude.
- Statusdateien `WORKLOG.md`, `NEXT_STEPS.md` und `CHANGELOG.md`.
- Agentenuebergreifende Ordner `skills/`, `agents/` und `templates/`.
- Erste Templates fuer EOS-, HSBA- und allgemeine Aufgaben.
- `.gitignore` fuer lokale Cache- und Systemordner.
- Git-Remote `origin` fuer `https://github.com/Hooked1234/arbeit.git` in der lokalen Ersatz-Git-Verwaltung.
- Helper `gitw` fuer kurze Git-Befehle mit separatem Git-Verzeichnis.
- Branch- und Commit-Workflow fuer Agenten im README.

### Changed

- `README.md` als zentrale Workspace-Uebersicht neu ausgerichtet.
- `AGENTS.md` fuer Codex mit Sitzungsstart, Arbeitsregeln, Git-Logik und Uebergabeprinzipien erweitert.
- `CLAUDE.md` fuer Claude / Claude Code mit denselben Grundregeln angepasst.
- Claude-spezifische Skills an die neue Template-Logik angepasst.
- Git-Regeln in `AGENTS.md` und `CLAUDE.md` auf den Wrapper `./gitw` konkretisiert.
