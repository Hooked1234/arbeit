# Worklog

## 2026-09-03

- **MOBIS-Prüfungsleistung ist erbracht und abgegeben** (Rückmeldung Felix).
  Der zugehörige Vertiefungstermin am 02.09.2026 hat stattgefunden. Vermerkt in
  `05_pruefungsleistung/README.md` (neuer Statusblock), im Modul-README unter
  „Aktueller Stand" und in `NEXT_STEPS.md`.
- `NEXT_STEPS.md` umgebaut: die Punkte 4 (Thema/Termin/Individualanteil/
  Abgabeformat klären) und 4a (Auflage 3 umsetzen) sind damit erledigt und in
  einen neuen Abschnitt „Erledigt" verschoben. Punkt 4 führt jetzt nur noch das,
  was tatsächlich offen ist: Bewertung und Rückmeldung des Dozenten erfassen.
- Bewusst *nicht* eingetragen: Note, Bewertung oder Dozentenfeedback — dazu
  liegt nichts vor. Ablageort dafür ist `05_pruefungsleistung/04_feedback/`.
- Die Vertiefungsübung „TherapistHive" (Punkt 4b) bleibt offen; sie ist eine
  Übung anderer Gruppen und läuft als Nachbereitung weiter.
- Repository aufgeräumt und auf einen Stand gebracht. Drei bis dahin nur lokal
  vorhandene Arbeitsstände sind nach `main` integriert: die MOBIS-Auflagen 1
  und 2 samt Software-Engineering-Handbuch, die Marketing-Fallstudie
  `GreenGlow` und der TherapistHive-Statusvermerk. Konflikte gab es nur in
  `WORKLOG.md` (Reihenfolge, GreenGlow in den bestehenden 10.08.-Abschnitt
  eingegliedert) und in `.gitignore` (Vereinigung beider Regelsätze).

## 2026-09-02

- Neue Vertiefungsübung `UML Use Case Vertiefungsübungen.pptx` (Christodoulou /
  Knoll) ausgewertet. Aufgabe 1 „Online-Therapie TherapistHive" unter
  `04_aufgaben/aufgabe-uc-01-therapisthive/` abgelegt: Aufgabentext wörtlich in
  `aufgabe.md`, dazu die sechs Sprachkonstrukte aus Folie 3 als verbindlicher
  Regelsatz (inklusive Pfeilrichtung bei `include` und `extend`).
- Mehr-Agenten-Lauf für das Use-Case-Modell: fünf unabhängige Entwürfe aus den
  Perspektiven `lehrbuch`, `purist`, `granular`, `akteure`, `fallen`, je gegen
  Texttreue, UML-Korrektheit und Prüfungstauglichkeit geprüft. Rohmaterial in
  `arbeitsstand/entwuerfe.json` (5 Entwürfe, 15 Kritiken).
- Lauf **unvollständig**: Synthese, Kritik und Finalisierung sind am
  Session-Limit abgebrochen. Es gibt daher noch kein abgestimmtes Modell und
  kein Diagramm; `abgabe/` ist leer. Details und offene Streitpunkte in
  `arbeitsstand/README.md`.
- Diagrammweg vorbereitet und im Browser verifiziert: draw.io lädt ein Modell
  reproduzierbar aus dem URL-Fragment. Werkzeugfrage bleibt offen, weil Folie 2
  der Aufgabenstellung Visual Paradigm Online empfiehlt.
- Finale Abgabe `Modellierung betrieblicher Informationssysteme Abgabe.pptx`
  (11 Folien) vollständig geprüft: jede Kardinalität, jedes Attribut und jede
  Methode beider Musterlösungen gegen den jeweiligen Szenariotext, dazu ein
  Pixelvergleich von Fehlerbild und Musterlösung zu Aufgabe 1. Ergebnis: exakt
  sechs Unterschiede, alle sechs Legendeneinträge korrekt, keine
  Modellierungsfehler. Die Fehler des Prüfberichts vom 01.09. sind behoben.
- Sechs offene Punkte dokumentiert, davon einer ein Widerspruch zwischen
  Antwortpanel/Folie 11 (Kleinschreibung) und den Diagrammen (Großschreibung).
  Bericht: `05_pruefungsleistung/06_aufgabe3/2026-09-02_Pruefbericht_finale-Abgabe.md`.
- Kriterium-9-Lücke belegt: Von den sechs Agendapunkten der Dozenten-
  präsentation sind „Einordnung in ARIS" (Folie 5) und „Historie" (Folie 3) in
  keiner der vier Aufgaben aufgegriffen.
- Aufgabe 5 „Einordnung und Herkunft" dafür gebaut (7 Minuten, Ende Block 1):
  `06_aufgabe3/Aufgabe_5_Einordnung.md` plus zwei einfügefertige Folien mit
  Notizenseiten in `Aufgabe_5_Einordnung.pptx`, aus der Abgabedatei geklont,
  daher identisches Layout und identische Schriftgrade.
- ARIS-Einordnung belegt statt geraten: `Konzept.pptx`, Folie 2, führt das
  Klassendiagramm zweimal — Datensicht und Funktionssicht, jeweils auf Höhe der
  DV-Konzept-Zeile. Die frühere Annahme „Fachkonzept" war falsch.
- Der Entwurf `Aufgabe_3_Fitnessstudio.md` vom 01.09. ist überholt: Aufgabe 3
  und 4 existieren inzwischen in der Abgabe.
- Entscheidung Felix: Aufgabe 3 und 4 werden selbst vorgetragen, nicht als Frage
  gestellt. Deshalb statt der Aufgabenfassung eine reine Vortragsfolie gebaut:
  `06_aufgabe3/Antwortfolie_ARIS.pptx`. Sie klont Folie 5 des Dozentenfoliensatzes
  (ARIS-Haus nach Scheer 2011) und ergänzt zwei Beschriftungen auf Höhe der
  DV-Konzept-Zeile in Daten- und Funktionssicht, einen Aussagesatz und die
  Quellenzeile im Stil von Folie 2 der Abgabe. Moderationstext samt
  Historie-Anschlusssatz liegt in den Notizen.
- `Aufgabe_5_Einordnung.pptx` (Frageform) ist damit hinfällig, bleibt aber liegen.

## 2026-08-30

- MOBIS-Vertiefungstermin 02.09.2026 geplant: `05_pruefungsleistung/03_entwurf/
  2026-08-30_Umsetzungsplan_vertiefung.md`. Format 2 × 45 Minuten, zwei Personen,
  eine Aufgabe in zwei Stufen mit Änderungsauftrag und Zielkonflikt. Termin,
  Format und Thema aus `Themen_Zeitplan_2026_BI-2.xlsx` (W6, Zeile 15) belegt.
- Kriterium 9 „Alle Themen wiederholt" ohne Folienwiederholung gelöst: Die
  Konzeptfolie ordnet die 10-Minuten-Wiederholung dem Dozenten zu (`KS`), der
  studentische Anteil ist ausdrücklich nur `STD` Übungen. Nachweis läuft über
  eine Konstruktabdeckungsmatrix.
- Drei Materiallieferungen ausgewertet. Wichtigster Befund: Der Foliensatz
  `7-UML-KD.pptx` behandelt nur fünf Sprachkonstrukte, und der eigene
  Aufgabensatz vom 12.08. (`OneDrive_2026-08-30.zip`) verwendet keine
  Sichtbarkeiten, Datentypen, abstrakten Klassen, Enumerationen oder
  Assoziationsklassen. Der 22-Konstrukte-Katalog der Auflage 3 war nie gegen
  die Realität geprüft.
- `Szenarien_vertiefung.md` deshalb in Fassung 2 neu geschrieben, strikt im
  belegten Rahmen. Die erste Fassung hätte sieben ungedeckte Konstrukte
  eingeführt und Kriterium 8 verletzt. Vertiefung entsteht jetzt über
  Modellgröße, Vernetzung, Umbau und Zielkonflikt statt über neue Notation.
- Auflage-3-Branch `claude/uml-klassendiagramme-bewertung-5d35e8` per
  Fast-Forward integriert; Diagramm- und Dokumentgeneratoren übernommen.
- Diagrammgenerator nach `05_abgabe/UML-Vertiefung_02-09/Diagramme/_generator/`
  kopiert und angepasst: farbige Kopfzeile im Hausstil vom 12.08., `tone` für
  die Differenzansicht, Dateinamen aus dem Modell. Die Attributunterstreichung
  der Auflage 3 entfernt — bei präfixloser Notation hätte sie jedes Attribut
  unterstrichen.
- Drei Musterdiagramme gebaut (Ist-Modell 9 Klassen, Endmodell 14 Klassen,
  Differenzansicht) als SVG, PNG, A3-PDF und drawio. Geometrieprüfung ohne
  Befund. Neu gegenüber Auflage 3: `build_pdf.py` erzeugt eigenständige
  A3-Quer-PDFs ohne drawio-CLI, was dort offen geblieben war.
- `check_konsistenz.py` ergänzt und bestanden: Stufe 1 ist bis auf die drei
  angekündigten Umbauten vollständig in Stufe 2 enthalten, Kardinalitäten
  übernommener Kanten unverändert, keine isolierte Klasse.
- Block 2 auf Idee von Felix umgestellt: statt Änderungsauftrag jetzt die
  Kritik eines KI-erzeugten Diagramms zum Text von Aufgabe 1. Der
  Änderungsauftrag bleibt als Reserve gepflegt, falls das Werkzeug ausfällt.
  Live-Erzeugung durch die Gruppen verworfen: Der KI-Output ist nicht
  reproduzierbar, damit gäbe es keine vorbereitete Musterlösung.
- Präsentationsarten von Stufe 2 nach Aufgabe 1 gezogen. Ohne sie fehlte die
  mehrstufige Vererbung in der Abdeckungsmatrix, weil Block 2 als Fremdprüfung
  keine Konstruktabdeckung mehr garantiert. Aufgabe 1 deckt jetzt alle neun
  Konstrukte allein ab, Modell 11 Klassen. Auslösender Satz im Szenariotext
  ergänzt und Rückführbarkeit nachgezogen.
- KI-Entwurf als vierte Diagrammseite gebaut: acht kuratierte Fehler nach den
  typischen Ausfallmustern eines Sprachmodells, dazu zwei zulässige
  Abweichungen. Die Unterscheidung falsch gegen bloß anders ist der Kern der
  Aufgabe. Herkunft in der Lehrendenfassung offengelegt.
- Dokumente gebaut: Aufgabenfolien (2 Folien im Dozentenformat), Aufgabenblatt
  mit Protokollbogen und Schlussfrage, Lehrendenfassung mit beiden
  Musterlösungen, Fundliste, zwei Rastern à 20 Punkten, Rollenteilung,
  wörtlicher Hinweisstaffel und FAQ-Katalog.
- `check_dokumente.py` ergänzt: 51 Prüfungen ohne Befund, darunter zwei
  Sprachprüfungen. Lösungswörter sind überall auf dem Blatt verboten,
  Notationswörter nur im Szenariotext — „Kardinalität" ist im Arbeitsauftrag
  erwünscht, es ist das Wort des Dozenten von Folie 6.
- Word-COM-Export hängt wie in Auflage 3; Prozess abgebrochen, PDF-Export der
  Word-Dateien bleibt Handarbeit. Strukturprüfung ersetzt die Sichtprüfung
  nicht vollständig.
- Offen: Zeittest am 31.08. durch Felix und den Abgabepartner.

## 2026-08-24 — Marketing Management (Praxisbericht Spotify)

- Zweite, unabhängige Fassung des Arbeitsstands erstellt und unter
  `projekte/HSBA 2. Semester/marketing management/05_pruefungsleistung/`
  als `Spotify_Praxisbericht_Arbeitsstand_1_Claude.docx` abgelegt. Sie
  beantwortet denselben Auftrag wie `Spotify_Praxisbericht_Arbeitsstand_1.docx`
  (Codex), wurde aber ohne Kenntnis von dessen Inhalt erarbeitet.
- Vergleich beider Fassungen als `Vergleich_Arbeitsstand_1.md` im selben Ordner.
  Ergebnis: Arbeitsstand 1 bleibt die Grundlage — er hat das echte
  Forschungsdesign (H1–H4), die breitere Theoriebasis, die Claim-Source-Matrix
  und die SEC-Filings als Primärquellen. Die zweite Fassung liefert die schärfere
  These, den engeren Vorlesungsbezug und die Wettbewerbsdynamik.
- Fünf Punkte zur Übernahme in Arbeitsstand 1 benannt: These in die
  Forschungsfrage ziehen (H2, Wichtigkeitsabfrage und H3b messen genau die drei
  Wettbewerbsvorteil-Kriterien nach Meffert et al.), Marktanteilsentwicklung
  2024→2025 in Kapitel 3, Kaufverhaltenstyp nach Kotler/Armstrong ergänzen,
  Preistabelle auf sechs Anbieter erweitern, Vorlesungsmodelle im 4P-Teil
  benennen.
- Fehler in der eigenen Fassung gefunden und korrigiert: Spotifys Abonnentenzahl
  für 2024 lautet ≈ 263 Mio., nicht 236 Mio. (32,2 % von 818,3 Mio. nach MIDiA,
  deckt sich mit dem Q4-2024-Bericht).
- Ungeklärter Widerspruch zwischen beiden Fassungen: Einzelpreis Amazon Music
  Unlimited (12,99 €/11,99 € gegen 10,99 €/9,99 €). `amazon.de` sperrt
  automatisierte Abrufe, die About-Amazon-Seite steht auf Stand 08/2024. Muss im
  eingeloggten Konto geprüft und als PDF archiviert werden.
- Zwei Unklarheiten im Leitfaden übernommen, die Arbeitsstand 1 zuerst erkannt
  hat: Cut-off nennt „drei Bewertungsbereiche“, der Bogen hat vier Blöcke; und
  ob die 300-Wörter-Fazits in die 6.000-Wörter-Grenze zählen.
- Hinweis: Der Prompt-Anhang muss beide Werkzeuge führen (Codex und Claude),
  bisher steht dort nur der Codex-Auftrag.

## 2026-08-15 — EOS Auslandseinsatz (Bewerbung)

- Englisches Motivationsschreiben für den internen Auslandseinsatz erstellt:
  `projekte/EOS Auslandseinsatz/motivation-letter_international-assignment.md`
  (273 Wörter, länderneutral für Spanien/Rumänien, natürliches Business English).
- Grundlage: EOS-Einsätze Sachbearbeitung, EOS Field Service, Cloud Services
  (AWS + Daten), Finance (Prognosen); belegte EOS-Group-Aussage „more than
  20 countries" (eos-solutions.com).
- Korrektur nach Review: EOS Field Service ist Tochterunternehmen, nicht der
  Arbeitgeber — Arbeitgeber ist EOS. In `context/felix.md` zu korrigieren.
- Offen: Name der Ansprechpartnerin, ggf. Länderfassung, englischer CV.
- Überarbeitete Endfassung (ca. 340 Wörter): Rücktransfer ergänzt (was EOS
  nach der Rückkehr davon hat), Absatz zur interkulturellen Anpassung
  konkretisiert, „patience" durch aktive Formulierung ersetzt, Dopplung
  „case handling" entfernt, Gedankenstriche auf zwei reduziert.
- Faktencheck bestanden: EPP-Studie 2025 nennt Spanien, Rumänien und Slowenien
  als Vorreiter bei digitalisierten Mahnprozessen, Deutschland als Nachzügler;
  „more than 20 countries" deckt sich mit Geschäftsbericht 2025/26.
- Bewusst weggelassen: Wunschzeitraum/Dauer, Sprachkenntnisse (keine
  Spanischkenntnisse vorhanden — Englisch-Argumentation trägt allein).
- Semikolon-Aufzählung der vier Einsatzbereiche auf Kommas + Klammern
  umgestellt (Cloud Services (AWS and data), Finance (forecasting)).
- Länder-Nennung umformuliert: „Both countries under discussion, Spain and
  Romania, …" — greift den Vorschlag der Ansprechpartnerin auf, statt eigene
  Auswahl zu suggerieren; Flexibilität für beide Optionen bleibt erhalten.
  Keine Präferenz genannt, da tatsächlich keine besteht.

## 2026-08-15 — EOS Auslandseinsatz (englischer CV)

- Englischen CV erstellt: `projekte/EOS Auslandseinsatz/Felix_Heinsius_CV_EN.docx`
  (eine Seite, ATS-freundlich: keine Tabellen/Textboxen, Calibri, Standard-
  Abschnittsnamen, Aufzählungen über echte Numbering-Definition).
- Alter CV war vollständig veraltet (nannte weder HSBA noch EOS, führte Würzburg
  als aktuelles Studium) und in sich widersprüchlich (Jura ab 10/2022 lag vor dem
  Abitur 07/2023). Inhaltlich neu aufgebaut.
- Chronologie bereinigt und bestätigt: Abitur 07/2023 → Botswana 09/2023 →
  Jura Frankfurt 10/2023–09/2024 → WI Würzburg 10/2024–04/2025 → EOS ab 08/2025 →
  HSBA ab 05.01.2026. Lücke 05/2025–07/2025 bewusst nicht kommentiert.
- HSBA (Education) und EOS (Experience) bewusst getrennt geführt, dualer Charakter
  in beiden Einträgen benannt — sonst verschwindet die Praxiserfahrung aus dem
  Abschnitt, in dem ATS und Leser sie suchen.
- Vier EOS-Rotationen unter einem Dachenttrag, ungleich gewichtet.
- Auf Wunsch keinerlei Bezug zum Auslandseinsatz im CV — Argumentation bleibt
  vollständig im Motivationsschreiben.
- Bewusst weggelassen: SAP-Zertifikat (im Workspace nicht auffindbar, unbelegt),
  SQL und Power BI (nie als eigene Anwendung bestätigt), Latinum (international
  ohne Aussagekraft), Zeitungsausträger und Kanzleipraktikum.
- Python nur als „basics, from personal projects" — Grundlage ist `context/felix.md`
  (Stack Python/Streamlit/yfinance), nicht bestätigte Berufserfahrung.
- AWS bewusst als „working basics from a hands-on rotation" formuliert, nicht als
  produktive Erfahrung — entspricht Felix' eigener Einschätzung.
- Offen: voraussichtliches Abschlussdatum HSBA, SAP-Zertifikat, Präzisierung der
  Tätigkeit bei EOS Field Service.
- Nachtrag: Voraussichtlicher Abschluss (Ende 2028) bestätigt und in der
  HSBA-Metazeile ergänzt statt in der Datumsspalte — vermeidet Zeilenumbruch
  bei langem Hochschulnamen. Verbleibend offen: SAP-Zertifikat, Präzisierung
  der Tätigkeit bei EOS Field Service.
- Umbau der EOS-Station nach Feedback: Zwischenüberschriften mit Einzelbullets
  entfernt (wirkten zerstückelt). Jetzt: Einsatzorte als eine Zeile, darunter
  Werkzeugliste mit ehrlicher Niveauangabe, darunter zusammenfassender Zweizeiler.
- Separate Skills-Sektion aufgelöst, da die Werkzeuge nun unter Experience stehen —
  sonst doppelte Nennung. Sprachen und Office als eigene Zeilen erhalten.
- Werkzeugniveaus nach Felix' Selbsteinschätzung: Excel (Grundkurs), AWS
  (Grundlagen + Bedrock), Git/GitHub (in Nutzung), Power BI (erste Versuche),
  SQL/Python/DBeaver/Azure (nur kurz getestet). Bewusst gestaffelt formuliert
  statt pauschal — schützt im Gespräch und wirkt selbstsicher statt aufgebläht.
- Rückbau auf Wunsch: Die vier Abteilungen stehen wieder als einzelne fette
  Überschriften untereinander, aber ohne Tätigkeitsbeschreibung — der Inhalt
  ergibt sich aus dem EOS-Kontext. Werkzeugliste und Zusammenfassung bleiben.

## 2026-08-10

- `MOBIS`-Prüfungsleistung Auflage 2 (UML-Klassendiagramme) bewertet. Befund:
  Artefakte und Bewertungsraster sind belastbar, das Zeitbudget von 115–135
  Minuten kollidiert aber mit dem laut Konzeptfolie und Prüfungsordner
  vorgesehenen Format `3 × 20 Min`. Das Studierendenblatt gibt Pflichtklassen und
  Pflichtbeziehungen inklusive Beziehungstyp vor und nimmt damit die Lösung
  vorweg; die Musterlösungen antworten auf identische Formulierungen in Aufgabe 2
  und 3 unterschiedlich; die Hinweisstaffel und der Moderationsteil aus Auflage 1
  fehlen, obwohl die Betreuung der Gruppen bewerteter Bestandteil ist.
- Aufgabenformat des Dozenten aus `Aufgaben_EPK_Keine_Lösung.pptx` rekonstruiert:
  eine Folie je Aufgabe, Titel plus durchgehender Fließtext aus Szene und
  genauerer Beschreibung, keine Arbeitsaufträge oder Vorgabelisten. Die
  Steigerung erfolgt über Konstruktvielfalt, nicht über Modellgröße.
- Umsetzungsplan für Auflage 3 erstellt:
  `05_pruefungsleistung/03_entwurf/2026-08-10_Umsetzungsplan_aufl.3.md`. Enthält
  Konstruktkatalog mit Abdeckungsmatrix über alle drei Aufgaben, Zuschnitt auf
  je 20 Minuten, Textregeln für die Szenarien, elf Arbeitsschritte mit Aufwand
  und Abnahmekriterien. Auflage 2 bleibt als Archiv und als Grundlage für den
  Vertiefungstermin am 02.09.2026 (`3 × 30 Min`) erhalten.
- Schritte 2 und 3 des Plans umgesetzt:
  `05_pruefungsleistung/03_entwurf/Szenarien_aufl.3.md`. Drei Szenariotexte im
  Format des Dozenten (210–250 Wörter Fließtext, keine UML-Begriffe, keine
  Arbeitsaufträge) samt Rückführbarkeitsmatrix, die jeden Satz auf genau ein
  Modellelement abbildet. Alle 22 Konstrukte des Katalogs sind belegt.
  Drei Abweichungen vom Plan dokumentiert: Rollennamen nur in Aufgabe 3,
  `Ticket` in Aufgabe 3 zugunsten von `anzahlPlätze` gestrichen, Aggregation
  zusätzlich in Aufgabe 3. Modellgrößen 5, 8 und 8 Klassen.
- Schritte 4 und 5 des Plans umgesetzt:
  `05_abgabe/UML-Klassendiagramme_aufl.3/Diagramme/`. Drei Musterdiagramme als
  editierbare drawio-Quelle, SVG-Vektorfassung und PNG mit 288 dpi. Erzeugt
  werden sie aus einem Layoutmodell unter `_generator/`, das vor jedem Export
  Kastenüberlappungen, Seitenüberläufe, zu schmale Kästen und Kantenendpunkte
  abseits der Klassenrahmen prüft. Abdeckungsprüfung: 22 von 22 Konstrukten
  belegt; `{disjoint, complete}` fehlte zunächst im Diagramm zu Aufgabe 3 und
  wurde als Beschriftung an der Generalisierungsmenge ergänzt. Drei Sätze in
  den Szenarien nachgezogen, damit Bestellung, Reservierung und
  Buchungsposition eine im Text begründete Operation erhalten.
  Offen: PDF-Export der Diagramme (in dieser Umgebung keine drawio-CLI und kein
  SVG-nach-PDF-Konverter verfügbar) sowie der Zeittest.
- Schritte 8 und 9 des Plans umgesetzt: `MOBIS_UML_Lehrendenfassung.docx` und
  `.pdf`, 13 Seiten, davon drei A3-Querseiten mit den Musterdiagrammen. Je
  Aufgabe Szenariotext, Moderation, Beziehungsübersicht, Prüfinstanzen,
  typische Fehler, zulässige Alternativen, Bewertungsraster und die
  vollständige Rückführbarkeitstabelle. Der Moderationsteil holt die in
  Auflage 2 verlorene Hinweisstaffel zurück: je Aufgabe eine offene Frage nach
  Minute 5, ein eingrenzender Hinweis nach Minute 10 und ein Checkpoint-Satz
  zur Auflösung, dazu ein Ablaufplan für die 20 Minuten und eine
  Priorisierungsregel bei Zeitnot.
- Zwei Layoutfehler im ersten Durchlauf behoben: Leerseiten vor den
  Abschnittswechseln und fehlende Kopfzeilenwiederholung der langen
  Rückführbarkeitstabellen. PDF-Prüfung anschließend ohne Befund.
- Schritte 6 und 7 des Plans umgesetzt: `MOBIS_UML_Aufgaben.pptx` mit drei
  Folien im Format des Dozenten (Titel plus Fließtext, 18 pt, volle Breite) und
  `MOBIS_UML_Aufgaben_Druckfassung.docx/.pdf` mit identischem Text auf zwei
  Seiten. Die Folien bauen auf seiner Vorlage `Aufgaben_EPK_Keine_Lösung.pptx`
  auf; Master, Theme und Layout bleiben unverändert, Folien 4 und 5 entfallen,
  Dokumenteigenschaften neu gesetzt. Ein aus dem Layout geerbtes
  Aufzählungszeichen auf Folie 1 wurde unterdrückt. Textgleichheit zwischen
  Folien und Quelle automatisiert geprüft.
- Werkzeugnotiz: PowerPoint kann in dieser Umgebung nicht nach PDF speichern
  (`SaveAs`, `SaveCopyAs` und `ExportAsFixedFormat` scheitern), wohl aber
  einzelne Folien über `Slide.Export` als PNG. Die visuelle Abnahme lief
  darüber.
- Werkzeugnotiz: Word `ExportAsFixedFormat` hängt hier reproduzierbar,
  `SaveAs2` mit Format 17 funktioniert. Bei hängendem Word hilft das Löschen
  des Resiliency-Schlüssels. Das erklärt auch den entsprechenden Befund in der
  Qualitätsprüfung der Auflage 2.
- Gruppenfallstudie `GreenGlow — Nachhaltige Körperpflege zwischen Anspruch und
  Akzeptanz` (Abschnitt 2.4, Sustainable Marketing und Marketingethik) aus
  `02_materialien/Gruppenfallstudien_Marketing.pdf` bearbeitet und unter
  `projekte/HSBA 2. Semester/marketing management/04_aufgaben/greenglow_sustainable-marketing/greenglow_loesung.md`
  abgelegt. Das Dokument beantwortet alle drei Aufgabenteile (Konsumentenverhalten,
  Norm-Aktivierungs-Modell mit drei Maßnahmen, Theory of Reasoned Action) sowie
  den geforderten Plenumsblock und visualisiert beide Modelle als Mermaid-Diagramme.
- Kernbefund der Analyse: Die 63 % „zu teuer" sind überwiegend ein Wert- und
  Nachweisproblem, nicht ein Preisproblem — Glaubwürdigkeitslücke (47 %) und
  fehlende wahrgenommene Differenzierung (38 %) entwerten den Aufpreis von +141 %.
- Einschränkung dokumentiert: Die Modellgrafiken auf S. 60 und 61 der
  Vorlesungsunterlagen liegen nur als Bild ohne Textebene vor. Die Phasen- und
  Konstruktbezeichnungen stammen daher aus der Primärliteratur (Meffert et al.
  2019; Ajzen/Fishbein 1973) und sind vor der Abgabe mit den Folien abzugleichen.

## 2026-08-07

- Für den ersten MOBIS-Prüfungstermin am 12.08.2026 drei progressive
  20-Minuten-Übungen zum UML-Klassendiagramm im Fall „Onlinehandel“ erstellt:
  Klassenabgrenzung und Generalisierung, Multiplizitäten in beide Richtungen
  sowie die fachlich begründete Modellierung von `Bestellposition`.
- Eine sieben Folien umfassende Aufgabenpräsentation im Stil der vorhandenen EPK-
  Übungsfolien sowie eine elfseitige Lösungs- und Moderationshilfe als
  bearbeitbare DOCX und inhaltsgleiche PDF unter
  `modellierung betrieblicher informationssysteme/05_pruefungsleistung/05_abgabe/`
  abgelegt. Der zweite Prüfungstermin am 02.09.2026 ist bewusst nicht enthalten.
- Alle sieben Folien und elf Dokumentseiten vollständig gerendert und visuell
  geprüft. Die Präsentation besteht den Canvas- und Vorlagenabgleich; DOCX und
  PDF stimmen in Inhalt und Seitenfolge überein und der Dokumentaudit meldet
  keine Barrierefreiheitsbefunde.

## 2026-08-06

- Ein englisches `Software Engineering Course Map & Reference Handbook` in
  einer eigenständigen, für das Modul passenden Nachschlagewerk-Struktur
  erstellt; bewusst ohne die Struktur der 1,0-Lernzettel-Vorlage.
- Die 11 lokal vorhandenen Kurs-PDFs vollständig ausgewertet und die
  Lernlogik als Rückkopplungssystem dargestellt: Grundlagen → Qualität und
  Anforderungen → Organisation und Prozess → System- und Softwarearchitektur
  → Design, Implementierung und Tests → Build und Release → Betrieb und
  Wartung → Feedback in frühere Entscheidungen.
- 51-seitige PDF und bearbeitbare DOCX unter
  `projekte/HSBA 2. Semester/software engineering/03_notizen/` abgelegt. Das
  Handbuch enthält Fragennavigator, 11 Quellenkapitel einschließlich der
  sichtbaren Lücke von Deck 04, MentorHive-End-to-End-Fall, Vergleichstabellen,
  Video-Club-Zuordnung, alphabetisches Glossar und Quellenkarte.
- Alle 51 PDF-Seiten visuell geprüft. Inhaltsverzeichnis und PDF-Lesezeichen
  funktionieren; 431 Tabellenzeilen bleiben ungeteilt. Abschließende Prüfungen
  melden 0 Barrierefreiheitsbefunde, konsistente Tabellengeometrie, keine
  Leerseiten, durchsuchbaren Text und eine getaggte PDF ohne Autorenmetadaten.

## 2026-08-04

- Gruppenfallstudie Jägermeister, Teil 2 („Zukunftsstrategie 2035") unter
  `projekte/HSBA 2. Semester/marketing management/04_aufgaben/jaegermeister_markt-und-strategie/`
  bearbeitet: `teil2_zukunftsstrategie-2035.md` enthält Taktplan für die
  35 Minuten Gruppenarbeit, die inhaltliche Ausarbeitung entlang STP,
  Wettbewerbsvorteil und Marketing-Mix sowie die drei geforderten
  Präsentationsergebnisse (neue Zielgruppe „Die Rückkehrer" 30–45, Maßnahme
  „Ice-Cold Residencies", Claim „56 Kräuter. Für jede Nacht, die zählt.").
  Ergänzend `praesentationsprompt_jaegermeister-2035.md` als selbsttragender
  Prompt für eine HSBA-konforme Kurzpräsentation (8 Folien inkl. Quellenfolie,
  Design-Tokens aus `standards/praesentation-hsba.md`). Marktzahlen bewusst nicht
  erfunden, Annahmen im Dokument ausgewiesen; 1878 wird ausschließlich als
  Unternehmensgründung geführt, nicht als Datierung von Rezeptur oder Marke.
- Die Module `principles of finance` und `marketing management` unter
  `projekte/HSBA 2. Semester/` in die bestehende sechs Bereiche umfassende
  Modulstruktur aufgenommen.
- Neun Ausgangsdateien aus den separaten Kursordnern unverändert nach
  `02_materialien/` kopiert: fünf Finance-Dateien und vier Marketing-PDFs.
  Die vier Finance-ZIP-Archive bleiben gemäß bestehender `.gitignore`-Regel
  ausschließlich lokal; ihre 16 PDF-Inhalte wurden sicher entpackt, geprüft und
  werden zusammen mit den übrigen Materialien versioniert.
- Modulbeschreibungen, Folien, Archivverzeichnisse, Praxisberichtsleitfaden,
  Fallstudien und HSBA-Regeln inhaltlich ausgewertet und bestätigte Angaben in
  Modulsteckbriefe, Prüfungsordner und Materialübersichten übernommen.
- Semesterübersicht und zentralen Workspace-Überblick um beide Fächer ergänzt
  sowie die dringende Marketing-Frist zur Team- und Unternehmensmeldung am
  10.08.2026 dokumentiert.
- Einseitiges `Semester-Cockpit` für das 2. Semester aus den Originalquellen
  erstellt. Die Seite bündelt fünf Module, belegte Prüfungsleistungen,
  Schlüsseltermine, offene Angaben und einen konkreten 90-Minuten-Startfokus.
- Prüfungs- und Terminangaben gegen 34 PDFs, vier PPTX- und zwei XLSX-Quellen
  abgeglichen; Widersprüche bei MOBIS, Marketing und Finance sichtbar markiert.
  Das DOCX wurde in Word auf genau eine Seite gerendert, visuell geprüft und
  mit fehlerfreiem Barrierefreiheits- und Tabellengeometrie-Audit abgeschlossen.
- Nutzerklarstellung zu den Prüfungsleistungen eingearbeitet: In Finance bildet
  die 90-minütige englische Klausur die reguläre Note; eine optionale
  Buchpräsentation kann 0,3 Notenpunkte gutschreiben. In MOBIS bestimmt die
  Erstellung der Übungsaufgabe nach dem Format von `Aufgabe 5 – Reklamation`
  die vollständige Modulnote. Semester-Cockpit, Modulsteckbriefe,
  Prüfungsordner, Modul-READMEs und offene nächste Schritte wurden konsistent
  korrigiert; Nutzerangaben bleiben von Primärquellen getrennt gekennzeichnet.
  Auch der ausführliche persönliche MOBIS-Lehrplan wurde an sieben betroffenen
  Stellen berichtigt, erneut auf 14 Seiten gerendert und ohne Layout- oder
  Barrierefreiheitsfehler geprüft.
- Fünf eigenständige Modulüberblicke für MOBIS, Software Engineering,
  Wirtschaftsstatistik, Principles of Finance und Marketing Management unter
  `projekte/HSBA 2. Semester/00_modulueberblicke/` erstellt. Jeder Überblick
  dokumentiert Prüfungsleistung, vollständigen lokalen Quellenbestand,
  prüfungsorientierten Inhaltskern, Fehlerfallen, Austrittskriterien,
  Prioritäten und offene Angaben mit der Statuslogik
  Belegt/Kursinfo/Abgeleitet/Offen.
- Die fünf DOCX-Dateien auf zusammen 27 Seiten mit Microsoft Word gerendert und
  vollständig visuell geprüft. Einen Leerseitenfehler durch Umbruchabsätze sowie
  eine OOXML-Reihenfolgeabweichung korrigiert. Abschließende Prüfungen melden
  jeweils 0 Barrierefreiheitsbefunde und konsistente Überschriften-, Abschnitts-
  und Tabellengeometrie-Strukturen.

## 2026-08-03

- Persönlichen Codex-Template-Skill `artifact-template-1-0-lernzettel` unter
  `C:/Users/felix/.codex/skills/` erstellt. Der Skill bewahrt den geprüften
  MOBIS-Lehrplan als Referenz, erzwingt Belegt/Abgeleitet/Offen-Status,
  prüfungsnahe Übungen und Render-QA und wurde mit `quick_validate.py`
  erfolgreich validiert.

## 2026-07-30

- Die neuen Module `software engineering` und `wirtschaftsstatistik` unter
  `projekte/HSBA 2. Semester/` nach der bestehenden sechs Bereiche umfassenden
  Modulstruktur eingerichtet.
- Elf PDF-Dateien für Software Engineering und vier Ausgangsdateien für
  Wirtschaftsstatistik unverändert unter den jeweiligen `02_materialien/`
  einsortiert.
- Modul- und Materialübersichten ergänzt sowie die Semester-README aktualisiert.

## 2026-07-29

- Projektstruktur `projekte/HSBA 2. Semester/` angelegt.
- Erstes Modul `modellierung betrieblicher informationssysteme` mit getrennten
  Bereichen für Organisation, Materialien, Notizen, Aufgaben, Prüfungsleistung
  und Quellen vorbereitet.
- Bestehende zentrale Standards und Templates bewusst referenziert statt
  innerhalb des Projekts zu duplizieren.
- Sechs ausgegebene Unterrichtsmaterialien unverändert nach Dateityp unter
  `02_materialien/` einsortiert: vier Präsentationen und zwei Tabellen.
- Persönlichen MOBIS-Lehrplan aus diesen Kursunterlagen erstellt, acht
  Semesterwochen sowie belegte, abgeleitete und offene Ereignisse dokumentiert
  und unter `projekte/HSBA 2. Semester/modellierung betrieblicher
  informationssysteme/03_notizen/2026-07-29_persoenlicher-lehrplan_mobis.docx`
  abgelegt.

## 2026-06-30

- Zwei Workspace-Varianten zusammengeführt: GitHub-Gerüst (Hooked1234/arbeit,
  Codex+Claude-Prozess) + lokale Substanz (ki-workspace mit Design-Tokens).
- 3-Schichten-Architektur eingeführt: `standards/` (Wie / Quelle der Wahrheit),
  `templates/` (Was / Struktur), `skills/` (schlanke Auslöser mit Frontmatter).
- Redundanz aufgelöst: AGENTS.md und CLAUDE.md teilen EINE Routing-Tabelle
  (in AGENTS.md §1); CLAUDE.md verweist darauf, statt Regeln zu duplizieren.
- Design-Tokens aus den lokalen Standards in die Templates verlinkt (Templates
  verweisen aufs jeweilige Standard statt Farben/Maße zu wiederholen).
- `context/` (felix, eos, hsba) und `decisions/` aus der lokalen Variante übernommen.
- Skills um `excel-pivot` und `ki-dokument` ergänzt; Standards dafür neu angelegt.
- Übergabe-Dateien (WORKLOG/NEXT_STEPS/CHANGELOG), `gitw`, `.gitignore` und
  `qualitaetspruefer`-Agent aus dem GitHub-Gerüst übernommen.
- Encoding: bewusst echte Umlaute (UTF-8) statt ASCII-Ersatz — bessere Lesbarkeit.
- HSBA-Markenwerte recherchiert und gesetzt: Farb-Tokens (#002C58 / #4779AE /
  #0C2950), Schrift *Titillium Web*, Logo-SVG-Pfad, Fließtext 18–20 pt,
  Chicago Author-Date. Praxisbericht-Eckdaten (Thema, Leitfrage, Modul, Name)
  in `context/felix.md` ergänzt. Fremder Vattenfall-Bericht bewusst ignoriert.
- Offen: EOS-Markenschrift/Logo (Designportal) sowie HSBA Datum/Matrikelnummer/
  Kurs/Dozent:in.
