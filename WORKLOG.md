# Worklog

## 2026-07-30

- Die neuen Module `software engineering` und `wirtschaftsstatistik` unter
  `projekte/HSBA 2. Semester/` nach der bestehenden sechs Bereiche umfassenden
  Modulstruktur eingerichtet.
- Elf PDF-Dateien für Software Engineering und vier Ausgangsdateien für
  Wirtschaftsstatistik unverändert unter den jeweiligen `02_materialien/`
  einsortiert.
- Modul- und Materialübersichten ergänzt sowie die Semester-README aktualisiert.

## 2026-07-29

- Projektstruktur `projekte/HSBA 2. Semester/` angelegt.
- Erstes Modul `modellierung betrieblicher informationssysteme` mit getrennten
  Bereichen für Organisation, Materialien, Notizen, Aufgaben, Prüfungsleistung
  und Quellen vorbereitet.
- Bestehende zentrale Standards und Templates bewusst referenziert statt
  innerhalb des Projekts zu duplizieren.
- Sechs ausgegebene Unterrichtsmaterialien unverändert nach Dateityp unter
  `02_materialien/` einsortiert: vier Präsentationen und zwei Tabellen.
- Persönlichen MOBIS-Lehrplan aus diesen Kursunterlagen erstellt, acht
  Semesterwochen sowie belegte, abgeleitete und offene Ereignisse dokumentiert
  und unter `projekte/HSBA 2. Semester/modellierung betrieblicher
  informationssysteme/03_notizen/2026-07-29_persoenlicher-lehrplan_mobis.docx`
  abgelegt.

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
