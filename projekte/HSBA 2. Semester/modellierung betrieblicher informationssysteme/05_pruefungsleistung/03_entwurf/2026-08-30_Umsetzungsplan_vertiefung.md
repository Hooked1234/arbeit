# Umsetzungsplan Vertiefung — UML-Klassendiagramm, 02.09.2026

Stand: 30.08.2026 · Durchführung: Mi 02.09.2026 · Format: 2 × 45 Minuten,
zwei Personen · Ziel: eine in sich geschlossene Aufgabe in zwei Stufen, bei der
Stufe 2 Stufe 1 fortführt.

---

## 1 Rahmen

### Belegt

| Punkt | Beleg |
|---|---|
| Termin 02.09.2026, Woche 6 | `02_materialien/tabellen/Themen_Zeitplan_2026_BI-2.xlsx`, Zeile 15, Spalte G |
| Thema UML-Klassendiagramm | ebenda: „UML-Klassendiagramm / Große Übungen" |
| Format 2 × 45 Minuten | ebenda; deckt sich mit der Kursinformation |
| Dozent hält Theorie und Wiederholung | `Konzept.pptx`, Folie 3: „Wdh. der Einzelthemen ca. 10 Min **(KS)**" |
| Studentischer Anteil = Übungen + Musterlösung + Betreuung | ebenda: „**(STD)**" |
| Bewertung 9 Kriterien, 100 Punkte | `Leitfaden_Präsentation_Mobis.docx`, Bewertungsschema MOBIS |
| Aufgabenformat des Dozenten | `Aufgaben_EPK_Keine_Lösung.pptx`: Titel + Fließtext, keine Vorgabelisten |
| Aufgabenformat einer Peer-Gruppe | `5-UML-Überblick.zip`: PPTX mit Agenda plus DOCX-Arbeitsblatt mit Teilaufgaben, Antwortlinien und Zwischenkorrektur |
| Notationsumfang des Moduls | `7-UML-KD.pptx`, Prof. Dr. Kamyar Sarshar, 25 Folien: Klasse, Assoziation, Aggregation, Komposition, Vererbung, Kardinalitäten `1`/`0..1`/`0..*`/`1..*` |
| Eigener Aufgabensatz vom 12.08. | `OneDrive_2026-08-30.zip`, „7 - UML Klassendiagramme": Onlinehandel, Veranstaltungsverwaltung, Hotelverwaltung mit Musterlösungsdiagrammen |

### Bestätigt am 30.08.2026

1. **Werkzeug:** wie am 12.08., zusätzlich sind Modellierungswebsites wie
   diagrams.net ausdrücklich zugelassen. Folge für die Zeitplanung: die
   Nettozeit ist nicht durch Handzeichnen begrenzt, und Gruppen können ihr
   Modell aus Block 1 in Block 2 direkt weiterbearbeiten statt neu zu zeichnen.
   Das ist die Voraussetzung dafür, dass Block 2 als Umbau funktioniert.
2. **Sitzung:** beide 45-Minuten-Blöcke liegen in derselben Sitzung.
3. **Abgabe:** identisch zum ersten Termin.

### Befunde aus dem Material vom 30.08.2026

Drei Lieferungen, drei Befunde. Der dritte war der wichtigste.

1. **`5-UML-Überblick.zip` ist das Material einer Peer-Gruppe** zum Einzelthema 5,
   nicht der Foliensatz. Verwertbar daraus: Das Format ist weiter als
   angenommen — die Gruppe arbeitet mit Arbeitsblatt, nummerierten Teilaufgaben,
   Antwortlinien und einer ausdrücklichen Zwischenkorrektur („Meldet euch zur
   Korrektur"). Und der Originalitätsmaßstab liegt hoch: Memory-Karten,
   Zuordnungsaufgabe und Fallbeispiel, drei Anwendungsformen in einer Sitzung.
2. **`OneDrive_2026-08-30.zip` ist der eigene Aufgabensatz vom 12.08.** — und
   nicht die Auflage 2 oder 3 aus dem Repository. Eingesetzt wurden Onlinehandel,
   Veranstaltungsverwaltung und Hotelverwaltung, mit einem deutlich schlankeren
   Notationsumfang als in den Repository-Auflagen: keine Sichtbarkeiten, keine
   Datentypen, keine Methodensignaturen, keine abstrakten Klassen, keine
   Enumerationen, keine Assoziationsklassen. Drei Domänen sind damit verbraucht.
3. **`7-UML-KD.pptx` ist der Foliensatz des Dozenten** — 25 Folien,
   Prof. Dr. Kamyar Sarshar. Er behandelt genau fünf Sprachkonstrukte: Klasse mit
   Attributen und Methoden, Assoziation, Aggregation, Komposition, Vererbung,
   dazu die vier Kardinalitäten `1`, `0..1`, `0..*`, `1..*`. Sichtbarkeit wird
   auf Folie 7 erwähnt, aber in keinem Beispiel notiert. Alles Weitere —
   abstrakte Klassen, Enumerationen, Assoziationsklassen, abgeleitete Attribute,
   Rollennamen, `{disjoint, complete}` — kommt nicht vor.

**Folge für die Aufgaben.** Die erste Fassung der Szenariotexte stützte sich auf
den 22-Konstrukte-Katalog der Auflage 3 und hätte sieben Konstrukte eingeführt,
die weder in den Folien noch in der eigenen Vorstellungsrunde vorkamen — ein
direkter Angriff auf Kriterium 8, das bestgewichtete vermeidbare Risiko der
ganzen Leistung. `Szenarien_vertiefung.md` liegt deshalb in **Fassung 2** vor
und bleibt strikt im belegten Rahmen. Die Vertiefung entsteht über Modellgröße,
Vernetzung, Umbau und Zielkonflikt — nicht über neue Notation.

**Vokabular.** Der Dozent sagt Kardinalität statt Multiplizität und Methode
statt Operation. Aufgabenblatt, Auflösung und Betreuungsskript übernehmen das.

**Formatentscheidung daraus:** Die Aufgabenfolien bleiben im Dozentenstil, also
Titel plus Fließtext ohne Vorgabelisten — der Szenariotext ist die
Modellierungssubstanz und darf die Lösung nicht vorwegnehmen. Zusätzlich gibt es
je Block ein **Aufgabenblatt** mit demselben Text, einem Kopf für Gruppenname
und Mitglieder und, bei Block 2, einem Feld für die Entscheidung zum
Zielkonflikt. Das ist die Mischung aus Dozentenvorlage und belegter Peer-Praxis
und schafft den Ort, an dem die geforderte Entscheidung festgehalten wird.

Nebenbefund: Das Fallbeispiel der Peer-Gruppe spielt in einer
Online-Fahrradvermietung. Die Alternativdomäne „Carsharing" wäre damit teilweise
verbraucht gewesen — die Wahl der Prüfungsverwaltung bleibt richtig.

### Abgrenzung

Die Vertiefung ist **keine Überarbeitung der Auflage 3**. Deren Domänen
— Onlineshop-Bestellsystem, Hotelverwaltung, Veranstaltungsmanagement — sind
verbraucht und werden nicht wiederverwendet. Neu ist eine einzige Domäne über
beide Blöcke.

---

## 2 Was die Bewertungsrubrik erzwingt

Neun Kriterien, 8 × 11 + 1 × 12 = 100 Punkte. Unter 2 Punkten in einem
einzelnen Kriterium gilt die gesamte Leistung als nicht bestanden. Jedes
Kriterium braucht daher ein benanntes Artefakt.

| # | Kriterium | P. | Wie es eingelöst wird | Artefakt |
|---|---|---:|---|---|
| 1 | Aufgabe und Musterlösung korrekt | 11 | Rückführbarkeitsmatrix: jedes Modellelement auf genau einen Szenariosatz; automatisierte Konsistenzprüfung, dass das Endmodell das Modell aus Stufe 1 echt enthält | Lehrendenfassung, QS-Protokoll |
| 2 | Originelle Aufgabe | 11 | Änderungsauftrag statt zweiter Standardaufgabe; zwei verschiedene Denkformen (konstruieren, dann umbauen); ein bewusst eingebauter Zielkonflikt, der eine begründete Entscheidung erzwingt | Szenario + Änderungsauftrag |
| 3 | Zeit eingehalten / ausreichend Zeit | 11 | Minutenplan je Block, Hinweisstaffel, Priorisierungsregel, **gemessener Pilotlauf** | Ablaufplan, Pilotprotokoll |
| 4 | Fragen beantwortet | 11 | Antwortkatalog erwartbarer Rückfragen mit abgestimmter Antwort, damit beide Betreuenden gleich antworten | Betreuungsskript, Abschnitt FAQ |
| 5 | Musterlösung vorhanden und vorgestellt | 11 | Auflösung fest im Minutenplan (15 Min je Block); Musterlösung aus Stufe 1 wird zu Beginn von Stufe 2 ausgeteilt | Ablaufplan, Zwischenstand-Handout |
| 6 | Musterlösung übersichtlich und verständlich | 11 | A3-Querformat; für Stufe 2 ein **Differenzdiagramm** mit farblicher Kennzeichnung von neu / geändert / unverändert | Diagramme, Lehrendenfassung |
| 7 | Betreuung während der Bearbeitung | 11 | Rollenteilung der zwei Personen, feste Raumhälften, identische Hinweisstaffel Minute 10 und Minute 20 | Betreuungsskript |
| 8 | Nicht über die Präsentation hinausgehend | 11 | Konstruktkatalog gegen `7-UML-KD.pptx` und die eigene Runde vom 12.08. geprüft; kein Konstrukt darüber hinaus | Katalogtabelle in `Szenarien_vertiefung.md` |
| 9 | Alle Themen wiederholt | 12 | Abdeckungsmatrix: jedes in der Vorstellungsrunde behandelte Konstrukt kommt in Stufe 1 oder Stufe 2 zwingend vor; die beiden Auflösungen greifen jedes noch einmal auf — **ohne Folienwiederholung** | Abdeckungsmatrix, Auflösungsskript |

### Zu Kriterium 9 im Besonderen

Die Konzeptfolie ordnet die zehnminütige Wiederholung dem Dozenten zu, der
Zeitplan weist den Studierenden für Woche 6 ausschließlich „Große Übungen" zu.
Eine eigene Wiederholungsfolie ist daher weder vorgesehen noch nötig. Das
Kriterium wird stattdessen dadurch erfüllt, dass **kein Konstrukt der
Vorstellungsrunde ohne Auslöser in den beiden Aufgaben bleibt** und die
Auflösung jedes davon benennt. Der Nachweis dafür ist die Abdeckungsmatrix in
der Lehrendenfassung.

---

## 3 Fortführungsprinzip

### Empfehlung: Änderungsauftrag mit Zielkonflikt

**Stufe 1** — Aus einem Szenario im Dozentenformat wird das Ist-Modell gebaut.

**Stufe 2** — Der fiktive Auftraggeber schickt ein Änderungsschreiben, im
gleichen Erzählstil und ohne UML-Begriffe. Es enthält drei Sorten von
Anforderungen:

1. **Erweiterungen**, die neue Klassen nach sich ziehen.
2. **Umbauten**, die eine bestehende Beziehung aus Stufe 1 unbrauchbar machen
   und ersetzen — nicht additiv, sondern korrigierend.
3. **Einen Zielkonflikt**: eine neue Regel widerspricht einer alten. Die Gruppe
   muss den Widerspruch erkennen, sich begründet entscheiden und die Annahme
   offenlegen.

Punkt 3 ist der Kern. Er unterscheidet die Aufgabe von einer bloßen
Vergrößerung und bedient wörtlich, was Kriterium 2 verlangt: „unterschiedliche
Denk- und Anwendungsformen".

### Verworfene Alternativen

| Alternative | Warum nicht |
|---|---|
| Abstraktionsebenen nach ARIS (Fachkonzept → DV-Konzept) | Belegt durch `MOBIS_Einleitung.pptx` Folien 20/21, aber die DV-Konzept-Notation steht vermutlich nicht im Klassendiagramm-Foliensatz. Verstößt womöglich gegen Kriterium 8. |
| Sichtwechsel (Klassendiagramm → Use Case oder Aktivitätsdiagramm) | Fremdes Einzelthema, klarer Verstoß gegen Kriterium 8. |
| Modellkritik: fehlerhaftes Fremdmodell reparieren | Didaktisch stark und gut betreubar, aber „Fortführung" ist schwächer eingelöst. Als Rückfalloption vermerkt. |

---

## 4 Domäne

### Empfehlung: Prüfungsverwaltung einer Hochschule

Begründung: Die Studierenden kennen die Domäne, die Bearbeitungszeit fließt
damit vollständig in die Modellierung statt ins Verstehen des Falls — bei
45 Minuten der entscheidende Faktor. Zugleich liefert die Domäne natürliche
Auslöser für genau die Konstrukte, die sonst konstruiert wirken:
Assoziationsklasse, reflexive Assoziation und Klassenattribut ergeben sich hier
von selbst.

**Entwurf Stufe 1 — Ist-Stand der Prüfungsverwaltung**

Rund 8 Klassen, 1 Assoziationsklasse, 1 Enumeration.

| Element | Auslösende Aussage im Szenario |
|---|---|
| `Studiengang` ◇— `Modul` (Aggregation) | Ein Studiengang fasst Module zusammen; ein Modul bleibt bestehen, wenn ein Studiengang eingestellt wird |
| `Modul` ◆— `Prüfung` (Komposition) | Zu einem Modul gehören Prüfungstermine, die mit dem Modul verschwinden |
| `Prüfungsleistung {abstract}` → `Klausur`, `MündlichePrüfung`, `Präsentation` | Jede Prüfung wird in genau einer dieser Formen abgenommen, etwas Viertes gibt es nicht |
| Assoziationsklasse `Prüfungsversuch` (Student ↔ Prüfung) | Zu jedem Antritt werden Versuchsnummer, Datum und Note festgehalten, die weder zum Studenten noch zur Prüfung allein gehören |
| Klassenattribut `maxVersuche` | Für alle Studierenden gilt dieselbe Höchstzahl an Versuchen, sie wird nur einmal geführt |
| Abgeleitetes Attribut `/durchschnittsnote` | Die Durchschnittsnote wird nicht gespeichert, sondern jederzeit berechnet |
| Enumeration `Versuchsstatus` | angemeldet, bestanden, nicht bestanden, versäumt — andere Werte sind nicht zulässig |
| Nebenbedingung | Kein Versuch über der Höchstzahl |

**Entwurf Stufe 2 — Änderungsauftrag „Neue Prüfungsordnung"**

| Anforderung | Wirkung auf das Modell | Sorte |
|---|---|---|
| Module sind je Studiengang Pflicht oder Wahlpflicht und einem Fachsemester zugeordnet | Die Aggregation aus Stufe 1 trägt die Information nicht → **Assoziationsklasse `Modulzuordnung`** | Umbau |
| Ein Modul kann andere Module voraussetzen | **Reflexive Assoziation** mit Rollennamen `voraussetzung` / `aufbauend` | Erweiterung |
| Von den Lehrenden eines Moduls ist genau einer verantwortlich | Zweite, anders benannte Assoziation zwischen denselben Klassen, Multiplizität 1 gegen 0..* | Erweiterung |
| Leistungen anderer Hochschulen werden anerkannt | Generalisierung `Leistung` → `Prüfungsversuch` / `AnerkannteLeistung` | Umbau |
| Prüfungsleistungen dürfen als Gruppenleistung erbracht werden | Das Studenten-Ende der Assoziationsklasse wird `1..*` — **widerspricht** der Versuchszählung pro Student aus Stufe 1 | **Zielkonflikt** |

Der Zielkonflikt lautet ausgeschrieben: Zählt ein nicht bestandener
Gruppenversuch als Versuch für jedes Mitglied? Beide Antworten sind vertretbar,
sie führen aber zu unterschiedlichen Modellen. Die Gruppe muss sich entscheiden
und die Annahme im Diagramm als Notiz festhalten. Genau das wird in der
Auflösung besprochen.

Endmodell nach Stufe 2: rund 12 Klassen, 2 Assoziationsklassen, 1 Enumeration.

### Alternativen, falls die Domäne zu selbstbezüglich wirkt

1. **Carsharing-Anbieter** — Stufe 1: Kunden, Mieten, Fahrzeuge, Stationen,
   Tarife. Stufe 2: Firmenkunden mit Sammelrechnung, E-Fahrzeuge mit
   Ladevorgängen, Schadensmeldungen. Zielkonflikt über Abo gegen Einzelmiete.
2. **Werkstatt und Reparaturaufträge** — Stufe 1: Auftrag, Position, Teil,
   Monteur, Fahrzeug. Stufe 2: Garantiefälle, Fremdvergabe, Kostenvoranschlag
   mit Freigabe. Zielkonflikt über Teilverwendung gegen Lagerbestand.

Hinweis: Die Domänen „Bibliothek", „Hotelreservierung", „Studienbewerbung",
„Arzttermin" und „Reklamation" sind durch die EPK-Aufgaben des Dozenten belegt
und scheiden aus.

---

## 5 Zeitarchitektur

### Block 1 — 45 Minuten

| Zeit | Inhalt | Wer |
|---|---|---|
| 0–3 | Szenario austeilen und einmal vorlesen. Keine Modellierungsfrage beantworten. | Person A |
| 3–30 | Gruppen modellieren (27 Min). Hinweise ausschließlich nach Staffel. | beide im Raum |
| Minute 10 | Erster Hinweis, offen gestellt | beide, gleicher Wortlaut |
| Minute 20 | Zweiter Hinweis, eingrenzend. Priorisierungsregel ansagen. | beide, gleicher Wortlaut |
| 30–45 | Musterlösung zeigen, an vier Prüffragen begründen, zwei typische Fehler ansprechen | Person A |

### Block 2 — 45 Minuten

| Zeit | Inhalt | Wer |
|---|---|---|
| 0–5 | Änderungsauftrag austeilen. **Musterlösung aus Block 1 als Arbeitsgrundlage mit austeilen.** | Person B |
| 5–30 | Umbau (25 Min). Hinweisstaffel Minute 10 und Minute 20. | beide im Raum |
| 30–43 | Differenzdiagramm zeigen, Zielkonflikt aufmachen, beide zulässigen Lösungen zeigen | Person B |
| 43–45 | Abschluss: welches Konstrukt wo aufgetreten ist — deckt Kriterium 9 ab | Person A |

**Die Ausgabe der Musterlösung aus Block 1 zu Beginn von Block 2 ist nicht
verhandelbar.** Ohne sie arbeitet jede Gruppe, die Block 1 falsch gelöst hat, in
Block 2 auf einer falschen Grundlage weiter — das strukturelle Hauptrisiko jeder
Fortführungsaufgabe.

---

## 6 Umfang und Konstruktabdeckung

### Kalibrierung

Referenzwerte aus Auflage 3: 5 Klassen entsprachen etwa 12 Minuten, 8 Klassen
etwa 15 Minuten — beides geschätzt, nicht gemessen. Die Schätzungen der
Auflage 2 lagen um rund den Faktor zwei daneben. Daraus folgt konservativ:

| | Nettozeit | Umfang |
|---|---:|---|
| Block 1 | 27 Min | 8–9 Klassen, 1 Assoziationsklasse, 1 Enumeration |
| Block 2 | 25 Min | + 3–4 Klassen, 3 Umbauten, 1 Konfliktentscheidung |

Der Pilotlauf entscheidet. Kürzungskandidaten werden vorab benannt, damit
gekürzt werden kann, ohne die Abdeckung zu zerstören.

### Vertiefung ohne neue Konstrukte

Kriterium 8 verbietet Inhalte jenseits der Präsentation. Die Vertiefung entsteht
daher nicht über neue Sprachkonstrukte, sondern über vier Achsen:

1. **Vernetzung** — mehr Beziehungen je Klasse statt mehr Klassen.
2. **Umbau statt Neubau** — ein bestehendes Modell korrigieren.
3. **Entscheidung unter Widerspruch** — Zielkonflikt mit offengelegter Annahme.
4. **Validierung** — vorgegebene Prüffälle gegen das eigene Modell prüfen.

Der Konstruktkatalog der Auflage 3 (22 Zeilen) wird übernommen und dient als
Obergrenze, nicht als Zielvorgabe.

---

## 7 Artefakte

Neuer Ordner `05_abgabe/UML-Vertiefung_02-09/`.

| Datei | Zweck |
|---|---|
| `Dokumente/MOBIS_UML_Vertiefung_Aufgaben.pptx` | 2 Folien im Dozentenformat: Titel + Fließtext, keine Vorgabelisten |
| `Dokumente/MOBIS_UML_Vertiefung_Aufgabenblatt.docx/.pdf` | Arbeitsblatt je Block: derselbe Text, Kopf für Gruppenname und Mitglieder, bei Block 2 ein Feld für die Entscheidung zum Zielkonflikt. Format belegt durch die Peer-Gruppe, siehe Abschnitt 1 |
| `Dokumente/MOBIS_UML_Vertiefung_Zwischenstand.pdf` | Musterlösung Block 1, wird zu Beginn von Block 2 ausgeteilt |
| `Dokumente/MOBIS_UML_Vertiefung_Lehrendenfassung.docx/.pdf` | Musterlösungen, Rückführbarkeit, Moderation, Hinweisstaffel, Raster, typische Fehler, zulässige Alternativen, Abdeckungsmatrix |
| `Diagramme/Stufe_1_Ist-Modell.svg/.pdf` | Musterlösung Block 1, A3 quer |
| `Diagramme/Stufe_2_Endmodell.svg/.pdf` | Musterlösung Block 2, A3 quer |
| `Diagramme/Stufe_2_Differenz.svg/.pdf` | Endmodell mit farblicher Kennzeichnung neu / geändert / unverändert |
| `Diagramme/Stufe_2_Konfliktvariante.svg` | zweite zulässige Lösung des Zielkonflikts |
| `Qualitaetssicherung/Betreuungsskript.md` | Rollenteilung, Hinweisstaffel, FAQ-Antwortkatalog |
| `Qualitaetssicherung/Pilotprotokoll.md` | ausgefüllt nach dem Zeittest |
| `Qualitaetssicherung/Qualitaetspruefung.md` | Abnahme |

### Wiederverwendung aus Auflage 3

Die Generatoren werden übernommen und angepasst, nicht neu geschrieben:

- `Diagramme/_generator/model.py` und `build.py` — Layoutmodell mit
  automatischer Prüfung auf Kastenüberlappung, Seitenüberlauf und
  Kantenendpunkte
- `Dokumente/_generator/content.py`, `build_docx.py`, `build_docx_aufgaben.py`,
  `build_pptx.py`

Das Datenschema von `content.py` je Aufgabe (`szenario`, `beziehungen`, `rueck`,
`checkpoint`, `pruef`, `fehler`, `alternativen`, `raster`) passt unverändert.
Neu hinzu kommen `aenderungen` und `konflikt` für Block 2.

---

## 8 Betreuung zu zweit

| Rolle | Person A | Person B |
|---|---|---|
| Moderation | Block 1 | Block 2 |
| Zeitwache | beide Blöcke | — |
| Auflösung | Block 1, Schlusswort Block 2 | Block 2 |
| Raumhälfte während der Bearbeitung | links | rechts |

Bindend: Hinweise werden **wörtlich nach Staffel** gegeben, damit keine Gruppe
einen Vorteil hat. Der FAQ-Katalog im Betreuungsskript legt für jede erwartbare
Rückfrage eine gemeinsame Antwort fest, insbesondere für Fragen, deren
Beantwortung die Lösung vorwegnehmen würde.

Diese Aufteilung dokumentiert zugleich den bislang offenen Individualanteil
innerhalb der Gruppenleistung.

---

## 9 Arbeitsschritte

| # | Schritt | Ergebnis | Aufwand |
|---|---|---|---|
| 0 | Auflage-3-Branch `claude/uml-klassendiagramme-bewertung-5d35e8` (`8985a53`) in den Arbeitsstand integrieren | Generatoren verfügbar | 15 Min |
| 1 | ~~Konstruktkatalog abgleichen~~ | erledigt, Katalogtabelle in `Szenarien_vertiefung.md` | — |
| 2 | Domäne und Fortführungsprinzip festlegen | Entscheidung dokumentiert | 15 Min |
| 3 | Szenariotext Block 1 schreiben (Fließtext, keine UML-Begriffe, 200–250 Wörter) | `Szenarien_vertiefung.md` | 60 Min |
| 4 | Änderungsauftrag Block 2 schreiben, inklusive Zielkonflikt | ebenda | 60 Min |
| 5 | Rückführbarkeitsmatrizen für beide Stufen | Tabellen, später Bewertungsgrundlage | 60 Min |
| 6 | ~~Musterdiagramme bauen~~ | erledigt: SVG, PNG, A3-PDF und drawio in `05_abgabe/UML-Vertiefung_02-09/Diagramme/` | — |
| 7 | ~~Konsistenzprüfung~~ | erledigt, `check_konsistenz.py` bestanden | — |
| 8 | Abdeckungsmatrix Konstrukte × Stufen | Nachweis für Kriterium 9 | 30 Min |
| 9 | Aufgaben-PPTX und Druckfassung | 2 Folien, Handout | 45 Min |
| 10 | Lehrendenfassung bauen | DOCX und PDF | 120 Min |
| 11 | Betreuungsskript mit Hinweisstaffel und FAQ | Nachweis für Kriterien 4 und 7 | 60 Min |
| 12 | **Zeittest mit einer unbeteiligten Person unter Uhr** | `Pilotprotokoll.md` ausgefüllt | 100 Min |
| 13 | Nachschärfen nach Pilotbefund | korrigierte Fassung | 60 Min |
| 14 | Abnahme, Exporte, Druck, Backup | Freigabe | 45 Min |

Summe ohne Wartezeiten rund 14 Stunden, ab Schritt 5 auf zwei Personen
verteilbar.

---

## 10 Terminplan

Heute ist Sonntag, der 30.08.2026. Bis zur Durchführung bleiben drei Tage.

| Tag | Schritte | Ergebnis am Abend |
|---|---|---|
| So 30.08. | 0, 1, 2, 3, 4 | Beide Texte im Rohentwurf, Katalog bestätigt |
| Mo 31.08. | 5, 6, 7, 8 | Alle drei Diagramme, Rückführbarkeit und Abdeckung geprüft |
| Di 01.09. vormittags | 9, 10, 11 | Alle Artefakte gebaut |
| Di 01.09. nachmittags | 12, 13 | Zeiten gemessen, Fassung korrigiert |
| Mi 02.09. früh | 14 | Ausdrucke, PDF-Backup, USB-Stick, Abnahmeliste abgehakt |

Schritt 12 ist der erste Kürzungskandidat unter Zeitdruck und darf es nicht
sein. Ohne gemessene Zeiten ist Kriterium 3 nicht abgesichert, und genau dort
lagen die bisherigen Schätzungen am weitesten daneben.

---

## 11 Risiken

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| ~~UML-Foliensatz fehlt~~ — erledigt am 30.08. | — | `7-UML-KD.pptx` liegt vor, Katalog geprüft, Fassung 2 der Szenarien darauf zugeschnitten |
| Gruppen scheitern schon an Stufe 1 und stehen in Stufe 2 fest | Block 2 bricht ein | Musterlösung Stufe 1 wird zu Beginn von Block 2 ausgeteilt |
| Modell wird für 45 Minuten zu groß | Kriterium 3 | Pilotlauf; vorab benannte Kürzungskandidaten; Priorisierungsregel ab Minute 20 |
| Zielkonflikt wird als Fehler in der Aufgabe gelesen | Kriterium 1 | Der Änderungsauftrag sagt ausdrücklich, dass eine Entscheidung zu treffen und zu vermerken ist; beide Varianten stehen in der Lehrendenfassung |
| Auflage 3 nicht integriert | Doppelarbeit an den Generatoren | Schritt 0 vor allem anderen |
| Uneinheitliche Hinweise durch zwei Betreuende | Kriterium 7 | Wörtliche Hinweisstaffel, gemeinsamer FAQ-Katalog |

---

## 12 Abnahmekriterien

Freigabe am 02.09. nur, wenn alle Punkte erfüllt sind:

- [ ] Jedes Element beider Musterlösungen ist auf genau einen Satz des Szenarios
      oder des Änderungsauftrags zurückführbar.
- [ ] Kein Aufgabentext enthält UML-Fachbegriffe.
- [ ] Das Modell aus Stufe 1 ist als echte Teilmenge im Endmodell enthalten;
      jede Abweichung ist eine der drei benannten Umbaumaßnahmen.
- [ ] Jedes Konstrukt aus dem bestätigten Katalog kommt in Stufe 1 oder Stufe 2
      mindestens einmal vor und ist in der Abdeckungsmatrix belegt.
- [ ] Kein Konstrukt außerhalb des bestätigten Katalogs.
- [ ] Gemessene Bearbeitungszeit: Block 1 höchstens 27, Block 2 höchstens
      25 Minuten.
- [ ] Aufgabenfolien enthalten ausschließlich Titel und Fließtext.
- [ ] Der Zielkonflikt hat zwei ausgearbeitete, zulässige Lösungen.
- [ ] Betreuungsskript enthält Rollenteilung, wörtliche Hinweisstaffel und
      FAQ-Katalog.
- [ ] Ausdrucke, PDF-Backup und USB-Stick liegen bereit.

---

## 13 Entscheidungen

### Getroffen am 30.08.2026

1. **Fortführungsprinzip: Änderungsauftrag mit Zielkonflikt.** Abschnitt 3 gilt
   verbindlich.
2. **Domäne: Prüfungsverwaltung einer Hochschule.** Abschnitt 4 gilt
   verbindlich, die dort genannten Alternativen entfallen.

3. **Werkzeug, Sitzung und Abgabeweg** bestätigt, siehe Abschnitt 1.
4. **Szenariotexte geschrieben** — `Szenarien_vertiefung.md`, Schritte 3 bis 5
   des Arbeitsplans erledigt, einschließlich beider Rückführbarkeitsmatrizen,
   Konstruktabdeckung und Kürzungskandidaten.
6. **Auflage 3 integriert** — Branch `claude/uml-klassendiagramme-bewertung-5d35e8`
   per Fast-Forward übernommen, Generatoren stehen bereit.
7. **Diagramme gebaut** — Schritte 6 bis 8 erledigt. Drei Seiten als SVG, PNG,
   A3-PDF und editierbare drawio-Quelle; Geometrieprüfung und
   Konsistenzprüfung ohne Befund.

### Weiterhin offen

5. **Konstruktkatalog bestätigt** — `7-UML-KD.pptx` geprüft, Kriterium 8
   abgesichert, Szenarien in Fassung 2 darauf zugeschnitten.
6. **Person für den Zeittest** — muss beide Aufgaben vorher nicht gesehen haben.
7. **Aufgaben-PPTX, Aufgabenblatt, Lehrendenfassung und Betreuungsskript** —
   Schritte 9 bis 11, noch offen.
