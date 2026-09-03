# Umsetzungsplan Auflage 3 — UML-Klassendiagramme

Stand: 10.08.2026 · Durchführung: 12.08.2026 · Ziel: Format des Dozenten treffen,
alle Sprachkonstrukte abdecken, 3 × 20 Minuten einhalten.

## 1. Formatentscheidung

Referenz ist `02_materialien/praesentationen/Aufgaben_EPK_Keine_Lösung.pptx`.
Format des Dozenten je Aufgabe:

- eine Folie
- Titel `Aufgabe N - <Domäne>`
- ein durchgehender Fließtext: kurze Szene, dann genauere Beschreibung
- keine Arbeitsauftragsliste, keine Pflichtklassen, keine Notationsregeln,
  keine Selbstprüffragen, kein Bewertungsraster

Konsequenz: Alles, was modelliert werden soll, steht **im Szenariotext**, nicht
in einer Vorgabeliste. Aufgabe 5 – Reklamation zeigt das Prinzip: Der Text ist
lang, das Ergebnismodell klein, und jedes Sprachkonstrukt wird durch einen Satz
ausgelöst.

### Was sich gegenüber Auflage 2 ändert

| | Auflage 2 | Auflage 3 |
|---|---|---|
| Studierendenartefakt | 4-seitiges DOCX-Handout | PPTX, 3 Folien (+ DOCX-Druckfassung mit identischem Text) |
| Aufgabenaufbau | Szenario + Arbeitsauftrag + Pflichtklassen + Pflichtbeziehungen + Abgabecheck | nur Szenario |
| Steigerung über die Aufgaben | Anzahl Klassen (7 → 11 → 11) | Zahl und Art der Sprachkonstrukte |
| Zeitbudget | 115–135 Minuten | 3 × 20 Minuten (14 Min Bearbeitung + 6 Min Auswertung) |
| Lehrendenfassung | bleibt im Prinzip | bleibt, wird auf neue Szenarien resynchronisiert |

Die Skalierung über die Klassenanzahl ist die eigentliche Fehlerquelle der
Auflage 2. Der Dozent skaliert über Konstruktvielfalt bei konstant kleinem
Modell — Aufgabe 1 (Bibliothek) hat eine Verzweigung, Aufgabe 5 (Reklamation)
hat alle Konstrukte, aber beide Modelle passen auf eine Tafel.

## 2. Inhaltskatalog — „alle Inhalte"

Abdeckung wird gegen diesen Katalog geprüft. Jedes Konstrukt muss mindestens
einmal durch einen Szenariosatz erzwungen werden.

| # | Konstrukt | A1 | A2 | A3 |
|---|---|:--:|:--:|:--:|
| 1 | Klasse mit drei Kammern | ● | ● | ● |
| 2 | Attribut mit Sichtbarkeit und Typ | ● | ● | ● |
| 3 | Sichtbarkeiten `+ - #` | ● | ● | ● |
| 4 | Operation mit Parametern und Rückgabetyp | ● | ● | ● |
| 5 | Initialwert / Standardwert | ● | | |
| 6 | Abgeleitetes Attribut `/` | | ● | ● |
| 7 | Klassenattribut (unterstrichen) | | ● | |
| 8 | Binäre Assoziation mit Name und Leserichtung | ● | ● | ● |
| 9 | Rollennamen an den Enden | ● | | ● |
| 10 | Multiplizitäten `1`, `0..1`, `0..*`, `1..*` | ● | ● | ● |
| 11 | Navigierbarkeit | | ● | |
| 12 | Aggregation (leere Raute) | ● | | ● |
| 13 | Komposition (gefüllte Raute) | ● | ● | ● |
| 14 | Generalisierung | | ● | ● |
| 15 | Mehrstufige Generalisierung | | ● | |
| 16 | Abstrakte Klasse | | ● | ● |
| 17 | Abstrakte Operation | | ● | |
| 18 | Generalisierungsmenge `{disjoint, complete}` | | | ● |
| 19 | Enumeration | | ● | ● |
| 20 | Reflexive Assoziation | | | ● |
| 21 | Assoziationsklasse | | | ● |
| 22 | Notiz / Constraint `{…}` | ● | ● | ● |

Optional, nur falls der Foliensatz des Dozenten sie enthält: Interface mit
Realisierung, n-äre Assoziation, Abhängigkeit, Paket. Vorschlag: als
Zusatzsatz in A3 vorbereiten und erst nach Sichtung der Theoriefolien
einbauen — siehe Abschnitt 6.

## 3. Zuschnitt der drei Aufgaben

Domänen bleiben (Modellinhalte und Qualitätssicherung aus Auflage 2 sind
belastbar), der Umfang wird auf 20 Minuten geschnitten.

### Aufgabe 1 – Bestellsystem eines Onlineshops
**Schwerpunkt:** Klassenaufbau, Assoziation, Multiplizität, Aggregation vs. Komposition
**Modell:** 5 Klassen — Kunde, Bestellung, Bestellposition, Produkt, Sortiment
**Konstrukte:** 1–5, 8–10, 12, 13, 22
**Szenario deckt ab:** Kunde ohne Bestellung möglich; Bestellung genau einem
Kunden; gültige Bestellung mit mindestens einer Position; Position stirbt mit
der Bestellung; Produkt überlebt; Produkt in mehreren Sortimenten und überlebt
deren Auflösung; Einzelpreis als Preisstand zum Bestellzeitpunkt.
**Keine Vererbung** — sie wandert nach A2, damit A1 in 14 Minuten machbar bleibt.

### Aufgabe 2 – Hotelverwaltung
**Schwerpunkt:** Abstraktion, Spezialisierung, Zustände, abgeleitete Werte
**Modell:** 8 Klassen — Gast, Reservierung, Buchungsposition,
BuchbareLeistung {abstract}, Zimmer, Standardzimmer, Suite, Zusatzleistung
**Konstrukte:** 1–4, 6–8, 10, 11, 13–17, 19, 22
**Szenario deckt ab:** gemeinsame Merkmale buchbarer Leistungen; Zimmer als
Spezialisierung mit eigenen Unterarten; je Leistungsart eigene Verfügbarkeits-
und Preisregel (abstrakte Operation); Gesamtpreis wird berechnet, nicht
gespeichert (abgeleitetes Attribut); feste Statuswerte für Reservierung
(Enumeration); Mehrwertsteuersatz gilt für alle Reservierungen
(Klassenattribut); Zeitraumprüfung statt Kennzeichen `belegt`.
**Hotel, Mitarbeiter, Zahlung entfallen** — sie tragen kein neues Konstrukt.

### Aufgabe 3 – Veranstaltungsmanagement (Integrationsaufgabe, Reklamations-Äquivalent)
**Schwerpunkt:** alle Konstrukte in einem Fall
**Modell:** 8 Klassen — Veranstalter, Veranstaltung {abstract},
Präsenzveranstaltung, Onlineveranstaltung, Mitarbeiter, Teilnehmer, Buchung,
Ticket, Veranstaltungsort (+ Assoziationsklasse Betreuung)
**Konstrukte:** 1–4, 6, 8–10, 12–14, 16, 18–22
**Szenario deckt ab:** Veranstalter mit Mitarbeiterteam (Aggregation);
Veranstaltungen ausschließlich als Präsenz- oder Onlineform
(`{disjoint, complete}`); nur Präsenz braucht einen Ort; Buchung mit
mindestens einem Ticket (Komposition); Mitarbeiter berichten an einen
Vorgesetzten (reflexiv); Betreuung einer Veranstaltung mit Rolle und Zeitraum
(Assoziationsklasse); feste Buchungsstatus (Enumeration); Gesamtbetrag als
Summe der Tickets (abgeleitet).
**Zahlung und Programmpunkt entfallen** — Konstrukte bereits abgedeckt.

## 4. Textregeln für die Szenarien

Bindend, weil sie die Mängel der Auflage 2 strukturell ausschließen:

1. **Rückführbarkeit.** Jedes Element der Musterlösung — jede Klasse, jede
   Multiplizität, jede Raute — hat genau einen auslösenden Satz im Szenario.
   Kein Modellelement ohne Textbeleg, kein Satz ohne Modellwirkung.
2. **Keine Fachbegriffe im Szenario.** Der Text sagt „bleibt bestehen, wenn …"
   und nicht „Aggregation". Wie im Reklamationsbeispiel.
3. **Multiplizitäten als Aussage, nicht als Zahl.** „Ein Kunde muss noch keine
   Bestellung aufgegeben haben" statt „0..*".
4. **Grenzfälle explizit.** Was es nicht geben darf, wird ebenfalls gesagt
   („Eine Onlineveranstaltung hat keinen Veranstaltungsort").
5. **Ein Absatz, Fließtext**, 90–150 Wörter, Aufzählungen nur, wenn der Dozent
   sie im Beispiel verwendet (Aufgabe 3 – Studienbewerbung tut das).
6. **Domänenübergreifende Konsistenz.** Gleiche Formulierung ⇒ gleiche
   Modellantwort in allen drei Aufgaben. In Auflage 2 ergab „beschäftigt
   Mitarbeiter als Bestandteile seines Teams" einmal `0..1` und einmal `1`.

## 5. Artefakte und Arbeitsschritte

Neuer Ordner `05_abgabe/UML-Klassendiagramme_aufl.3/`. Auflage 2 bleibt
unangetastet als Archiv und als Rohstoff für den Vertiefungstermin
(siehe Abschnitt 7).

| # | Schritt | Ergebnis | Aufwand |
|---|---|---|---|
| 1 | Konstruktkatalog gegen den UML-Foliensatz des Dozenten abgleichen | bestätigter Katalog, optionale Konstrukte entschieden | 15 Min nach Erhalt der Folien |
| 2 | Drei Szenariotexte nach den Regeln aus Abschnitt 4 schreiben | `Szenarien.md` als Zwischenstand | 90 Min |
| 3 | Rückführbarkeitsmatrix je Aufgabe (Satz → Modellelement) | Tabelle, wird später Soll-Ist-Matrix der Lehrendenfassung | 45 Min |
| 4 | Musterdiagramme in `MOBIS_UML_Loesungen.drawio` neu aufbauen | 3 Diagramme, SVG- und PDF-Export | 120 Min |
| 5 | Abdeckungsprüfung Katalog × Diagramme automatisiert | Prüfprotokoll, jede Zeile aus Abschnitt 2 belegt | 30 Min |
| 6 | Aufgaben-PPTX im Layout des Dozenten (3 Folien, Titel + Fließtext) | `Aufgaben_UML_Klassendiagramm.pptx` | 45 Min |
| 7 | DOCX-Druckfassung mit identischem Text, ohne Zusätze | Handout | 20 Min |
| 8 | Lehrendenfassung resynchronisieren: Musterlösung, Begründungstabelle, Prüfinstanzen, typische Fehler, zulässige Alternativen, Raster 3 × 20 Punkte | `MOBIS_UML_Lehrendenfassung.docx/.pdf` | 120 Min |
| 9 | Moderationsteil ergänzen: je Aufgabe Hinweisstaffel (Minute 5 / Minute 10) und Checkpoint-Satz | Teil der Lehrendenfassung | 60 Min |
| 10 | Zeittest: eine Person modelliert alle drei Aufgaben unter Uhr | `Pilotprotokoll.md` ausgefüllt | 60 Min + Auswertung |
| 11 | Abnahme und Freigabe | `Qualitaetspruefung.md` aktualisiert | 30 Min |

Schritt 9 holt zurück, was Auflage 1 hatte und Auflage 2 verloren hat. Die
Betreuung der Gruppen während der Übung ist laut Modulsteckbrief bewerteter
Bestandteil der Prüfungsleistung — ohne Hinweisstaffel ist sie nicht
vorbereitet.

Schritt 10 ist nicht verhandelbar: Die Zeitangaben der Auflage 2 waren fachlich
plausibilisiert, aber nie gemessen, und lagen um den Faktor zwei daneben.

## 6. Was aus Auflage 2 übernommen wird

Unverändert übernehmen:

- Aggregationskonvention (leere Raute nur bei ausdrücklicher Teil-Ganzes-Aussage)
- Prüfinstanzen und Soll-Ist-Matrix als Aufbau der Lehrendenfassung
- Bewertungsraster mit 5 Dimensionen, 20 Punkte je Aufgabe, 60 gesamt
- Abschnitte „Typische Fehler" und „Zulässige Alternativen"
- Zeitraumprüfung statt `belegt: Boolean` (A2), Online-ohne-Ort-Regel (A3),
  Preisstand zum Bestellzeitpunkt (A1)

Nicht übernehmen:

- „Verbindlicher UML-Standard" auf dem Studierendenblatt — der Dozent hält die
  Vorlesung über die Notation
- Pflichtklassenkästen und Pflichtbeziehungslisten — sie nehmen die Lösung vorweg
- Abgabecheck auf dem Studierendenblatt — wandert als Auswertungsfragen in die
  Moderation der Lehrendenfassung
- die Übersichtstabelle mit Niveaustufen und Richtzeiten

## 7. Wiederverwendung für den Vertiefungstermin

Der Vertiefungstermin am 02.09.2026 sieht laut Konzeptfolie `3 × 30 Min` vor.
Die Auflage-2-Modelle mit 11 Klassen sind für 20 Minuten zu groß, für 30 Minuten
aber brauchbar. Vorschlag: Auflage 2 nicht überarbeiten, sondern als Grundlage
für die Vertiefungsaufgaben aufheben und dort um Zahlung, Programmpunkt, Hotel
und Mitarbeiter erweitern, die jetzt aus den Kurzaufgaben herausfallen.

## 8. Offene Punkte

1. **UML-Foliensatz des Dozenten liegt nicht vor.** In `02_materialien/` sind
   nur Einleitung, Konzept und EPK. Der Katalog in Abschnitt 2 unterstellt den
   Standardumfang eines Klassendiagramms. Zu klären ist, ob Interface mit
   Realisierung, n-äre Assoziation und Abhängigkeit behandelt werden. Bis dahin
   sind diese vier Konstrukte als optional geführt; die Aufgaben funktionieren
   ohne sie vollständig.
2. **Abgabeweg und Uploadformat** weiterhin offen.
3. **Werkzeug für die Studierenden** — handgezeichnet oder diagrams.net — sollte
   vor der Veranstaltung feststehen, weil es die 14 Minuten Bearbeitungszeit
   unmittelbar betrifft.

## 9. Abnahmekriterien

Freigabe nur, wenn alle Punkte erfüllt sind:

- [ ] Jede Zeile des Konstruktkatalogs ist mindestens einmal belegt.
- [ ] Jedes Modellelement der drei Musterlösungen ist auf genau einen
      Szenariosatz zurückführbar.
- [ ] Kein Szenariotext enthält UML-Fachbegriffe.
- [ ] Gleiche Formulierungen führen in allen drei Aufgaben zur gleichen
      Modellantwort.
- [ ] Gemessene Bearbeitungszeit je Aufgabe ≤ 14 Minuten.
- [ ] Aufgabenfolien enthalten ausschließlich Titel und Szenariotext.
- [ ] Lehrendenfassung enthält je Aufgabe Musterlösung, Begründung,
      Prüfinstanzen, typische Fehler, zulässige Alternativen, Raster und
      Hinweisstaffel.
