---
name: excel-pivot
description: Nutze diesen Skill fuer Excel, PivotTables, Power Query, Power BI-nahe Datenauswertung, Feldlogik, Monats-/Jahreslogik und Plan-Ist-Vergleiche mit anonymisierten Unternehmensdaten.
---

# Excel- und Pivot-Skill

## Ziel

Hilf Felix, Excel- und Pivot-Probleme praktisch zu loesen, ohne echte interne Daten zu benoetigen.

## Datenschutz

- Keine echten Unternehmensdaten anfordern.
- Nutze abstrakte Feldnamen und Dummy-Beispiele.
- Sensible Daten nicht in Beispiele uebernehmen.

## Antwortstruktur

1. Kurzantwort
2. Erklaerung
3. Vorgehen in Excel
4. Hinweis / typische Fehlerquelle

## Typische Felder

- `portfolio`
- `monat`
- `jahr`
- `ze_ist`
- `ze_aktueller_plan`
- `ze_ursprungsplan`

## Grundregeln

- Felder, die in der Pivot nutzbar sein sollen, muessen in der Quelldatentabelle oder im Datenmodell vorhanden sein.
- Wenn Monate als Spalten vorliegen, ist Entpivotieren in Power Query oft die sauberste Loesung.
- Bei Monatswerten im Format `YYYY-MM` kann das Jahr mit `=WERT(LINKS([@Monat];4))` abgeleitet werden.
- Bei echten Datumswerten kann das Jahr mit `=JAHR([@Monat])` abgeleitet werden.

## Vorgehen bei unklarer Struktur

Frage knapp:

- Sind Monate Spalten oder Werte in einer Spalte?
- Arbeitest du direkt in Excel, Power Query oder Power BI?
- Soll das Ergebnis Filter, Zeilenfeld, Spaltenfeld oder Measure sein?
