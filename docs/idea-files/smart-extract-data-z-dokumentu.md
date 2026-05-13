# Smart Extract — data z dokumentů

> **Modul:** Modul 8
> Definujete schéma, AI extrahuje přesně to, co chcete ze smluv, faktur nebo zápisů.

---

# Smart Extract — Strukturovaná data z dokumentů

Máš dokument — smlouvu, fakturu, zápis ze schůzky, analýzu, legislativu — a potřebuješ z něj vytáhnout konkrétní informace. Ne "shrnutí." Konkrétní pole v konkrétním formátu. Definuješ schéma předem, AI extrahuje přesně to, co chceš. Funguje na 1-10 dokumentů v chatu, bez skriptování.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — pomoz uživateli definovat schéma extrakce. Zeptej se, jaký dokument zpracovává a jaká pole potřebuje. Navrhni strukturu výstupu, extrahuj data, vrať jako tabulku.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — vytvoř workflow: definice schématu → test na jednom dokumentu → zpracování zbytku → export do tabulky.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — pro 1-10 dokumentů stačí chat. Pokud uživatel potřebuje víc, nasměruj ho na Batch Intelligence idea file.

## The core idea

Většina lidí dělá s dokumenty jednu ze dvou věcí:
- **Čtou celé** — 30 stránek smlouvy kvůli 5 klíčovým údajům
- **"Shrň mi to"** — dostanou volný text, hezký na přečtení, ale nepoužitelný dál

Obojí je neefektivní.

**Klíčový insight: nedávej AI volnou ruku. Definuj schéma předem — řekni přesně, jaká pole chceš, v jakém formátu, s jakými pravidly. AI pak funguje jako precizní extraktor, ne jako neřízený sumarizátor.**

Rozdíl:

- "Shrň mi tuhle smlouvu" → 5 odstavců volného textu
- "Z této smlouvy vytáhni: strany, předmět, částka, datum podpisu, výpovědní lhůta, sankce" → tabulka s konkrétními hodnotami

Schema-first přístup znamená: nejdřív řekneš CO chceš, pak dáš AI dokument. Ne naopak.

## Architecture

### 1. Schéma (Schema Layer)

Definice toho, co chceš vytáhnout. Pro každé pole:

- **Název** — co to je (např. "datum_splatnosti")
- **Typ** — text, číslo, datum, boolean, seznam
- **Pravidla** — formát, co dělat když chybí
- **Příklad** — ukázka správné hodnoty

Typická schémata podle typu dokumentu:

**Smlouvy:** strany (kdo s kým), předmět, částka, datum podpisu, termín plnění, sankce, výpovědní lhůta, rozhodné právo

**Faktury:** dodavatel, IČO, částka bez DPH, DPH, celkem, datum vystavení, datum splatnosti, variabilní symbol

**Meeting zápisy:** datum, účastníci, rozhodnutí, úkoly (kdo + co + deadline), otevřené otázky

**Legislativa / výzvy:** číslo předpisu, datum účinnosti, dotčené subjekty, klíčové povinnosti, termíny, sankce za nesplnění

**Výzkumné rozhovory:** respondent, klíčové citace, hlavní témata, sentiment, doporučení

### 2. Extrakce (Extraction Layer)

AI dostane dokument + schéma a pro každé pole:
- Najde relevantní pasáž v dokumentu
- Extrahuje hodnotu ve správném formátu
- Pokud pole nelze najít, zapíše "N/A" (nevymýšlí si)

Výstup: tabulka, kde řádek = dokument, sloupce = pole ze schématu.

### 3. Validace (Validation Layer)

Po extrakci rychlá kontrola:
- Jsou povinná pole vyplněná?
- Sedí formáty (datum jako datum, číslo jako číslo)?
- Dávají hodnoty smysl (částka není záporná, datum není z roku 1900)?
- Jsou ve vzájemné konzistenci (částka bez DPH + DPH = celkem)?

### 4. Výstup (Output Layer)

- **Tabulka v chatu** — pro rychlý přehled
- **CSV / Excel** — pro další zpracování
- **Markdown** — pro vložení do druhého mozku / kontextu
- **Strukturovaný text** — pro email kolegovi

## Operations

### Operace 1: Jeden dokument (2 minuty)

1. Nahraj dokument do AI
2. Řekni: "Z tohoto dokumentu vytáhni: [seznam polí]. Výstup jako tabulku."
3. Hotovo

Doslova to je. Pro jednotlivý dokument není potřeba nic víc.

### Operace 2: Sada dokumentů stejného typu (10 minut)

1. Nahraj 3-5 dokumentů (např. 5 smluv od různých dodavatelů)
2. Definuj schéma jednou: "Z každé smlouvy vytáhni: strany, částka, termín, sankce"
3. AI zpracuje všechny a vrátí jednu tabulku — řádek per dokument

### Operace 3: Iterativní zpřesňování (15 minut)

1. Začni jedním dokumentem a jednoduchým schématem
2. Podívej se na výstup — chybí ti něco? Je něco nepřesné?
3. Upřesni: "Přidej pole 'garanční lhůta'" / "U částky rozliš měnu" / "U sankcí uveď konkrétní procento"
4. Opakuj dokud výstup přesně odpovídá tomu, co potřebuješ
5. Uložené schéma použij na další dokumenty

### Operace 4: Porovnání dokumentů

1. Nahraj dvě verze stejného dokumentu (např. smlouva + dodatek)
2. "Porovnej tyto dva dokumenty. Co se změnilo? Výstup jako tabulku: pole | původní | nové."
3. AI identifikuje rozdíly — užitečné pro review smluv, legislativních změn, aktualizací

## Tips and tricks

- **Schéma definuj na konkrétním příkladu.** Nepiš schéma od stolu. Otevři reálný dokument, projdi ho, a zapiš pole, která bys normálně ručně vypisoval.

- **Buď explicitní ohledně chybějících hodnot.** Řekni: "Pokud pole nelze najít, napiš 'N/A' — nevymýšlej si." Bez toho má AI tendenci hádat.

- **PDF ≠ PDF.** Skenovaný dokument (obrázek) potřebuje OCR. Nativní PDF (text) se zpracuje přímo. Test: otevři PDF a zkus text označit myší. Pokud nejde, je to sken.

- **Čím specifičtější schéma, tím lepší výsledky.** "Důležité informace" → špatné. "Dodavatel, IČO, částka bez DPH, DPH, celkem, datum splatnosti, variabilní symbol" → výborné.

- **U prvního dokumentu validuj ručně.** Ověř 3-4 vytažené hodnoty proti originálu. Hlavně u čísel a dat — AI občas přehodí řádky tabulky nebo špatně přečte formátování.

- **Schéma je znovupoužitelné.** Jednou definuješ schéma pro typ dokumentu (smlouva, faktura, zápis). Pak ho použiješ na každý další dokument stejného typu. Ulož si ho.

- **Pro víc než 10 dokumentů přejdi na Batch Intelligence.** Chat zvládne pohodlně do 10 dokumentů. Nad to potřebuješ skript nebo API — viz idea file Batch Intelligence.

## Why this works

Dokumenty jsou kontejnery na informace. Problém není "jak přečíst PDF" — problém je "jak z 30stránkového dokumentu vytáhnout 5 faktů, aniž bych ho celý četl."

Schema-first přístup funguje, protože:
1. **Eliminuje šum.** AI nečte celý dokument "od A do Z" — hledá konkrétní informace
2. **Zajistí konzistenci.** Každý dokument je zpracován stejně, se stejnými poli
3. **Umožní další práci.** Strukturovaná data (tabulka) můžeš filtrovat, řadit, porovnávat, vizualizovat — volný text ne
4. **Šetří čas exponenciálně.** 1. dokument: 2 minuty (místo 20 minut čtení). 5. dokument: stále 2 minuty. 50 minut ušetřených na 5 dokumentech.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context.
