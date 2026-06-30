# Changelog

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
