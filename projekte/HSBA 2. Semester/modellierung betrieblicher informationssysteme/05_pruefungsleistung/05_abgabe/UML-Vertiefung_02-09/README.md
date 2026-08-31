# UML-Vertiefung — Abgabe für den 02.09.2026

Stand: 30.08.2026 · Format: 2 × 45 Minuten · Gruppe: zwei Personen ·
Grundlage: [Umsetzungsplan](../../03_entwurf/2026-08-30_Umsetzungsplan_vertiefung.md)
und [Szenarien Fassung 2](../../03_entwurf/Szenarien_vertiefung.md)

## Stand der Umsetzung

| Schritt | Stand |
|---|---|
| 0 Auflage-3-Branch integrieren | fertig, Generatoren übernommen |
| 1 Konstruktkatalog gegen den Foliensatz prüfen | fertig, `7-UML-KD.pptx` ausgewertet |
| 2 Domäne und Fortführungsprinzip | fertig, Prüfungsverwaltung mit Änderungsauftrag |
| 3–4 Szenariotexte | fertig, Fassung 2 |
| 5 Rückführbarkeitsmatrizen | fertig |
| 6 Musterdiagramme | **fertig, dieser Ordner** |
| 7 Konsistenzprüfung Stufe 1 ⊂ Stufe 2 | fertig, `check_konsistenz.py` bestanden |
| 8 Abdeckungsmatrix | fertig, in `Szenarien_vertiefung.md` |
| 9 Aufgaben-PPTX und Aufgabenblatt | fertig, `Dokumente/` |
| 10 Lehrendenfassung | fertig, `Dokumente/` |
| 11 Betreuungsskript | fertig, Kapitel 5 der Lehrendenfassung |
| 12 Zeittest | offen, blockiert die Freigabe |

## Diagramme

| Datei | Zweck |
|---|---|
| `Diagramme/Stufe_1_Ist-Modell.svg/.png/.pdf` | Musterlösung Aufgabe 1, 9 Klassen |
| `Diagramme/Stufe_2_Endmodell.svg/.png/.pdf` | Musterlösung Aufgabe 2, 14 Klassen |
| `Diagramme/Stufe_2_Differenz.svg/.png/.pdf` | Endmodell mit Kennzeichnung neu / geändert / unverändert |
| `Diagramme/MOBIS_UML_Vertiefung.drawio` | editierbare Quelle, drei Seiten |
| `Diagramme/preview_*.png` | schnelle Kontrollansicht, nicht für die Abgabe |

**Stufe_2_Differenz** ist das Blatt für die Auflösung von Block 2. Grün sind die
fünf neuen Klassen, gelb die fünf gegenüber Aufgabe 1 umgebauten, blau die
unveränderten. Zwei Notizen halten fest, was entfällt (die Aggregation
Studiengang–Modul) und wie der Zielkonflikt aufgelöst wurde (Variante B).

## Notation

Strikt nach dem belegten Katalog aus `7-UML-KD.pptx` (Prof. Dr. Kamyar Sarshar)
und der eigenen Vorstellungsrunde vom 12.08.2026:

- Klasse mit drei Kammern, hellblaue Kopfzeile
- Attribute **ohne** Sichtbarkeit und **ohne** Datentyp
- Methoden **ohne** Parameter und Rückgabetyp, nur leere Klammern
- benannte Assoziation mit kursiver Leserichtung
- Kardinalitäten `1`, `0..1`, `0..*`, `1..*`
- Aggregation weiße Raute, Komposition schwarze Raute, jeweils am Ganzen
- Vererbung als Dreieck, ein- und zweistufig

Nicht verwendet, weil in keiner der beiden Quellen belegt: abstrakte Klassen,
Enumerationen, Assoziationsklassen, abgeleitete Attribute, Klassenattribute,
Initialwerte, Rollennamen, Navigierbarkeit, `{disjoint, complete}`, reflexive
Assoziationen, Nebenbedingungen.

## Neu bauen

```bash
python _generator/build.py ..
```

```bash
python _generator/build_pdf.py ..
```

Beides aus `Diagramme/_generator/` heraus aufrufen. Inhalt und Layout stehen in
`_generator/model.py`, nicht in den erzeugten Dateien — Änderungen dort
vornehmen, sonst gehen sie beim nächsten Lauf verloren.

`build.py` prüft vor dem Schreiben auf Kastenüberlappungen, Kästen außerhalb der
Seite, zu schmale Kästen und Kantenendpunkte, die nicht am Klassenrahmen liegen.
Alle drei Seiten sind ohne Befund. `build_pdf.py` legt die 288-dpi-Rasterbilder
zentriert auf A3 quer (1190,5 × 842 pt, je eine Seite).

### Unterschiede zum Generator der Auflage 3

Der Generator ist von dort übernommen und an vier Stellen angepasst:

1. Farbige Kopfzeile je Klasse statt einfarbigem Kasten, Hausstil vom 12.08.
2. `tone` je Klasse für die Differenzansicht (neu / geändert / unverändert).
3. Die Unterstreichung von Attributen ohne `+`/`-`-Präfix ist entfernt. In der
   Auflage 3 markierte sie Klassenattribute; bei präfixloser Notation hätte sie
   **jedes** Attribut unterstrichen.
4. Dateinamen kommen aus `FILES` in `model.py` statt aus einer festen Tabelle.

## Dokumente

| Datei | Zweck |
|---|---|
| `Dokumente/MOBIS_UML_Vertiefung_Aufgaben.pptx` | zwei Folien im Dozentenformat, nur Titel und Text |
| `Dokumente/MOBIS_UML_Vertiefung_Aufgabenblatt.docx` | zwei Blätter zum Austeilen: Szenario mit Arbeitsauftrag, dann Auftrag mit Protokollbogen und Schlussfrage |
| `Dokumente/MOBIS_UML_Vertiefung_Lehrendenfassung.docx` | Ablauf, Leitplanken, beide Musterlösungen, Fundliste, Raster, Betreuungsskript, Abnahme |

Neu bauen, aus `Dokumente/_generator/` heraus:

```bash
python build_docx.py ../MOBIS_UML_Vertiefung_Lehrendenfassung.docx ../../Diagramme
```

```bash
python build_docx_aufgaben.py ../MOBIS_UML_Vertiefung_Aufgabenblatt.docx
```

```bash
python build_pptx.py "<Pfad zu Aufgaben_EPK_Keine_Lösung.pptx>" ../MOBIS_UML_Vertiefung_Aufgaben.pptx
```

Der Inhalt steht in `_generator/content.py`, das Layout in den Bauskripten.
Änderungen dort vornehmen, nicht in den erzeugten Dateien.

### Zwei bewusste Abweichungen von der Dozentenvorlage

1. **Schriftgröße 14 pt auf Folie 1** statt 18 pt. Die Reklamationsfolie des
   Dozenten trägt rund 175 Wörter, der Text zu Aufgabe 1 rund 300 — die
   Vertiefung trägt ein größeres Modell. Maßgeblich zum Mitlesen ist das
   Aufgabenblatt, das gleichzeitig ausgeteilt wird.
2. **Ein Aufgabenblatt zusätzlich zu den Folien.** Belegt durch die Peer-Gruppe
   zum UML-Überblick, die ebenfalls mit Arbeitsblatt und Antwortfeldern
   arbeitet. Ohne Blatt gäbe es keinen Ort für den Protokollbogen und die
   Konfliktentscheidung.

Bewusst **nicht** enthalten: Pflichtklassenlisten, Beziehungstypen,
Notationsregeln. Sie nähmen die Lösung vorweg. Die eigene Runde vom 12.08.
hatte eine solche Checkliste nur bei der leichtesten Aufgabe.

## Dokumentenprüfung

```bash
python _generator/check_dokumente.py ..
```

Prüft ohne Office: ZIP-Integrität aller drei Dateien, zwei A3-Querabschnitte
und zwei eingebettete Diagramme in der Lehrendenfassung, Vollständigkeit der
Rückführbarkeitstabelle und der Fundliste, Punktsummen der beiden Raster
(je 20), alle FAQ-Zeilen, Protokollbogen mit zehn Zeilen, Wortgleichheit
zwischen Folie und Aufgabenblatt sowie bereinigte Dokumenteigenschaften.

Zusätzlich zwei Sprachprüfungen: Kein **Lösungswort** (Aggregation,
Komposition, Assoziation, Vererbung, abstrakt, Raute) steht irgendwo auf dem
Aufgabenblatt oder den Folien. Im **Szenariotext** sind zusätzlich die
Notationswörter Kardinalität und Multiplizität verboten; im Arbeitsauftrag ist
„Kardinalität" ausdrücklich erlaubt und erwünscht — es ist das Wort des
Dozenten von Folie 6.

Ergebnis: **51 Prüfungen, kein Befund.**

**Word-Export.** `SaveAs2` über die lokale Word-COM-Instanz hängt in dieser
Umgebung reproduzierbar; der Prozess wurde abgebrochen. PDFs der beiden
Word-Dateien müssen von Hand erzeugt werden: Datei öffnen, Speichern unter,
PDF. Vor dem Ausdruck ohnehin einmal in der Ziel-Office-Version öffnen und
Seitenumbrüche prüfen. Falls Word beim Öffnen hängt, hilft das Löschen von
`HKCU:\Software\Microsoft\Office.0\Word\Resiliency`.

## Konsistenzprüfung

```bash
python _generator/check_konsistenz.py
```

Prüft automatisiert, dass Stufe 2 das Modell aus Stufe 1 enthält. Erlaubt sind
ausschließlich die drei im Änderungsauftrag angekündigten Umbauten; jede andere
Abweichung ist ein Fehler, weil die Gruppen zu Beginn von Block 2 die Lösung zu
Aufgabe 1 ausgehändigt bekommen und darauf aufbauen. Zusätzlich geprüft: keine
Klasse verschwindet, Kardinalitäten und Beziehungsnamen übernommener Kanten
bleiben unverändert, keine Klasse ohne Beziehung.

Ergebnis: **bestanden**. Angekündigt und bestätigt sind

- `datum`, `note` und `alsBestandenVerbuchen()` wandern von `Prüfungsversuch`
  nach `Leistung`
- die Aggregation `Studiengang` ◇— `Modul` entfällt
- die Komposition `Student` ◆— `Prüfungsversuch` wird zu
  `Student` ◆— `Leistung`

## Offen

- **Zeittest** am 31.08.2026 durch Felix und den Abgabepartner. Ohne gemessene
  Zeiten keine Freigabe. Aufgabe 1 ist auf 11 Klassen gewachsen, Aufgabe 2 ist
  eine Aufgabenart ohne eigenen Erfahrungswert.
- PDF-Export der beiden Word-Dateien von Hand, siehe oben.
- Sichtprüfung von Seitenumbrüchen und Tabellenumbrüchen in der
  Ziel-Office-Version.
