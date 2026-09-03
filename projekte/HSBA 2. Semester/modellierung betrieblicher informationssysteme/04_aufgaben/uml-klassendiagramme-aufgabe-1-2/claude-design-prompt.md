# Prompt für Claude Design — Abgabe-Präsentation MOBIS

Stand: 31.08.2026 · Quelle des Designs: `standards/praesentation-hsba.md`

Der folgende Block ist der fertige Prompt. Unverändert kopieren, nur die mit
⟦…⟧ markierten Stellen vorher füllen.

---

## AUFTRAG

Baue eine prüfungsfertige Präsentation im Format 16:9 (33,87 × 19,05 cm) als
finale Abgabe für ein Hochschulmodul. Die Folien müssen ohne Nacharbeit
präsentierbar und abgabefähig sein. Alle Diagramme als native, editierbare
Formen aufbauen — keine Rasterbilder, kein eingebetteter Screenshot.

## KONTEXT

- Autor: Felix Heinsius, HSBA (Hamburg School of Business Administration),
  duales Studium, 2. Semester.
- Modul: Modellierung betrieblicher Informationssysteme, Lehrsprache Deutsch.
- Anlass: Übungsabgabe zu zwei UML-Modellierungsaufgaben. Bewertet wird
  fachliche Korrektheit, roter Faden und saubere Notation.
- Publikum: Dozent:in und Kommilitonen, alle mit UML-Grundkenntnissen.
  Fachbegriffe müssen nicht erklärt, aber korrekt verwendet werden.
- Vortragsdauer: ca. 15 Minuten.
- Titelblattdaten: Felix Heinsius · Matrikelnummer ⟦offen⟧ · HSBA · 2. Semester ·
  Dozent:in ⟦offen⟧ · Datum ⟦Abgabedatum⟧.

## DESIGNSYSTEM (verbindlich, keine Abweichung)

Farben
- Primär `#002C58` (Titel, Flächen, Diagrammrahmen)
- Sekundär `#4779AE` (Akzentlinien, Beschriftungen, Aufzählungszeichen)
- Text `#212121` · Hintergrund `#FFFFFF` · Gedämpft `#6B6B6B` (Fußzeile, Quellen)
- Kompartiment-Füllung Klassenkopf `#E4ECF4`, Tabellenzeile alternierend `#F2F5F9`

Typografie
- Schrift: Titillium Web, Fallback Arial. Nur eine Schriftfamilie.
- Folientitel 28–32 pt bold · Untertitel 20–24 pt · Fließtext 18–20 pt ·
  Bullet-Ebene 2 16–18 pt · Diagrammbeschriftung 8–9 pt · Quelle/Fußzeile 9–10 pt
- Zeilenabstand 1,15–1,2. Maximal zwei Schriftgrößensprünge pro Folie.

Layout
- Seitenränder 2,0 cm seitlich, 1,5 cm oben/unten. Alles am Raster ausrichten,
  keine freischwebenden Elemente.
- Folientitel linksbündig oben, als **Aussagesatz** formuliert
  („Neun Klassen bilden Studium, Lehre und Prüfung ab" statt „Klassendiagramm"),
  einzeilig, kein Punkt am Ende. Darunter eine 4,2 cm breite Akzentlinie in `#4779AE`.
- Maximal ~40 Wörter oder 5–6 Bullets pro Folie. Ein Kerngedanke pro Folie.
- Bullets parallel formuliert, keine ganzen Sätze.
- Fußzeile auf jeder Inhaltsfolie: „Felix Heinsius · Modellierung betrieblicher
  Informationssysteme · HSBA" links, Foliennummer rechts, 9 pt, gedämpft.
- Abschnittstrenner: vollflächig `#002C58`, Text weiß, ohne Fußzeile.

## FOLIENSTRUKTUR (14 Folien)

1. Titel — Thema, beide Aufgaben als Untertitel, Autorenblock
2. Agenda, nummeriert
3. Abschnittstrenner „Aufgabe 1 · Hochschulverwaltung"
4. Vorgehen und Notation — links das Vorgehen vom Text zum Modell, rechts eine
   gezeichnete Legende der vier Beziehungstypen (Assoziation, Aggregation,
   Komposition, Vererbung) mit den echten UML-Symbolen
5. **Vollformatfolie: Klassendiagramm 1** (Spezifikation unten)
6. Tabelle: Beziehung · Typ · Multiplizität · Begründung aus dem Aufgabentext
7. Vererbung der Prüfungsformen — kleines Diagramm plus 4 Bullets zum Nutzen
8. Abschnittstrenner „Aufgabe 2 · Finanzbuchhaltung"
9. **Vollformatfolie: Klassendiagramm 2** (Spezifikation unten)
10. Kernentscheidungen des Modells, 5 Bullets
11. Antwortfolie zur gestellten Frage: Zugriff der Klasse Administrator —
    links die Vererbungskette als Diagramm, rechts die Aufzählung, darunter ein
    Hinweiskasten in `#E4ECF4` zur Sichtbarkeit
12. Prüfpunkte: Tabelle mit Stelle im Modell · Aufgabentext · Anpassung
13. Fazit, 5 Kernaussagen, keine neuen Informationen
14. Quellen, Chicago Author-Date, alphabetisch

## DIAGRAMM 1 — HOCHSCHULVERWALTUNG (Folie 5, Vollformat)

Klassen im Format `Name(attribute | methoden())`:
- `Studiengang(kuerzel, bezeichnung, regelstudienzeit | modulAufnehmen(), studienplanDrucken())`
- `Modul(modulnummer, titel, credits | prüfungAnsetzen())`
- `Dozent(personalnummer, name | noteEintragen())`
- `Student(matrikelnummer, name, email | zuPrüfungAnmelden(), notenspiegelAbrufen())`
- `Prüfung(prüfungsnummer, datum, raum | anmeldungÖffnen(), prüfungAbsagen())`
- `Prüfungsversuch(versuchsnummer, datum, note | alsBestandenVerbuchen(), versuchZurücktreten())`
- `Klausur(bearbeitungsdauer | aufsichtEinteilen())`
- `MündlichePrüfung(dauer, beisitzer | protokollAnlegen())`
- `Präsentation(vortragsdauer | technikPrüfen())`

Beziehungen (Raute steht jeweils bei der zuerst genannten Klasse):
- Studiengang ◇— Modul · 0..* : 1..* · „fasst zusammen"
- Modul — Dozent · 0..* : 1..* · „lehrt"
- Modul ◆— Prüfung · 1 : 1..* · „setzt an"
- Studiengang — Student · 1 : 0..* · „ist eingeschrieben in"
- Dozent — Prüfung · 0..1 : 0..* · „beaufsichtigt"
- Student ◆— Prüfungsversuch · 1 : 0..* · „unternimmt"
- Prüfungsversuch ◇— Prüfung · 0..* : 1 · „bezieht sich auf"
- Generalisierung: Prüfung ◁— Klausur, MündlichePrüfung, Präsentation

## DIAGRAMM 2 — FINANZBUCHHALTUNG (Folie 9, Vollformat)

- `Geschäftspartner(name, adresse, telefonnummer | löschen(), duplizieren())`
- `Kunde(sepaMandat | abmahnen())` · `Lieferant(iban | bezahlen())`
- `Rechnung(rechnungsnummer, rechnungsdatum, gesamtbetrag | gesamtbetragBerechnen())`
- `Rechnungsposition(produkt, menge, einzelpreis | —)`
- `Zahlung(zahlungsdatum, betrag | wiederholen())`
- `Buchungssatz(buchungsdatum, rechnungsnummer, buchungstext | wiederholen())`
- `Buchungsposition(betrag, sachkonto | wiederholen())`
- `Sachkonto(kontonummer, bezeichnung, kontotyp | löschen(), duplizieren())`
- `Buchungsperiode(beginn, ende, status | —)`
- `Mitarbeiter(personalnummer, name, e-mail | —)`
- `Buchhalter(— | buchen())` · `Administrator(— | benutzerVerwalten(), einstellungenVerwalten())`

Beziehungen:
- Generalisierung: Geschäftspartner ◁— Kunde, Lieferant
- Generalisierung: Mitarbeiter ◁— Buchhalter ◁— Administrator (zweistufig!)
- Kunde — Rechnung · 1 : 0..* · Lieferant — Rechnung · 1 : 0..*
- Rechnung ◆— Rechnungsposition · Rechnung — Zahlung · 1 : 0..*
- Rechnung — Buchungssatz · 1..* : 1
- Buchungsperiode ◇— Buchungssatz
- Buchungssatz ◆— Buchungsposition
- Buchungsposition — Sachkonto · 0..* : 1
- Buchhalter — Buchungssatz · 1 : 0..*

## DIAGRAMM-REGELN

- Klassenkasten mit drei Kompartimenten: Name (zentriert, bold, `#E4ECF4`),
  Attribute, Methoden. Leere Kompartimente als leerer Kasten zeichnen, nicht weglassen.
- Rahmen und Verbindungslinien `#002C58`, 0,75 pt.
- Komposition = gefüllte Raute, Aggregation = offene Raute, jeweils beim Ganzen.
  Vererbung = offenes Dreieck an der Oberklasse.
- Multiplizitäten stehen an dem Ende, für dessen Klasse sie gelten.
- Beziehungsnamen kursiv in `#4779AE`.
- Verbindungen rechtwinklig führen, Kreuzungen vermeiden, keine Linie durch
  einen Klassenkasten.
- Unter jedes Diagramm eine Abbildungsunterschrift, 9 pt, gedämpft:
  „Abb. n: … (eigene Darstellung, Notation nach OMG 2017)".

## FACHLICHE KERNAUSSAGEN, DIE NICHT VERLOREN GEHEN DÜRFEN

1. Die Bestandsregel entscheidet: existiert der Teil ohne das Ganze nicht,
   wird aus der Aggregation eine Komposition.
2. Multiplizitäten lassen sich direkt aus den Formulierungen des Aufgabentexts
   ableiten („genau ein", „mindestens ein", „beliebig viele") und sind damit prüfbar.
3. Antwort auf die Prüfungsfrage: Ein Objekt der Klasse Administrator greift zu
   auf die geerbten Attribute personalnummer, name, e-mail (von Mitarbeiter),
   auf die geerbte Methode buchen() (von Buchhalter) sowie auf die eigenen
   Methoden benutzerVerwalten() und einstellungenVerwalten() — drei Attribute und
   drei Methoden. Voraussetzung ist die Sichtbarkeit public oder protected;
   das Diagramm gibt keine Sichtbarkeiten an, sie werden als public angenommen.
4. Offene Prüfpunkte im Modell 2 (Folie 12): Zahlung müsste 1..* statt 0..*
   sein; Buchungssatz–Buchungsposition braucht 2..* (Soll und Haben);
   Buchungsperiode–Buchungssatz braucht 0..1 zu 0..*; Kunde/Lieferant–Rechnung
   braucht einen {xor}-Constraint; die Attribute rechnungsnummer und sachkonto
   doppeln bestehende Assoziationen.

## NICHT TUN

- Keine Marketing-Sprache, keine Icons, keine Verlaufsflächen, keine Animationen.
- Keine Schlagworttitel, keine Folie über ~40 Wörter.
- Keine Farben außerhalb der Palette, keine zweite Schriftfamilie.
- Keine erfundenen Quellen, Zahlen oder Bewertungskriterien; unbekannte Angaben
  als ⟦offen⟧ stehen lassen.
