# Aufgabe 5 — „Einordnung und Herkunft"

Stand: 02.09.2026 · Durchführung: heute · Umfang: 7 Minuten (3 Bearbeitung + 4 Auflösung)
· Platz: Ende Block 1, direkt nach der Auflösung von Aufgabe 3

Fertige Folien: `Aufgabe_5_Einordnung.pptx` (zwei Folien, gleiches Layout und
gleiche Schriftgrade wie die vorhandenen Aufgaben 3 und 4, inklusive
Notizenseiten). In PowerPoint öffnen, beide Folien in der Miniaturansicht
markieren, kopieren und in der Abgabe **hinter Folie 9** einfügen.

---

## 1 Warum diese Aufgabe

Die Abgabe deckt vier der sechs Agendapunkte der Dozentenpräsentation ab. Zwei
kommen in keiner Aufgabe vor: **Einordnung in ARIS** (Folie 5) und **Historie**
(Folie 3). Kriterium 9 verlangt aber „alle wesentlichen Inhalte und Themen der
Präsentation noch einmal aufgegriffen und gefestigt, kein wichtiger
Themenbereich ausgelassen" — 12 Punkte, das höchstgewichtete Einzelkriterium.

Nebeneffekt für Kriterium 2: Aufgabe 5 bringt eine fünfte Denkform ins Set.

| Denkform | Aufgabe |
|---|---|
| Ein gegebenes Modell prüfen und korrigieren | 1 |
| Aus einem Text ein Modell konstruieren | 2 |
| Ein Werkzeug bewerten | 3 |
| Eine Modellierungsentscheidung übertragen | 4 |
| **Ein Werkzeug einordnen und verorten** | **5** |

Die Aufgabe verlangt kein Zeichnen und kein neues Diagramm. Sie kostet deshalb
wenig Zeit und braucht kein Aufgabenblatt.

---

## 2 Folie „Aufgabe 5: Einordnung und Herkunft"

**Titel:** `Aufgabe 5: Einordnung und Herkunft`

**Text:**

> ARIS gliedert Modelle in vier Sichten – Organisations-, Daten-, Funktions- und
> Prozesssicht – auf drei Ebenen: Fachkonzept, DV-Konzept, Implementierung.
>
> **„In welche ARIS-Sicht gehört das Klassendiagramm – und warum?"**
>
> Zusatz: Seit wann ist die UML genormt, und zu welcher Diagrammfamilie zählt
> das Klassendiagramm?
>
> Gruppenarbeit, 4 Minuten – anschließend Auflösung im Plenum.

Der einleitende Satz nennt die Sichten und Ebenen bewusst vor. Ohne ihn wird aus
der Einordnungsfrage eine Abfrage von Vokabeln, und die Gruppen kommen in vier
Minuten nicht zu einer Begründung. Die Vorlesungsfolie 5 zeigt das ARIS-Haus
genau mit diesen Beschriftungen.

---

## 3 Folie „Musterlösung Aufgabe 5"

**Titel:** `Musterlösung Aufgabe 5`

**Einordnung in ARIS**

- **Datensicht:** Das Klassendiagramm beschreibt, welche Daten das System führt
  und wie sie strukturiert sind.
- Der Modulüberblick führt es **zusätzlich in der Funktionssicht** — Klassen
  tragen neben Attributen auch Methoden.
- **Ebene: DV-Konzept** (Modulüberblick, Folie „Behandelte
  Modellierungssprachen").
- **Nicht Prozesssicht:** Abläufe zeigt das Klassendiagramm nicht — siehe
  Aufgabe 3.

**Herkunft**

- **1997:** Die OMG standardisiert UML 1.0; das Klassendiagramm wird eines der
  wichtigsten UML-Diagramme.
- **2005:** UML 2.0 erweitert und präzisiert es.
- Es zählt zu den **Strukturdiagrammen**, nicht zu den Verhaltensdiagrammen
  (Vorlesung, Folie 3).

**Merksatz:** Struktur statt Ablauf — deshalb Datensicht.

---

## 4 Belege

| Aussage | Quelle |
|---|---|
| Vier Sichten, drei Ebenen | `7-UML-KD.pptx`, Folie 5 „Einordnung in ARIS", nach Scheer (2011) |
| Klassendiagramm in Datensicht **und** Funktionssicht, Ebene DV-Konzept | `Konzept.pptx`, Folie 2 „Behandelte Modellierungsprachen" — der Eintrag steht dort zweimal, links neben der Datensicht und rechts neben der Funktionssicht, jeweils auf Höhe der DV-Konzept-Zeile |
| 1997 UML 1.0 durch die OMG, 2005 UML 2.0 | `7-UML-KD.pptx`, Folie 3 „Historie" |
| Strukturdiagramm | `7-UML-KD.pptx`, Folie 3, letzter Absatz: „gehört das Klassendiagramm zu den wichtigsten Strukturdiagrammen (Structure Diagrams) der UML" |
| Zeigt keine Abläufe | `7-UML-KD.pptx`, Folie 24 „Bewertung" |

**Kriterium 8 bleibt unberührt.** Jede Aussage der Musterlösung steht wörtlich
oder als Abbildung in einer Folie, die der Dozent gehalten hat. Es kommt kein
neues Sprachkonstrukt und keine neue Notation dazu.

---

## 5 Betreuung

**Hinweis nach 2 Minuten, wörtlich, von beiden Betreuenden gleich:**

> „Die Frage ist nicht, was das Diagramm zeigt, sondern wohin es im ARIS-Haus
> gehört."

**Erwartbare Rückfragen und die abgestimmte Antwort:**

| Rückfrage | Antwort |
|---|---|
| „Datensicht oder Funktionssicht?" | Beides gilt. Der Modulüberblick führt das Klassendiagramm in beiden Sichten. Bewertet wird die Begründung, nicht das Stichwort. |
| „Fachkonzept oder DV-Konzept?" | Der Modulüberblick setzt es auf DV-Konzept. Wer Fachkonzept nennt und mit „fachliche Struktur, noch keine Technik" begründet, bekommt das ebenfalls anerkannt. |
| „Was ist ein Strukturdiagramm?" | Das Gegenstück sind Verhaltensdiagramme wie Aktivitäts- oder Sequenzdiagramm — die Themen anderer Gruppen. |
| „Müssen wir die Jahreszahlen auswendig können?" | Nein. Die Reihenfolge genügt: erst UML 1.0, dann UML 2.0. |

**Auflösung in vier Minuten:** zuerst die Sicht mit Begründung sammeln, dann die
Doppelnennung im Modulüberblick zeigen, zum Schluss die Historie als
Blitzabfrage. Die Zusatzfrage entfällt, wenn Block 1 hinter dem Zeitplan liegt.

---

## 6 Abdeckung nach dem Einfügen

| Thema der Dozentenpräsentation | A1 | A2 | A3 | A4 | A5 |
|---|:--:|:--:|:--:|:--:|:--:|
| Klasse, Attribute, Methoden | ✓ | ✓ | ✓ | ✓ | — |
| Assoziation | ✓ | ✓ | — | — | — |
| Aggregation | ✓ | ✓ | — | — | — |
| Komposition | ✓ | ✓ | — | — | — |
| Vererbung | ✓ | ✓ | — | ✓ | — |
| Kardinalität `1`, `0..*`, `1..*` | ✓ | ✓ | — | — | — |
| Kardinalität `0..1` | — | ✓ | — | — | — |
| Sichtbarkeit | — | — | — | ✓ | — |
| Einsatzzweck (Folie 4) | — | — | ✓ | — | ✓ |
| Bewertung, Stärken und Grenzen (Folie 24) | — | — | ✓ | — | ✓ |
| **Einordnung in ARIS (Folie 5)** | — | — | — | — | **✓** |
| **Historie (Folie 3)** | — | — | — | — | **✓** |
| Literatur (Folie 25) | — | — | — | — | über die Quellenfolie |

Damit ist jeder Agendapunkt der Dozentenpräsentation mindestens einmal
aufgegriffen.

---

## 7 Dateien

| Datei | Zweck |
|---|---|
| `Aufgabe_5_Einordnung.pptx` | zwei fertige Folien im Layout der Abgabe, mit Notizenseiten |
| `Aufgabe_5_Einordnung.md` | diese Datei: Aufgabentext, Musterlösung, Belege, Betreuung |
| `2026-09-02_Pruefbericht_finale-Abgabe.md` | Prüfbericht zur Abgabe |
