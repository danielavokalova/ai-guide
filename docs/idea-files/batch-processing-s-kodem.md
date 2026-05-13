# ⚡ Batch Processing s kódem

> **Modul:** Modul 9
> 500 souborů, 200 dokumentů, nebo celou databázi? Nechte AI napsat script — vy jen popíšete, co chcete.

---

# Batch Processing s kódem (Vibe Coding)

Potřebujete zpracovat 500 souborů, vygenerovat 200 dokumentů, nebo transformovat celou databázi? Nechte AI napsat script — vy jen popíšete, co chcete.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — help the user popsat, co přesně chtějí zpracovat, navrhnout architekturu scriptu, a iterativně ho napsat.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — vytvořte plan: jaký vstup, jaký výstup, jaký model, jaký limit, jaký error handling. Pak napište script.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — build it. Python/Node script s API voláním na LLM, vstup z CSV/JSON/složky, výstup kam uživatel potřebuje.

## The core idea

Spreadsheet batch processing (=AI(), =COPILOT()) je skvělý pro jednoduché úlohy — klasifikaci, shrnutí, extrakci. Ale narazíte na limity:

- Chcete zpracovat PDF soubory, ne řádky v tabulce
- Potřebujete víc kroků za sebou (extract → transform → generate)
- Chcete výstup jako soubory, ne jako buňky
- Potřebujete pokročilý prompt s kontextem z více zdrojů
- Chcete kontrolu nad modelem, teplotou, structured output

**Klíčový insight: nemusíte umět programovat. Stačí popsat, co chcete, a AI vám script napíše.** Vibe coding = vy jste architekt, AI je programátor. Popíšete vstup, výstup, logiku — Cursor/Claude Code/Codex napíše funkční script za 10-30 minut.

Výsledek: místo ručního copy-paste spustíte jeden příkaz a za hodinu máte 500 zpracovaných výstupů.

## Architecture

### Vrstva 1: Vstup (co zpracovávám)

| Typ vstupu | Příklad | Jak script čte |
|------------|---------|----------------|
| CSV/Excel | Seznam zákazníků, produktů | pandas / csv modul |
| Složka souborů | 200 PDF faktur, 50 Word dokumentů | os.listdir + parser |
| API | CRM záznamy, databáze | requests / SDK |
| Webové stránky | 100 URL konkurentů | Firecrawl / requests |
| Databáze | SQL tabulka s 10k řádky | sqlalchemy / psycopg2 |

### Vrstva 2: Zpracování (co s tím dělám)

Každá položka prochází pipeline:
```
Vstup → [Pre-processing] → [LLM volání] → [Post-processing] → Výstup
```

Příklad pipeline pro faktury:
```
PDF soubor → extrakce textu (pdfplumber) → LLM: "extrahuj data" → JSON → zápis do CSV
```

Příklad pipeline pro personalizované emaily:
```
CSV řádek → enrichment (web search) → LLM: "napiš email" → markdown → uložit
```

### Vrstva 3: LLM volání

Script volá AI model přes API:
- **OpenAI API** (GPT-4o, GPT-4o-mini, o3-mini)
- **Anthropic API** (Claude Sonnet, Opus)
- **OpenRouter** (přístup ke všem modelům přes jedno API)
- **Lokální model** (Ollama pro citlivá data)

Klíčové parametry:
- Model (levný pro jednoduché, drahý pro complex)
- Temperature (0 pro fakta, 0.7 pro kreativní)
- Structured output (JSON schema pro konzistenci)
- Max tokens (limit délky odpovědi)

### Vrstva 4: Řízení běhu

- **Rate limiting:** pauza mezi requesty (API limity)
- **Retry logic:** pokud API selže, zkus znovu (3× s exponential backoff)
- **Checkpointing:** ukládej průběh, aby při pádu nemusel začínat znovu
- **Progress bar:** vidíte, kolik je hotovo (tqdm)
- **Cost tracking:** počítej tokeny, ukazuj celkovou cenu

### Vrstva 5: Výstup

| Typ výstupu | Kdy použít |
|-------------|-----------|
| CSV/Excel | Strukturovaná data, import do jiného systému |
| Složka souborů | Jeden soubor per položka (emaily, reporty, certifikáty) |
| Databáze | Velké objemy, navazující systémy |
| Google Sheet | Sdílení s týmem, manuální review |
| Slack/Email | Notifikace o dokončení + souhrn |

## Operations

**Jak na to — krok za krokem:**

**1. Popište svůj úkol AI (5 minut)**
```
Potřebuji zpracovat 300 zákaznických feedbacků z CSV souboru.
Pro každý feedback chci:
- Klasifikaci sentimentu (positive/negative/neutral)
- Shrnutí jednou větou
- Extrakci akčních položek (pokud jsou)

Vstup: feedback.csv (sloupec "text")
Výstup: results.csv (sloupce: original, sentiment, summary, actions)

Napiš mi Python script, který to udělá přes OpenAI API.
```

**2. AI napíše script (10-20 minut iterací)**
- AI navrhne architekturu
- Napíše první verzi
- Vy řeknete, co upravit ("přidej progress bar", "používej levnější model", "přidej retry")

**3. Test na 5 položkách (5 minut)**
```bash
python process.py --input feedback.csv --limit 5
```
Zkontrolujte výstupy. Pokud OK → spusťte na všechny.

**4. Spusťte na plný dataset (čekejte)**
```bash
python process.py --input feedback.csv
```
U 300 položek s GPT-4o-mini: ~5-10 minut, ~$0.50.

**Typické use cases:**

| Úkol | Vstup | Výstup | Čas scriptu | Cena běhu |
|------|-------|--------|-------------|-----------|
| Klasifikace feedbacku | 500 řádků CSV | CSV s kategoriemi | 15 min | $1-2 |
| Personalizované emaily | 200 kontaktů + enrichment | 200 .md souborů | 25 min | $3-5 |
| Extrakce z PDF faktur | 100 PDF souborů | Strukturovaný CSV | 20 min | $2-3 |
| Generování popisků produktů | 1000 produktů | CSV s titulky + popisky | 15 min | $5-10 |
| Certifikáty/diplomy | 50 jmen + dat | 50 HTML/PDF souborů | 20 min | $0.50 |
| Analýza konkurence | 20 URL | Report per konkurent | 30 min | $2-4 |

## Tips and tricks

- **Začněte s `--limit 5`.** NIKDY nespouštějte na celém datasetu napoprvé. Vždy 5 → kontrola → oprava promptu → 50 → kontrola → všechny.
- **GPT-4o-mini pro jednoduché, Sonnet/Opus pro complex.** Klasifikace sentimentu? Mini za $0.001/request. Psaní personalizovaných emailů? Sonnet za $0.01/request. Rozdíl v kvalitě je obrovský u kreativních úloh.
- **Structured output = konzistence.** Vždy definujte JSON schema pro výstup. Jinak dostanete pokaždé trochu jiný formát a parsing selže na řádku 47.
- **Checkpointing šetří peníze.** Pokud script spadne na řádku 150 z 500, nechcete začínat znovu. Ukládejte zpracované ID a přeskakujte je při restartu.
- **API klíče do `.env`, NIKDY do kódu.** Přidejte `.env` do `.gitignore`. Toto je bezpečnostní pravidlo #1.
- **OpenRouter jako pojistka.** Jedno API, přístup ke všem modelům. Pokud jeden provider má výpadek, přepnete na jiný bez změny kódu.
- **Paralelizace opatrně.** Asyncio/threading zrychlí 5-10×, ale narazíte na rate limity. Začněte sekvenčně, optimalizujte až když funguje.
- **Cost estimation před spuštěním.** Script by měl spočítat: "500 položek × ~800 tokenů = ~400k tokenů = ~$X. Pokračovat? [y/n]"

## Why this works

Spreadsheet batch (=AI(), =COPILOT()) je omezený na jednoduché operace uvnitř buňky. Jakmile potřebujete pracovat se soubory, kombinovat zdroje, řetězit kroky, nebo mít kontrolu nad parametry — potřebujete script.

Ale "napsat script" dnes neznamená "umět programovat". Znamená to umět **popsat, co chcete** — a to je dovednost, kterou už máte z promptování. Cursor/Claude Code/Codex vám napíše funkční pipeline za 15-30 minut. Vy jste architekt, AI je stavitel.

Výsledek: práce, která by jednomu člověku zabrala 3 dny ručního copy-paste, běží automaticky za hodinu. A script můžete spustit znovu příští měsíc — zdarma, okamžitě, bez práce.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context. Nástroje: Cursor, Claude Code, Codex, Windsurf, nebo jakýkoli AI coding assistant. Jazyk: Python (nejčastější pro data), Node.js (pro web/API), nebo cokoliv, co vám AI navrhne.
