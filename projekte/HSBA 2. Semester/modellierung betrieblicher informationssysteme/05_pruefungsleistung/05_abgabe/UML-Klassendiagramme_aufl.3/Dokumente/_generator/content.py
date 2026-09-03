# -*- coding: utf-8 -*-
"""Inhalte der Lehrendenfassung (Auflage 3)."""

STAND = "10.08.2026"

ABLAUF = [
    ("0-2 Min", "Szenario zeigen und einmal laut vorlesen. Keine Rückfrage zur "
                "Modellierung beantworten.", "Leitung"),
    ("2-14 Min", "Gruppen modellieren. Hinweise ausschließlich nach der "
                 "Staffel unten.", "Gruppen"),
    ("Minute 5", "Erster Hinweis, offen gestellt.", "Leitung"),
    ("Minute 10", "Zweiter Hinweis, eingrenzend. Zugleich Priorisierungsregel "
                  "ansagen, falls Kästen fehlen.", "Leitung"),
    ("14-20 Min", "Musterlösung zeigen, Checkpoint-Satz sprechen, zwei typische "
                  "Fehler ansprechen.", "Leitung"),
]

PRIORITAET = [
    "alle Klassen mit Namen",
    "alle Beziehungen mit dem richtigen Typ",
    "Multiplizitäten an beiden Enden",
    "Attribute mit Datentyp",
    "Operationen mit Signatur",
]

GESAMTRASTER = [
    ("Klassen und Abstraktion", "20 %",
     "Sind die fachlichen Begriffe vollständig und richtig spezialisiert?"),
    ("Attribute und Operationen", "20 %",
     "Sind Typen, Sichtbarkeiten und Verantwortungen konsistent?"),
    ("Beziehungstypen", "25 %",
     "Sind Assoziation, Aggregation, Komposition und Vererbung richtig "
     "eingesetzt?"),
    ("Multiplizitäten", "20 %",
     "Entsprechen alle Kardinalitäten den Aussagen des Szenarios?"),
    ("Notation und Nebenbedingungen", "15 %",
     "Ist das Modell lesbar, vollständig und prüfbar?"),
]

LEITPLANKEN = [
    "Der Dozent hält die Theoriepräsentation. Die Aufgabenfolien enthalten "
    "ausschließlich Titel und Szenariotext, keine Notationsregeln und keine "
    "Vorgabeliste.",
    "Jedes Element der Musterlösung ist auf genau einen Satz des Szenarios "
    "zurückführbar. Die Rückführbarkeitstabellen sind die Bewertungsgrundlage.",
    "Die Steigerung über die drei Aufgaben erfolgt über die Zahl der "
    "Sprachkonstrukte, nicht über die Modellgröße.",
    "Wer eine andere Lösung wählt, muss die zusätzliche Annahme offenlegen; "
    "das Modell muss widerspruchsfrei bleiben.",
    "Die leere Raute ist nur dort vorgesehen, wo das Szenario ausdrücklich "
    "eine Teil-Ganzes-Beziehung beschreibt. Lebenszyklusunabhängigkeit allein "
    "genügt nicht.",
]

# ---------------------------------------------------------------- Aufgabe 1
A1 = dict(
    nr=1,
    titel="Bestellsystem eines Onlineshops",
    umfang="5 Klassen, 4 Beziehungen",
    schwerpunkt="Klassenaufbau, Assoziation, Multiplizität, Aggregation gegen "
                "Komposition",
    szenario=(
        "Ein Onlineshop verwaltet seine Kunden, deren Bestellungen und sein "
        "Warenangebot. Zu jedem Kunden gehören eine Kundennummer, ein Name und "
        "eine E-Mail-Adresse, die er selbst ändern kann. Ein neu registrierter "
        "Kunde hat noch keine Bestellung aufgegeben, mit der Zeit können "
        "beliebig viele hinzukommen. Jede Bestellung gehört genau einem Kunden, "
        "trägt ein Bestelldatum und erhält beim Anlegen zunächst den Status "
        "offen; eine offene Bestellung kann storniert werden. Eine gültige "
        "Bestellung enthält mindestens eine Position, und mit der Bestellung "
        "verschwinden auch ihre Positionen, denn jede Position gehört "
        "ausschließlich zu dieser einen Bestellung. Eine Position nennt die "
        "bestellte Menge, mindestens jedoch ein Stück, hält den zum "
        "Bestellzeitpunkt gültigen Preis fest und kann daraus ihren "
        "Positionsbetrag berechnen; ändert der Shop später den Preis, bleiben "
        "bereits aufgegebene Bestellungen davon unberührt. Jede Position "
        "verweist auf genau ein Produkt, dasselbe Produkt kann in beliebig "
        "vielen Positionen vorkommen und bleibt erhalten, wenn eine Bestellung "
        "gelöscht wird. Ein Produkt hat eine Produktnummer, eine Bezeichnung "
        "und einen aktuellen Preis, den der Shop ändern kann. Produkte werden "
        "außerdem in Sortimenten zusammengefasst: Ein Sortiment trägt einen "
        "Namen, kann Produkte aufnehmen und wieder entfernen, dasselbe Produkt "
        "kann in mehreren oder in gar keinem Sortiment geführt werden, und beim "
        "Auflösen eines Sortiments bleiben die enthaltenen Produkte bestehen."),
    beziehungen=[
        ("Kunde – Bestellung", "Assoziation", "1 : 0..*", "gibt auf"),
        ("Bestellung – Bestellposition", "Komposition", "1 : 1..*",
         "besteht aus; Raute an Bestellung"),
        ("Bestellposition – Produkt", "Assoziation", "0..* : 1",
         "bezieht sich auf"),
        ("Sortiment – Produkt", "Aggregation", "0..* : 0..*",
         "führt; leere Raute an Sortiment"),
    ],
    rueck=[
        ("verwaltet seine Kunden, deren Bestellungen und sein Warenangebot",
         "Klassen Kunde, Bestellung, Produkt"),
        ("Kundennummer, ein Name und eine E-Mail-Adresse",
         "-kundennummer: String, -name: String, -eMailAdresse: String"),
        ("die er selbst ändern kann",
         "+eMailAdresseÄndern(neu: String): void"),
        ("hat noch keine Bestellung aufgegeben, … beliebig viele",
         "Assoziationsende Bestellung 0..*"),
        ("gehört genau einem Kunden",
         "Assoziationsende Kunde 1, Assoziationsname „gibt auf“"),
        ("trägt ein Bestelldatum", "-bestelldatum: Date"),
        ("erhält beim Anlegen zunächst den Status offen",
         "-status: String = \"offen\" (Initialwert)"),
        ("eine offene Bestellung kann storniert werden",
         "+stornieren(): void"),
        ("enthält mindestens eine Position", "Ende Bestellposition 1..*"),
        ("mit der Bestellung verschwinden auch ihre Positionen",
         "Komposition, gefüllte Raute an Bestellung"),
        ("gehört ausschließlich zu dieser einen Bestellung",
         "Ende Bestellung 1, Exklusivität der Komposition"),
        ("nennt die bestellte Menge", "-menge: Integer"),
        ("mindestens jedoch ein Stück", "Nebenbedingung {menge >= 1}"),
        ("hält den zum Bestellzeitpunkt gültigen Preis fest",
         "-einzelpreis: Decimal"),
        ("kann daraus ihren Positionsbetrag berechnen",
         "+positionsbetragBerechnen(): Decimal"),
        ("bleiben bereits aufgegebene Bestellungen davon unberührt",
         "Notiz zum Preisstand"),
        ("verweist auf genau ein Produkt", "Ende Produkt 1"),
        ("in beliebig vielen Positionen vorkommen",
         "Ende Bestellposition 0..*"),
        ("bleibt erhalten, wenn eine Bestellung gelöscht wird",
         "Assoziation statt Komposition"),
        ("Produktnummer, Bezeichnung, aktueller Preis",
         "drei Attribute in Produkt"),
        ("den der Shop ändern kann", "+preisÄndern(neu: Decimal): void"),
        ("in Sortimenten zusammengefasst", "Klasse Sortiment, Aggregation"),
        ("trägt einen Namen", "-name: String"),
        ("kann Produkte aufnehmen und wieder entfernen",
         "zwei Operationen in Sortiment"),
        ("in mehreren oder in gar keinem Sortiment", "Enden 0..* / 0..*"),
        ("beim Auflösen bleiben die Produkte bestehen",
         "leere Raute an Sortiment"),
    ],
    hinweis5="Welche Begriffe im Text haben eine eigene Identität — etwas, das "
             "man einzeln wiederfinden und ändern kann?",
    hinweis10="Lest den Satz zum Löschen noch einmal. Was verschwindet mit der "
              "Bestellung, was bleibt bestehen? Die Antwort entscheidet über "
              "die Rautenart.",
    checkpoint="Eine Bestellposition gehört exklusiv zu ihrer Bestellung und "
               "verschwindet mit ihr — gefüllte Raute. Ein Produkt wird "
               "geteilt und lebt weiter — beim Sortiment leere Raute, bei der "
               "Position gar keine.",
    pruef=[
        ("Neukunde", "Kunde ohne jede Bestellung",
         "Durch 0..* am Bestellungsende zulässig"),
        ("Geteiltes Produkt", "Zwei Bestellungen enthalten denselben Artikel",
         "Zwei Positionen zeigen auf dasselbe Produkt; Löschen der ersten "
         "Bestellung entfernt das Produkt nicht"),
        ("Preisänderung", "Produktpreis steigt nach der Bestellung",
         "Positionsbetrag der alten Bestellung bleibt unverändert"),
        ("Sortiment auflösen", "Ein Produkt liegt in zwei Sortimenten",
         "Nach Auflösen eines Sortiments existiert das Produkt weiter"),
    ],
    fehler=[
        "Bestellposition – Produkt als Komposition; das Produkt würde mit der "
        "Bestellung gelöscht.",
        "Sortiment – Produkt mit gefüllter Raute; Produkte wären exklusiv und "
        "nicht mehrfach führbar.",
        "Einzelpreis nur am Produkt geführt; historische Bestellungen ändern "
        "sich rückwirkend.",
        "Bestellposition als Unterklasse von Produkt statt als eigene Klasse.",
        "0..* am Positionsende, obwohl das Szenario von einer gültigen "
        "Bestellung spricht.",
        "Attribute ohne Datentyp oder Operationen ohne Rückgabetyp.",
    ],
    alternativen=[
        "status als Enumeration Bestellstatus statt als String; der Initialwert "
        "muss erhalten bleiben.",
        "Zusätzliche Attribute wie Lieferadresse, solange sie dem Szenario "
        "nicht widersprechen.",
        "Zusätzliche Operationen an der Bestellung, etwa "
        "gesamtbetragBerechnen().",
        "Money statt Decimal, wenn Währung und Rundung genannt werden.",
    ],
    raster=[
        ("Klassen", "4", "Fünf Klassen, keine Attributklasse, keine fehlende."),
        ("Attribute und Operationen", "4",
         "Typisiert, sichtbar, Initialwert am Status."),
        ("Beziehungstypen", "5",
         "Komposition und Aggregation am richtigen Ende, zwei Assoziationen."),
        ("Multiplizitäten", "4", "Alle acht Enden, 1..* an der Position."),
        ("Notation und Nebenbedingungen", "3",
         "Benannte Assoziationen, Mengenregel, Preisstand."),
    ],
)

# ---------------------------------------------------------------- Aufgabe 2
A2 = dict(
    nr=2,
    titel="Hotelverwaltung",
    umfang="8 Klassen, 1 Enumeration, 3 Beziehungen, 4 Generalisierungen",
    schwerpunkt="Abstraktion, zweistufige Spezialisierung, Enumeration, "
                "abgeleitetes Attribut, Klassenattribut, Navigierbarkeit",
    szenario=(
        "Ein Hotel verwaltet die Reservierungen seiner Gäste. Zu jedem Gast "
        "gehören eine Gastnummer, ein Name und eine E-Mail-Adresse; ein Gast "
        "kann eine Reservierung anlegen und hat zu Beginn noch keine. Eine "
        "Reservierung nennt Anreise- und Abreisedatum und befindet sich stets "
        "in genau einem von fünf Zuständen: angelegt, bestätigt, eingecheckt, "
        "abgeschlossen oder storniert; andere Werte sind nicht zulässig, und "
        "sie kann bestätigt und storniert werden. Ihr Gesamtpreis wird nicht "
        "gespeichert, sondern jederzeit aus ihren Positionen berechnet. Auf "
        "alle Reservierungen wird derselbe Mehrwertsteuersatz angewendet; er "
        "gilt für das ganze Haus und wird nur einmal geführt. Jede Reservierung "
        "besteht aus mindestens einer Position, und wird sie gelöscht, "
        "verschwinden ihre Positionen mit ihr. Eine Position nennt eine Anzahl "
        "und den vereinbarten Einzelpreis, aus denen sich ihr Positionspreis "
        "ermitteln lässt. Von einer Position aus muss die gebuchte Leistung "
        "erreichbar sein, die Leistung selbst weiß nicht, in welchen Positionen "
        "sie gebucht wurde. Buchbar sind Zimmer und Zusatzleistungen wie "
        "Frühstück oder Massage. Beide tragen eine Leistungsnummer, eine "
        "Bezeichnung und einen Grundpreis, und von beiden muss man erfragen "
        "können, ob sie in einem Zeitraum verfügbar sind und was sie in diesem "
        "Zeitraum kosten — Zimmer und Zusatzleistungen beantworten das jeweils "
        "auf ihre eigene Weise. Etwas, das nur allgemein eine buchbare Leistung "
        "wäre, lässt sich nicht buchen. Ein Zimmer hat eine Zimmernummer und "
        "eine Etage und kann vom 10. bis 12. Oktober vergeben und vom 15. bis "
        "18. Oktober frei sein. Betrifft eine Position ein Zimmer, bezeichnet "
        "sie immer genau dieses eine; Zusatzleistungen dürfen dagegen mehrfach "
        "auf einer Position stehen. Zimmer werden weiter in Standardzimmer mit "
        "einer Bettenzahl und Suiten mit einer Wohnfläche unterschieden."),
    beziehungen=[
        ("Gast – Reservierung", "Assoziation", "1 : 0..*", "tätigt"),
        ("Reservierung – Buchungsposition", "Komposition", "1 : 1..*",
         "besteht aus; Raute an Reservierung"),
        ("Buchungsposition – BuchbareLeistung", "Assoziation, gerichtet",
         "0..* : 1", "bezieht sich auf; navigierbar zur Leistung"),
        ("Zimmer – BuchbareLeistung", "Generalisierung", "—",
         "Zimmer ist Spezialisierung"),
        ("Zusatzleistung – BuchbareLeistung", "Generalisierung", "—",
         "Zusatzleistung ist Spezialisierung"),
        ("Standardzimmer – Zimmer", "Generalisierung", "—", "zweite Ebene"),
        ("Suite – Zimmer", "Generalisierung", "—", "zweite Ebene"),
    ],
    rueck=[
        ("Reservierungen seiner Gäste", "Klassen Gast, Reservierung"),
        ("Gastnummer, Name, E-Mail-Adresse", "drei Attribute in Gast"),
        ("kann eine Reservierung anlegen",
         "+reservierungAnlegen(von: Date, bis: Date): Reservierung"),
        ("hat zu Beginn noch keine",
         "Ende Reservierung 0..*, Gegenende Gast 1"),
        ("Anreise- und Abreisedatum", "-anreise: Date, -abreise: Date"),
        ("genau einem von fünf Zuständen … andere Werte sind nicht zulässig",
         "Enumeration Reservierungsstatus, Attribut -status"),
        ("kann bestätigt und storniert werden",
         "+bestätigen(): void, +stornieren(): void"),
        ("Gesamtpreis wird nicht gespeichert, sondern berechnet",
         "abgeleitetes Attribut /gesamtpreis: Money"),
        ("derselbe Mehrwertsteuersatz … nur einmal geführt",
         "Klassenattribut mehrwertsteuersatz: Decimal (unterstrichen)"),
        ("besteht aus mindestens einer Position",
         "Ende Buchungsposition 1..*"),
        ("wird sie gelöscht, verschwinden ihre Positionen",
         "Komposition, gefüllte Raute an Reservierung"),
        ("nennt eine Anzahl und den vereinbarten Einzelpreis",
         "zwei Attribute in Buchungsposition"),
        ("aus denen sich ihr Positionspreis ermitteln lässt",
         "+positionspreisErmitteln(): Money"),
        ("von einer Position aus muss die Leistung erreichbar sein",
         "Navigierbarkeit Position → Leistung"),
        ("die Leistung weiß nicht, in welchen Positionen",
         "kein Rückverweis, gerichtete Assoziation"),
        ("Buchbar sind Zimmer und Zusatzleistungen",
         "Klassen Zimmer, Zusatzleistung, zwei Generalisierungen"),
        ("Beide tragen Leistungsnummer, Bezeichnung, Grundpreis",
         "drei Attribute in BuchbareLeistung"),
        ("von beiden muss man erfragen können, ob … und was …",
         "zwei Operationen in BuchbareLeistung"),
        ("beantworten das jeweils auf ihre eigene Weise",
         "beide Operationen abstrakt, in den Unterklassen überschrieben"),
        ("nur allgemein eine buchbare Leistung … lässt sich nicht buchen",
         "BuchbareLeistung {abstract}"),
        ("Zimmernummer und eine Etage", "zwei Attribute in Zimmer"),
        ("vom 10. bis 12. Oktober vergeben, vom 15. bis 18. frei",
         "+istVerfügbar(von: Date, bis: Date): Boolean, Zeitraumnotiz"),
        ("betrifft eine Position ein Zimmer, genau dieses eine",
         "Nebenbedingung {Leistung ist Zimmer => anzahl = 1}"),
        ("Zusatzleistungen mehrfach auf einer Position",
         "anzahl >= 1 für Zusatzleistung"),
        ("Standardzimmer mit Bettenzahl, Suiten mit Wohnfläche",
         "zweite Generalisierungsebene, je ein Attribut"),
    ],
    hinweis5="Welche Angaben gelten für ein Zimmer und für eine Massage "
             "gleichermaßen? Wo gehören die hin?",
    hinweis10="Der Satz mit dem 10. bis 12. Oktober: Lässt sich Verfügbarkeit "
              "mit einem Ja-Nein-Attribut beantworten?",
    checkpoint="BuchbareLeistung ist abstrakt, weil sich eine buchbare "
               "Leistung als solche nicht buchen lässt. Verfügbarkeit und "
               "Preis stehen dort als abstrakte Operationen und werden in "
               "Zimmer und Zusatzleistung unterschiedlich beantwortet. "
               "Verfügbarkeit braucht einen Zeitraum als Parameter, kein "
               "Attribut.",
    pruef=[
        ("Gültige Zimmerbuchung",
         "Standardzimmer vom 10. bis 12.10., eine Position mit anzahl = 1",
         "Reservierung bestätigt, Zimmer im Zeitraum belegt"),
        ("Überschneidung",
         "Zweite Reservierung desselben Zimmers vom 11. bis 13.10.",
         "Wird abgewiesen; ein Anschluss ab 12.10. ist zulässig"),
        ("Suite mit Zusatzleistungen",
         "Suite plus zwei Massagen auf einer Position",
         "anzahl = 2 bei der Zusatzleistung zulässig, bei der Zimmerposition "
         "nicht"),
        ("Preisprüfung", "Eine Position wird nachträglich geändert",
         "/gesamtpreis ändert sich mit, weil er nicht gespeichert ist"),
    ],
    fehler=[
        "belegt: Boolean am Zimmer statt einer Zeitraumprüfung.",
        "BuchbareLeistung nicht abstrakt oder ohne abstrakte Operationen.",
        "Buchungsposition – BuchbareLeistung mit einer Raute versehen; es ist "
        "eine gewöhnliche Assoziation.",
        "Reservierung – Buchungsposition nur als Assoziation; die Position "
        "überlebt dann die Reservierung.",
        "Mehrwertsteuersatz je Reservierung statt als Klassenattribut.",
        "Gesamtpreis als gespeichertes statt als abgeleitetes Attribut.",
        "Statuswerte als freier String, obwohl der Text andere Werte "
        "ausschließt.",
        "Standardzimmer und Suite direkt unter BuchbareLeistung statt unter "
        "Zimmer.",
    ],
    alternativen=[
        "Zeitraum als eigener Werttyp statt als zwei Datumsattribute.",
        "Statt der Enumeration eine Zustandsklasse, wenn Übergänge modelliert "
        "werden.",
        "Weitere Unterklassen von Zusatzleistung; die Generalisierung bleibt "
        "offen.",
        "Navigierbarkeit statt am Pfeil durch eine Notiz ausgedrückt.",
        "Money oder Decimal gleichwertig bei dokumentierter Währung und "
        "Rundung.",
    ],
    raster=[
        ("Klassen und Abstraktion", "4",
         "Acht Klassen, abstrakte Oberklasse, zwei Vererbungsebenen."),
        ("Attribute und Operationen", "4",
         "Abgeleitetes Attribut, Klassenattribut, abstrakte Operationen."),
        ("Beziehungstypen", "5",
         "Komposition, zwei Assoziationen, vier Generalisierungen."),
        ("Multiplizitäten", "4", "Vollständig, 1..* an der Position."),
        ("Notation und Nebenbedingungen", "3",
         "Enumeration, Zeitraumregel, Mengenregel für Zimmer."),
    ],
)

# ---------------------------------------------------------------- Aufgabe 3
A3 = dict(
    nr=3,
    titel="Veranstaltungsmanagement",
    umfang="8 Klassen, 1 Assoziationsklasse, 1 Enumeration, 6 Beziehungen, "
           "2 Generalisierungen",
    schwerpunkt="Integrationsaufgabe: reflexive Assoziation mit Rollennamen, "
                "Assoziationsklasse, Generalisierungsmenge",
    szenario=(
        "Ein Veranstalter organisiert Weiterbildungsveranstaltungen. Er führt "
        "ein Team von Mitarbeitern, die er aufnehmen und wieder abgeben kann; "
        "wechselt ein Mitarbeiter zu einem anderen Veranstalter, bleibt er als "
        "Person im Personalstamm bestehen. Jeder Mitarbeiter berichtet an "
        "höchstens einen anderen Mitarbeiter als Vorgesetzten, ein Vorgesetzter "
        "kann mehrere Mitarbeiter unter sich haben, und die Geschäftsführung "
        "berichtet an niemanden. Mitarbeiter betreuen Veranstaltungen, und eine "
        "Veranstaltung kann von mehreren betreut werden; zu jedem einzelnen "
        "Einsatz werden die Rolle und der Einsatzzeitraum festgehalten, die "
        "weder zur Person noch zur Veranstaltung allein gehören. Jede "
        "Veranstaltung trägt einen Titel, einen Zeitraum und einen "
        "Ticketpreis. Sie ist entweder eine Präsenz- oder eine "
        "Onlineveranstaltung; etwas Drittes gibt es nicht, keine ist beides "
        "zugleich, und eine Veranstaltung ohne eine dieser beiden Formen kann "
        "nicht angelegt werden. Eine Präsenzveranstaltung findet an genau einem "
        "Veranstaltungsort statt. Ein Ort trägt einen Namen, eine Adresse und "
        "eine Kapazität, wird unabhängig verwaltet, kann zu verschiedenen "
        "Zeiten für verschiedene Veranstaltungen genutzt werden und bleibt "
        "bestehen, wenn eine Veranstaltung abgesagt wird. Eine "
        "Onlineveranstaltung hat keinen Ort, sondern eine Plattform und eine "
        "Zugangsadresse. Teilnehmer buchen Veranstaltungen. Jede Buchung gehört "
        "genau einem Teilnehmer, bezieht sich auf genau eine Veranstaltung, "
        "nennt die Zahl der gebuchten Plätze und ist angelegt, bestätigt oder "
        "storniert; andere Zustände gibt es nicht. Der Betrag einer Buchung "
        "wird nicht gespeichert, sondern aus der Platzzahl und dem Ticketpreis "
        "der Veranstaltung errechnet. Für eine Präsenzveranstaltung dürfen "
        "insgesamt nicht mehr Plätze gebucht werden, als der Ort fasst."),
    beziehungen=[
        ("Veranstalter – Mitarbeiter", "Aggregation", "1 : 0..*",
         "beschäftigt; leere Raute an Veranstalter"),
        ("Mitarbeiter – Mitarbeiter", "Assoziation, reflexiv", "0..1 : 0..*",
         "berichtet an; Rollen vorgesetzter und unterstellte"),
        ("Mitarbeiter – Veranstaltung", "Assoziation mit Assoziationsklasse",
         "0..* : 0..*", "betreut; Assoziationsklasse Betreuung"),
        ("Veranstalter – Veranstaltung", "Assoziation", "1 : 0..*",
         "organisiert"),
        ("Präsenzveranstaltung – Veranstaltung", "Generalisierung", "—",
         "{disjoint, complete}"),
        ("Onlineveranstaltung – Veranstaltung", "Generalisierung", "—",
         "{disjoint, complete}"),
        ("Präsenzveranstaltung – Veranstaltungsort", "Assoziation", "0..* : 1",
         "findet statt an; nur an der Unterklasse"),
        ("Teilnehmer – Buchung", "Assoziation", "1 : 0..*", "tätigt"),
        ("Buchung – Veranstaltung", "Assoziation", "0..* : 1",
         "bezieht sich auf"),
    ],
    rueck=[
        ("Veranstalter organisiert Weiterbildungsveranstaltungen",
         "Klassen Veranstalter, Veranstaltung, Assoziation „organisiert“"),
        ("führt ein Team von Mitarbeitern",
         "Aggregation Veranstalter – Mitarbeiter"),
        ("aufnehmen und wieder abgeben", "zwei Operationen in Veranstalter"),
        ("bleibt als Person im Personalstamm bestehen",
         "leere Raute statt gefüllter"),
        ("berichtet an höchstens einen anderen Mitarbeiter als Vorgesetzten",
         "reflexive Assoziation, Ende 0..1, Rollenname vorgesetzter"),
        ("ein Vorgesetzter kann mehrere unter sich haben",
         "Gegenende 0..*, Rollenname unterstellte"),
        ("die Geschäftsführung berichtet an niemanden",
         "0..1 statt 1 — Grenzfall"),
        ("Mitarbeiter betreuen Veranstaltungen, … von mehreren betreut",
         "Assoziation 0..* : 0..*"),
        ("Rolle und Einsatzzeitraum, die weder zur Person noch zur "
         "Veranstaltung allein gehören",
         "Assoziationsklasse Betreuung mit zwei Attributen"),
        ("Titel, Zeitraum und Ticketpreis", "drei Attribute in Veranstaltung"),
        ("entweder Präsenz- oder Onlineveranstaltung",
         "zwei Generalisierungen"),
        ("etwas Drittes gibt es nicht", "{complete}"),
        ("keine ist beides zugleich", "{disjoint}"),
        ("ohne eine dieser beiden Formen nicht anlegbar",
         "Veranstaltung {abstract}"),
        ("findet an genau einem Veranstaltungsort statt",
         "Ende Veranstaltungsort 1, nur an Präsenzveranstaltung"),
        ("Name, Adresse und Kapazität",
         "drei Attribute in Veranstaltungsort"),
        ("unabhängig verwaltet, mehrfach genutzt, bleibt bestehen",
         "Assoziation, Ende Präsenzveranstaltung 0..*"),
        ("Onlineveranstaltung hat keinen Ort",
         "keine Beziehung von Onlineveranstaltung — Grenzfall"),
        ("sondern Plattform und Zugangsadresse",
         "zwei Attribute in Onlineveranstaltung"),
        ("Teilnehmer buchen Veranstaltungen", "Klassen Teilnehmer, Buchung"),
        ("gehört genau einem Teilnehmer",
         "Ende Teilnehmer 1, Gegenende 0..*"),
        ("bezieht sich auf genau eine Veranstaltung",
         "Ende Veranstaltung 1, Gegenende 0..*"),
        ("Zahl der gebuchten Plätze", "-anzahlPlätze: Integer"),
        ("angelegt, bestätigt oder storniert; andere Zustände gibt es nicht",
         "Enumeration Buchungsstatus"),
        ("Betrag wird nicht gespeichert, sondern errechnet",
         "abgeleitetes Attribut /betrag: Money"),
        ("nicht mehr Plätze, als der Ort fasst",
         "Nebenbedingung über Veranstaltungsort.kapazität"),
    ],
    hinweis5="Rolle und Einsatzzeitraum eines Betreuungseinsatzes — gehören "
             "die zum Mitarbeiter oder zur Veranstaltung? Wenn beides nicht "
             "stimmt: wohin dann?",
    hinweis10="Prüft eure Onlineveranstaltung: Kann sie in eurem Modell "
              "versehentlich einen Veranstaltungsort bekommen?",
    checkpoint="Die Ortsbeziehung hängt an der Präsenzveranstaltung, nicht an "
               "der Oberklasse — sonst könnte eine Onlineveranstaltung einen "
               "Ort haben. Rolle und Einsatzzeitraum gehören an die Verbindung "
               "selbst, also an eine Assoziationsklasse.",
    pruef=[
        ("Präsenzfall", "Ort mit Kapazität 40, 30 gebuchte Plätze",
         "Modell gültig, Kapazitätsregel eingehalten"),
        ("Kapazitätsverstoß", "45 gebuchte Plätze bei Kapazität 40",
         "Verletzt die Kapazitätsregel"),
        ("Onlinefall", "Plattform und Zugangsadresse gesetzt, kein Ort",
         "Gültig; ein Ortslink wäre ein Fehler"),
        ("Geschäftsführung", "Mitarbeiter ohne Vorgesetzten",
         "Durch 0..1 am Vorgesetztenende zulässig"),
        ("Doppelbetreuung",
         "Zwei Mitarbeiter betreuen dieselbe Veranstaltung in verschiedenen "
         "Rollen",
         "Zwei Betreuungsobjekte mit unterschiedlicher Rolle"),
    ],
    fehler=[
        "Ortsbeziehung an Veranstaltung statt an Präsenzveranstaltung; eine "
        "Onlineveranstaltung könnte dann einen Ort haben.",
        "Rolle und Einsatzzeitraum als Attribute am Mitarbeiter oder an der "
        "Veranstaltung.",
        "Reflexive Assoziation ohne Rollennamen; das Modell ist dann nicht "
        "lesbar.",
        "1 statt 0..1 am Vorgesetztenende; die Geschäftsführung wäre nicht "
        "modellierbar.",
        "Veranstalter – Mitarbeiter als Komposition; Mitarbeiter würden mit "
        "dem Veranstalter gelöscht.",
        "Generalisierungsmenge ohne {disjoint, complete}, obwohl der Text "
        "beides ausdrücklich sagt.",
        "Betrag als gespeichertes statt als abgeleitetes Attribut.",
    ],
    alternativen=[
        "Statt der Assoziationsklasse eine gewöhnliche Klasse Betreuung mit "
        "zwei Assoziationen, wenn die Multiplizitäten stimmen.",
        "Ticket als eigene Klasse mit Komposition zur Buchung, wenn "
        "Einzeltickets gewünscht sind; anzahlPlätze entfällt dann.",
        "Kapazität zusätzlich an der Präsenzveranstaltung, solange die Regel "
        "den Ort einbezieht.",
        "Zeitraum als zwei DateTime-Attribute statt als Werttyp.",
    ],
    raster=[
        ("Klassen und Generalisierung", "4",
         "Acht Klassen, abstrakte Oberklasse, {disjoint, complete}."),
        ("Attribute und Operationen", "4",
         "Typisiert, abgeleiteter Betrag, Enumeration."),
        ("Beziehungstypen", "5",
         "Aggregation, reflexive Assoziation, Assoziationsklasse und beide "
         "Generalisierungen."),
        ("Multiplizitäten", "4",
         "Vollständig, 0..1 am Vorgesetztenende."),
        ("Notation und Nebenbedingungen", "3",
         "Rollennamen, Ortsregel, Kapazitätsregel."),
    ],
)

AUFGABEN = [A1, A2, A3]

ABNAHME = [
    "Die Aufgabenfolien enthalten ausschließlich Titel und Szenariotext.",
    "Jedes Element der drei Musterlösungen ist auf genau einen Szenariosatz "
    "zurückführbar.",
    "Gleiche Formulierungen führen in allen drei Aufgaben zur gleichen "
    "Modellantwort.",
    "Die gemessene Bearbeitungszeit je Aufgabe liegt bei höchstens "
    "14 Minuten.",
    "Die Diagramme wurden bei 100 Prozent und im Ausdruck auf Lesbarkeit "
    "geprüft.",
    "Hinweisstaffel und Checkpoint-Sätze sind der leitenden Person vertraut.",
]
