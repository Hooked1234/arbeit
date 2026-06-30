# AGENTS.md — Hauptanweisung (Codex)

> Wird von Codex automatisch geladen. Claude nutzt `CLAUDE.md`.
> Beide Agenten teilen dieselbe Steuerlogik: **Routing-Tabelle unten → passende
> `standards/`-Datei laden → erst dann arbeiten.** Inhalt liegt in `standards/`,
> Struktur in `templates/`, Auslöser in `skills/`.

## 0 · Immer gültig

- **Sprache:** Deutsch (Code-Bezeichner/Kommentare Englisch erlaubt).
- **Stil:** Knapp, präzise, direkt. Ergebnis vor Erklärung, kein Fülltext.
- **Fakten/Annahmen/Offenes** sauber trennen. Spekulation als Annahme markieren.
- **Umsetzung vor Theorie.** Kein Plan verlangt → direkt umsetzen. Nur bei
  ergebnisverfälschender Unsicherheit kurz nachfragen.
- **Kontext zuerst:** Bei Personen-/Org-Bezug `context/` lesen
  (`felix.md`, `eos.md`, `hsba.md`).
- **Datenschutz:** Keine echten Kunden-, Personen-, Vertrags-, Bank-, Bonitäts-,
  Scoring- oder Zugangsdaten anfordern. Mit anonymisierten Feldnamen/Dummy-Werten
  arbeiten. Keine internen Richtlinien erfinden.

## 1 · Aufgaben-Routing (gemeinsam mit CLAUDE.md)

Aufgabentyp aus Felix' Formulierung bestimmen, Standard laden. Mehrere Treffer →
alle laden; bei Folien hat die Präsentations-Standarddatei Layout-Vorrang.

| Auslöser (Stichwörter)                                    | Standard (Wie)                      | Template (Was)                          |
|-----------------------------------------------------------|-------------------------------------|-----------------------------------------|
| „HSBA-Präsentation", „Uni-Folien", „Praxisbericht-Slides" | `standards/praesentation-hsba.md`   | `templates/hsba/hsba-praesentation.md`  |
| „EOS-Präsentation", „Firmen-Folien", „Pitch"              | `standards/praesentation-eos.md`    | `templates/eos/eos-praesentation.md`    |
| „Akademischer Text", „Bericht", „Hausarbeit", „Zitieren"  | `standards/schreiben-akademisch.md` | `templates/hsba/hsba-textschreiben.md`  |
| „Projektanweisung", „Arbeitsauftrag definieren"           | `standards/projektanweisung.md`     | `templates/allgemein/projektanweisung.md` |
| „E-Mail", „Mail an …", „Anschreiben"                      | `standards/email.md`                | `templates/allgemein/kurze-email.md`    |
| „Dokumentprüfung", „Korrektur", „Review", „gegenlesen"    | `standards/dokumentpruefung.md`     | `templates/allgemein/dokumentpruefung.md` |
| „Excel", „Pivot", „Power Query", „Power BI"               | `standards/excel-pivot.md`          | —                                       |
| „KI-Dokument", „KI-Nutzung dokumentieren", „Prompt-Log"   | `standards/ki-dokument.md`          | `templates/allgemein/ki-dokument.md`    |

Kein Treffer → Aufgabentyp kurz erfragen *oder* generisch nach (0) arbeiten.

## 2 · Ablauf pro Auftrag

1. Aufgabentyp erkennen → `standards/`-Datei laden (+ ggf. Template).
2. Bei Org-Bezug zusätzlich `context/`-Datei laden.
3. Regeln strikt anwenden (Tokens: Farben, Schrift, Layout, Ton).
4. Neue verbindliche Festlegung → `decisions/decisions.md` ergänzen.
5. Nach relevanter Änderung → `WORKLOG.md` (+ ggf. `NEXT_STEPS.md` / `CHANGELOG.md`).

## 3 · Rollen (Orientierung, keine harte Grenze)

Codex eignet sich für: Datei-/Ordnerstruktur, Skills technisch vorbereiten,
README/AGENTS/CLAUDE pflegen, Versionierung.
Claude eignet sich für: längere Textarbeit, Stil-/Präsentationslogik,
konzeptionelle Ausarbeitung, Skill-Inhalte formulieren.

## 4 · Zusammenarbeit & Git

- Vor Änderung: bestehende Dateien lesen, Stand verstehen, **nichts Unbekanntes
  überschreiben**, nichts ohne Auftrag löschen, Änderungen eng am Ziel halten.
- Konflikt (Datei seit letztem Stand geändert): nicht überschreiben, erst Diff
  prüfen, gezielt ergänzen, bei Unklarheit nachfragen.
- Git nur über `gitw` (siehe Datei). Kein `git reset --hard`, kein Force-Push,
  keine fremden Änderungen zurücksetzen. Commit-Vorschläge nur auf Wunsch.
