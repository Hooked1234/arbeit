# Workspace · Felix (HSBA / EOS)

Gemeinsames Arbeitsgedächtnis für KI-Agenten (**Claude Code** und **Codex**).
Ziel: **Kein Chat startet bei null.** Die Agenten lesen hier, *wie* Felix
arbeitet, *welche* Standards gelten und *welche* Entscheidungen schon getroffen
sind. Andere Tools nur auf ausdrücklichen Wunsch.

## Architektur (3 Schichten + Steuerung)

```text
Steuerung   AGENTS.md (Codex) / CLAUDE.md (Claude)  → eine Routing-Tabelle
   │
   ├─ WAS    templates/   strukturelle Vorlagen (Gliederung, Ablauf)
   ├─ WIE    standards/   Quelle der Wahrheit: Design-Tokens & harte Regeln
   └─ TRIGGER skills/      schlanke Auslöser (Frontmatter) → laden Standard+Template
```

Du sagst nur *was* — der Workspace liefert das *wie*. Beide Agenten nutzen
dieselbe Routing-Tabelle (`AGENTS.md` §1).

## Struktur

```text
/
├── README.md            # dieser Überblick
├── AGENTS.md            # Hauptanweisung Codex (+ gemeinsame Routing-Tabelle)
├── CLAUDE.md            # Hauptanweisung Claude (verweist auf dieselbe Logik)
├── WORKLOG.md           # laufende Änderungen und Entscheidungen
├── NEXT_STEPS.md        # offene Aufgaben + nächster sinnvoller Schritt
├── CHANGELOG.md         # abgeschlossene größere Änderungen
├── standards/           # WIE: Design-Tokens, harte Regeln pro Aufgabentyp
├── templates/           # WAS: strukturelle Vorlagen (hsba / eos / allgemein)
├── skills/              # Auslöser je Aufgabentyp (für Codex sichtbar)
├── .claude/skills/      # identische Auslöser mit Frontmatter (Claude-Autotrigger)
├── agents/              # spezialisierte Rollen (qualitaetspruefer)
├── .claude/agents/      # Claude-Spiegelung der Agenten
├── context/             # Wer ist Felix, EOS, HSBA — Arbeitsweise & Tonalität
└── decisions/           # Entscheidungs-Logbuch — was gilt, warum
```

## Routing (Kurzfassung)

| Felix sagt …          | Standard (Wie)                      |
|------------------------|-------------------------------------|
| „HSBA-Präsentation"    | `standards/praesentation-hsba.md`   |
| „EOS-Präsentation"     | `standards/praesentation-eos.md`    |
| „Akademischer Text"    | `standards/schreiben-akademisch.md` |
| „Projektanweisung"     | `standards/projektanweisung.md`     |
| „E-Mail"               | `standards/email.md`                |
| „Dokumentprüfung"      | `standards/dokumentpruefung.md`     |
| „Excel / Pivot / BI"   | `standards/excel-pivot.md`          |
| „KI-Dokument"          | `standards/ki-dokument.md`          |

Vollständige Tabelle mit Templates & Auslösern: `AGENTS.md` §1.

## Nutzung

1. Diesen Ordner als Projekt-Wurzel ablegen.
2. Claude Code / Codex im Ordner starten → `CLAUDE.md` / `AGENTS.md` laden automatisch.
3. **`⟦…⟧`-Platzhalter** in den `standards/`-Dateien an echte Vorgaben anpassen —
   v. a. exakte Farb-Codes, Markenschrift, Logo-Pfade.

## Erweitern

Neuer wiederkehrender Aufgabentyp?
1. `standards/<aufgabe>.md` anlegen (bestehende Datei als Vorlage).
2. Optional `templates/<…>.md` für die Struktur.
3. Schlanken Auslöser in `skills/<aufgabe>/SKILL.md` **und**
   `.claude/skills/<aufgabe>/SKILL.md` ergänzen (Frontmatter + Verweis auf Standard).
4. Zeile in der Routing-Tabelle (`AGENTS.md` §1) ergänzen.

## Grundprinzip

Gemeinsamer Kontext entsteht über **Dateien**, nicht über geteiltes Chat-Gedächtnis.
Vor Änderungen lesen & verstehen, nichts Unbekanntes überschreiben, nichts ohne
Auftrag löschen. Übergabe-Disziplin: `WORKLOG.md` / `NEXT_STEPS.md` / `CHANGELOG.md`.
