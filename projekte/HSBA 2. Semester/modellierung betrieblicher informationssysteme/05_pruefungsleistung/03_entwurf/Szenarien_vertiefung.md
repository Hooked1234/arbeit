# Szenariotexte Vertiefung — Fassung 2

> **Statusänderung am 30.08.2026, nachmittags.** Block 2 ist nicht mehr der
> Änderungsauftrag, sondern die **Kritik eines KI-erzeugten Diagramms** zum Text
> von Aufgabe 1. Damit gilt:
>
> - **Aufgabe 1 bleibt unverändert gültig** — mit einer Ergänzung: `Präsentation`
>   wird in `Einzelpräsentation` und `Gruppenpräsentation` unterteilt. Die
>   mehrstufige Vererbung steckte bisher nur in Stufe 2; ohne sie hätte
>   Kriterium 9 eine Lücke. Modell jetzt 11 Klassen, 8 Beziehungen,
>   5 Vererbungen — es deckt alle neun Konstrukte allein ab.
> - **Aufgabe 2 unten (Änderungsauftrag mit Zielkonflikt) ist Reserve.** Sie
>   greift, falls das KI-Werkzeug im Raum nicht verfügbar ist. Modell, Diagramme
>   und Konsistenzprüfung dafür bleiben gepflegt.
> - Der neue Text zu Aufgabe 2 wird geschrieben, sobald der eingefrorene
>   KI-Output vorliegt. Die Musterlösung dazu ist die kuratierte Abweichungsliste
>   gegen den Szenariotext, nicht das korrekte Modell.
> - **Die Musterlösung zu Aufgabe 1 wird nicht mehr zu Beginn von Block 2
>   ausgeteilt.** Sie wird am Ende von Block 1 vorgestellt; Maßstab in Block 2
>   ist der Szenariotext. Sonst verkommt die Fehlersuche zum Diagrammvergleich.

Stand: 30.08.2026 · Grundlage:
[Umsetzungsplan](2026-08-30_Umsetzungsplan_vertiefung.md) · Domäne:
Prüfungsverwaltung einer Hochschule · Prinzip: erst modellieren,
dann einen KI-Entwurf zum selben Text prüfen

> **Warum Fassung 2.** Fassung 1 stützte sich auf den 22-Konstrukte-Katalog der
> Auflage 3 aus dem Repository. Am 30.08. kam heraus, dass am 12.08. gar nicht
> die Auflage 2 oder 3 zum Einsatz kam, sondern ein eigener, deutlich
> schlankerer Aufgabensatz (`02_materialien/OneDrive_2026-08-30.zip`,
> „7 - UML Klassendiagramme", Autoren Felix Heinsius und Timo Menzel). Die
> Musterlösungen dort verwenden **neun** Konstrukte — ohne Sichtbarkeiten, ohne
> Datentypen, ohne abstrakte Klassen, Enumerationen, Assoziationsklassen,
> Klassenattribute, abgeleitete Attribute, Rollennamen oder Nebenbedingungen.
> Fassung 1 hätte damit fünf bis sieben Konstrukte eingeführt, die in der
> eigenen Vorstellungsrunde nie vorkamen — direkter Angriff auf Kriterium 8.
> Fassung 2 bleibt strikt im belegten Rahmen.

---

## Belegter Konstruktkatalog

Zwei Quellen, am 30.08.2026 beide beschafft und gegeneinander geprüft:

- **Theoriefoliensatz des Dozenten**, `02_materialien/7-UML-KD.pptx`,
  Prof. Dr. Kamyar Sarshar, 25 Folien — die maßgebliche Quelle für Kriterium 8.
- **Eigene Vorstellungsrunde vom 12.08.2026**,
  `02_materialien/OneDrive_2026-08-30.zip`, Musterlösungsdiagramme zu
  Onlinehandel, Veranstaltungsverwaltung und Hotelverwaltung.

| # | Konstrukt | Foliensatz Dozent | Eigene Runde 12.08. |
|---|---|---|---|
| 1 | Klasse mit drei Kammern | Folien 6, 7, 9 | alle Klassen |
| 2 | Attribut, schlicht — ohne Datentyp | Folien 8, 9 | `kundennummer`, `belegt` |
| 3 | Methode, schlicht — leere Klammern, ohne Parameter | Folien 8, 9 | `einkaufen()` |
| 4 | Assoziation, durchgezogene Linie | Folien 10–12 | alle |
| 5 | Kardinalitäten `1`, `0..1`, `*` / `0..*`, `1..*` | Folie 6 nennt genau diese vier | alle vier verwendet |
| 6 | Aggregation, weiße Raute am Ganzen | Folien 16–18 | `Buchungsposition` ◇— `BuchbareLeistung` |
| 7 | Komposition, schwarze Raute am Ganzen | Folien 13–15 | `Reservierung` ◆— `Buchungsposition` |
| 8 | Vererbung, Dreieck | Folien 19–23 | `Produkt` → physisch / digital |

Zwei Elemente stammen **nur** aus der eigenen Runde, nicht aus den Folien. Beide
sind keine neuen Sprachkonstrukte, sondern Anwendungen der gezeigten, und sind
über die eigene Praxis vom 12.08. gedeckt:

| Element | Status |
|---|---|
| Benannter Assoziationsname mit Leserichtung (*gibt auf*, *tätigt*) | Folien zeigen Assoziationen ohne Namen; eigene Runde verwendet sie durchgehend |
| Mehrstufige Vererbung (`BuchbareLeistung` → `Zimmer` → Suite) | Folien zeigen nur eine Ebene; eigene Runde verwendet zwei |

**Ausgeschlossen, weil in keiner der beiden Quellen notiert:** Datentypen,
Methodensignaturen mit Parametern und Rückgabetypen, Initialwerte, abgeleitete
Attribute, Klassenattribute, Rollennamen, Navigierbarkeit, abstrakte Klassen und
Methoden, `{disjoint, complete}`, Enumerationen, reflexive Assoziationen,
Assoziationsklassen, Notizen und Nebenbedingungen.

**Sonderfall Sichtbarkeit.** Folie 7 nennt sie als Merkmal
(„Die Sichtbarkeit gibt an, wer auf Attribute oder Methoden zugreifen darf"),
aber weder der Dozent noch die eigene Runde notiert `+` oder `-` in einem
Diagramm. Sie bleibt draußen: zulässig, aber nicht eingeführt.

**Vokabular.** Der Dozent sagt **Kardinalität** (nicht Multiplizität) und
**Methode** (nicht Operation). Auflösung, Aufgabenblatt und Betreuungsskript
übernehmen seine Begriffe.

**Größenreferenz.** Die Hotelaufgabe vom 12.08. umfasst mit Extra 13 Klassen und
war für 20 Minuten angesetzt. Ob das gehalten hat, ist nicht protokolliert — der
Zeittest bleibt zwingend. Als Arbeitsannahme sind für 27 Minuten rund
10 Klassen vertretbar; Aufgabe 1 liegt mit 11 knapp darüber. Erster
Kürzungskandidat bleibt `MündlichePrüfung`.

---

## Aufgabe 1 — Prüfungsverwaltung einer Hochschule

> Eine Hochschule verwaltet ihre Studiengänge, Module und Prüfungen in einem
> Softwaresystem. Zu einem Studiengang werden Kürzel, Bezeichnung und
> Regelstudienzeit gespeichert; Module können aufgenommen und der Studienplan
> gedruckt werden. Ein Studiengang fasst mindestens ein Modul zusammen. Dasselbe
> Modul kann in mehreren Studiengängen angeboten werden und bleibt bestehen,
> wenn ein Studiengang eingestellt wird.
>
> Zu einem Modul werden Modulnummer, Titel und Credits gespeichert, außerdem
> kann ein Prüfungstermin angesetzt werden. Zu jedem Modul gehört mindestens ein
> Prüfungstermin, der ohne das Modul nicht existiert. Ein Modul wird von
> mindestens einem Dozenten gelehrt, ein Dozent lehrt beliebig viele Module. Zu
> einem Dozenten werden Personalnummer und Name gespeichert, er kann Noten
> eintragen.
>
> Ein Prüfungstermin besitzt Prüfungsnummer, Datum und Raum; die Anmeldung kann
> geöffnet und der Termin abgesagt werden. Jeder Termin wird von höchstens einem
> Dozenten beaufsichtigt, ein Dozent beaufsichtigt beliebig viele Termine.
> Unterschieden werden:
>
> - Klausuren: Bearbeitungsdauer; Aufsicht einteilen
> - Mündliche Prüfungen: Dauer, Beisitzer; Protokoll anlegen
> - Präsentationen: Vortragsdauer; Technik prüfen
>
> Präsentationen werden weiter unterschieden in Einzelpräsentationen mit einem
> Vortragstermin, der verschoben werden kann, und Gruppenpräsentationen mit
> einer Mitgliederzahl, für die eine Gruppe eingeteilt werden kann.
>
> Zu einem Studenten werden Matrikelnummer, Name und E-Mail gespeichert, er kann
> sich zu einer Prüfung anmelden und seinen Notenspiegel abrufen. Jeder Student
> ist in genau einem Studiengang eingeschrieben, ein Studiengang führt beliebig
> viele Studierende.
>
> Tritt ein Student zu einem Prüfungstermin an, entsteht ein Prüfungsversuch mit
> Versuchsnummer, Datum und Note; er kann als bestanden verbucht werden, und es
> kann von ihm zurückgetreten werden. Ein Prüfungsversuch gehört zu genau einem
> Studenten und existiert ohne ihn nicht; ein Student unternimmt beliebig viele
> Versuche. Jeder Versuch bezieht sich auf genau einen Prüfungstermin. Ein Termin
> wird von beliebig vielen Versuchen genutzt und bleibt bestehen, wenn ein
> Versuch gelöscht wird.

**Ergebnismodell:** 11 Klassen, 6 Beziehungen, 5 Vererbungen.

`Studiengang`, `Modul`, `Dozent`, `Prüfung`, `Klausur`, `MündlichePrüfung`,
`Präsentation`, `Einzelpräsentation`, `Gruppenpräsentation`, `Student`,
`Prüfungsversuch`

Die zweite Vererbungsebene unter `Präsentation` ist seit dem 30.08. Teil von
Aufgabe 1. Sie trägt Konstrukt 9 des belegten Katalogs; ohne sie bliebe die
mehrstufige Vererbung in der Abdeckungsmatrix leer.

Die Klasse `Prüfungsversuch` folgt genau dem Muster, das am 12.08. zweimal
belegt ist: `Bestellposition` zwischen Bestellung und Produkt,
`Buchungsposition` zwischen Reservierung und Leistung. Sie ist eine gewöhnliche
Klasse, keine Assoziationsklasse.

### Rückführbarkeit Aufgabe 1

| Satz | Modellelement |
|---|---|
| verwaltet Studiengänge, Module und Prüfungen | Klassen `Studiengang`, `Modul`, `Prüfung` |
| Kürzel, Bezeichnung und Regelstudienzeit | drei Attribute in `Studiengang` |
| Module können aufgenommen, Studienplan gedruckt werden | `modulAufnehmen()`, `studienplanDrucken()` |
| fasst mindestens ein Modul zusammen | Aggregation `Studiengang` ◇— `Modul`, Ende `Modul 1..*` |
| kann in mehreren Studiengängen angeboten werden | Ende `Studiengang 0..*` |
| bleibt bestehen, wenn ein Studiengang eingestellt wird | leere Raute statt gefüllter |
| Modulnummer, Titel und Credits | drei Attribute in `Modul` |
| kann ein Prüfungstermin angesetzt werden | `pruefungAnsetzen()` |
| Zu jedem Modul gehört mindestens ein Prüfungstermin | Ende `Prüfung 1..*` |
| der ohne das Modul nicht existiert | Komposition, gefüllte Raute an `Modul`, Ende `Modul 1` |
| von mindestens einem Dozenten gelehrt | Assoziation *lehrt*, Ende `Dozent 1..*` |
| ein Dozent lehrt beliebig viele Module | Ende `Modul 0..*` |
| Personalnummer und Name | zwei Attribute in `Dozent` |
| kann Noten eintragen | `noteEintragen()` |
| Prüfungsnummer, Datum und Raum | drei Attribute in `Prüfung` |
| Anmeldung geöffnet, Termin abgesagt | `anmeldungOeffnen()`, `pruefungAbsagen()` |
| von höchstens einem Dozenten beaufsichtigt | zweite Assoziation *beaufsichtigt*, Ende `Dozent 0..1` |
| ein Dozent beaufsichtigt beliebig viele Termine | Ende `Prüfung 0..*` |
| Unterschieden werden: Klausuren, mündliche Prüfungen, Präsentationen | drei Generalisierungen |
| Bearbeitungsdauer; Aufsicht einteilen | `Klausur` mit Attribut und Operation |
| Dauer, Beisitzer; Protokoll anlegen | `MündlichePrüfung` mit zwei Attributen und Operation |
| Vortragsdauer; Technik prüfen | `Präsentation` mit Attribut und Methode |
| Präsentationen werden weiter unterschieden in … | zweite Vererbungsebene unter `Präsentation` |
| Einzelpräsentationen mit einem Vortragstermin, der verschoben werden kann | `Einzelpräsentation`, `vortragstermin`, `terminVerschieben()` |
| Gruppenpräsentationen mit einer Mitgliederzahl, für die eine Gruppe eingeteilt werden kann | `Gruppenpräsentation`, `mitgliederzahl`, `gruppeEinteilen()` |
| Matrikelnummer, Name und E-Mail | drei Attribute in `Student` |
| kann sich anmelden, Notenspiegel abrufen | `zuPruefungAnmelden()`, `notenspiegelAbrufen()` |
| in genau einem Studiengang eingeschrieben | Assoziation *ist eingeschrieben in*, Ende `Studiengang 1` |
| führt beliebig viele Studierende | Ende `Student 0..*` |
| Versuchsnummer, Datum und Note | drei Attribute in `Prüfungsversuch` |
| als bestanden verbucht, zurückgetreten | `alsBestandenVerbuchen()`, `versuchZurücktreten()` |
| gehört zu genau einem Studenten und existiert ohne ihn nicht | Komposition `Student` ◆— `Prüfungsversuch`, Ende `Student 1` |
| ein Student unternimmt beliebig viele Versuche | Ende `Prüfungsversuch 0..*` |
| bezieht sich auf genau einen Prüfungstermin | Ende `Prüfung 1` |
| von beliebig vielen Versuchen genutzt | Ende `Prüfungsversuch 0..*` |
| bleibt bestehen, wenn ein Versuch gelöscht wird | Aggregation `Prüfungsversuch` ◇— `Prüfung` |

---

## Aufgabe 2 — Was ein KI-Werkzeug daraus gemacht hat

Ausgeteilt wird `Diagramme/Aufgabe_2_KI-Entwurf.pdf` (A3 quer). Der
Szenariotext aus Aufgabe 1 liegt weiter auf dem Tisch. Die Musterlösung zu
Aufgabe 1 wird **nicht** ausgeteilt — Maßstab ist der Text.

> Derselbe Szenariotext wurde einem KI-Werkzeug übergeben, mit der Bitte, daraus
> ein UML-Klassendiagramm zu erzeugen. Das Ergebnis liegt euch vor.
>
> Prüft es gegen den Szenariotext, nicht gegen euer eigenes Diagramm. Haltet
> jede Abweichung fest und entscheidet für jede einzeln: Ist das ein Fehler,
> weil der Text etwas anderes verlangt? Oder ist es eine zulässige Abweichung,
> die der Text ebenfalls hergibt?
>
> Tragt zu jeder Abweichung ein, wo im Diagramm sie steht, welche Aussage des
> Textes betroffen ist, wie ihr sie einstuft und wie die Korrektur aussieht.
>
> Zum Schluss beantwortet ihr gemeinsam eine Frage: Welchen der gefundenen
> Fehler hätte das Werkzeug nicht machen können, wenn der Szenariotext an einer
> Stelle genauer gewesen wäre?

**Herkunft des Diagramms, offen gehalten.** Der Entwurf stammt aus einem
KI-Werkzeug, ist aber für den Unterricht kuratiert: Fehlerzahl und Fehlerarten
sind bewusst so gewählt, dass jeder Befund einen eigenen Lernpunkt trifft. Auf
dem Aufgabenblatt steht deshalb „ein KI-Werkzeug hat aus demselben Text das
folgende Diagramm erzeugt" — nicht „unveränderter Output von Werkzeug X".

**Protokollbogen** auf dem Aufgabenblatt, acht bis zehn Zeilen:

| Nr. | Stelle im Diagramm | Betroffene Aussage im Text | Fehler oder zulässig | Korrektur |
|---|---|---|---|---|

### Musterlösung — Fundliste

Acht Fehler, zwei zulässige Abweichungen. Volle Punktzahl bei sechs Fehlern
**und** mindestens einer richtig als zulässig eingestuften Abweichung.

| Nr. | Stelle im KI-Entwurf | Aussage im Text | Befund | Korrektur |
|---|---|---|---|---|
| 1 | `Studiengang` ◆— `Modul`, schwarze Raute | „bleibt bestehen, wenn ein Studiengang eingestellt wird" | **Fehler.** Schwarze Raute heißt: das Teil stirbt mit dem Ganzen. Der Text sagt das Gegenteil. | weiße Raute |
| 2 | `Modul` — `Prüfungstermin`, schlichte Linie | „der ohne das Modul nicht existiert" | **Fehler.** Existenzabhängigkeit verlangt die Komposition. | schwarze Raute an `Modul` |
| 3 | *beaufsichtigt*, Ende am Dozenten `1` | „wird von höchstens einem Dozenten beaufsichtigt" | **Fehler.** „höchstens" schließt null ein. | `0..1` |
| 4 | *ist eingeschrieben in*, `Studiengang 0..*` und `Student 1` | „ist in genau einem Studiengang eingeschrieben, ein Studiengang führt beliebig viele Studierende" | **Fehler.** Beide Enden vertauscht. | `Studiengang 1`, `Student 0..*` |
| 5 | keine Verbindung zwischen `Dozent` und `Modul` | „Ein Modul wird von mindestens einem Dozenten gelehrt, ein Dozent lehrt beliebig viele Module" | **Fehler.** Eine ganze Aussage ist nicht modelliert. | Assoziation *lehrt*, `Dozent 1..*` / `Modul 0..*` |
| 6 | `Einzelpräsentation` und `Gruppenpräsentation` erben von `Prüfungstermin` | „Präsentationen werden unterschieden in …" | **Fehler.** Die zweite Vererbungsebene ist geplättet; beide sind Arten von Präsentation, nicht von Prüfung. | Oberklasse `Präsentation` |
| 7 | `Modul.beschreibung`, `Student.status`, `Prüfungstermin.status` | steht nirgends im Text | **Fehler.** Drei erfundene Attribute. | streichen |
| 8 | `Prüfungsversuch.id` | „mit Versuchsnummer, Datum und Note" | **Fehler.** Der Text nennt eine fachliche Nummer, das Werkzeug setzt einen technischen Schlüssel. | `versuchsnummer` |
| 9 | `Prüfungsversuch` — `Prüfungstermin`, schlichte Linie | „bleibt bestehen, wenn ein Versuch gelöscht wird" | **Zulässig.** Der Satz schließt nur die Komposition aus. Weiße Raute und schlichte Assoziation sind beide vertretbar. | keine |
| 10 | Klasse heißt `Prüfungstermin` statt `Prüfung` | Text verwendet beide Wörter | **Zulässig.** Benennung ist keine Korrektheitsfrage, solange sie durchgehalten wird. | keine |

### Antwort auf die Schlussfrage

Nur zwei Befunde hängen wirklich am Text. Die **erfundenen Attribute** (Nr. 7)
entstehen, weil der Text nirgends sagt, dass die genannten Angaben abschließend
sind. Und die **Rautenfrage bei Prüfungsversuch** (Nr. 9) ist offen, weil der
Text nur sagt, was nicht gilt, aber nicht, ob eine Teil-Ganzes-Beziehung
gemeint ist.

Alle übrigen sechs Fehler stehen eindeutig im Text — das Werkzeug hat sie
schlicht überlesen. Das ist der Punkt der Aufgabe: Ein Modell ist höchstens so
eindeutig wie seine Anforderungen, aber die meisten Fehler entstehen trotzdem
nicht am Text, sondern beim Modellieren.

### Ablauf Block 2

| Zeit | Inhalt |
|---|---|
| 0–5 | KI-Entwurf und Protokollbogen austeilen, Auftrag vorlesen |
| 5–28 | Bearbeitung. Hinweis Minute 12: „Geht die Beziehungen der Reihe nach durch, nicht die Kästen." Hinweis Minute 20: „Zwei der Abweichungen sind keine Fehler." |
| 28–43 | Auflösung: Fundliste durchgehen, dabei Musterlösung Aufgabe 1 zeigen |
| 43–45 | Schlussfrage gemeinsam beantworten |

### Warum das die Fortführung einlöst

Block 2 arbeitet an demselben Text und demselben Modell wie Block 1, aber in
umgekehrter Richtung: erst konstruieren, dann prüfen. Wer Block 1 nicht
fertigbekommen hat, kann Block 2 trotzdem vollständig bearbeiten — der Maßstab
ist der Text, nicht das eigene Ergebnis. Das ist robuster als der
Änderungsauftrag, der eine korrekte Ausgangslösung voraussetzt.

---

## Reserve — Aufgabe 2 als Änderungsauftrag

Greift nur, falls der KI-Entwurf nicht eingesetzt werden kann. Modell,
Diagramme und Konsistenzprüfung dafür sind gepflegt.

### Die neue Prüfungsordnung

> Zwei Jahre später tritt eine neue Prüfungsordnung in Kraft. Das bestehende
> Modell ist an die folgenden Änderungen anzupassen.
>
> Ob ein Modul in einem Studiengang Pflicht oder Wahlpflicht ist, unterscheidet
> sich von Studiengang zu Studiengang, ebenso das Fachsemester, in dem es dort
> vorgesehen ist. Für jede Zuordnung eines Moduls zu einem Studiengang werden
> deshalb Art und Fachsemester gespeichert, und die Art kann geändert werden.
> Ein Studiengang hat mindestens eine solche Zuordnung und ohne ihn existiert
> sie nicht; ein Modul kann in beliebig vielen Zuordnungen vorkommen und bleibt
> bestehen, wenn eine davon entfällt. Jede Zuordnung betrifft genau einen
> Studiengang und genau ein Modul.
>
> Leistungen, die an einer anderen Hochschule erbracht wurden, werden künftig
> anerkannt und zählen wie eigene Prüfungsversuche. Zu einer anerkannten
> Leistung werden Hochschule und dortige Bezeichnung gespeichert, der Nachweis
> kann geprüft werden; einen Prüfungstermin an der eigenen Hochschule hat sie
> nicht. Stattdessen bezieht sie sich auf genau ein Modul, das unabhängig von ihr
> bestehen bleibt und in beliebig vielen anerkannten Leistungen vorkommen kann.
> Anerkannte Leistungen und Prüfungsversuche haben Datum und Note gemeinsam,
> gehören beide zu genau einem Studenten und können beide angeben, auf welches
> Modul sie angerechnet werden.
>
> Präsentationen werden künftig unterschieden in Einzelpräsentationen mit einem
> Vortragstermin, der verschoben werden kann, und Gruppenpräsentationen mit einer
> Mitgliederzahl, für die eine Gruppe eingeteilt werden kann.
>
> Eine Gruppenpräsentation wird nur einmal bewertet, und die Note gilt für alle
> Beteiligten gleichermaßen. Bisher gilt: Ein Prüfungsversuch gehört zu genau
> einem Studenten und existiert ohne ihn nicht. Entscheidet, wie beides
> zusammenpasst, und haltet eure Entscheidung im Diagramm fest.

**Endmodell:** 14 Klassen, 8 Beziehungen, 7 Generalisierungen.

Neu: `Modulzuordnung`, `Leistung`, `AnerkannteLeistung`, `Einzelpräsentation`,
`Gruppenpräsentation`. `Prüfungsversuch` behält nur noch `versuchsnummer`, alles
Gemeinsame wandert nach `Leistung`.

### Rückführbarkeit Aufgabe 2

| Satz | Modellelement | Sorte |
|---|---|---|
| Art und Fachsemester je Zuordnung; die Art kann geändert werden | neue Klasse `Modulzuordnung` mit zwei Attributen und `artÄndern()` | Umbau |
| Ein Studiengang hat mindestens eine Zuordnung, ohne ihn existiert sie nicht | Komposition `Studiengang` ◆— `Modulzuordnung`, Enden `1` und `1..*` | Umbau |
| ein Modul kann in beliebig vielen vorkommen und bleibt bestehen | Aggregation `Modulzuordnung` ◇— `Modul`, Enden `0..*` und `1` | Umbau |
| Jede Zuordnung betrifft genau einen Studiengang und genau ein Modul | die Aggregation `Studiengang` ◇— `Modul` aus Aufgabe 1 entfällt ersatzlos | **Umbau, Kern** |
| Hochschule und dortige Bezeichnung, Nachweis prüfen | neue Klasse `AnerkannteLeistung` mit zwei Attributen und `nachweisPrüfen()` | neu |
| einen Prüfungstermin an der eigenen Hochschule hat sie nicht | die Beziehung zu `Prüfung` bleibt allein bei `Prüfungsversuch` | **Umbau, Kern** |
| bezieht sich auf genau ein Modul, das unabhängig bestehen bleibt | Aggregation `AnerkannteLeistung` ◇— `Modul`, Enden `0..*` und `1` | neu |
| haben Datum und Note gemeinsam | neue Oberklasse `Leistung` mit `datum` und `note`; beide Attribute verlassen `Prüfungsversuch` | Umbau |
| gehören beide zu genau einem Studenten | die Komposition `Student` ◆— `Prüfungsversuch` wandert nach `Student` ◆— `Leistung` | Umbau |
| können beide angeben, auf welches Modul sie angerechnet werden | `angerechnetesModulErmitteln()` in `Leistung` | Umbau |
| zählen wie eigene Prüfungsversuche | zwei Generalisierungen `Leistung` → `Prüfungsversuch`, `AnerkannteLeistung` | Umbau |
| Einzelpräsentationen mit Vortragstermin, verschieben | `Einzelpräsentation` mit Attribut und `terminVerschieben()` | neu |
| Gruppenpräsentationen mit Mitgliederzahl, Gruppe einteilen | `Gruppenpräsentation` mit Attribut und `gruppeEinteilen()` | neu |
| Präsentationen werden unterschieden in … | zweite Generalisierungsebene unter `Präsentation` | neu |
| nur einmal bewertet, Note gilt für alle Beteiligten | Auslöser des Zielkonflikts | **Konflikt** |
| Bisher gilt: gehört zu genau einem Studenten und existiert ohne ihn nicht | die Komposition aus Aufgabe 1 gerät in Widerspruch | **Konflikt** |
| Entscheidet … und haltet eure Entscheidung im Diagramm fest | Pflichtbestandteil der Abgabe, Feld auf dem Aufgabenblatt | **Konflikt** |

---

## Der Zielkonflikt

Der Konflikt ist schärfer als in Fassung 1, weil er an einer **Komposition**
hängt: Eine Komposition erlaubt am Ganzen-Ende nur `1`. Eine gemeinsam bewertete
Gruppenleistung gehört aber zu mehreren Studierenden.

**Variante A — eine Leistung für die ganze Gruppe.**
Die Komposition wird zur gewöhnlichen Assoziation, das Studenten-Ende wird
`1..*`. Ein Objekt trägt die Note für alle. Preis: Die Existenzabhängigkeit
geht verloren — eine Leistung könnte ohne Studenten weiterexistieren.

**Variante B — eine Leistung je Mitglied.**
Die Komposition bleibt unverändert. Für jedes Gruppenmitglied entsteht eine
eigene Leistung; alle beziehen sich auf dieselbe `Gruppenpräsentation`. Preis:
Die Note steht mehrfach im System, ihre Gleichheit ist im Diagramm nicht
erzwungen.

Beide Varianten sind zulässig. Bewertet wird nicht die Wahl, sondern ob der
Widerspruch erkannt, entschieden und im Diagramm vermerkt wurde. Die
Lehrendenfassung enthält beide ausgearbeitet, das Differenzdiagramm zeigt
Variante B, weil sie die Beziehung aus Aufgabe 1 unangetastet lässt.

Didaktischer Kern der Auflösung: **Eine Komposition ist eine Aussage über
Existenz, nicht über Zugehörigkeit.** Genau daran scheitert sie hier.

---

## Konstruktabdeckung

Nachweis für Kriterium 9 gegen den belegten Katalog. Alle neun Konstrukte
kommen in beiden Aufgaben vor.

| # | Konstrukt | A1 | A2 |
|---|---|:--:|:--:|
| 1 | Klasse mit drei Kammern | ● | ● |
| 2 | Attribut, schlicht | ● | ● |
| 3 | Operation, schlicht | ● | ● |
| 4 | Benannte Assoziation mit Leserichtung | ● | ● |
| 5 | Multiplizität `1` | ● | ● |
| 5 | Multiplizität `0..1` | ● *beaufsichtigt* | |
| 5 | Multiplizität `0..*` | ● | ● |
| 5 | Multiplizität `1..*` | ● | ● |
| 6 | Aggregation | ● | ● |
| 7 | Komposition | ● | ● |
| 8 | Generalisierung | ● | ● |
| 9 | Mehrstufige Vererbung | ● | ● |

**Aufgabe 1 deckt seit dem 30.08. alle neun Konstrukte allein ab.** Das ist
der Grund, warum die Präsentationsarten dorthin gewandert sind: Block 2 ist
jetzt die Prüfung eines fremden Entwurfs und garantiert von sich aus keine
Konstruktabdeckung mehr.

Zwei Konstrukte hängen an je einer Stelle und sind nicht kürzbar: `0..1` allein
an *beaufsichtigt*, die mehrstufige Vererbung allein an den Präsentationsarten.

Der KI-Entwurf in Block 2 greift acht der neun Konstrukte erneut auf — jeder
Befund der Fundliste betrifft mindestens eines. Die Auflösung benennt sie
einzeln; das ist der Nachweis für Kriterium 9 aus dem zweiten Block heraus.

---

## Kürzungskandidaten

| Rang | Kandidat | Verlust |
|---|---|---|
| 1 | `MündlichePrüfung` in Aufgabe 1 streichen, zwei statt drei Prüfungsformen | keiner |
| 2 | `Dozent` verliert die Operation `noteEintragen()` | keiner |
| 3 | `AnerkannteLeistung` in Aufgabe 2 streichen | der zweite Umbau entfällt; Aufgabe 2 verliert erheblich an Substanz |

Nicht kürzbar: die Beziehung *beaufsichtigt* (einziger `0..1`), die
Präsentationsarten (einzige mehrstufige Generalisierung), der Umbau der
Studiengang-Modul-Beziehung, der Zielkonflikt.

---

## Offene Prüfpunkte

- **Kriterium 8 ist geprüft und erfüllt.** Der Foliensatz liegt seit dem
  30.08. vor. Jedes in beiden Aufgaben verlangte Konstrukt steht entweder in den
  Folien oder war in der eigenen Vorstellungsrunde bereits im Einsatz. Kein
  Konstrukt geht darüber hinaus. Die Fassung 1 dieses Dokuments hätte sieben
  Konstrukte eingeführt, die in keiner der beiden Quellen vorkommen.
- **Zeit.** Aufgabe 1 geschätzt 22 bis 26 Minuten für 9 Klassen, Aufgabe 2
  geschätzt 20 bis 25 Minuten für 5 neue Klassen und drei Umbauten. Die
  Schätzung bleibt wertlos bis zum Zeittest.
- **Keine Checkliste.** Die eigene Aufgabe 1 vom 12.08. hatte eine
  Checklistenfolie, die die Beziehungstypen ausdrücklich nannte; die Aufgaben 2
  und 3 hatten keine. Für eine Vertiefung nähme eine solche Checkliste die
  Lösung vorweg. Das Aufgabenblatt enthält deshalb nur Szenario, Arbeitsauftrag
  und, bei Aufgabe 2, das Feld für die Konfliktentscheidung.
- **Domänenkollision geprüft.** Onlinehandel, Veranstaltungsverwaltung und
  Hotelverwaltung sind durch die eigene Vorstellungsrunde verbraucht, Bibliothek,
  Hotelreservierung, Studienbewerbung, Arzttermin und Reklamation durch die
  EPK-Aufgaben des Dozenten, Online-Fahrradvermietung durch die Peer-Gruppe zum
  UML-Überblick. Prüfungsverwaltung ist frei.
