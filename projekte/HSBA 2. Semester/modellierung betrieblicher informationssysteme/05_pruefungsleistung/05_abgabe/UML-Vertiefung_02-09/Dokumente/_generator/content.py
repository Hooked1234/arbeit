# -*- coding: utf-8 -*-
"""Inhalte der Vertiefung, Termin 02.09.2026.

Quelle der Wahrheit fuer Texte und Fundliste ist
`03_entwurf/Szenarien_vertiefung.md`. Aenderungen hier vornehmen, nicht in den
erzeugten Dateien.
"""

STAND = "30.08.2026"
TERMIN = "02.09.2026"

# ------------------------------------------------------------------ Ablauf
ABLAUF_1 = [
    ("0-3 Min", "Szenario austeilen und einmal laut vorlesen. Keine Frage zur "
                "Modellierung beantworten.", "Person A"),
    ("3-30 Min", "Gruppen modellieren. Hinweise ausschliesslich nach der "
                 "Staffel unten.", "beide im Raum"),
    ("Minute 10", "Erster Hinweis, offen gestellt.", "beide, gleicher Wortlaut"),
    ("Minute 20", "Zweiter Hinweis, eingrenzend. Zugleich Priorisierungsregel "
                  "ansagen.", "beide, gleicher Wortlaut"),
    ("30-45 Min", "Musterloesung zeigen, an den Pruefinstanzen begruenden, "
                  "zwei typische Fehler ansprechen.", "Person A"),
]

ABLAUF_2 = [
    ("0-5 Min", "KI-Entwurf und Protokollbogen austeilen, Auftrag vorlesen. "
                "Die Musterloesung zu Aufgabe 1 bleibt eingesammelt.",
     "Person B"),
    ("5-28 Min", "Gruppen pruefen den Entwurf gegen den Szenariotext.",
     "beide im Raum"),
    ("Minute 12", "Erster Hinweis, offen gestellt.", "beide, gleicher Wortlaut"),
    ("Minute 20", "Zweiter Hinweis, eingrenzend.", "beide, gleicher Wortlaut"),
    ("28-43 Min", "Fundliste durchgehen, dabei die Musterloesung aus Aufgabe 1 "
                  "danebenlegen.", "Person B"),
    ("43-45 Min", "Schlussfrage gemeinsam beantworten. Zugleich Abschluss: "
                  "welches Konstrukt wo vorkam.", "Person A"),
]

PRIORITAET = [
    "alle Klassen mit Namen",
    "alle Beziehungen mit dem richtigen Typ",
    "Kardinalitaeten an beiden Enden",
    "Attribute",
    "Methoden",
]

LEITPLANKEN = [
    "Der Dozent haelt die Theoriepraesentation. Die Aufgabenfolien enthalten "
    "ausschliesslich Titel und Text, keine Notationsregeln und keine "
    "Vorgabeliste.",
    "Notation strikt im belegten Katalog: keine Sichtbarkeiten, keine "
    "Datentypen, keine Methodensignaturen, keine abstrakten Klassen, keine "
    "Enumerationen, keine Assoziationsklassen. Grundlage sind 7-UML-KD.pptx "
    "und die eigene Vorstellungsrunde vom 12.08.2026.",
    "Vokabular des Dozenten uebernehmen: Kardinalitaet statt Multiplizitaet, "
    "Methode statt Operation.",
    "Jedes Element der Musterloesung ist auf genau einen Satz des Szenarios "
    "zurueckfuehrbar. Die Rueckfuehrbarkeitstabelle ist die "
    "Bewertungsgrundlage.",
    "Die leere Raute nur dort, wo der Text ausdruecklich eine "
    "Teil-Ganzes-Aussage macht. Lebenszyklusunabhaengigkeit allein genuegt "
    "nicht - deshalb ist in Aufgabe 2 die schlichte Assoziation an dieser "
    "Stelle zulaessig.",
    "In Aufgabe 2 ist der Szenariotext der Massstab, nicht das eigene "
    "Diagramm aus Aufgabe 1. Sonst wird aus der Pruefung ein Abgleich.",
    "Wer eine andere Loesung waehlt, muss die zusaetzliche Annahme offenlegen; "
    "das Modell muss widerspruchsfrei bleiben.",
]

# ----------------------------------------------------------------- Aufgabe 1
A1 = dict(
    nr=1,
    titel="Pruefungsverwaltung einer Hochschule",
    art="Modellieren",
    umfang="11 Klassen, 6 Beziehungen, 5 Vererbungen",
    schwerpunkt="Aggregation gegen Komposition, Kardinalitaeten einschliesslich "
                "der Grenzfaelle, zweistufige Vererbung",
    szenario=(
        "Eine Hochschule verwaltet ihre Studiengaenge, Module und Pruefungen in "
        "einem Softwaresystem. Zu einem Studiengang werden Kuerzel, Bezeichnung "
        "und Regelstudienzeit gespeichert; Module koennen aufgenommen und der "
        "Studienplan gedruckt werden. Ein Studiengang fasst mindestens ein Modul "
        "zusammen. Dasselbe Modul kann in mehreren Studiengaengen angeboten "
        "werden und bleibt bestehen, wenn ein Studiengang eingestellt wird.\n\n"
        "Zu einem Modul werden Modulnummer, Titel und Credits gespeichert, "
        "ausserdem kann ein Pruefungstermin angesetzt werden. Zu jedem Modul "
        "gehoert mindestens ein Pruefungstermin, der ohne das Modul nicht "
        "existiert. Ein Modul wird von mindestens einem Dozenten gelehrt, ein "
        "Dozent lehrt beliebig viele Module. Zu einem Dozenten werden "
        "Personalnummer und Name gespeichert, er kann Noten eintragen.\n\n"
        "Ein Pruefungstermin besitzt Pruefungsnummer, Datum und Raum; die "
        "Anmeldung kann geoeffnet und der Termin abgesagt werden. Jeder Termin "
        "wird von hoechstens einem Dozenten beaufsichtigt, ein Dozent "
        "beaufsichtigt beliebig viele Termine. Unterschieden werden Klausuren "
        "mit einer Bearbeitungsdauer, zu denen die Aufsicht eingeteilt werden "
        "kann; muendliche Pruefungen mit Dauer und Beisitzer, zu denen ein "
        "Protokoll angelegt werden kann; und Praesentationen mit einer "
        "Vortragsdauer, zu denen die Technik geprueft werden kann.\n\n"
        "Praesentationen werden weiter unterschieden in Einzelpraesentationen "
        "mit einem Vortragstermin, der verschoben werden kann, und "
        "Gruppenpraesentationen mit einer Mitgliederzahl, fuer die eine Gruppe "
        "eingeteilt werden kann.\n\n"
        "Zu einem Studenten werden Matrikelnummer, Name und E-Mail "
        "gespeichert, er kann sich zu einer Pruefung anmelden und seinen "
        "Notenspiegel abrufen. Jeder Student ist in genau einem Studiengang "
        "eingeschrieben, ein Studiengang fuehrt beliebig viele Studierende.\n\n"
        "Tritt ein Student zu einem Pruefungstermin an, entsteht ein "
        "Pruefungsversuch mit Versuchsnummer, Datum und Note; er kann als "
        "bestanden verbucht werden, und es kann von ihm zurueckgetreten werden. "
        "Ein Pruefungsversuch gehoert zu genau einem Studenten und existiert "
        "ohne ihn nicht; ein Student unternimmt beliebig viele Versuche. Jeder "
        "Versuch bezieht sich auf genau einen Pruefungstermin. Ein Termin wird "
        "von beliebig vielen Versuchen genutzt und bleibt bestehen, wenn ein "
        "Versuch geloescht wird."
    ),
    auftrag=[
        "Erstellt das Klassendiagramm zum Szenario.",
        "Tragt zu jeder Klasse die im Text genannten Attribute und Methoden "
        "ein - nur diese.",
        "Benennt jede Beziehung und tragt an beiden Enden die Kardinalitaet "
        "ein.",
        "Bei Nutzung von diagrams.net sind alle Elemente unter "
        "Shapes - UML zu finden.",
    ],
    hinweis1="Geht das Szenario Satz fuer Satz durch. Jeder Satz, der zwei "
             "Dinge in Beziehung setzt, ist eine Linie im Diagramm.",
    hinweis2="Prueft jede Raute einzeln: Kann das Teil ohne das Ganze "
             "weiterexistieren? Der Text sagt es an drei Stellen ausdruecklich.",
    checkpoint="Ein Pruefungsversuch stirbt mit seinem Studenten, ein "
               "Pruefungstermin stirbt nicht mit seinem Versuch. Genau das "
               "unterscheidet die gefuellte von der leeren Raute - und der "
               "Text sagt beides ausdruecklich.",
    beziehungen=[
        ("Studiengang - Modul", "Aggregation", "0..* / 1..*",
         "Modul ueberlebt den Studiengang"),
        ("Modul - Pruefung", "Komposition", "1 / 1..*",
         "Termin stirbt mit dem Modul"),
        ("Dozent - Modul", "Assoziation, lehrt", "1..* / 0..*",
         "mindestens ein Lehrender je Modul"),
        ("Dozent - Pruefung", "Assoziation, beaufsichtigt", "0..1 / 0..*",
         "Aufsicht darf offen bleiben"),
        ("Student - Studiengang", "Assoziation", "0..* / 1",
         "genau ein Studiengang je Student"),
        ("Student - Pruefungsversuch", "Komposition", "1 / 0..*",
         "Versuch stirbt mit dem Studenten"),
        ("Pruefungsversuch - Pruefung", "Aggregation", "0..* / 1",
         "Termin ueberlebt den Versuch"),
        ("Pruefung - drei Formen", "Vererbung", "-",
         "Klausur, muendliche Pruefung, Praesentation"),
        ("Praesentation - zwei Arten", "Vererbung", "-",
         "Einzel- und Gruppenpraesentation"),
    ],
    pruef=[
        ("Studiengang eingestellt", "Modul ist in keinem anderen Studiengang",
         "Modul bleibt bestehen - leere Raute"),
        ("Modul gestrichen", "Modul hat drei Pruefungstermine",
         "Termine verschwinden mit - gefuellte Raute"),
        ("Neuer Termin angelegt", "noch keine Aufsicht benannt",
         "zulaessig, Ende am Dozenten ist 0..1"),
        ("Student frisch immatrikuliert", "noch kein Versuch",
         "genau ein Studiengang, null Versuche"),
        ("Versuch geloescht", "Termin hat weitere Versuche",
         "Termin bleibt bestehen - keine Komposition"),
        ("Gruppenpraesentation angelegt", "Vortragsdauer und Mitgliederzahl",
         "erbt von Praesentation, nicht von Pruefung"),
    ],
    fehler=[
        "Pruefungsversuch wird als Attribut von Student gefuehrt statt als "
        "eigene Klasse. Der Text nennt eigene Angaben dazu - das ist eine "
        "Klasse, wie Bestellposition am 12.08.",
        "Gefuellte Raute zwischen Studiengang und Modul. Der Text sagt "
        "ausdruecklich, dass das Modul bestehen bleibt.",
        "Kardinalitaet 1 statt 0..1 bei der Aufsicht. Hoechstens einer "
        "schliesst keinen ein.",
        "Einzel- und Gruppenpraesentation haengen direkt unter Pruefung. Die "
        "zweite Vererbungsebene geht dabei verloren.",
        "Kardinalitaeten nur an einem Ende eingetragen.",
        "Erfundene Attribute wie Status oder ID, die der Text nicht nennt.",
    ],
    alternativen=[
        "Statt der leeren Raute zwischen Pruefungsversuch und Pruefung eine "
        "schlichte Assoziation. Der Text schliesst nur die Komposition aus.",
        "Die Klasse Pruefung darf Pruefungstermin heissen; der Text verwendet "
        "beide Woerter. Entscheidend ist, dass es durchgehalten wird.",
        "Andere Anordnung und Reihenfolge der Klassen.",
        "Methodennamen duerfen abweichen, solange die Bedeutung stimmt.",
    ],
    raster=[
        ("Klassen", "4", "alle elf Klassen vorhanden, keine erfundene"),
        ("Attribute und Methoden", "4",
         "aus dem Text abgeleitet, nichts hinzugefuegt"),
        ("Beziehungstypen", "5",
         "Aggregation, Komposition, Assoziation und Vererbung richtig gewaehlt"),
        ("Kardinalitaeten", "4",
         "an beiden Enden, Grenzfaelle 0..1 und 1..* stimmen"),
        ("Zweistufige Vererbung", "3",
         "Praesentationsarten haengen unter Praesentation"),
    ],
    rueck=[
        ("verwaltet Studiengaenge, Module und Pruefungen",
         "Klassen Studiengang, Modul, Pruefung"),
        ("Kuerzel, Bezeichnung und Regelstudienzeit",
         "drei Attribute in Studiengang"),
        ("Module aufgenommen, Studienplan gedruckt",
         "modulAufnehmen(), studienplanDrucken()"),
        ("fasst mindestens ein Modul zusammen",
         "Aggregation, Ende Modul 1..*"),
        ("kann in mehreren Studiengaengen angeboten werden",
         "Ende Studiengang 0..*"),
        ("bleibt bestehen, wenn ein Studiengang eingestellt wird",
         "leere Raute statt gefuellter"),
        ("Modulnummer, Titel und Credits", "drei Attribute in Modul"),
        ("kann ein Pruefungstermin angesetzt werden", "pruefungAnsetzen()"),
        ("Zu jedem Modul gehoert mindestens ein Pruefungstermin",
         "Ende Pruefung 1..*"),
        ("der ohne das Modul nicht existiert",
         "Komposition, gefuellte Raute an Modul, Ende Modul 1"),
        ("von mindestens einem Dozenten gelehrt",
         "Assoziation lehrt, Ende Dozent 1..*"),
        ("ein Dozent lehrt beliebig viele Module", "Ende Modul 0..*"),
        ("Personalnummer und Name", "zwei Attribute in Dozent"),
        ("kann Noten eintragen", "noteEintragen()"),
        ("Pruefungsnummer, Datum und Raum", "drei Attribute in Pruefung"),
        ("Anmeldung geoeffnet, Termin abgesagt",
         "anmeldungOeffnen(), pruefungAbsagen()"),
        ("von hoechstens einem Dozenten beaufsichtigt",
         "zweite Assoziation beaufsichtigt, Ende Dozent 0..1"),
        ("beaufsichtigt beliebig viele Termine", "Ende Pruefung 0..*"),
        ("Unterschieden werden Klausuren, muendliche Pruefungen, "
         "Praesentationen", "drei Vererbungen"),
        ("Bearbeitungsdauer; Aufsicht einteilen",
         "Klausur mit Attribut und Methode"),
        ("Dauer und Beisitzer; Protokoll anlegen",
         "MuendlichePruefung mit zwei Attributen und Methode"),
        ("Vortragsdauer; Technik pruefen",
         "Praesentation mit Attribut und Methode"),
        ("Praesentationen werden weiter unterschieden",
         "zweite Vererbungsebene unter Praesentation"),
        ("Einzelpraesentationen mit Vortragstermin, verschieben",
         "Einzelpraesentation, vortragstermin, terminVerschieben()"),
        ("Gruppenpraesentationen mit Mitgliederzahl, Gruppe einteilen",
         "Gruppenpraesentation, mitgliederzahl, gruppeEinteilen()"),
        ("Matrikelnummer, Name und E-Mail", "drei Attribute in Student"),
        ("kann sich anmelden, Notenspiegel abrufen",
         "zuPruefungAnmelden(), notenspiegelAbrufen()"),
        ("in genau einem Studiengang eingeschrieben", "Ende Studiengang 1"),
        ("fuehrt beliebig viele Studierende", "Ende Student 0..*"),
        ("Versuchsnummer, Datum und Note",
         "drei Attribute in Pruefungsversuch"),
        ("als bestanden verbucht, zurueckgetreten",
         "alsBestandenVerbuchen(), versuchZuruecktreten()"),
        ("gehoert zu genau einem Studenten und existiert ohne ihn nicht",
         "Komposition Student - Pruefungsversuch, Ende Student 1"),
        ("unternimmt beliebig viele Versuche", "Ende Pruefungsversuch 0..*"),
        ("bezieht sich auf genau einen Pruefungstermin", "Ende Pruefung 1"),
        ("von beliebig vielen Versuchen genutzt",
         "Ende Pruefungsversuch 0..*"),
        ("bleibt bestehen, wenn ein Versuch geloescht wird",
         "Aggregation statt Komposition"),
    ],
)

# ----------------------------------------------------------------- Aufgabe 2
A2 = dict(
    nr=2,
    titel="Was ein KI-Werkzeug daraus gemacht hat",
    art="Pruefen",
    umfang="acht Fehler, zwei zulaessige Abweichungen",
    schwerpunkt="Ein fremdes Modell gegen die Anforderung pruefen und zwischen "
                "falsch und bloss anders unterscheiden",
    szenario=(
        "Derselbe Szenariotext wurde einem KI-Werkzeug uebergeben, mit der "
        "Bitte, daraus ein UML-Klassendiagramm zu erzeugen. Das Ergebnis liegt "
        "euch vor.\n\n"
        "Prueft es gegen den Szenariotext, nicht gegen euer eigenes Diagramm. "
        "Haltet jede Abweichung fest und entscheidet fuer jede einzeln: Ist das "
        "ein Fehler, weil der Text etwas anderes verlangt? Oder ist es eine "
        "zulaessige Abweichung, die der Text ebenfalls hergibt?\n\n"
        "Tragt zu jeder Abweichung ein, wo im Diagramm sie steht, welche "
        "Aussage des Textes betroffen ist, wie ihr sie einstuft und wie die "
        "Korrektur aussieht.\n\n"
        "Zum Schluss beantwortet ihr gemeinsam eine Frage: Welchen der "
        "gefundenen Fehler haette das Werkzeug nicht machen koennen, wenn der "
        "Szenariotext an einer Stelle genauer gewesen waere?"
    ),
    auftrag=[
        "Nicht alle Abweichungen sind Fehler.",
        "Jeder Fund braucht die betroffene Aussage aus dem Text.",
        "Der Protokollbogen hat zehn Zeilen; ihr braucht nicht alle.",
    ],
    hinweis1="Geht die Beziehungen der Reihe nach durch, nicht die Kaesten. "
             "Die meisten Abweichungen sitzen an den Linien.",
    hinweis2="Zwei der Abweichungen sind keine Fehler. Wer nur Fehler findet, "
             "hat etwas uebersehen.",
    checkpoint="Ein Modell ist hoechstens so eindeutig wie seine Anforderung - "
               "aber nur zwei dieser zehn Befunde gehen wirklich auf den Text "
               "zurueck. Die anderen sechs Fehler standen eindeutig da und "
               "wurden ueberlesen.",
    fundliste=[
        ("1", "Studiengang - Modul, gefuellte Raute",
         "bleibt bestehen, wenn ein Studiengang eingestellt wird",
         "Fehler", "leere Raute"),
        ("2", "Modul - Pruefungstermin, schlichte Linie",
         "der ohne das Modul nicht existiert",
         "Fehler", "gefuellte Raute an Modul"),
        ("3", "beaufsichtigt, Ende am Dozenten 1",
         "von hoechstens einem Dozenten beaufsichtigt",
         "Fehler", "0..1"),
        ("4", "ist eingeschrieben in, beide Enden",
         "in genau einem Studiengang eingeschrieben, fuehrt beliebig viele",
         "Fehler", "Studiengang 1, Student 0..*"),
        ("5", "keine Verbindung Dozent - Modul",
         "von mindestens einem Dozenten gelehrt",
         "Fehler", "Assoziation lehrt, 1..* / 0..*"),
        ("6", "Einzel- und Gruppenpraesentation unter Pruefungstermin",
         "Praesentationen werden weiter unterschieden",
         "Fehler", "Oberklasse Praesentation"),
        ("7", "Modul.beschreibung, Student.status, Pruefungstermin.status",
         "steht nirgends im Text", "Fehler", "streichen"),
        ("8", "Pruefungsversuch.id",
         "mit Versuchsnummer, Datum und Note",
         "Fehler", "versuchsnummer"),
        ("9", "Pruefungsversuch - Pruefungstermin, schlichte Linie",
         "bleibt bestehen, wenn ein Versuch geloescht wird",
         "zulaessig", "keine - der Satz schliesst nur die Komposition aus"),
        ("10", "Klasse heisst Pruefungstermin statt Pruefung",
         "Text verwendet beide Woerter",
         "zulaessig", "keine - Benennung ist keine Korrektheitsfrage"),
    ],
    schlussantwort=(
        "Nur zwei Befunde haengen wirklich am Text. Die erfundenen Attribute "
        "(Nr. 7) entstehen, weil der Text nirgends sagt, dass die genannten "
        "Angaben abschliessend sind. Und die Rautenfrage bei Pruefungsversuch "
        "(Nr. 9) ist offen, weil der Text nur sagt, was nicht gilt, aber nicht, "
        "ob eine Teil-Ganzes-Beziehung gemeint ist. Alle uebrigen sechs Fehler "
        "stehen eindeutig im Text - das Werkzeug hat sie ueberlesen."
    ),
    fehler=[
        "Das eigene Diagramm aus Aufgabe 1 wird zum Massstab gemacht statt der "
        "Szenariotext. Dann werden eigene Fehler mitgeschleppt.",
        "Nur Kaesten geprueft, nicht Linien. Sechs der acht Fehler sitzen an "
        "den Beziehungen.",
        "Alle zehn Abweichungen werden als Fehler eingestuft. Die "
        "Unterscheidung falsch gegen bloss anders ist der Kern der Aufgabe.",
        "Layout- und Anordnungsunterschiede werden als Befunde gezaehlt.",
        "Korrektur genannt, aber ohne die betroffene Aussage aus dem Text.",
    ],
    alternativen=[
        "Wer Nr. 9 als Fehler einstuft und die leere Raute fordert, bekommt "
        "Teilpunkte, wenn die Begruendung am Text haengt.",
        "Weitere echte Funde ausserhalb der Liste werden anerkannt, sofern sie "
        "am Text belegt sind.",
        "Die Reihenfolge im Protokollbogen ist frei.",
    ],
    raster=[
        ("Gefundene Fehler", "8",
         "sechs der acht Fehler gefunden und beschrieben"),
        ("Richtige Einstufung", "4",
         "mindestens eine zulaessige Abweichung als solche erkannt"),
        ("Begruendung am Text", "4",
         "jeder Fund nennt die betroffene Aussage des Szenarios"),
        ("Korrektur", "2", "der Korrekturvorschlag ist selbst korrekt"),
        ("Schlussfrage", "2",
         "erkennt, dass nur zwei Befunde textbedingt sind"),
    ],
)

AUFGABEN = [A1, A2]

# ---------------------------------------------------------------- Betreuung
ROLLEN = [
    ("Moderation", "Aufgabe 1", "Aufgabe 2"),
    ("Zeitwache", "beide Bloecke", "-"),
    ("Aufloesung", "Aufgabe 1, Schlusswort Aufgabe 2", "Aufgabe 2"),
    ("Raumhaelfte waehrend der Bearbeitung", "links", "rechts"),
    ("Ausgabe der Blaetter", "Aufgabe 1", "KI-Entwurf und Protokollbogen"),
]

FAQ = [
    ("Sollen wir Datentypen angeben?",
     "Nein. Nur das, was in der Vorlesung gezeigt wurde."),
    ("Muessen wir Sichtbarkeiten eintragen?",
     "Nein. Weder plus noch minus."),
    ("Ist der Pruefungsversuch eine eigene Klasse?",
     "Der Text nennt eigene Angaben dazu. Mehr sage ich nicht."),
    ("Welche Raute gehoert hierhin?",
     "Lest den Satz noch einmal: Was passiert mit dem Teil, wenn das Ganze "
     "verschwindet?"),
    ("Muessen wir alle Methoden aufnehmen?",
     "Alle, die der Text nennt. Keine weiteren."),
    ("Duerfen wir Klassen anders benennen?",
     "Ja, solange ihr es durchhaltet."),
    ("Duerfen wir diagrams.net benutzen?",
     "Ja. Alle Elemente stehen unter Shapes - UML."),
    ("Aufgabe 2: Ist das wirklich falsch?",
     "Prueft gegen den Text, nicht gegen euer Diagramm."),
    ("Aufgabe 2: Wie viele Fehler gibt es?",
     "Mehr als fuenf. Genauer sage ich es nicht."),
    ("Aufgabe 2: Zaehlt der Klassenname als Fehler?",
     "Entscheidet selbst und begruendet es. Genau darum geht die Aufgabe."),
]

ABNAHME = [
    "Jedes Element der Musterloesung ist auf genau einen Satz des Szenarios "
    "zurueckfuehrbar.",
    "Kein Aufgabentext enthaelt UML-Fachbegriffe.",
    "Kein Konstrukt ausserhalb des belegten Katalogs.",
    "Jedes der neun Konstrukte kommt in Aufgabe 1 vor und wird in der "
    "Aufloesung von Aufgabe 2 erneut aufgegriffen.",
    "Gemessene Bearbeitungszeit: Aufgabe 1 hoechstens 27, Aufgabe 2 "
    "hoechstens 23 Minuten.",
    "Der KI-Entwurf enthaelt genau die zehn Befunde der Fundliste.",
    "Aufgabenfolien enthalten ausschliesslich Titel und Text.",
    "Hinweisstaffel und FAQ sind zwischen beiden Betreuenden abgestimmt.",
    "Ausdrucke, PDF-Sicherung und USB-Stick liegen bereit.",
]
