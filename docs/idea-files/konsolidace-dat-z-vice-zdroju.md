# 🔗 Konsolidace dat z více zdrojů

> **Modul:** Modul 8
> AI sjednotí formáty, odstraní duplicity a propojí záznamy z různých systémů.

---

# Data Consolidation — Z chaosu jeden čistý dataset

Máš data na pěti místech v šesti formátech a nikdo nevidí celek. CRM, Excel, účetní export, emaily, PDF. Pomocí AI dáš všechno dohromady — sjednotíš formáty, odstraníš duplicity, doplníš chybějící propojení. Výsledek: jeden čistý dataset, se kterým můžeš pracovat dál.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — pomoz uživateli zmapovat, kde všude má data. Zeptej se, co chce propojit a jaký výsledek potřebuje. Navrhni postup: co exportovat, jak sjednotit, čím propojit.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — zmapuj datové zdroje, navrhni propojovací klíče, vytvoř sjednocený soubor ze zdrojů, které uživatel nahraje.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — postav skript, který vezme exporty z různých zdrojů, sjednotí formáty, propojí záznamy a vytvoří čistý výstup.

## The core idea

Každý druhý manažer nebo analytik řeší stejný problém: data jsou rozházená. CRM má zákazníky. Účetnictví má faktury. Banka má platby. Excel má budget. Emaily mají kontext. Každý systém vidí svůj kousek, ale nikdo nemá celý obrázek.

Tradičně to řešíš ručně: exportuješ z každého systému, otevřeš 3 Excely vedle sebe, kopíruješ, matchuješ přes VLOOKUP, čistíš duplicity. Pokaždé znovu, pokaždé hodiny.

**Klíčový insight: AI je nejlepší "lepidlo" na data. Popíšeš mu strukturu dvou souborů — a on je propojí. Sjednotí formáty, najde duplicity, navrhne propojovací klíče. Nepotřebuješ být datový inženýr. Potřebuješ vědět, co chceš dát dohromady.**

Tři úrovně konsolidace:

1. **Merge** — dva soubory se stejnou strukturou dát do jednoho (exporty za různé měsíce, pobočky, systémy)
2. **Join** — propojit záznamy z různých systémů přes společný klíč (zákazník z CRM + jeho faktury z účetnictví)
3. **Enrich** — obohatit existující data o informace z jiného zdroje (ke kontaktům přidat obraty, k produktům přidat feedbacky)

## Architecture

### 1. Inventura zdrojů (Source Map)

Než cokoliv propojuješ, zmapuj co máš. Pro každý zdroj:

- **Co tam je** — jaká data, jaké entity (zákazníci, fakturace, produkty)
- **Jaký formát** — Excel, CSV, PDF, API, ruční kopie
- **Jaký klíč** — čím se záznamy identifikují (email, IČO, ID, variabilní symbol)
- **Jak často se mění** — jednorázový export nebo živý zdroj

Příklad inventury:
- CRM (HubSpot): zákazníci, kontaktní osoby, dealy → export CSV, klíč = email
- Účetnictví (Pohoda): faktury, platby → CSV export, klíč = IČO + VS
- Banka (FIO): pohyby na účtu → CSV, klíč = variabilní symbol
- Excel: ruční tabulka s budgetem → soubor, klíč = název střediska

### 2. Párování a propojení (Join Logic)

Klíčová otázka: čím se záznamy z různých systémů párují?

Typické propojovací klíče:
- Email zákazníka → CRM + fakturace + komunikace
- IČO / DIČ → firmy napříč systémy
- Variabilní symbol → banka + fakturace
- Jméno + firma → fuzzy matching kde přesný klíč neexistuje
- Datum + částka → nouzové párování plateb

AI pomůže identifikovat klíče, i když nejsou dokonalé — umí fuzzy matching na jména firem, normalizaci emailů, rozpoznání variant názvů.

### 3. Čištění a sjednocení (Normalization)

Data z různých systémů mají různé formáty:

| Problém | Příklady |
|---------|----------|
| Datum | "1.4.2025" vs "2025-04-01" vs "April 1, 2025" |
| Částky | "1 234,50 Kč" vs "1234.50" vs "1 234,50 CZK" |
| Jména | "Jan Novák" vs "Novák Jan" vs "novak.jan" |
| Firmy | "Kofola a.s." vs "KOFOLA" vs "Kofola, a.s." |
| Prázdné hodnoty | prázdné vs "N/A" vs "0" vs "-" |
| Kódování | UTF-8 vs Windows-1250 vs ISO |

AI napíše pravidla normalizace — jednou nastavíš, pak běží automaticky.

### 4. Deduplikace (Dedup)

Po spojení dat se často objeví duplicity:
- Zákazník má dva emaily → dva záznamy v CRM
- Stejná firma s různými názvy → dvě entity
- Import ze dvou systémů vytvořil překryv

AI navrhne kandidáty na sloučení a nechá tě rozhodnout (nebo rozhodne sám s definovanými pravidly).

### 5. Výstup (Clean Output)

Sjednocená data v jednom souboru nebo na jednom místě:
- **CSV / Excel** — pro další práci, import jinam
- **Google Sheet** — pro sdílení a ruční editaci
- **Markdown tabulka** — pro kontext AI nástrojů
- **Databáze** — pro opakované dotazování

## Operations

### Operace 1: Rychlý merge dvou souborů (chat, 5 minut)

1. Nahraj dva soubory do AI: "Tady je export zákazníků z CRM a tady z účetnictví"
2. "Propoj tyto dva soubory přes email. Kde email nesedí, zkus matchovat přes název firmy."
3. AI spojí, sjednotí formáty, ukáže výsledek
4. Zkontroluj záznamy, které se nepodařilo spárovat

### Operace 2: Konsolidace z více zdrojů (chat/cowork, 20 minut)

1. Nahraj 3-5 exportů z různých systémů
2. Popiš, co v každém je a co chceš na výstupu: "Chci jednu tabulku zákazníků s obratem, počtem faktur a posledním kontaktem"
3. AI navrhne propojovací strategii
4. Iteruj: "Tyto dva záznamy jsou stejná firma" / "Přidej sloupec s kategorií"

### Operace 3: Automatizovaná pipeline (code)

1. AI napíše skript, který:
   - Načte exporty ze definovaných složek
   - Normalizuje formáty
   - Propojí přes definované klíče
   - Odstraní duplicity
   - Uloží čistý výstup
2. Příští měsíc: nové exporty → spustíš skript → hotovo

### Operace 4: Přidání nového zdroje

Máš fungující propojení tří systémů. Chceš přidat čtvrtý:
1. Zmapuj nový zdroj (co, jak, klíč)
2. AI rozšíří existující logiku o nový join
3. Ověříš na vzorku, pak spustíš na všechna data

## Tips and tricks

- **Začni dvěma zdroji, ne pěti.** Propoj nejdřív ty dva, které ti dají nejvíc hodnoty. Ověř, že to funguje. Pak přidávej.

- **Export je rychlejší než API.** Na prototypování je manuální export (CSV) rychlejší. API řeš až když víš, že propojovací logika funguje a chceš to automatizovat.

- **"Co se nespárovalo" je nejdůležitější tabulka.** Vždy si nech zobrazit záznamy, které se nepodařilo propojit. Odhalíš špatné klíče, duplicity, chybějící data.

- **Pozor na vícenásobné párování.** Zákazník se 2 emaily + 2 IČO = potenciálně 4 záznamy místo jednoho. Vždy kontroluj, jestli spojení nevytváří více záznamů, než bylo na vstupu.

- **Fuzzy matching funguje lépe, než čekáš.** AI umí "Kofola a.s." = "KOFOLA" = "Kofola, a.s." bez explicitních pravidel. Řekni: "Páruj přes název firmy, toleruj rozdíly ve velikosti písmen, právní formě a interpunkci."

- **Verzuj data.** Každý běh konsolidace ulož s datumem. Pokud se něco rozbije, chceš se vrátit k předchozí verzi.

- **Dokumentuj logiku.** Za měsíc si nebudeš pamatovat, proč pároval přes variabilní symbol a ne přes název. Nech AI napsat krátký README ke každému propojení.

## Why this works

Data v izolovaných systémech jsou jako puzzle rozházené po pěti krabicích. Každá krabice ukazuje kousek reality, ale nikdo nevidí celek. Otázky typu "kolik nám tento zákazník přinesl celkově?" jsou nezodpověditelné, protože obchod je v CRM a platby v účetnictví.

AI tento problém řeší, protože:
1. **Rozumí struktuře** — popíšeš mu dva soubory a pochopí, co v nich je
2. **Navrhne propojení** — identifikuje klíče, i nepřesné (fuzzy matching)
3. **Napíše transformaci** — sjednotí formáty, vyčistí, normalizuje
4. **Iteruje rychle** — něco nesedí → upravíš instrukci → znovu za sekundy

Výsledek: jednotný pohled na data za hodiny místo za týdny. A otázky, které byly dřív nezodpověditelné, mají najednou odpovědi.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context.
