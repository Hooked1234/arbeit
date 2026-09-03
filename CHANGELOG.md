# Changelog

## 2026-09-03

### Geändert
- MOBIS-Prüfungsleistung als **erbracht und abgegeben** vermerkt (Termin
  02.09.2026). Statusblock in `05_pruefungsleistung/README.md`, „Aktueller
  Stand" im Modul-README und `NEXT_STEPS.md` entsprechend nachgezogen.
- `NEXT_STEPS.md` um einen Abschnitt „Erledigt" ergänzt; die abgeschlossenen
  MOBIS-Punkte 4 und 4a dorthin verschoben.

### Offen
- Bewertung und Rückmeldung des Dozenten sind noch nicht dokumentiert.

## 2026-06-30

### Hinzugefügt
- 3-Schichten-Architektur: `standards/` (Wie) + `templates/` (Was) + `skills/` (Auslöser).
- Übergabe-Dateien `WORKLOG.md`, `NEXT_STEPS.md`, `CHANGELOG.md`.
- `context/` (felix, eos, hsba) und `decisions/` als eigene Dateien.
- Neue Standards `projektanweisung`, `excel-pivot`, `ki-dokument`.
- `qualitaetspruefer`-Agent, `gitw`-Wrapper, `.gitignore`.

### Geändert
- AGENTS.md (Codex) und CLAUDE.md (Claude) auf schlanke, rollenspezifische Form
  gekürzt; gemeinsame Routing-Tabelle nur einmal in AGENTS.md §1.
- Templates verweisen auf ihren Standard, statt Design-Vorgaben zu duplizieren.
- Skills sind schlanke Auslöser (Frontmatter + Verweis) statt Regel-Kopien.

### Entfernt
- Verschachtelte Workspace-Zips als Altlast (nicht übernommen).
