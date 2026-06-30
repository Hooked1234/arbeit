# Worklog

## 2026-06-30

- Zwei Workspace-Varianten zusammengeführt: GitHub-Gerüst (Hooked1234/arbeit,
  Codex+Claude-Prozess) + lokale Substanz (ki-workspace mit Design-Tokens).
- 3-Schichten-Architektur eingeführt: `standards/` (Wie / Quelle der Wahrheit),
  `templates/` (Was / Struktur), `skills/` (schlanke Auslöser mit Frontmatter).
- Redundanz aufgelöst: AGENTS.md und CLAUDE.md teilen EINE Routing-Tabelle
  (in AGENTS.md §1); CLAUDE.md verweist darauf, statt Regeln zu duplizieren.
- Design-Tokens aus den lokalen Standards in die Templates verlinkt (Templates
  verweisen aufs jeweilige Standard statt Farben/Maße zu wiederholen).
- `context/` (felix, eos, hsba) und `decisions/` aus der lokalen Variante übernommen.
- Skills um `excel-pivot` und `ki-dokument` ergänzt; Standards dafür neu angelegt.
- Übergabe-Dateien (WORKLOG/NEXT_STEPS/CHANGELOG), `gitw`, `.gitignore` und
  `qualitaetspruefer`-Agent aus dem GitHub-Gerüst übernommen.
- Encoding: bewusst echte Umlaute (UTF-8) statt ASCII-Ersatz — bessere Lesbarkeit.
- HSBA-Markenwerte recherchiert und gesetzt: Farb-Tokens (#002C58 / #4779AE /
  #0C2950), Schrift *Titillium Web*, Logo-SVG-Pfad, Fließtext 18–20 pt,
  Chicago Author-Date. Praxisbericht-Eckdaten (Thema, Leitfrage, Modul, Name)
  in `context/felix.md` ergänzt. Fremder Vattenfall-Bericht bewusst ignoriert.
- Offen: EOS-Markenschrift/Logo (Designportal) sowie HSBA Datum/Matrikelnummer/
  Kurs/Dozent:in.
