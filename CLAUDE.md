# CLAUDE.md — Hauptanweisung (Claude / Claude Code)

> Steuerlogik identisch zu `AGENTS.md` (Codex): **Routing-Tabelle dort ist
> maßgeblich** — Aufgabentyp bestimmen → `standards/`-Datei laden → arbeiten.
> Diese Datei ergänzt nur Claude-spezifische Hinweise. Inhalt nicht duplizieren.

## Kurzfassung

- **Sprache Deutsch, knapp, Ergebnis vor Erklärung.** Kein Plan verlangt → direkt
  umsetzen. Nur bei ergebnisverfälschender Unsicherheit kurz nachfragen.
- **Routing:** siehe Tabelle in `AGENTS.md` §1. Quelle der Wahrheit für das *Wie*
  ist `standards/`, für die *Struktur* `templates/`, Auslöser in `skills/`.
- **Kontext:** Bei Personen-/Org-Bezug `context/felix.md`, `eos.md`, `hsba.md` lesen.
- **Datenschutz:** keine echten sensiblen Daten anfordern; anonymisierte
  Feldnamen/Dummy-Werte. Keine internen Richtlinien erfinden.

## Sitzungsstart prüfen

1. `README.md` → 2. `CLAUDE.md` → 3. `WORKLOG.md` → 4. `NEXT_STEPS.md`
5. relevante Dateien aus `standards/`, `skills/`, `agents/`, `templates/`.

## Claude-Code-spezifisch

- **Skills** liegen mit YAML-Frontmatter unter `.claude/skills/<name>/SKILL.md`
  und aktivieren automatisch über ihr `description`-Feld. Sie sind **schlanke
  Auslöser**: sie verweisen auf den passenden Standard + Template, statt Regeln
  zu duplizieren. Quelle der Wahrheit bleibt `standards/`.
- **Agent** `qualitaetspruefer` (`.claude/agents/`) für Reviews einsetzen.
- **Folien erzeugen:** PowerPoint strikt nach den Design-Tokens der jeweiligen
  Standarddatei bauen (Farben, Schriftgrößen, Layout, Folientypen).

## Antwortverhalten

- **Lernfragen:** Kurzantwort → Erklärung → konkretes Vorgehen → Fehlerquellen/Alternativen.
- **Texte:** direkt kopierbare Version, natürlicher Ton, Kontext passend.
- **Präsentationen:** 8–12 Folien; erst roter Faden, dann Folienstruktur, dann
  Inhalte; klare Titel, kurze Stichpunkte.
- **Bewertungen:** klar sagen, was stimmt, was nicht, was verbessert werden sollte.

## Änderungsdisziplin

Vor Änderung lesen & verstehen, nichts Unbekanntes überschreiben, nichts ohne
Auftrag löschen. Nach relevanter Änderung `WORKLOG.md` ergänzen, Offenes in
`NEXT_STEPS.md`, Größeres in `CHANGELOG.md`. Neue Festlegungen in
`decisions/decisions.md`.
