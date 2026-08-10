# Worklog

## 2026-08-10

- `MOBIS`-Prüfungsleistung Auflage 2 (UML-Klassendiagramme) bewertet. Befund:
  Artefakte und Bewertungsraster sind belastbar, das Zeitbudget von 115–135
  Minuten kollidiert aber mit dem laut Konzeptfolie und Prüfungsordner
  vorgesehenen Format `3 × 20 Min`. Das Studierendenblatt gibt Pflichtklassen und
  Pflichtbeziehungen inklusive Beziehungstyp vor und nimmt damit die Lösung
  vorweg; die Musterlösungen antworten auf identische Formulierungen in Aufgabe 2
  und 3 unterschiedlich; die Hinweisstaffel und der Moderationsteil aus Auflage 1
  fehlen, obwohl die Betreuung der Gruppen bewerteter Bestandteil ist.
- Aufgabenformat des Dozenten aus `Aufgaben_EPK_Keine_Lösung.pptx` rekonstruiert:
  eine Folie je Aufgabe, Titel plus durchgehender Fließtext aus Szene und
  genauerer Beschreibung, keine Arbeitsaufträge oder Vorgabelisten. Die
  Steigerung erfolgt über Konstruktvielfalt, nicht über Modellgröße.
- Umsetzungsplan für Auflage 3 erstellt:
  `05_pruefungsleistung/03_entwurf/2026-08-10_Umsetzungsplan_aufl.3.md`. Enthält
  Konstruktkatalog mit Abdeckungsmatrix über alle drei Aufgaben, Zuschnitt auf
  je 20 Minuten, Textregeln für die Szenarien, elf Arbeitsschritte mit Aufwand
  und Abnahmekriterien. Auflage 2 bleibt als Archiv und als Grundlage für den
  Vertiefungstermin am 02.09.2026 (`3 × 30 Min`) erhalten.
- Schritte 2 und 3 des Plans umgesetzt:
  `05_pruefungsleistung/03_entwurf/Szenarien_aufl.3.md`. Drei Szenariotexte im
  Format des Dozenten (210–250 Wörter Fließtext, keine UML-Begriffe, keine
  Arbeitsaufträge) samt Rückführbarkeitsmatrix, die jeden Satz auf genau ein
  Modellelement abbildet. Alle 22 Konstrukte des Katalogs sind belegt.
  Drei Abweichungen vom Plan dokumentiert: Rollennamen nur in Aufgabe 3,
  `Ticket` in Aufgabe 3 zugunsten von `anzahlPlätze` gestrichen, Aggregation
  zusätzlich in Aufgabe 3. Modellgrößen 5, 8 und 8 Klassen.
- Schritte 4 und 5 des Plans umgesetzt:
  `05_abgabe/UML-Klassendiagramme_aufl.3/Diagramme/`. Drei Musterdiagramme als
  editierbare drawio-Quelle, SVG-Vektorfassung und PNG mit 288 dpi. Erzeugt
  werden sie aus einem Layoutmodell unter `_generator/`, das vor jedem Export
  Kastenüberlappungen, Seitenüberläufe, zu schmale Kästen und Kantenendpunkte
  abseits der Klassenrahmen prüft. Abdeckungsprüfung: 22 von 22 Konstrukten
  belegt; `{disjoint, complete}` fehlte zunächst im Diagramm zu Aufgabe 3 und
  wurde als Beschriftung an der Generalisierungsmenge ergänzt. Drei Sätze in
  den Szenarien nachgezogen, damit Bestellung, Reservierung und
  Buchungsposition eine im Text begründete Operation erhalten.
  Offen: PDF-Export der Diagramme (in dieser Umgebung keine drawio-CLI und kein
  SVG-nach-PDF-Konverter verfügbar) sowie der Zeittest.
- Schritte 8 und 9 des Plans umgesetzt: `MOBIS_UML_Lehrendenfassung.docx` und
  `.pdf`, 13 Seiten, davon drei A3-Querseiten mit den Musterdiagrammen. Je
  Aufgabe Szenariotext, Moderation, Beziehungsübersicht, Prüfinstanzen,
  typische Fehler, zulässige Alternativen, Bewertungsraster und die
  vollständige Rückführbarkeitstabelle. Der Moderationsteil holt die in
  Auflage 2 verlorene Hinweisstaffel zurück: je Aufgabe eine offene Frage nach
  Minute 5, ein eingrenzender Hinweis nach Minute 10 und ein Checkpoint-Satz
  zur Auflösung, dazu ein Ablaufplan für die 20 Minuten und eine
  Priorisierungsregel bei Zeitnot.
- Zwei Layoutfehler im ersten Durchlauf behoben: Leerseiten vor den
  Abschnittswechseln und fehlende Kopfzeilenwiederholung der langen
  Rückführbarkeitstabellen. PDF-Prüfung anschließend ohne Befund.
- Schritte 6 und 7 des Plans umgesetzt: `MOBIS_UML_Aufgaben.pptx` mit drei
  Folien im Format des Dozenten (Titel plus Fließtext, 18 pt, volle Breite) und
  `MOBIS_UML_Aufgaben_Druckfassung.docx/.pdf` mit identischem Text auf zwei
  Seiten. Die Folien bauen auf seiner Vorlage `Aufgaben_EPK_Keine_Lösung.pptx`
  auf; Master, Theme und Layout bleiben unverändert, Folien 4 und 5 entfallen,
  Dokumenteigenschaften neu gesetzt. Ein aus dem Layout geerbtes
  Aufzählungszeichen auf Folie 1 wurde unterdrückt. Textgleichheit zwischen
  Folien und Quelle automatisiert geprüft.
- Werkzeugnotiz: PowerPoint kann in dieser Umgebung nicht nach PDF speichern
  (`SaveAs`, `SaveCopyAs` und `ExportAsFixedFormat` scheitern), wohl aber
  einzelne Folien über `Slide.Export` als PNG. Die visuelle Abnahme lief
  darüber.
- Werkzeugnotiz: Word `ExportAsFixedFormat` hängt hier reproduzierbar,
  `SaveAs2` mit Format 17 funktioniert. Bei hängendem Word hilft das Löschen
  des Resiliency-Schlüssels. Das erklärt auch den entsprechenden Befund in der
  Qualitätsprüfung der Auflage 2.

## 2026-08-04

- Die Module `principles of finance` und `marketing management` unter
  `projekte/HSBA 2. Semester/` in die bestehende sechs Bereiche umfassende
  Modulstruktur aufgenommen.
- Neun Ausgangsdateien aus den separaten Kursordnern unverändert nach
  `02_materialien/` kopiert: fünf Finance-Dateien und vier Marketing-PDFs.
  Die vier Finance-ZIP-Archive bleiben gemäß bestehender `.gitignore`-Regel
  ausschließlich lokal; ihre 16 PDF-Inhalte wurden sicher entpackt, geprüft und
  werden zusammen mit den übrigen Materialien versioniert.
- Modulbeschreibungen, Folien, Archivverzeichnisse, Praxisberichtsleitfaden,
  Fallstudien und HSBA-Regeln inhaltlich ausgewertet und bestätigte Angaben in
  Modulsteckbriefe, Prüfungsordner und Materialübersichten übernommen.
- Semesterübersicht und zentralen Workspace-Überblick um beide Fächer ergänzt
  sowie die dringende Marketing-Frist zur Team- und Unternehmensmeldung am
  10.08.2026 dokumentiert.
- Einseitiges `Semester-Cockpit` für das 2. Semester aus den Originalquellen
  erstellt. Die Seite bündelt fünf Module, belegte Prüfungsleistungen,
  Schlüsseltermine, offene Angaben und einen konkreten 90-Minuten-Startfokus.
- Prüfungs- und Terminangaben gegen 34 PDFs, vier PPTX- und zwei XLSX-Quellen
  abgeglichen; Widersprüche bei MOBIS, Marketing und Finance sichtbar markiert.
  Das DOCX wurde in Word auf genau eine Seite gerendert, visuell geprüft und
  mit fehlerfreiem Barrierefreiheits- und Tabellengeometrie-Audit abgeschlossen.
- Nutzerklarstellung zu den Prüfungsleistungen eingearbeitet: In Finance bildet
  die 90-minütige englische Klausur die reguläre Note; eine optionale
  Buchpräsentation kann 0,3 Notenpunkte gutschreiben. In MOBIS bestimmt die
  Erstellung der Übungsaufgabe nach dem Format von `Aufgabe 5 – Reklamation`
  die vollständige Modulnote. Semester-Cockpit, Modulsteckbriefe,
  Prüfungsordner, Modul-READMEs und offene nächste Schritte wurden konsistent
  korrigiert; Nutzerangaben bleiben von Primärquellen getrennt gekennzeichnet.
  Auch der ausführliche persönliche MOBIS-Lehrplan wurde an sieben betroffenen
  Stellen berichtigt, erneut auf 14 Seiten gerendert und ohne Layout- oder
  Barrierefreiheitsfehler geprüft.
- Fünf eigenständige Modulüberblicke für MOBIS, Software Engineering,
  Wirtschaftsstatistik, Principles of Finance und Marketing Management unter
  `projekte/HSBA 2. Semester/00_modulueberblicke/` erstellt. Jeder Überblick
  dokumentiert Prüfungsleistung, vollständigen lokalen Quellenbestand,
  prüfungsorientierten Inhaltskern, Fehlerfallen, Austrittskriterien,
  Prioritäten und offene Angaben mit der Statuslogik
  Belegt/Kursinfo/Abgeleitet/Offen.
- Die fünf DOCX-Dateien auf zusammen 27 Seiten mit Microsoft Word gerendert und
  vollständig visuell geprüft. Einen Leerseitenfehler durch Umbruchabsätze sowie
  eine OOXML-Reihenfolgeabweichung korrigiert. Abschließende Prüfungen melden
  jeweils 0 Barrierefreiheitsbefunde und konsistente Überschriften-, Abschnitts-
  und Tabellengeometrie-Strukturen.

## 2026-08-03

- Persönlichen Codex-Template-Skill `artifact-template-1-0-lernzettel` unter
  `C:/Users/felix/.codex/skills/` erstellt. Der Skill bewahrt den geprüften
  MOBIS-Lehrplan als Referenz, erzwingt Belegt/Abgeleitet/Offen-Status,
  prüfungsnahe Übungen und Render-QA und wurde mit `quick_validate.py`
  erfolgreich validiert.

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
