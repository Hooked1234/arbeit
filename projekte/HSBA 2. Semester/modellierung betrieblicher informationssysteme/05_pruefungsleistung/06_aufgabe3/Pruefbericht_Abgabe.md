# Prüfbericht — `Modellierung betrieblicher Informationssysteme Abgabe.pptx`

Stand: 01.09.2026 · Durchführung: Mi 02.09.2026 · Geprüft: 6 Folien, 3 Diagramme

Geprüft gegen
`02_materialien/7-UML-KD.pptx` (Foliensatz Prof. Dr. Sarshar, 25 Folien),
`02_materialien/praesentationen/Konzept.pptx` (Folie 3, Leistungsaufbau),
`02_materialien/tabellen/Themen_Zeitplan_2026_BI-2.xlsx` (Woche 6, 2 × 45 Min) und
`Leitfaden_Präsentation_Mobis.docx` (Bewertungsschema, 9 Kriterien, 100 Punkte).

---

## Kurzfassung

Fachlich ist die Abgabe **weitgehend richtig**. Beide Musterlösungen sind
korrekt aus den Szenariotexten abgeleitet, und die Notation bleibt vollständig
im Umfang der Dozentenpräsentation — das schützt Kriterium 8.

Sechs Dinge sind vor morgen zu erledigen, davon ist eines ein echter
Widerspruch zwischen Legende und Musterlösung. Der größere Hebel liegt
allerdings nicht bei den Inhalten, sondern bei den Punkten, die die Abgabe
gar nicht adressiert: **44 der 100 Punkte hängen an Durchführung und
Betreuung, und dazu enthält die Datei keine Zeile** — keine Notizen, keinen
Zeitplan, kein Aufgabenblatt. Dazu kommt Kriterium 9 (12 Punkte), das mit zwei
Aufgaben nicht vollständig eingelöst ist. Genau dort setzt die neue Aufgabe 3 an
(→ `Aufgabe_3_Fitnessstudio.md`).

---

## 1 Inhaltliche Fehler

### 1.1 Legende und Musterlösung widersprechen sich (Folie 4)

Die Legende sagt in Punkt 6:

> Prüfungstermin – Prüfungsversuch: **1..\*** statt 0..\*

Im Musterlösungsdiagramm steht an dieser Kante am Ende `Prüfungstermin` aber
eine **`1`**, am Ende `Prüfungsversuch` ein `0..*`.

Richtig ist das Diagramm, falsch die Legende. Der Aufgabentext lautet: „Jeder
Versuch bezieht sich auf **genau einen** Prüfungstermin. Ein Termin wird von
beliebig vielen Versuchen genutzt." `1..*` würde bedeuten, dass ein Versuch sich
auf mehrere Termine bezieht — das Gegenteil der Vorgabe.

**Korrektur:** `Prüfungstermin – Prüfungsversuch: 1 statt 0..* (Seite Prüfungstermin)`

*Beleg:* Der Bildvergleich von Fehlerbild und Musterlösung ergibt genau sechs
Unterschiede. An dieser Kante ändert sich ausschließlich das linke Label von
`0..*` auf `1`; das rechte Label bleibt `0..*`.

### 1.2 Zwei Tippfehler im Text von Aufgabe 2 (Folie 5)

| Ist | Soll |
|---|---|
| „Jeder Geschäftsvorfall **wir** durch einen Buchungssatz erfasst." | „…**wird** durch…" |
| „…mehreren **Buchungspositonen** zugeordnet sein." | „…**Buchungspositionen**…" |

### 1.3 Zwei Klassennamen in den Diagrammen zu Aufgabe 1

| Ist | Soll | Wo |
|---|---|---|
| `Prüfungversuch` | `Prüfungsversuch` | Fehlerbild **und** Musterlösung |
| `Klausuren` | `Klausur` | beide Bilder; die Geschwisterklassen stehen im Singular |

Der Aufgabentext schreibt „Prüfungsversuch" korrekt. Die Abweichung fällt auf,
sobald Gruppen Text und Bild nebeneinanderlegen — und sie werden es als
gefundenen Fehler melden. Beide Bilder sind aus der Quelldatei neu zu
exportieren.

### 1.4 Die Musterlösung zu Aufgabe 2 beantwortet die gestellte Frage nicht

Folie 5 endet mit: „Auf welche Attribute und Methoden kann ein Objekt der Klasse
Administrator zugreifen?" Folie 6 zeigt nur das Diagramm. Die Antwort fehlt —
und sie ist der didaktische Kern der Aufgabe.

**Ergänzen (Textfeld neben dem Diagramm):**

> Ein `Administrator` erbt über `Buchhalter` von `Mitarbeiter` und verfügt damit über:
> `personalnummer`, `name`, `e-mail` (aus `Mitarbeiter`) ·
> `buchungErfassen()`, `buchungÄndern()` (aus `Buchhalter`) ·
> `benutzerVerwalten()`, `einstellungenVerwalten()` (eigene).

---

## 2 Stellen, an denen Text und Modell auseinandergehen

Keine Fehler, aber Streitpunkte während der Betreuung. Für jede Stelle sollte
die Antwort vorher feststehen.

**2.1 „Eine Rechnung gehört immer genau zu einem Kunden oder einem Lieferanten."**
Das Modell zeigt `0..1` an beiden Enden. Wer den Satz wörtlich nimmt, schreibt
`1`/`1` — und das ist falsch, weil dann jede Rechnung gleichzeitig einen Kunden
*und* einen Lieferanten hätte. Das gemeinte „entweder/oder" lässt sich mit den
behandelten Konstrukten nicht notieren.
→ Satz ändern in: „Eine Rechnung ist **entweder** einem Kunden **oder** einem
Lieferanten zugeordnet, nie beiden." und in der Auflösung einen Satz dazu sagen.
`0..1`/`0..1` bleibt die richtige Lösung.

**2.2 „Zu einer Rechnung können eine oder mehrere Zahlungen gehören."**
Das Modell zeigt `1..*`. „Können … eine oder mehrere" ist doppeldeutig, und eine
noch unbezahlte Rechnung hat null Zahlungen — das spricht für `0..*`.
→ Entweder „können" streichen (dann ist `1..*` zwingend) oder `0..*` in der
Auflösung ausdrücklich als gleichwertig anerkennen.

**2.3 „Ein Buchungssatz besitzt unter anderem ein Buchungsdatum und einen Buchungstext."**
„Unter anderem" lädt dazu ein, weitere Attribute zu erfinden, und macht den
Vergleich mit der Musterlösung strittig. → streichen.

---

## 3 Was in der Aufgabenstellung fehlt

**3.1 Es gibt keinen Arbeitsauftrag.** Weder Aufgabe 1 noch Aufgabe 2 sagt, was
zu tun ist, in welcher Form, wie lange und in welcher Sozialform. Die
Folientitel sind die einzige Anweisung. Je ein Satz genügt:

> *Aufgabe 1:* „Im folgenden Diagramm sind **sechs** Fehler enthalten. Finden Sie
> die Fehler, markieren Sie sie auf dem Aufgabenblatt und notieren Sie jeweils in
> einem Stichwort, was richtig wäre. Gruppenarbeit, 15 Minuten."
>
> *Aufgabe 2:* „Erstellen Sie zu folgendem Szenario ein UML-Klassendiagramm mit
> Klassen, Attributen, Methoden, Beziehungen und Kardinalitäten. Beantworten Sie
> zum Schluss die Frage am Ende des Textes. Gruppenarbeit, 27 Minuten."

**3.2 Die Zahl der Fehler fehlt** — der Titel sagt sogar „Finde den Fehler" im
Singular, eingebaut sind sechs. Ohne Zahl wissen die Gruppen nicht, wann sie
fertig sind.

**3.3 Zusatzfunde sind nicht geregelt.** In beiden Diagrammen tragen die
Aggregations- und Kompositionskanten keine Kardinalitäten, während alle
Assoziationen welche haben. Das ist **kein Fehler** — es ist exakt die Notation
des Dozenten (`7-UML-KD.pptx`, Folien 14–18 und 23) — aber Gruppen werden es
melden. Antwort vorher festlegen, ebenso für `Prüfungversuch` und `Klausuren`,
solange 1.3 nicht korrigiert ist.

---

## 4 Abgleich mit dem Punkteverteilungsblatt

Aus `Leitfaden_Präsentation_Mobis.docx`, Bewertungsschema MOBIS: neun Kriterien,
8 × 11 + 1 × 12 = 100 Punkte. **Unter zwei Punkten in einem einzelnen Kriterium
gilt die gesamte Leistung als nicht bestanden.** (Randnotiz: die Blocküberschriften
nennen 40 / 20 / 40 Punkte, die Einzelzeilen ergeben 44 / 22 / 34. Maßgeblich sind
die Zeilenwerte, weil nur sie 100 ergeben.)

| # | Kriterium | P. | Stand in der Abgabe | Risiko |
|---|---|---:|---|---|
| 1 | Aufgabe und Musterlösung korrekt | 11 | Beide Modelle sind richtig aus den Texten abgeleitet. Offen: der Legendenwiderspruch (1.1), die fehlende Antwort auf die Administrator-Frage (1.4), die Tippfehler | **mittel**, mit den Korrekturen aus Abschnitt 1 klein |
| 2 | Originelle Aufgabe | 11 | Zwei verschiedene Denkformen: Modell prüfen (A1), Modell konstruieren (A2). Solide, aber ohne dritte Form | **klein**, mit Aufgabe 3 sehr klein |
| 3 | Zeit eingehalten / ausreichend Zeit | 11 | Kein Zeitplan in der Datei. Aufgabe 2 ist mit 13 Klassen und 12 Beziehungen für 45 Minuten sehr groß; kein gemessener Testlauf | **hoch** |
| 4 | Fragen beantwortet | 11 | Kein Antwortkatalog. Die Streitpunkte aus Abschnitt 2 und 3.3 kommen mit hoher Wahrscheinlichkeit | **hoch** |
| 5 | Musterlösung vorhanden und vorgestellt | 11 | Beide Musterlösungen liegen vor. Die Frage aus Aufgabe 2 bleibt unbeantwortet | **klein** |
| 6 | Musterlösung übersichtlich und verständlich | 11 | Diagramme sauber und kreuzungsfrei. Aber: Beschriftung umgerechnet ca. 7 pt, Bilder nutzen nur die halbe Folienbreite, kein Ausdruck | **mittel** |
| 7 | Betreuung während der Bearbeitung | 11 | Keine Rollenteilung, keine Hinweisstaffel dokumentiert | **hoch** |
| 8 | Nicht über die Präsentation hinausgehend | 11 | Vollständig eingehalten: nur Klasse, Assoziation, Aggregation, Komposition, Vererbung und die vier Kardinalitäten `1`, `0..1`, `0..*`, `1..*`. Keine Sichtbarkeiten, keine Datentypen, keine abstrakten Klassen, keine Enumerationen, keine Assoziationsklassen | **sehr klein** |
| 9 | Alle Themen wiederholt | **12** | Alle fünf Sprachkonstrukte und drei der vier Kardinalitäten kommen vor. Nicht aufgegriffen: `0..1` in Aufgabe 1, Einsatzzweck, Einordnung in ARIS, Stärken und Grenzen, Sichtbarkeit | **hoch** |

**Die Lücke bei Kriterium 9 im Detail.** Die Agenda der Dozentenpräsentation
lautet: Historie · Einsatzzweck · Einordnung in ARIS · Sprachkonstrukte ·
Bewertung · Literatur. Aufgabe 1 und 2 decken ausschließlich den Punkt
„Sprachkonstrukte" ab. „Einsatzzweck" (Folie 4), „Einordnung in ARIS" (Folie 5)
und „Bewertung" mit den Stärken und Grenzen (Folie 24) kommen in keiner der
beiden Aufgaben vor — obwohl das Kriterium ausdrücklich „alle wesentlichen
Inhalte und Themen der Präsentation" verlangt und mit 12 Punkten am höchsten
gewichtet ist.

**Genau diese Lücke schließt Aufgabe 3.** Details, Aufgabentext, Musterlösung,
Zeitgerüst und Abdeckungsmatrix in `Aufgabe_3_Fitnessstudio.md`, das Diagramm in
`Aufgabe_3_Fitnessstudio.svg`.

---

## 5 Formales

**5.1 Titelfolie ohne Namen, Kurs und Datum.** Der Untertitel ist leer. Der
Bewertungsbogen hat genau diese drei Felder in der Kopfzeile.

**5.2 Keine Quellenangabe.** Der Leitfaden verlangt: „Die
Präsentation/Dokumentation ist, zusammen mit einer Liste der verwendeten
Literatur und sonstigen Quellenangaben, in einfacher Ausfertigung vor der
Präsentation an den/die Lehrende auszuhändigen." Eine Schlussfolie mit dem
Foliensatz des Dozenten und der Literaturangabe seiner Folie 25
(Hoffmann-Elbern u. a. (2021): UML 2.5, Rheinwerk) genügt.

**5.3 Schriftgrößen.** Folie 2: 14 pt bei 233 Wörtern. Folie 5: 12 pt bei 307
Wörtern und zusätzlich 10 % reduziertem Zeilenabstand. Die
Diagrammbeschriftungen liegen umgerechnet bei etwa 7 pt, also bei der Hälfte des
ohnehin kleinen Fließtextes. Von der Leinwand ist beides nicht lesbar.

**5.4 Kein Aufgabenblatt.** Beide Aufgaben verlangen, dass die Gruppen Text und
Diagramm 15 bis 27 Minuten vor sich haben. Ein Ausdruck je Gruppe löst 5.3 und
5.4 zusammen und ist die wirksamste Einzelmaßnahme für die Kriterien 1, 3 und 6.

**5.5 Null Notizenseiten.** Die Datei enthält keine Moderationshinweise. Die
Kriterien 3, 4, 5 und 7 machen zusammen **44 Punkte** aus und hängen
ausschließlich an der Durchführung.

**5.6 Umfang von Aufgabe 2.** 13 Klassen, 3 Vererbungskanten, 2 Kompositionen,
1 Aggregation, 4 Assoziationen mit Kardinalitäten, rund 30 Attribute und
Methoden, dazu eine Transferfrage. Zum Vergleich: Aufgabe 1 kommt mit 9 Klassen
aus und verlangt nur Korrekturen. Ohne gemessenen Testlauf ist Kriterium 3 nicht
abgesichert. Kürzungskandidaten vorab benennen: `Buchungsperiode` und `Zahlung`
lassen sich streichen, ohne dass ein Sprachkonstrukt wegfällt.

---

## 6 Was ausdrücklich stimmt

- **Aufgabe 1:** Jedes Attribut und jede Methode aus dem Text steht im Diagramm,
  nichts Zusätzliches. Zwischen Fehlerbild und Musterlösung liegen genau sechs
  Unterschiede — nicht fünf, nicht sieben. Die Markierungen 1 bis 6 sitzen an den
  richtigen Stellen, die Legendeneinträge 1 bis 5 treffen zu.
- **Aufgabe 2:** Alle Kardinalitäten außer den unter 2.1 und 2.2 genannten sind
  richtig aus dem Text abgeleitet, insbesondere `Rechnung` `1..*`/`0..1`
  `Buchungssatz`, `Buchungsposition` `0..*`/`1` `Sachkonto` und `Buchungssatz`
  `0..*`/`1` `Buchhalter`. Die zweistufige Vererbung `Mitarbeiter` →
  `Buchhalter` → `Administrator` ist die richtige Lesart von „zusätzlich" und
  trägt die Schlussfrage.
- **Notation:** durchgehend im Rahmen von `7-UML-KD.pptx`. Kein einziges
  Konstrukt darüber hinaus. Kriterium 8 ist sauber, und das ist das am
  leichtesten zu verlierende Kriterium.
- **Diagrammqualität:** keine Kantenkreuzungen, keine überlappenden Kästen,
  einheitliche Fächeraufteilung, konsequente `lowerCamelCase`-Schreibweise.

---

## 7 Reihenfolge für heute

| # | Was | Dauer |
|---|---|---|
| 1 | Legende Folie 4, Punkt 6 korrigieren (1.1) | 2 Min |
| 2 | Zwei Tippfehler auf Folie 5 (1.2) | 2 Min |
| 3 | Antwort auf die Administrator-Frage auf Folie 6 ergänzen (1.4) | 10 Min |
| 4 | Arbeitsauftrag und Fehlerzahl auf die Aufgabenfolien (3.1, 3.2) | 15 Min |
| 5 | Titelfolie und Quellenfolie (5.1, 5.2) | 15 Min |
| 6 | **Aufgabe 3 einfügen** — zwei Folien nach Folie 4 | 20 Min |
| 7 | Aufgabenblätter drucken, ein Satz je Gruppe (5.4) | 30 Min |
| 8 | Notizenseiten: Zeitplan, Rollenteilung, Hinweisstaffel, Antwortkatalog aus Abschnitt 2 und 3.3 (5.5) | 60 Min |
| 9 | Klassennamen in den Diagrammen zu Aufgabe 1 korrigieren und neu exportieren (1.3) | 20 Min |
| 10 | Zeittest für Aufgabe 2 mit einer unbeteiligten Person (5.6) | 45 Min |

Schritte 1 bis 6 sind die Pflicht. Schritt 8 ist der größte Punktehebel:
44 Punkte hängen daran, und die Datei enthält dazu bisher nichts.
