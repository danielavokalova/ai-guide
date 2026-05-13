# ⚡ Batch Intelligence — hromadné zpracování

> **Modul:** Modul 8
> Systém projde stovky položek podle vašich pravidel a dá souhrnný výstup.

---

# Batch Intelligence — Hromadné zpracování desítek až tisíců položek

Máš 200 odpovědí z dotazníku, 500 tiketů zákaznické podpory, 100 faktur nebo 1000 řádků CRM dat. Ručně to neprojdeš. V chatu to nezpracuješ najednou. Potřebuješ systém, který projde každou položku, zpracuje ji podle tvých pravidel a dá ti souhrnný výstup. AI to zvládne — jen musíš zvolit správný nástroj podle objemu.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — pomoz uživateli definovat, co chce s daty dělat (extrakce, klasifikace, hodnocení, sumarizace). Navrhni postup a správný nástroj podle objemu. Pro malé vzorky zpracuj přímo v chatu.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — rozlož práci: definice pravidel → test na vzorku → zpracování celku → agregace výsledků. Zpracuj soubory ze složky postupně.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — postav pipeline, který projde všechny položky (soubory ve složce nebo řádky v tabulce), zavolá AI pro každou, a výsledky agreguje do souhrnného reportu.

## The core idea

Práce s jedním dokumentem nebo tabulkou je jednoduchá — hodíš to do chatu a zeptáš se. Ale co když máš 200 odpovědí z průzkumu? 500 tiketů? 1000 faktur? Chat má limit na velikost vstupu a tvůj čas má limit na manuální opakování.

**Klíčový insight: pro hromadné zpracování potřebuješ tři věci: (1) jasná pravidla co s každou položkou dělat, (2) správný nástroj podle objemu, (3) validaci na vzorku předtím, než to pustíš na celý dataset.**

Čtyři základní operace, které na objemu děláš:

1. **Extract** — z každé položky vytáhni konkrétní informace (schéma)
2. **Classify** — každou položku zařaď do kategorie (štítek)
3. **Score** — každou položku ohodnoť podle kritérií (rubric)
4. **Summarize** — z celku vytáhni vzorce, trendy, insighty (agregace)

## Architecture

### 1. Definice pravidel (Rules Layer)

Před zpracováním musíš přesně definovat, co AI s každou položkou udělá:

**Pro extrakci:** schéma s poli (viz Smart Extract idea file)
**Pro klasifikaci:** seznam kategorií + popis co do každé patří + příklady
**Pro hodnocení:** bodovací kritéria (rubric) se škálou a příklady pro každý stupeň
**Pro sumarizaci:** co hledáš (trendy, anomálie, opakující se témata, sentiment)

Příklad klasifikace zákaznických odpovědí:
- **Pozitivní** — zákazník je spokojený, chválí (příklad: "Výborná zkušenost")
- **Neutrální** — konstatuje fakt bez emocí (příklad: "Objednávka dorazila ve středu")
- **Negativní — řešitelné** — stížnost, kterou můžeme napravit (příklad: "Zboží přišlo pozdě")
- **Negativní — systémové** — opakující se problém, vyžaduje změnu procesu (příklad: "Už podruhé špatná faktura")

### 2. Volba nástroje (Tool Selection)

Klíčové rozhodnutí — jaký nástroj podle objemu:

| Objem | Nástroj | Jak to funguje |
|-------|---------|----------------|
| 1-5 položek | **Chat** (Claude, ChatGPT) | Nahraj všechno najednou, zpracuj v jedné konverzaci |
| 5-20 položek | **Cowork** (Claude Cowork) | Nahraj soubory do složky, Cowork je projde postupně |
| 20-200 položek | **Code + chat** (Cursor, Claude Code) | AI napíše skript, který položky projde a zavolá model přes API |
| 200+ položek | **API pipeline** (Python + Anthropic/OpenAI API) | Automatizovaný skript s paralelním voláním, error handling, logováním |

Pro API pipeline:
- **Anthropic API** — Claude modely, dobrý na analytiku a extrakci
- **OpenAI API** — GPT modely, široká podpora
- **OpenRouter** — přístup k více modelům přes jedno API, porovnání výsledků

### 3. Zpracovací vrstva (Processing Loop)

Pro každou položku:
1. Načti položku (soubor, řádek tabulky, text)
2. Pošli AI s definovanými pravidly
3. Zpracuj odpověď do strukturovaného formátu
4. Zapiš výsledek + případné chyby

Důležité parametry:
- **Batch size** — kolik položek zpracovat najednou (API limity, kontext window)
- **Error handling** — co dělat když zpracování jedné položky selže (přeskočit, retry, logovat)
- **Rate limiting** — nepřetížit API (pauzy mezi voláními)
- **Cost estimate** — kolik to bude stát (počet tokenů × cena per token)

### 4. Validační vrstva (Quality Gate)

Před zpracováním celého datasetu:
1. Spusť na 5-10 vzorcích
2. Ručně ověř výsledky — sedí klasifikace? Jsou extrahovaná data správná?
3. Pokud ne, uprav pravidla a znovu testuj
4. Až když vzorek sedí, pusť na celý dataset

Po zpracování celku:
- Zkontroluj náhodný vzorek 5-10% výsledků
- Podívej se na edge cases (nejkratší/nejdelší položky, prázdné, neočekávané)
- Ověř agregované statistiky (dávají čísla smysl?)

### 5. Agregační vrstva (Insights)

Z jednotlivých výsledků vytvoř souhrnný pohled:
- **Distribuce** — kolik položek v každé kategorii
- **Trendy** — co se opakuje, co je anomálie
- **Top/Bottom** — nejlepší a nejhorší podle skóre
- **Klíčové citace** — konkrétní příklady pro každou kategorii
- **Doporučení** — co s výsledky dělat

## Operations

### Operace 1: Hromadná klasifikace (dotazníky, feedbacky)

1. Definuj kategorie + příklady
2. Otestuj na 5 odpovědích v chatu
3. Pusť na celý dataset (Cowork nebo skript)
4. Výstup: tabulka s kategorií per odpověď + souhrnný report

**Příklad:** 200 odpovědí z průzkumu → 5 kategorií (spokojený, neutrální, nespokojený-řešitelný, nespokojený-systémový, nerelevantní) → "62% spokojených, 15% systémových problémů v oblasti dodání"

### Operace 2: Hromadná extrakce (faktury, smlouvy)

1. Definuj schéma (viz Smart Extract)
2. Otestuj na 3 dokumentech v chatu
3. Zpracuj složku dokumentů skriptem
4. Výstup: jedna tabulka, řádek per dokument

**Příklad:** 50 faktur → tabulka: dodavatel, částka, DPH, splatnost, VS → import do účetního systému

### Operace 3: Hromadné hodnocení (quality audit)

1. Definuj scoring rubric (kritéria, škála, váhy, příklady)
2. Kalibruj na 5-10 záznamech (porovnej AI skóre s tvým)
3. Pusť na celý dataset
4. Výstup: skóre per záznam + souhrnný report (průměr, distribuce, nejslabší oblasti)

**Příklad:** 100 tiketů zákaznické podpory → hodnocení kvality odpovědí (empatie, rychlost, řešení) → "průměr 3.8/5, nejslabší oblast: proaktivní nabídka řešení"

### Operace 4: Trend analýza z velkého objemu textu

1. Řekni AI: "Projdi všechny odpovědi a identifikuj opakující se témata, vzorce a anomálie"
2. AI projde, kategorizuje a agreguje
3. Výstup: "Top 5 témat, 3 nové trendy oproti minulému období, 2 červené vlajky"

## Tips and tricks

- **Vždy testuj na vzorku.** Nikdy nepouštěj batch bez ruční validace 5-10 položek. Špatná pravidla × 500 položek = 500 špatných výsledků.

- **Náklady spočítej předem.** 500 dokumentů × průměrně 2000 tokenů × cena per token = X dolarů. Pro Claude Sonnet je to řádově $1-5 za 500 dokumentů. Pro Opus víc. Kalkuluj.

- **Začni s levnějším modelem.** Pro klasifikaci a jednoduchou extrakci stačí menší model (Haiku, GPT-4o-mini). Větší model nasaď jen tam, kde kvalita nestačí.

- **Paralelizuj opatrně.** API má rate limity. 10 paralelních volání je OK, 100 najednou pravděpodobně dostaneš 429 error. Přidej retry logiku.

- **Loguj všechno.** Každý API call ulož — vstup, výstup, čas, cena. Když se něco rozbije, chceš vědět kde a proč.

- **Rubric je 80% úspěchu.** U hodnocení platí: čas investovaný do definice kritérií a příkladů se vrátí stonásobně. Špatný rubric = nekonzistentní výsledky.

- **Kombinuj operace.** Nejdřív klasifikuj (rozděl do skupin), pak pro každou skupinu extrahuj jiná pole. Efektivnější než jedna složitá operace na všem.

- **Porovnávej modely.** Pro důležitý batch pusť 20 položek přes 2-3 modely a porovnej kvalitu. Někdy levnější model dává stejné výsledky.

## Why this works

Lidé jsou špatní na repetitivní úkoly ve velkém měřítku. Po 20 dokumentech klesá pozornost. Po 50 začínáš podvědomě zrychlovat a zjednodušovat. A dvě různé osoby klasifikují stejný dokument jinak.

AI tento problém nemá:
1. **Konzistence** — 500. položku zpracuje stejně pečlivě jako 1.
2. **Rychlost** — 500 položek za minuty, ne za dny
3. **Transparentnost** — ke každému výsledku napíše zdůvodnění
4. **Škálovatelnost** — od 10 po 10 000 bez změny přístupu
5. **Cenová efektivita** — $1-5 za 500 dokumentů vs hodiny lidské práce

Klíčem je kvalita pravidel na vstupu. AI je výkonný motor — ale potřebuje dobré instrukce. Investuj čas do definice pravidel a validace na vzorku. Zbytek se škáluje sám.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context.
