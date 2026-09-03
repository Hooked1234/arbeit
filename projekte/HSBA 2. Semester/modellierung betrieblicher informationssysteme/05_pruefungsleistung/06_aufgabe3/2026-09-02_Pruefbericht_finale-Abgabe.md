# Prüfbericht — finale Abgabe (Stand 02.09.2026)

Datei: `05_pruefungsleistung/Modellierung betrieblicher Informationssysteme Abgabe.pptx`
· 11 Folien · 3 Diagramme · 0 Notizenseiten
Durchführung: heute, Mi 02.09.2026, Woche 6, 2 × 45 Minuten

Geprüft gegen
`02_materialien/7-UML-KD.pptx` (Foliensatz Prof. Dr. Sarshar, 25 Folien) ·
`02_materialien/praesentationen/Konzept.pptx` (Folien 2 und 3) ·
`02_materialien/tabellen/Themen_Zeitplan_2026_BI-2.xlsx` (Woche 6) ·
`Leitfaden_Präsentation_Mobis.docx` (Bewertungsschema, 9 Kriterien, 100 Punkte).

Dieser Bericht ersetzt `Pruefbericht_Abgabe.md` vom 01.09.2026. Die dort
gemeldeten inhaltlichen Fehler sind alle behoben.

---

## Kurzfassung

Die beiden großen Musterlösungen sind **fachlich richtig**. Jede Kardinalität,
jedes Attribut und jede Methode wurde gegen den Szenariotext geprüft, die beiden
Diagramme zu Aufgabe 1 zusätzlich pixelweise verglichen: es sind **exakt sechs**
Unterschiede, und alle sechs Legendeneinträge treffen zu. Die Notation bleibt
vollständig im Umfang der Dozentenpräsentation — Kriterium 8 ist damit sauber,
und das ist das am leichtesten zu verlierende Kriterium.

Offen sind sechs kleine Korrekturen, davon eine echte Inkonsistenz zwischen
Folientext und Diagramm. Der größere Hebel liegt aber weiterhin nicht im Inhalt:
**44 der 100 Punkte hängen an Durchführung und Betreuung**, und die Datei enthält
dazu keine Zeile — keine Notizen, keinen Zeitplan, kein Aufgabenblatt.
Kriterium 9 (12 Punkte, das höchstgewichtete) ist mit vier Aufgaben nah dran,
aber zwei Agendapunkte der Vorlesung fehlen. Genau dort setzt Aufgabe 5 an
(→ `Aufgabe_5_Einordnung.md`, fertige Folien in `Aufgabe_5_Einordnung.pptx`).

---

## 1 Was nachweislich stimmt

- **Aufgabe 1, Musterlösung.** Alle neun Klassen tragen genau die Attribute und
  Methoden aus dem Szenariotext, nichts Zusätzliches. Alle Kardinalitäten sind
  richtig herum abgeleitet: `Studiengang 1 – 0..* Student`,
  `Modul 0..* – 1..* Dozent`, `Prüfungstermin 0..* – 1 Dozent`,
  `Prüfungstermin 1 – 0..* Prüfungsversuch`. Aggregation an `Studiengang`,
  Komposition an `Modul` und an `Student` — jeweils die Raute am Ganzen.
- **Genau sechs Fehler.** Der Bildvergleich von Fehlerbild und Musterlösung
  ergibt sechs logische Unterschiede: zwei vertauschte Rauten, eine falsche
  Kardinalität an `Modul`, die drei umgedrehten Vererbungspfeile (zählen als
  einer), die überzählige Kante `Dozent – Student` und die Kardinalität an
  `Prüfungstermin`. Kein siebter, kein fünfter.
- **Legende Folie 5.** Alle sechs Einträge sind korrekt; der frühere Widerspruch
  bei Punkt 6 (`1..*` statt `1`) ist behoben.
- **Klassennamen** `Prüfungsversuch` und `Klausur` sind korrigiert.
- **Aufgabe 2, Musterlösung.** Alle zwölf Kardinalitäten sind richtig aus dem
  Text abgeleitet, einschließlich `Rechnung 1..* – 0..1 Buchungssatz`,
  `Buchungsposition 0..* – 1 Sachkonto` und `Buchungssatz 0..* – 1 Buchhalter`.
  Die zweistufige Vererbung `Mitarbeiter → Buchhalter → Administrator` ist die
  richtige Lesart von „zusätzlich" und trägt die Schlussfrage. Die Antwort auf
  die Administrator-Frage steht jetzt auf Folie 7.
- **Kriterium 8 vollständig eingehalten.** Verwendet werden nur Klasse,
  Attribut, Methode, Assoziation, Aggregation, Komposition, Vererbung und die
  vier Kardinalitäten `1`, `0..1`, `0..*`, `1..*`. Keine Sichtbarkeitszeichen,
  keine Datentypen, keine abstrakten Klassen, keine Assoziationsklassen.
- **Folie 2** ist als Vorlesungsfolie gekennzeichnet („Folie aus der Vorlesung
  von Prof. Dr. Kamyar Sarshar"). Richtig so.
- **Diagrammqualität:** keine Kantenkreuzungen, keine Überlappungen,
  einheitliche `lowerCamelCase`-Methodennamen.

---

## 2 Inhaltliche Fehler und Widersprüche

### 2.1 Folie 10: Der Titel ist unvollständig

Die Folie heißt `Aufgabe 4:` — nach dem Doppelpunkt steht nichts. Alle anderen
Aufgabenfolien haben eine Bezeichnung.

**Korrektur:** `Aufgabe 4: Sichtbarkeit` oder, wenn die Antwort nicht vorweg
genommen werden soll, `Aufgabe 4: Schutz eines Attributs`.

### 2.2 Groß- und Kleinschreibung: Text und Diagramm widersprechen sich

Kriterium 1 verlangt ausdrücklich Widerspruchsfreiheit.

| Wo | Steht dort | Diagramm zeigt |
|---|---|---|
| Folie 7, Antwortpanel | `personalnummer, name, e-mail` | `Personalnummer`, `Name`, `Email` |
| Folie 11, Musterlösung | „Attribut `gesamtbetrag`" | `Gesamtbetrag` — auch Folie 10 schreibt groß |

Die Diagramme schreiben Attribute durchgängig groß, genau wie der Dozent
(`7-UML-KD.pptx`, Folien 9 und 23). Das ist die Referenz.

**Korrektur:** Antwortpanel und Folie 11 an die Diagramme angleichen. Die
Methodennamen im Antwortpanel stimmen bereits.

### 2.3 `Email` gegen `E-Mail`

Beide Szenariotexte schreiben „E-Mail" beziehungsweise „E-Mail-Adresse", beide
Diagramme schreiben `Email`. Kleinigkeit, aber sie wird gemeldet, sobald Gruppen
Text und Bild nebeneinanderlegen. Entweder im Text „Email" schreiben oder die
Abweichung in der Auflösung als unerheblich benennen.

### 2.4 Folie 6: Ein Satz führt in eine falsche Lösung

> „Eine Rechnung gehört immer genau zu einem Kunden oder einem Lieferanten."

Die Musterlösung zeigt an beiden Enden `0..1`. Wer den Satz wörtlich nimmt,
schreibt `1`/`1` — und das ist falsch, weil dann jede Rechnung gleichzeitig einen
Kunden **und** einen Lieferanten hätte. Das gemeinte Entweder-oder lässt sich mit
den behandelten Konstrukten nicht notieren.

**Korrektur des Satzes:** „Eine Rechnung ist **entweder** einem Kunden **oder**
einem Lieferanten zugeordnet, nie beiden." `0..1`/`0..1` bleibt die richtige
Lösung; in der Auflösung einen Satz dazu sagen.

### 2.5 Aufgabe 1 und 2 nennen keine Bearbeitungszeit

Aufgabe 3 und 4 sagen „Gruppenarbeit, 4 Minuten – anschließend Auflösung im
Plenum." Aufgabe 1 und 2 sagen nichts: weder Dauer noch Sozialform noch
Abgabeform. Das ist inkonsistent, und Kriterium 3 („ausreichend Zeit gegeben")
hängt genau daran.

**Ergänzen, je eine Zeile unter den Aufgabentext:**

> *Folie 3/4:* „Gruppenarbeit, 14 Minuten. Markieren Sie die sechs Fehler und
> notieren Sie in einem Stichwort, was richtig wäre."
>
> *Folie 6:* „Gruppenarbeit, 22 Minuten. Zeichnen Sie das Klassendiagramm mit
> Klassen, Attributen, Methoden, Beziehungen und Kardinalitäten und beantworten
> Sie zum Schluss die Frage am Ende des Textes."

### 2.6 Aufgabe 4 steht auf einem einzigen Satz der Vorlesung

Die Vorlesung nennt die Sichtbarkeit genau einmal, als Aufzählungspunkt auf
Folie 7: „Die Sichtbarkeit gibt an, wer auf Attribute oder Methoden zugreifen
darf." Notation (`+`/`-`) und die Begriffe privat und öffentlich kommen dort
nicht vor. Die Musterlösung führt „privat" und „öffentlich" neu ein.

Das ist kein Fehler — der Begriff wurde vermittelt, und die Folie verzichtet
richtigerweise auf `+`/`-`-Zeichen. Aber es ist das einzige Kriterium-8-Risiko im
ganzen Satz, und ohne Anker sind vier Minuten für die meisten Gruppen zu wenig.

**Absichern, drei Minuten Aufwand:**

- Auf Folie 11 den Beleg ergänzen: `(Vorlesung, Folie 7)`.
- Auf Folie 10 einen Tipp ergänzen: „Tipp: eines der fünf Merkmale einer Klasse
  aus der Vorlesung."

---

## 3 Streitpunkte während der Betreuung

Keine Fehler, aber Rückfragen, die mit hoher Wahrscheinlichkeit kommen.
Kriterium 4 (11 Punkte) misst genau das. Die Antworten sollten vorher zwischen
beiden Betreuenden abgestimmt sein.

| Rückfrage | Abgestimmte Antwort |
|---|---|
| „An der Raute stehen keine Zahlen — fehlt da was?" | Nein. Aggregation und Komposition zeigen wir wie in der Vorlesung ohne Kardinalitäten (`7-UML-KD.pptx`, Folien 14–18 und 23). |
| „Sind die drei umgedrehten Vererbungspfeile ein Fehler oder drei?" | Einer. Es ist eine Vererbungsbeziehung mit drei Unterklassen. |
| „Zu jedem Modul gehört *ein* Prüfungstermin — also genau einer?" | Der Satz meint: mindestens einer, und keiner ohne sein Modul. Entscheidend für die Aufgabe ist die schwarze Raute, nicht die Zahl. |
| „Warum `0..1` bei Kunde und Lieferant und nicht `1`?" | Eine Rechnung hat entweder einen Kunden oder einen Lieferanten. `1`/`1` würde beide gleichzeitig verlangen. |
| „`Mitarbeiter → Buchhalter → Administrator` — geht Vererbung über zwei Stufen?" | Ja. „Zusätzlich" im Text heißt: der Administrator kann alles, was der Buchhalter kann. Die Vorlesung zeigt nur eine Stufe, mehr Stufen sind aber dieselbe Beziehung. |
| „Zählen bei der Administrator-Frage auch die geerbten Methoden?" | Ja, alles was vererbt wird. |
| „`0..*` oder `*` — was sollen wir schreiben?" | Beides. Die Vorlesung nennt beide Schreibweisen gleichwertig (Folie 6). |

---

## 4 Formales

**4.1 Es fehlt eine Quellenfolie.** Der Leitfaden verlangt sie wörtlich: die
Präsentation ist „zusammen mit einer Liste der verwendeten Literatur und
sonstigen Quellenangaben […] vor der Präsentation an den/die Lehrende
auszuhändigen". Eine Schlussfolie genügt:

> **Quellen**
> Sarshar, K. (2026): UML-Klassendiagramm. Vorlesungsfoliensatz, HSBA.
> Hoffmann-Elbern, R. u. a. (2021): UML 2.5 — Das umfassende Handbuch. Rheinwerk Computing.
> Scheer, A.-W. (2011): ARIS. Zitiert nach Vorlesungsfolie 5.

**4.2 Null Notizenseiten.** Alle 11 Folien sind ohne Moderationshinweise. Die
Kriterien 3, 4, 5 und 7 machen zusammen 44 Punkte aus und hängen ausschließlich
an der Durchführung. Der Zeitplan aus Abschnitt 6 gehört mindestens auf Folie 1,
der Antwortkatalog aus Abschnitt 3 auf die Musterlösungsfolien.

**4.3 Kein Aufgabenblatt.** Die Diagrammbeschriftung erscheint auf der Leinwand
bei umgerechnet etwa 7 pt — das ist die Hälfte des ohnehin kleinen Fließtextes
und aus der dritten Reihe nicht lesbar. Ein Ausdruck je Gruppe (Folien 3, 4
und 6) ist die wirksamste Einzelmaßnahme und zahlt gleichzeitig auf die
Kriterien 1, 3 und 6 ein.

**4.4 Folie 6 ist an der Grenze.** 325 Wörter bei 12 pt, und PowerPoint hat den
Zeilenabstand automatisch um 10 % gestaucht, um den Text unterzubringen. Mit
Ausdruck unkritisch, ohne Ausdruck ein Problem für Kriterium 6.

**4.5 Marker 6 auf Folie 5** sitzt etwa 0,3 Zoll unterhalb der Kante
`Prüfungstermin – Prüfungsversuch` und zeigt dadurch in eine leere Fläche.
Ein Stück nach oben schieben. Die Marker 1 bis 5 sitzen richtig.

---

## 5 Abgleich mit dem Punkteverteilungsblatt

Aus `Leitfaden_Präsentation_Mobis.docx`, Bewertungsschema MOBIS: neun Kriterien,
8 × 11 + 1 × 12 = 100 Punkte. **Weniger als zwei Punkte in einem einzelnen
Kriterium bedeutet „nicht bestanden", unabhängig von allen anderen Kriterien.**
(Randnotiz: die Blocküberschriften nennen 40 / 20 / 40, die Einzelzeilen ergeben
44 / 22 / 34. Maßgeblich sind die Zeilenwerte, weil nur sie 100 ergeben.)

| # | Kriterium | P. | Stand | Risiko |
|---|---|---:|---|---|
| 1 | Aufgabe und Musterlösung korrekt | 11 | Beide Modelle vollständig gegen den Text geprüft und richtig. Offen: 2.2, 2.3, 2.4 | **klein**, nach Abschnitt 2 sehr klein |
| 2 | Originelle Aufgabe | 11 | Vier Denkformen: prüfen (A1), konstruieren (A2), bewerten (A3), transferieren (A4). Mit A5 kommt einordnen dazu | **sehr klein** |
| 3 | Zeit eingehalten / ausreichend Zeit | 11 | A1 und A2 nennen keine Zeit, kein Zeitplan in der Datei, kein gemessener Testlauf für A2 | **hoch** |
| 4 | Fragen beantwortet | 11 | Kein Antwortkatalog. Die sieben Rückfragen aus Abschnitt 3 kommen mit hoher Wahrscheinlichkeit | **hoch** |
| 5 | Musterlösung vorhanden und vorgestellt | 11 | Zu allen vier Aufgaben liegt eine Musterlösung vor, die Administrator-Frage ist beantwortet | **sehr klein** |
| 6 | Musterlösung übersichtlich & verständlich | 11 | Diagramme sauber und kreuzungsfrei, aber ca. 7 pt Beschriftung und kein Ausdruck | **mittel** |
| 7 | Betreuung während der Bearbeitung | 11 | Keine Rollenteilung, keine Hinweisstaffel dokumentiert | **hoch** |
| 8 | Nicht über die Präsentation hinausgehend | 11 | Vollständig eingehalten. Einzige Stelle: privat/öffentlich in A4 (→ 2.6) | **sehr klein** |
| 9 | Alle Themen wiederholt | **12** | Sprachkonstrukte, Kardinalitäten, Bewertung und Sichtbarkeit sind abgedeckt. **Einordnung in ARIS und Historie fehlen** | **mittel** |

### Die Lücke bei Kriterium 9

Die Agenda der Dozentenpräsentation lautet: Einsatzzweck · **Einordnung in
ARIS** · Sprachkonstrukte · Bewertung · **Historie** · Literatur.

| Agendapunkt | Folie | Abgedeckt durch |
|---|---|---|
| Einsatzzweck | 4 | Aufgabe 3 — die Stärkenliste deckt sich mit den Einsatzbereichen |
| Einordnung in ARIS | 5 | **nichts** |
| Sprachkonstrukte | 6–23 | Aufgabe 1, Aufgabe 2, Sichtbarkeit über Aufgabe 4 |
| Bewertung | 24 | Aufgabe 3 |
| Historie | 3 | **nichts** |
| Literatur | 25 | fehlt auch formal (→ 4.1) |

Zwei von sechs Agendapunkten kommen in keiner Aufgabe vor, obwohl das Kriterium
„alle wesentlichen Inhalte und Themen der Präsentation" verlangt und mit 12
Punkten am höchsten gewichtet ist. **Beide schließt Aufgabe 5**
(→ `Aufgabe_5_Einordnung.md`).

---

## 6 Zeitplan für 2 × 45 Minuten

Die Kurstabelle weist Woche 6 als „Große Übungen (2 × 45 Min)" aus; die
Konzeptfolie nennt für die Vertiefungsphase „ca. 3 × 30 Min". Beide ergeben 90
Minuten, die Konzeptfolie erwartet aber ausdrücklich **drei** Übungsblöcke. Mit
Aufgabe 5 sind es fünf Aufgaben in drei Blöcken — das passt zu beiden Vorgaben.

**Block 1 — 45 Minuten**

| Zeit | Inhalt |
|---|---|
| 0–3 | Einstieg, Folie 2 Sprachkonstrukte kurz durchgehen |
| 3–5 | Aufgabe 1 austeilen, Szenario einmal vorlesen |
| 5–19 | Bearbeitung Aufgabe 1 (14 Min) |
| 19–30 | Auflösung Aufgabe 1, die sechs Marker der Reihe nach (11 Min) |
| 30–34 | Bearbeitung Aufgabe 3 (4 Min) |
| 34–38 | Auflösung Aufgabe 3 (4 Min) |
| 38–41 | **Bearbeitung Aufgabe 5 (3 Min)** |
| 41–45 | **Auflösung Aufgabe 5 (4 Min)** |

**Block 2 — 45 Minuten**

| Zeit | Inhalt |
|---|---|
| 0–3 | Aufgabe 2 austeilen, Szenario einmal vorlesen |
| 3–25 | Bearbeitung Aufgabe 2 (22 Min) |
| 25–38 | Auflösung Aufgabe 2 inklusive Administrator-Frage (13 Min) |
| 38–42 | Bearbeitung Aufgabe 4 (4 Min) |
| 42–45 | Auflösung Aufgabe 4 (3 Min) |

**Kürzungsregel bei Zeitdruck.** Erst die Zusatzfrage in Aufgabe 5 streichen
(spart 2 Min), dann Aufgabe 4 in die Auflösung von Aufgabe 2 integrieren und nur
mündlich stellen (spart 5 Min). Aufgabe 1 und 2 nicht kürzen — sie tragen die
Kriterien 1, 5 und 6.

**Rollenteilung während der Bearbeitung.** Einer geht die Gruppen der Reihe nach
ab, einer bleibt vorn ansprechbar und hält die Zeit. Nach der Hälfte der
Bearbeitungszeit einmal laut die verbleibende Zeit ansagen. Hinweise nur aus dem
Katalog in Abschnitt 3 geben, damit beide dasselbe sagen.

---

## 7 Reihenfolge für heute

| # | Was | Dauer | Kriterium |
|---|---|---|---|
| 1 | Titel Folie 10 vervollständigen (2.1) | 1 Min | 1 |
| 2 | Schreibweisen auf Folie 7 und 11 angleichen (2.2) | 5 Min | 1 |
| 3 | Rechnungssatz auf Folie 6 umformulieren (2.4) | 3 Min | 1, 4 |
| 4 | Zeitangaben auf Folie 3/4 und 6 ergänzen (2.5) | 5 Min | 3 |
| 5 | Folienverweis und Tipp bei Aufgabe 4 (2.6) | 3 Min | 8, 3 |
| 6 | **Aufgabe 5 einfügen** — zwei Folien ans Ende von Block 1 | 5 Min | **9, 2** |
| 7 | Quellenfolie anlegen (4.1) | 10 Min | formal |
| 8 | Zeitplan aus Abschnitt 6 und Antwortkatalog aus Abschnitt 3 in die Notizen (4.2) | 30 Min | **3, 4, 7 — 33 Punkte** |
| 9 | Aufgabenblätter drucken, ein Satz je Gruppe (4.3) | 30 Min | 1, 3, 6 |
| 10 | Marker 6 auf Folie 5 nach oben schieben (4.5) | 1 Min | 6 |

Schritte 1 bis 6 kosten zusammen 22 Minuten und sind Pflicht. Schritt 8 und 9
sind der eigentliche Punktehebel.
