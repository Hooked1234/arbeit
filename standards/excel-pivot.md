# Standard · Excel / Pivot / Power Query / Power BI

Für Datenaufbereitung und Auswertung. Erst Datenstruktur klären, dann konkrete
Schritte. Keine echten sensiblen Daten — mit anonymisierten Feldnamen arbeiten.

## Vorgehen (immer in dieser Reihenfolge)
1. **Datenform klären:** breite Tabelle, lange Tabelle, Pivot, Power-Query-Abfrage
   oder Datenmodell? Quelle und Granularität bestimmen.
2. **Ziel klären:** welche Kennzahl/Aggregation, welche Dimensionen, welcher Filter.
3. **Konkrete Schritte** nennen (Klickpfad oder Formel), nicht nur Theorie.
4. **Prüfen:** Liefert das Ergebnis plausible Werte? Edge Cases (leere/0/Duplikate)?

## Harte Regeln
- **Pivot-Felder müssen in der Quelltabelle oder im Datenmodell existieren** —
  ein Feld, das in der Pivot genutzt werden soll, vorher in der Quelle anlegen.
- **Deutsch-Excel-Funktionen** verwenden, wenn Felix Deutsch schreibt
  (z. B. `SUMMEWENNS`, `WENN`, `SVERWEIS`/`XVERWEIS`, `INDEX`/`VERGLEICH`).
- Für Modelle/Wachstum Power Query / Datenmodell bevorzugen statt verschachtelter
  Formeln über viele Zellen.

## Anonymisierte Beispiel-Feldnamen
`ze_ist`, `ze_aktueller_plan`, `ze_ursprungsplan`, `portfolio`, `monat`, `jahr`.
Für eigene Fälle analog abstrakte Feldnamen/Dummy-Werte verwenden.

## Ausgabeformat
- **Kurzantwort:** der konkrete Lösungsweg in 1–2 Sätzen.
- **Schritte/Formel:** nummeriert bzw. als kopierbare Formel.
- **Hinweis:** typische Fehlerquelle oder Alternative.

⟦Hier ergänzen: reale (anonymisierte) Tabellenschemata, Standardberichte, Measures.⟧
