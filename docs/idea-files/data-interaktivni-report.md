# 📊 Data → Interaktivní report

> **Modul:** Modul 8
> Z jakýchkoli dat vytvoříte interaktivní HTML report s grafy a přehlednou hierarchií.

---

# Data → Interactive Report

Z jakýchkoli dat vytvoříš interaktivní HTML report — s grafy, přehlednou hierarchií a možností proklikávat se do detailů. AI nejdřív zanalyzuje typ dat, zvolí vhodné vizualizace a postaví report s dobrou informační architekturou. Výsledek vypadá profesionálně, bez řádky kódu od tebe.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — uživatel ti dá data (tabulku, CSV, JSON, copy-paste). Nejdřív analyzuj strukturu a navrhni, jaké vizualizace dávají smysl. Pak vytvoř interaktivní HTML report s grafy a přehlednou hierarchií.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — analyzuj data, navrhni strukturu reportu (sekce, grafy, drill-down), vytvoř HTML soubor s inline styly a Chart.js nebo podobnou knihovnou.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — načti data, proveď exploratory analýzu, zvol vhodné vizualizace, postav kompletní interaktivní HTML report. Použij moderní design, tmavý nebo světlý theme, responsivní layout.

## The core idea

Každý má data, ze kterých potřebuje report. Prodejní čísla, finanční výsledky, HR metriky, zákaznické chování, výsledky kampaně. Tradičně to znamená: otevřít Excel → pivot tabulka → graf → zkopírovat do PowerPointu → hodina práce na něco, co vypadá průměrně.

**Klíčový insight: AI nemusí jen odpovídat na otázky o datech. Může z nich rovnou postavit kompletní interaktivní report — s grafy, tabulkami, filtry a drill-down sekcemi. A může to udělat chytře: nejdřív analyzuje, co v datech je, a pak zvolí vizualizace, které dávají smysl pro daný typ dat.**

Tři věci dělají tento přístup jiným než "hoď data do Excelu a udělej graf":

1. **AI jako analytik + designér.** Nepřekládáš data do grafů ty — AI samo navrhne, co vizualizovat a jak. Časové řady → line chart. Kategorie → bar chart. Distribuce → histogram. Proporce → donut. AI volí, ne ty.

2. **Informační hierarchie.** Nejdůležitější čísla nahoře, velká, jasná. Detaily schované za kliknutím. Management vidí executive summary, analytik si proklikne do detailu. Jeden report, dvě úrovně.

3. **HTML = univerzální formát.** Otevřeš v prohlížeči, pošleš kolegovi jako odkaz nebo soubor, funguje na mobilu i na projektoru. Žádný PowerPoint, žádné sdílené přístupy, žádné licence.

## Architecture

### 1. Vstupní vrstva (Data Input)

Co všechno může být vstupem:
- Excel / CSV / Google Sheet — nejběžnější
- JSON — exporty z API, konfigurací
- Copy-paste z webu nebo emailu
- Screenshot tabulky — AI přečte i obrázek (méně spolehlivé, ale funguje)
- Kombinace — "tady je tabulka z CRM a tady budget z Excelu"

AI nejdřív potřebuje pochopit, co dostal: kolik řádků, jaké sloupce, jaké typy (čísla, texty, datumy, kategorie), co data pravděpodobně reprezentují.

### 2. Analytická vrstva (Auto-Analysis)

AI provede automatickou analýzu předtím, než cokoliv vizualizuje:

- **Struktura** — jaké entity data popisují (zákazníci? transakce? měsíce?)
- **Klíčové metriky** — co jsou hlavní čísla (revenue, count, average, %)
- **Dimenze** — podle čeho se dá rozřezávat (čas, region, kategorie, osoba)
- **Zajímavosti** — trendy, outliers, anomálie, korelace
- **Doporučení** — jaké vizualizace dávají smysl a proč

### 3. Vizualizační vrstva (Chart Selection)

Na základě analýzy AI zvolí vhodné typy grafů:

| Typ dat | Vizualizace |
|---------|-------------|
| Vývoj v čase | Line chart, area chart |
| Srovnání kategorií | Bar chart (horizontal/vertical) |
| Proporce celku | Donut chart, stacked bar |
| Distribuce | Histogram, box plot |
| Vztah dvou proměnných | Scatter plot |
| Geografická data | Tabulka se zvýrazněním, heat map |
| KPI / headline čísla | Velké karty s delta (↑↓) |

Klíčové: AI nevolí "nejhezčí" graf. Volí ten, který **nejlíp komunikuje insight**.

### 4. Vrstva informační hierarchie (Layout)

Report není plochý seznam grafů. Má strukturu:

- **Level 0 — Executive summary.** 3-5 hlavních čísel jako velké karty. Jedno shrnutí v přirozené řeči. "Revenue +12% MoM, margin pod tlakem kvůli Q2 slevám."
- **Level 1 — Sekce s grafy.** Každá sekce = jeden pohled na data (revenue, zákazníci, produkty). Graf + stručný komentář.
- **Level 2 — Detaily na klik.** Tabulka s jednotlivými záznamy, filtrování, rozbalení. Schované defaultně — vidí je jen ten, kdo chce jít hlouběji.

### 5. Výstupní vrstva (HTML Output)

Jeden HTML soubor, který obsahuje všechno:
- Inline CSS (moderní design, responsivní)
- Grafy (Chart.js nebo inline SVG)
- Interaktivní prvky (expandable sekce, tabs, filtry)
- Žádné externí závislosti (nebo s CDN)

## Operations

### Operace 1: Quick report z jedné tabulky (chat, 5 minut)

1. Nahraj tabulku do AI
2. "Podívej se na ta data a udělej mi z nich interaktivní HTML report. Zvol vhodné grafy, přidej executive summary a umožni prokliknutí do detailů."
3. AI analyzuje, zvolí vizualizace, vygeneruje HTML
4. Otevřeš v prohlížeči — hotovo

### Operace 2: Report na míru (chat/code, 15 minut)

1. Nahraj data + řekni, co chceš vidět: "Zaměř se na vývoj revenue per region a identifikuj top 10 zákazníků"
2. AI vytvoří report zaměřený na tvé priority
3. Iteruješ: "Přidej srovnání s loňským rokem" / "Změň barvy na firemní" / "Přidej filtr po měsících"

### Operace 3: Dashboard z více zdrojů (code, 30 minut)

1. Nahraj víc souborů: "Tady je P&L, tady pipeline, tady headcount"
2. AI propojí data a vytvoří multi-section dashboard
3. Každá sekce má vlastní vizualizace, ale celkový design je konzistentní

### Operace 4: Opakovaný report (šablona)

1. Vytvoříš report jednou
2. Příští měsíc nahraješ nová data: "Tady jsou data za květen, vygeneruj report ve stejné struktuře jako minule"
3. AI zachová strukturu, aktualizuje čísla, napíše nový komentář

## Tips and tricks

- **"Udělej mi z toho report" je silnější než "analyzuj."** Když řekneš "analyzuj," dostaneš text. Když řekneš "udělej interaktivní HTML report," dostaneš vizuální výstup, který můžeš rovnou poslat dál.

- **Řekni, pro koho je report.** "Pro management" = stručné, velká čísla, doporučení. "Pro tým" = detailní, breakdown, akční kroky. "Pro mě" = explorativní, všechny grafy, raw data k dispozici.

- **Nech AI navrhnout vizualizace.** Neříkej "udělej mi pie chart." Řekni "zvol vhodné vizualizace pro tato data." AI často vybere lepší formát, než bys vybral sám.

- **Informační hierarchie je klíč.** Řekni: "Nejdůležitější čísla nahoře, detaily na klik." Šéf čte 30 sekund — musí vidět pointu hned. Analytik si proklikne detail.

- **Iteruj design.** První verze nebude dokonalá. "Změň font na systémový" / "Tmavší pozadí" / "Přidej logo" — každá iterace zabere 30 sekund.

- **Validuj čísla.** U prvního reportu ověř 3-4 čísla ručně. Hlavně součty a procenta — AI občas špatně agreguje přes kategorie.

- **HTML > PowerPoint.** HTML report je interaktivní, sdílí se jako soubor nebo odkaz, funguje na jakémkoli zařízení, nevyžaduje licence. A vypadá líp.

## Why this works

Data bez vizualizace jsou jen čísla. Čísla bez kontextu jsou šum. Vizualizace bez hierarchie je kaše grafů.

AI řeší všechny tři problémy najednou:
1. **Přečte data** a pochopí, co v nich je — rychleji a důkladněji než člověk na prvním průchodu
2. **Zvolí vizualizace** podle typu dat — ne podle toho, co umíš v Excelu
3. **Postaví hierarchii** — důležité nahoře, detail na klik, komentář u každé sekce

Výsledek: místo hodiny v Excelu máš za 5 minut profesionální interaktivní report, který můžeš rovnou sdílet. A příští měsíc ho vygeneruješ znovu za 2 minuty.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context.
