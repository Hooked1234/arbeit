# UML-Klassendiagramme — Auflage 3

Stand: 10.08.2026 · Format nach `Aufgaben_EPK_Keine_Lösung.pptx` (Dozentenvorlage)

## Stand der Umsetzung

Grundlage ist
`../../03_entwurf/2026-08-10_Umsetzungsplan_aufl.3.md`.

| Schritt | Stand |
|---|---|
| 1 Konstruktkatalog gegen Foliensatz abgleichen | offen, Foliensatz liegt nicht vor |
| 2 Szenariotexte | fertig, `../../03_entwurf/Szenarien_aufl.3.md` |
| 3 Rückführbarkeitsmatrix | fertig, im selben Dokument |
| 4 Musterdiagramme | fertig, `Diagramme/` |
| 5 Abdeckungsprüfung | fertig, 22 von 22 Konstrukten belegt |
| 6 Aufgaben-PPTX | fertig, `Dokumente/` |
| 7 DOCX-Druckfassung | fertig, `Dokumente/` |
| 8 Lehrendenfassung | fertig, `Dokumente/` |
| 9 Moderationsteil mit Hinweisstaffel | fertig, Teil der Lehrendenfassung |
| 10 Zeittest | offen, blockiert die Freigabe |
| 11 Abnahme | offen |

## Dokumente

| Datei | Zweck |
|---|---|
| `Dokumente/MOBIS_UML_Aufgaben.pptx` | Aufgabenfolien, drei Folien — das Artefakt für die Veranstaltung |
| `Dokumente/MOBIS_UML_Aufgaben_Druckfassung.docx/.pdf` | derselbe Text als Handout, 2 Seiten |
| `Dokumente/MOBIS_UML_Lehrendenfassung.docx` | Arbeitsfassung, 13 Seiten |
| `Dokumente/MOBIS_UML_Lehrendenfassung.pdf` | aus Word exportiert |
| `Dokumente/_generator/` | Inhalte und Generatoren |

Die Aufgabenfolien bauen auf der Dozentenvorlage
`02_materialien/praesentationen/Aufgaben_EPK_Keine_Lösung.pptx` auf: Master,
Theme und Layout `Headline & 2 Contents` bleiben unverändert, Folien 4 und 5
entfallen, die verbleibenden drei werden mit unseren Szenarien belegt.
Schriftgröße 18 pt und volle Textbreite entsprechen seiner Reklamationsfolie.
Die Dokumenteigenschaften werden neu gesetzt, damit die Datei nicht als seine
ausgewiesen ist.

Neu bauen:

```bash
python _generator/build_docx.py MOBIS_UML_Lehrendenfassung.docx ../Diagramme
```

```bash
python _generator/build_pptx.py "<Pfad zur Dozentenvorlage>" MOBIS_UML_Aufgaben.pptx
```

```bash
python _generator/build_docx_aufgaben.py MOBIS_UML_Aufgaben_Druckfassung.docx
```

Der Inhalt steht in `_generator/content.py`, das Layout in `build_docx.py`.
Änderungen dort vornehmen, nicht in der DOCX — sonst gehen sie beim nächsten
Lauf verloren.

Aufbau: Durchführung mit Ablaufplan je 20 Minuten und Priorisierungsregel,
didaktische Leitplanken, Gesamtraster, dann je Aufgabe Szenariotext,
Moderation (Hinweis Minute 5, Hinweis Minute 10, Checkpoint-Satz),
Beziehungsübersicht, Prüfinstanzen, typische Fehler, zulässige Alternativen,
Bewertungsraster und die vollständige Rückführbarkeitstabelle. Jedes
Musterdiagramm steht auf einer eigenen A3-Querseite.

## Diagramme

| Datei | Zweck |
|---|---|
| `Diagramme/MOBIS_UML_Loesungen.drawio` | editierbare Quelle, drei Seiten |
| `Diagramme/Aufgabe_*.svg` | Vektorfassung für Dokument und Druck |
| `Diagramme/Aufgabe_*.png` | Rasterfassung, 288 dpi, für schnelle Ansicht |
| `Diagramme/_generator/` | Layoutmodell und Generator |

Die PNG- und SVG-Dateien werden aus `_generator/model.py` erzeugt:

```bash
python _generator/build.py .
```

Der Generator prüft vor dem Schreiben auf Kastenüberlappungen, Kästen außerhalb
der Seite, zu schmale Kästen und Kantenendpunkte, die nicht am Klassenrahmen
liegen. Wird die `.drawio`-Datei direkt bearbeitet, laufen Quelle und Export
auseinander — dann entweder das Modell nachziehen oder den Generator aufgeben
und die Exporte künftig aus diagrams.net erzeugen.

**Offen:** separater PDF-Export der drei Diagramme. In dieser Umgebung ist
weder eine drawio-CLI noch ein SVG-nach-PDF-Konverter verfügbar. In der
Lehrendenfassung sind die Diagramme als 288-dpi-Raster auf A3-Querseiten
enthalten; für eigenständige Diagramm-PDFs ist der Export aus diagrams.net
nötig (Datei → Exportieren als → PDF, Seitengröße A3 quer).

Hinweis zum Word-Export: `ExportAsFixedFormat` hängt in dieser Umgebung
reproduzierbar. `SaveAs2` mit Format 17 funktioniert. Falls Word beim Öffnen
hängt, hilft das Löschen von `HKCU:\Software\Microsoft\Office\16.0\Word\Resiliency`.

## Modellumfang

| Aufgabe | Klassen | Beziehungen | Besonderheiten |
|---|---:|---:|---|
| 1 Bestellsystem eines Onlineshops | 5 | 4 | Initialwert, Aggregation gegen Komposition |
| 2 Hotelverwaltung | 8 + 1 Enum | 3 + 4 Generalisierungen | abstrakte Klasse und Operationen, zweistufige Vererbung, Klassenattribut, abgeleitetes Attribut, Navigierbarkeit |
| 3 Veranstaltungsmanagement | 8 + 1 Assoziationsklasse + 1 Enum | 6 + 2 Generalisierungen | reflexive Assoziation mit Rollennamen, Assoziationsklasse, `{disjoint, complete}` |

## Prüfstand

- Geometrie und Endpunkte: automatisch geprüft, ohne Befund.
- Konstruktabdeckung: 22 von 22 belegt.
- SVG-Wohlgeformtheit und drawio-Struktur: geprüft.
- Sichtprüfung der drei Seiten: erfolgt.
- **Nicht geprüft:** reale Bearbeitungszeit. Schätzung 12 / 15 / 15 Minuten
  gegen einen Zielwert von 14. Kürzungskandidaten sind `Veranstaltungsort`
  in Aufgabe 3 und die zweite Vererbungsebene in Aufgabe 2.
