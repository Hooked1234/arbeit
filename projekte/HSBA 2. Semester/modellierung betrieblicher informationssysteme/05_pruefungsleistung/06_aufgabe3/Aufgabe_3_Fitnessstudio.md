# Aufgabe 3 — „Lies das Modell" (Fitnessstudio)

Stand: 01.09.2026 · Durchführung: 02.09.2026 · Umfang: 13 Minuten
· Platz: Ende Block 1, direkt nach der Auflösung von Aufgabe 1

Ergänzung zur Abgabe `Modellierung betrieblicher Informationssysteme Abgabe.pptx`.
Zweck: die Themen der Dozentenpräsentation schließen, die Aufgabe 1 und Aufgabe 2
nicht berühren — vor allem Kriterium 9 („Alle Themen wiederholt", 12 Punkte, das
höchstgewichtete Einzelkriterium) und Kriterium 2 („unterschiedliche Denk- und
Anwendungsformen").

---

## 1 Warum diese Aufgabe

| Denkform | Aufgabe |
|---|---|
| Ein gegebenes Modell prüfen und korrigieren | Aufgabe 1 |
| Aus einem Text ein Modell konstruieren | Aufgabe 2 |
| **Ein Modell lesen, versprachlichen und einordnen** | **Aufgabe 3** |

Aufgabe 3 verlangt kein Zeichnen. Sie kostet deshalb wenig Zeit, greift aber
genau die Themen auf, die in Aufgabe 1 und 2 fehlen: Einsatzzweck des
Klassendiagramms, seine Grenzen (Folie „Bewertung"), die Sichtbarkeit als
Begriff und die vier Kardinalitäten als geschlossener Satz.

---

## 2 Folie „Aufgabe 3: Lies das Modell"

**Titel:** `Aufgabe 3: Lies das Modell`

**Text (direkt übernehmbar):**

> Das folgende Klassendiagramm beschreibt ein Fitnessstudio. Beantworten Sie die
> fünf Fragen stichpunktartig. Es ist nichts zu zeichnen.
> Bearbeitungszeit: 7 Minuten.
>
> 1. Das Studio wird geschlossen und aus dem System gelöscht. Was geschieht mit
>    den Kursen, was mit den Mitgliedern? Begründen Sie mit dem jeweiligen
>    Beziehungstyp.
> 2. Über welche Attribute und Methoden verfügt ein Objekt der Klasse `Trainer`
>    insgesamt? Warum steht `name` nicht in der Klasse `Trainer` selbst?
> 3. Formulieren Sie die Beziehung zwischen `Trainer` und `Kurs` in zwei
>    Sätzen — je Leserichtung einen.
> 4. Ein neues Mitglied hat noch keinen Kurs gebucht und kein Schließfach. Ist
>    das nach dem Modell zulässig? Nennen Sie die beiden Kardinalitäten, die
>    Ihre Antwort belegen.
> 5. Der Betreiber fragt: „In welcher Reihenfolge läuft eine Kursbuchung ab?"
>    Kann das Klassendiagramm diese Frage beantworten? Wenn nein: warum nicht,
>    und welche Modellart wäre geeignet?

**Bild:** `Aufgabe_3_Fitnessstudio.svg` (Diagramm ohne Fehler, dient nur zum
Lesen). Die SVG-Datei über *Einfügen → Bilder → Dieses Gerät* einsetzen;
PowerPoint skaliert sie verlustfrei.

---

## 3 Folie „Musterlösung Aufgabe 3"

**Titel:** `Musterlösung Aufgabe 3`

| Nr. | Antwort |
|---|---|
| 1 | Die **Kurse werden mitgelöscht** — Komposition, schwarze Raute am `Fitnessstudio` als dem Ganzen: das Teil kann ohne das Ganze nicht existieren. Die **Mitglieder bleiben bestehen** — Aggregation, weiße Raute: die Teile sind vom Ganzen unabhängig. |
| 2 | Geerbt von `Person`: `name`, `geburtsdatum`, `kontaktdatenÄndern()`. Eigene: `personalnummer`, `qualifikation`, `kursLeiten()`. `name` steht in `Person`, weil `Mitglied` und `Trainer` dieses Merkmal teilen — es wird einmal in der Oberklasse festgelegt und an beide Unterklassen vererbt. |
| 3 | „Jeder Kurs wird von genau einem Trainer geleitet." (Kardinalität `1` am Ende `Trainer`) — „Jeder Trainer leitet mindestens einen Kurs." (Kardinalität `1..*` am Ende `Kurs`) |
| 4 | Ja, zulässig. `0..*` am Ende `Kurs` der Beziehung `Mitglied`–`Kurs` erlaubt null Kurse; `0..1` am Ende `Schließfach` erlaubt kein Schließfach. |
| 5 | Nein. Das Klassendiagramm zeigt nur die **statische Struktur** — welche Klassen es gibt, welche Merkmale sie haben und wie sie zusammenhängen. Reihenfolgen, Ereignisse und Abläufe stellt es nicht dar (Folie „Bewertung": „Zeigt keine Abläufe oder Prozesse"). Für Abläufe eignen sich Aktivitätsdiagramm, EPK oder BPMN. |

**Zwei Zusatzfragen, nur mündlich in der Auflösung** (nicht auf der Folie, damit
sie nicht bewertet werden müssen):

- „Der Foliensatz nennt die **Sichtbarkeit** als Merkmal einer Klasse. Was legt
  sie fest?" → Wer auf Attribute und Methoden zugreifen darf.
- „Wo steht das Klassendiagramm im **ARIS**-Haus?" → auf der Struktur- bzw.
  Datenseite, Ebene Fachkonzept. *Achtung:* Die Konzeptfolie führt das
  Klassendiagramm sowohl unter Datensicht als auch unter Funktionssicht. Die
  Frage deshalb offen stellen und beide Nennungen gelten lassen.

---

## 4 Zeitgerüst

**Block 1 — 45 Minuten**

| Zeit | Inhalt |
|---|---|
| 0–3 | Einstieg, Aufgabe 1 austeilen und Text einmal vorlesen |
| 3–18 | Bearbeitung Aufgabe 1 (15 Min) |
| 18–30 | Auflösung Aufgabe 1 mit den sechs Markierungen (12 Min) |
| 30–37 | **Bearbeitung Aufgabe 3 (7 Min)** |
| 37–43 | **Auflösung Aufgabe 3 inklusive der zwei Zusatzfragen (6 Min)** |
| 43–45 | Puffer |

**Block 2 — 45 Minuten:** unverändert Aufgabe 2 (3 Min austeilen, 27 Min
Bearbeitung, 14 Min Auflösung, 1 Min Abschluss).

**Kürzungsregel bei Zeitdruck:** Fragen 3 und 5 entfallen schriftlich und werden
in der Auflösung nur mündlich gestellt. Damit sinkt Aufgabe 3 auf 8 Minuten,
ohne dass ein Thema wegfällt.

**Alternative Platzierung:** Aufgabe 3 als Einstieg in Block 2. Dann als
Aufwärmer, gleiche Zeiten. Block 1 ist mit Aufgabe 1 allein aber weniger
ausgelastet, deshalb die Empfehlung oben.

---

## 5 Das Modell

Sechs Klassen, sechs Beziehungen. Bewusst so klein, dass es in einer Minute
erfasst ist — Substanz der Aufgabe ist das Lesen, nicht das Erschließen.

| Beziehung | Typ | Kardinalitäten |
|---|---|---|
| `Person` → `Mitglied`, `Trainer` | Vererbung | — |
| `Fitnessstudio` ◆— `Kurs` | Komposition | — |
| `Fitnessstudio` ◇— `Mitglied` | Aggregation | — |
| `Schließfach` — `Mitglied` | Assoziation | `0..1` / `1` |
| `Mitglied` — `Kurs` | Assoziation | `0..*` / `0..*` |
| `Trainer` — `Kurs` | Assoziation | `1` / `1..*` |

Aggregation und Komposition tragen keine Kardinalitäten — genau wie in den
Beispielen des Dozenten (`7-UML-KD.pptx`, Folien 14–18 und 23) und wie in den
Musterlösungen der Aufgaben 1 und 2. Die Notation bleibt damit im ganzen
Foliensatz einheitlich.

**Domänenwahl.** „Fitnessstudio / Kurs / Mitglied / Trainer" ist das gleiche
Muster wie die Aggregationsbeispiele des Dozenten (`Firma / Mitarbeiter`,
`Mannschaft / Spieler`, `Musikband / Musiker`) und deshalb ohne Erklärung
verständlich. Verbraucht sind: Onlinehandel, Veranstaltungsverwaltung und
Hotelverwaltung (eigene Runde 12.08.), Hochschulprüfungsverwaltung (Aufgabe 1),
Finanzbuchhaltung (Aufgabe 2), Bibliothek, Hotelreservierung, Studienbewerbung,
Arzttermin und Reklamation (EPK-Aufgaben des Dozenten) sowie Fahrradvermietung
(Peer-Gruppe Einzelthema 5).

---

## 6 Abdeckung — Nachweis für Kriterium 9

| Thema der Dozentenpräsentation | Aufg. 1 | Aufg. 2 | Aufg. 3 |
|---|:--:|:--:|:--:|
| Klasse, Attribute, Methoden | ✓ | ✓ | ✓ |
| Assoziation | ✓ | ✓ | ✓ |
| Aggregation | ✓ | ✓ | ✓ |
| Komposition | ✓ | ✓ | ✓ |
| Vererbung | ✓ | ✓ | ✓ |
| Kardinalität `1` | ✓ | ✓ | ✓ |
| Kardinalität `0..1` | — | ✓ | ✓ |
| Kardinalität `0..*` / `*` | ✓ | ✓ | ✓ |
| Kardinalität `1..*` | ✓ | ✓ | ✓ |
| Sichtbarkeit (Begriff, Folie 7) | — | — | ✓ Zusatzfrage |
| Einsatzzweck (Folie 4) | — | — | ✓ Frage 5 |
| Stärken und Grenzen (Folie 24) | — | — | ✓ Frage 5 |
| Einordnung in ARIS (Folie 5) | — | — | ✓ Zusatzfrage |
| Historie (Folie 3) | — | — | — |

Die Historie bleibt bewusst außen vor: sie ist kein Modellierungsinhalt und
lässt sich in einer Übung nicht sinnvoll anwenden.

**Kein Konstrukt außerhalb des Katalogs.** Aufgabe 3 verwendet ausschließlich
Klasse, Attribut, Methode, Assoziation, Aggregation, Komposition, Vererbung und
die vier Kardinalitäten `1`, `0..1`, `0..*`, `1..*` — also genau den Umfang von
`7-UML-KD.pptx`. Keine Sichtbarkeitszeichen, keine Datentypen, keine abstrakten
Klassen, keine Enumerationen. Kriterium 8 bleibt unberührt.

---

## 7 Betreuung

**Hinweisstaffel, wörtlich, von beiden Betreuenden gleich:**

- Minute 3: „Frage 1 beantworten Sie über die Form der Raute, nicht über den
  Text."
- Minute 5: „Wer bei Frage 4 unsicher ist: lesen Sie die Kardinalität immer am
  Ende der Linie, die bei der Klasse steht, über die Sie sprechen."

**Erwartbare Rückfragen und die abgestimmte Antwort:**

| Rückfrage | Antwort |
|---|---|
| „Warum stehen an der Raute keine Zahlen?" | Richtig beobachtet — Aggregation und Komposition zeigen wir wie in der Präsentation ohne Kardinalitäten. Für die Frage ist das nicht nötig. |
| „Zählen bei Frage 2 auch die Methoden der Oberklasse?" | Ja, alles, was vererbt wird. |
| „Muss ich bei Frage 3 UML-Begriffe verwenden?" | Nein, ein normaler deutscher Satz je Richtung genügt. |
| „Bei Frage 5 — welches Diagramm genau?" | Nennen Sie eine Modellart, die Abläufe zeigt; mehrere Antworten sind richtig. |

---

## 8 Dateien

| Datei | Zweck |
|---|---|
| `Aufgabe_3_Fitnessstudio.svg` | Diagramm für die Aufgabenfolie und das Handout |
| `Aufgabe_3_Fitnessstudio.md` | diese Datei: Aufgabentext, Musterlösung, Zeitplan, Abdeckung |
| `Pruefbericht_Abgabe.md` | Prüfbericht zur bestehenden Abgabe |

Das SVG lässt sich in draw.io öffnen (*Datei → Importieren*), falls das Modell
noch angepasst werden soll.

Das Diagramm gehört zusätzlich **auf Papier**. Auf der Folie erscheint die
Beschriftung von Klassendiagrammen in dieser Größe bei etwa 7 Punkt — zum Lesen
und Beantworten reicht das nicht. Das gilt gleichermaßen für die Diagramme der
Aufgaben 1 und 2.
