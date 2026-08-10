# Szenariotexte Auflage 3 — Entwurf

Stand: 10.08.2026 · Grundlage:
[Umsetzungsplan](2026-08-10_Umsetzungsplan_aufl.3.md) Abschnitte 3 und 4

Die Texte folgen dem Format aus `Aufgaben_EPK_Keine_Lösung.pptx`: Titel plus
durchgehender Fließtext, keine Arbeitsaufträge, keine Vorgabelisten, keine
UML-Begriffe. Umfang je Aufgabe 210–250 Wörter, das Reklamationsbeispiel liegt
bei rund 175.

Je Aufgabe folgt die Rückführbarkeitsmatrix: linke Spalte der auslösende Satz,
rechte Spalte das Modellelement. Kein Satz ohne Modellwirkung, kein
Modellelement ohne Satz.

---

## Aufgabe 1 - Bestellsystem eines Onlineshops

> Ein Onlineshop verwaltet seine Kunden, deren Bestellungen und sein
> Warenangebot. Zu jedem Kunden gehören eine Kundennummer, ein Name und eine
> E-Mail-Adresse, die er selbst ändern kann. Ein neu registrierter Kunde hat
> noch keine Bestellung aufgegeben, mit der Zeit können beliebig viele
> hinzukommen. Jede Bestellung gehört genau einem Kunden, trägt ein
> Bestelldatum und erhält beim Anlegen zunächst den Status offen; eine offene
> Bestellung kann storniert werden. Eine gültige
> Bestellung enthält mindestens eine Position, und mit der Bestellung
> verschwinden auch ihre Positionen, denn jede Position gehört ausschließlich zu
> dieser einen Bestellung. Eine Position nennt die bestellte Menge, mindestens
> jedoch ein Stück, hält den zum Bestellzeitpunkt gültigen Preis fest und kann
> daraus ihren Positionsbetrag berechnen; ändert der Shop später den Preis,
> bleiben bereits aufgegebene Bestellungen davon unberührt. Jede Position
> verweist auf genau ein Produkt, dasselbe Produkt kann in beliebig vielen
> Positionen vorkommen und bleibt erhalten, wenn eine Bestellung gelöscht wird.
> Ein Produkt hat eine Produktnummer, eine Bezeichnung und einen aktuellen
> Preis, den der Shop ändern kann. Produkte werden außerdem in Sortimenten
> zusammengefasst: Ein Sortiment trägt einen Namen, kann Produkte aufnehmen und
> wieder entfernen, dasselbe Produkt kann in mehreren oder in gar keinem
> Sortiment geführt werden, und beim Auflösen eines Sortiments bleiben die
> enthaltenen Produkte bestehen.

**Ergebnismodell:** 5 Klassen, 4 Beziehungen

### Rückführbarkeit Aufgabe 1

| Satz | Modellelement |
|---|---|
| verwaltet seine Kunden, deren Bestellungen und sein Warenangebot | Klassen `Kunde`, `Bestellung`, `Produkt` |
| Kundennummer, ein Name und eine E-Mail-Adresse | `-kundennummer: String`, `-name: String`, `-eMailAdresse: String` |
| die er selbst ändern kann | `+eMailAdresseÄndern(neu: String): void` |
| hat noch keine Bestellung aufgegeben, … beliebig viele | Assoziationsende `Bestellung 0..*` |
| gehört genau einem Kunden | Assoziationsende `Kunde 1`, Assoziationsname „gibt auf" |
| trägt ein Bestelldatum | `-bestelldatum: Date` |
| eine offene Bestellung kann storniert werden | `+stornieren(): void` |
| erhält beim Anlegen zunächst den Status offen | `-status: String = "offen"` (Initialwert) |
| enthält mindestens eine Position | Ende `Bestellposition 1..*` |
| mit der Bestellung verschwinden auch ihre Positionen | Komposition, Raute an `Bestellung` |
| gehört ausschließlich zu dieser einen Bestellung | Ende `Bestellung 1`, Exklusivität der Komposition |
| nennt die bestellte Menge | `-menge: Integer` |
| mindestens jedoch ein Stück | Nebenbedingung `{menge >= 1}` |
| hält den zum Bestellzeitpunkt gültigen Preis fest | `-einzelpreis: Decimal` |
| kann daraus ihren Positionsbetrag berechnen | `+positionsbetragBerechnen(): Decimal` |
| bleiben bereits aufgegebene Bestellungen davon unberührt | Notiz zum Preisstand |
| verweist auf genau ein Produkt | Ende `Produkt 1` |
| in beliebig vielen Positionen vorkommen | Ende `Bestellposition 0..*` |
| bleibt erhalten, wenn eine Bestellung gelöscht wird | Assoziation statt Komposition |
| Produktnummer, Bezeichnung, aktueller Preis | drei Attribute in `Produkt` |
| den der Shop ändern kann | `+preisÄndern(neu: Decimal): void` |
| in Sortimenten zusammengefasst | Klasse `Sortiment`, Aggregation |
| trägt einen Namen | `-name: String` |
| kann Produkte aufnehmen und wieder entfernen | zwei Operationen in `Sortiment` |
| in mehreren oder in gar keinem Sortiment | Enden `0..*` / `0..*` |
| beim Auflösen bleiben die Produkte bestehen | leere Raute an `Sortiment` |

---

## Aufgabe 2 - Hotelverwaltung

> Ein Hotel verwaltet die Reservierungen seiner Gäste. Zu jedem Gast gehören
> eine Gastnummer, ein Name und eine E-Mail-Adresse; ein Gast kann eine
> Reservierung anlegen und hat zu Beginn noch keine. Eine Reservierung nennt
> Anreise- und Abreisedatum und befindet sich stets in genau einem von fünf
> Zuständen: angelegt, bestätigt, eingecheckt, abgeschlossen oder storniert;
> andere Werte sind nicht zulässig, und sie kann bestätigt und storniert
> werden. Ihr Gesamtpreis wird nicht gespeichert,
> sondern jederzeit aus ihren Positionen berechnet. Auf alle Reservierungen wird
> derselbe Mehrwertsteuersatz angewendet; er gilt für das ganze Haus und wird
> nur einmal geführt. Jede Reservierung besteht aus mindestens einer Position,
> und wird sie gelöscht, verschwinden ihre Positionen mit ihr. Eine Position
> nennt eine Anzahl und den vereinbarten Einzelpreis, aus denen sich ihr
> Positionspreis ermitteln lässt. Von einer Position aus
> muss die gebuchte Leistung erreichbar sein, die Leistung selbst weiß nicht, in
> welchen Positionen sie gebucht wurde. Buchbar sind Zimmer und Zusatzleistungen
> wie Frühstück oder Massage. Beide tragen eine Leistungsnummer, eine
> Bezeichnung und einen Grundpreis, und von beiden muss man erfragen können, ob
> sie in einem Zeitraum verfügbar sind und was sie in diesem Zeitraum kosten —
> Zimmer und Zusatzleistungen beantworten das jeweils auf ihre eigene Weise.
> Etwas, das nur allgemein eine buchbare Leistung wäre, lässt sich nicht buchen.
> Ein Zimmer hat eine Zimmernummer und eine Etage und kann vom 10. bis 12.
> Oktober vergeben und vom 15. bis 18. Oktober frei sein. Betrifft eine Position
> ein Zimmer, bezeichnet sie immer genau dieses eine; Zusatzleistungen dürfen
> dagegen mehrfach auf einer Position stehen. Zimmer werden weiter in
> Standardzimmer mit einer Bettenzahl und Suiten mit einer Wohnfläche
> unterschieden.

**Ergebnismodell:** 8 Klassen (zwei davon mit je einem Attribut), 3 Beziehungen,
4 Generalisierungen, 1 Enumeration

### Rückführbarkeit Aufgabe 2

| Satz | Modellelement |
|---|---|
| Reservierungen seiner Gäste | Klassen `Gast`, `Reservierung` |
| Gastnummer, Name, E-Mail-Adresse | drei Attribute in `Gast` |
| kann eine Reservierung anlegen | `+reservierungAnlegen(von: Date, bis: Date): Reservierung` |
| hat zu Beginn noch keine | Ende `Reservierung 0..*`, Gegenende `Gast 1` |
| Anreise- und Abreisedatum | `-anreise: Date`, `-abreise: Date` |
| genau einem von fünf Zuständen … andere Werte sind nicht zulässig | Enumeration `Reservierungsstatus`, Attribut `-status` |
| kann bestätigt und storniert werden | `+bestätigen(): void`, `+stornieren(): void` |
| Gesamtpreis wird nicht gespeichert, sondern berechnet | abgeleitetes Attribut `/gesamtpreis: Money` |
| derselbe Mehrwertsteuersatz … nur einmal geführt | Klassenattribut `mehrwertsteuersatz: Decimal` (unterstrichen) |
| besteht aus mindestens einer Position | Ende `Buchungsposition 1..*` |
| wird sie gelöscht, verschwinden ihre Positionen | Komposition, Raute an `Reservierung` |
| nennt eine Anzahl und den vereinbarten Einzelpreis | zwei Attribute in `Buchungsposition` |
| aus denen sich ihr Positionspreis ermitteln lässt | `+positionspreisErmitteln(): Money` |
| von einer Position aus muss die Leistung erreichbar sein | Navigierbarkeit Position → Leistung |
| die Leistung weiß nicht, in welchen Positionen | kein Rückverweis, Assoziation gerichtet |
| Buchbar sind Zimmer und Zusatzleistungen | Klassen `Zimmer`, `Zusatzleistung`, zwei Generalisierungen |
| Beide tragen Leistungsnummer, Bezeichnung, Grundpreis | drei Attribute in `BuchbareLeistung` |
| von beiden muss man erfragen können, ob … und was … | zwei Operationen in `BuchbareLeistung` |
| beantworten das jeweils auf ihre eigene Weise | beide Operationen abstrakt, in Unterklassen überschrieben |
| nur allgemein eine buchbare Leistung … lässt sich nicht buchen | `BuchbareLeistung {abstract}` |
| Zimmernummer und eine Etage | zwei Attribute in `Zimmer` |
| vom 10. bis 12. Oktober vergeben, vom 15. bis 18. frei | `+istVerfügbar(von: Date, bis: Date): Boolean`, Notiz zur Zeitraumprüfung |
| betrifft eine Position ein Zimmer, genau dieses eine | Nebenbedingung `{Leistung ist Zimmer ⇒ anzahl = 1}` |
| Zusatzleistungen mehrfach auf einer Position | `anzahl >= 1` für `Zusatzleistung` |
| Standardzimmer mit Bettenzahl, Suiten mit Wohnfläche | zweite Generalisierungsebene, je ein Attribut |

---

## Aufgabe 3 - Veranstaltungsmanagement

> Ein Veranstalter organisiert Weiterbildungsveranstaltungen. Er führt ein Team
> von Mitarbeitern, die er aufnehmen und wieder abgeben kann; wechselt ein
> Mitarbeiter zu einem anderen Veranstalter, bleibt er als Person im
> Personalstamm bestehen. Jeder Mitarbeiter berichtet an höchstens einen anderen
> Mitarbeiter als Vorgesetzten, ein Vorgesetzter kann mehrere Mitarbeiter unter
> sich haben, und die Geschäftsführung berichtet an niemanden. Mitarbeiter
> betreuen Veranstaltungen, und eine Veranstaltung kann von mehreren betreut
> werden; zu jedem einzelnen Einsatz werden die Rolle und der Einsatzzeitraum
> festgehalten, die weder zur Person noch zur Veranstaltung allein gehören. Jede
> Veranstaltung trägt einen Titel, einen Zeitraum und einen Ticketpreis. Sie ist
> entweder eine Präsenz- oder eine Onlineveranstaltung; etwas Drittes gibt es
> nicht, keine ist beides zugleich, und eine Veranstaltung ohne eine dieser
> beiden Formen kann nicht angelegt werden. Eine Präsenzveranstaltung findet an
> genau einem Veranstaltungsort statt. Ein Ort trägt einen Namen, eine Adresse
> und eine Kapazität, wird unabhängig verwaltet, kann zu verschiedenen Zeiten
> für verschiedene Veranstaltungen genutzt werden und bleibt bestehen, wenn eine
> Veranstaltung abgesagt wird. Eine Onlineveranstaltung hat keinen Ort, sondern
> eine Plattform und eine Zugangsadresse. Teilnehmer buchen Veranstaltungen.
> Jede Buchung gehört genau einem Teilnehmer, bezieht sich auf genau eine
> Veranstaltung, nennt die Zahl der gebuchten Plätze und ist angelegt, bestätigt
> oder storniert; andere Zustände gibt es nicht. Der Betrag einer Buchung wird
> nicht gespeichert, sondern aus der Platzzahl und dem Ticketpreis der
> Veranstaltung errechnet. Für eine Präsenzveranstaltung dürfen insgesamt nicht
> mehr Plätze gebucht werden, als der Ort fasst.

**Ergebnismodell:** 8 Klassen (zwei davon mit je zwei Attributen),
1 Assoziationsklasse, 6 Beziehungen, 2 Generalisierungen, 1 Enumeration

### Rückführbarkeit Aufgabe 3

| Satz | Modellelement |
|---|---|
| Veranstalter organisiert Weiterbildungsveranstaltungen | Klassen `Veranstalter`, `Veranstaltung`, Assoziation „organisiert" |
| führt ein Team von Mitarbeitern | Aggregation `Veranstalter` ◇— `Mitarbeiter` |
| aufnehmen und wieder abgeben | zwei Operationen in `Veranstalter` |
| bleibt als Person im Personalstamm bestehen | leere Raute statt gefüllter |
| berichtet an höchstens einen anderen Mitarbeiter als Vorgesetzten | reflexive Assoziation, Ende `0..1`, Rollenname `vorgesetzter` |
| ein Vorgesetzter kann mehrere unter sich haben | Gegenende `0..*`, Rollenname `unterstellte` |
| die Geschäftsführung berichtet an niemanden | `0..1` statt `1` — Grenzfall |
| Mitarbeiter betreuen Veranstaltungen, … von mehreren betreut | Assoziation `0..*` : `0..*` |
| zu jedem Einsatz Rolle und Einsatzzeitraum, die weder zur Person noch zur Veranstaltung allein gehören | Assoziationsklasse `Betreuung` mit zwei Attributen |
| Titel, Zeitraum und Ticketpreis | drei Attribute in `Veranstaltung` |
| entweder Präsenz- oder Onlineveranstaltung | zwei Generalisierungen |
| etwas Drittes gibt es nicht | `{complete}` |
| keine ist beides zugleich | `{disjoint}` |
| ohne eine dieser beiden Formen nicht anlegbar | `Veranstaltung {abstract}` |
| findet an genau einem Veranstaltungsort statt | Ende `Veranstaltungsort 1`, nur an `Präsenzveranstaltung` |
| Name, Adresse und Kapazität | drei Attribute in `Veranstaltungsort` |
| unabhängig verwaltet, mehrfach genutzt, bleibt bestehen | Assoziation, Ende `Präsenzveranstaltung 0..*` |
| Onlineveranstaltung hat keinen Ort | keine Beziehung von `Onlineveranstaltung` — Grenzfall |
| sondern Plattform und Zugangsadresse | zwei Attribute in `Onlineveranstaltung` |
| Teilnehmer buchen Veranstaltungen | Klassen `Teilnehmer`, `Buchung` |
| gehört genau einem Teilnehmer | Ende `Teilnehmer 1`, Gegenende `0..*` |
| bezieht sich auf genau eine Veranstaltung | Ende `Veranstaltung 1`, Gegenende `0..*` |
| Zahl der gebuchten Plätze | `-anzahlPlätze: Integer` |
| angelegt, bestätigt oder storniert; andere Zustände gibt es nicht | Enumeration `Buchungsstatus` |
| Betrag wird nicht gespeichert, sondern errechnet | abgeleitetes Attribut `/betrag: Money` |
| nicht mehr Plätze, als der Ort fasst | Nebenbedingung über `Veranstaltungsort.kapazität` |

---

## Abweichungen vom Umsetzungsplan

Drei Anpassungen gegenüber Abschnitt 2 und 3 des Plans, jeweils beim Schreiben
entschieden:

1. **Rollennamen (Konstrukt 9) nur in Aufgabe 3.** In Aufgabe 1 gab es keinen
   Auslöser, der ohne konstruierten Zusatzsatz auskommt. Die reflexive
   Assoziation in Aufgabe 3 erzwingt Rollennamen dagegen zwingend — ohne sie
   ist das Modell nicht lesbar. Das ist die didaktisch bessere Stelle.
2. **`Ticket` entfällt in Aufgabe 3**, stattdessen `anzahlPlätze` an der
   Buchung. Die Komposition ist über Aufgabe 1 und 2 bereits zweifach abgedeckt,
   und das Modell fällt von 9 auf 8 Klassen. Der abgeleitete Betrag bleibt
   erhalten, er rechnet jetzt Platzzahl mal Ticketpreis.
3. **Aggregation zusätzlich in Aufgabe 3** (Veranstalter–Mitarbeiter), damit der
   Unterschied zur Komposition ein zweites Mal in anderem Kontext auftritt.

## Offene Prüfpunkte

- **Zeit.** Aufgabe 1 liegt geschätzt bei 12 Minuten, Aufgabe 2 und 3 bei je
  etwa 15. Das ist über dem Zielwert von 14 Minuten Bearbeitungszeit. Der
  Zeittest aus Schritt 10 entscheidet; erste Kürzungskandidaten sind
  `Veranstaltungsort` in Aufgabe 3 und die zweite Generalisierungsebene
  (`Standardzimmer`, `Suite`) in Aufgabe 2.
- **Konstrukt 5 Initialwert** hängt allein an einem Satz in Aufgabe 1
  („erhält beim Anlegen zunächst den Status offen"). Falls der Foliensatz des
  Dozenten Initialwerte nicht behandelt, ersatzlos streichbar.
- **Konstrukt 11 Navigierbarkeit** hängt allein an zwei Sätzen in Aufgabe 2.
  Gleiche Einschränkung.
- Beide Konstrukte sind vor dem Diagrammbau gegen den Foliensatz zu prüfen.
