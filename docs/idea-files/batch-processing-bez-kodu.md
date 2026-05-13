# Batch Processing bez kódu

> **Modul:** Modul 9
> Zpracujte 50–500 položek jedním promptem — přímo v Google Sheets nebo Excelu.

---

# Batch Processing bez kódu

Zpracujte 50-500 položek jedním promptem — přímo v Google Sheets nebo Excelu.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — help the user choose the right tool (Gemini in Google Sheets vs. Excel =COPILOT()), write the prompt, and plan the batch run.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — prepare the spreadsheet structure, draft prompts for each column, plan the test-and-scale approach.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — this is a no-code task. Help only if the user needs a script for pre-processing data before the spreadsheet step.

## The core idea

Většina lidí zpracovává data po jednom — kopíruje řádek do ChatGPT, čeká na odpověď, kopíruje zpět. To je jako ručně prát prádlo vedle pračky.

**Klíčový posun: jeden prompt, stovky výstupů.** Napíšete prompt jednou a spreadsheet ho aplikuje na každý řádek. Dva hlavní nástroje v květnu 2026:

### Google Sheets: Gemini v Google Sheets

- Nativní integrace — žádný add-on, funguje přímo v Sheets
- Funkce `=AI()` přímo v buňkách (Gemini 3 Flash/Pro pod kapotou)
- Gemini side panel: "Analyzuj tento sloupec", "Vytvoř souhrn", "Klasifikuj data"
- Help me organize: AI navrhne strukturu, formátování, formule
- Zdarma pro Google Workspace uživatele (AI Pro/Ultra pro pokročilé modely)
- Výhoda oproti add-onům: nativní, rychlejší, žádné API limity třetích stran

### Excel: =COPILOT() funkce

- Nativní funkce v Excelu (vyžaduje M365 Copilot licenci)
- `=COPILOT("Klasifikuj sentiment", A2:A201)` → jeden call, 200 výsledků
- Limit: 100 volání / 10 minut, 300 / hodinu
- **Klíčový trik:** Reference na celý range (A2:A201) = 1 volání. Tažení vzorce po řádcích = 200 volání → okamžitě narazíte na limit
- Agent Mode: "Analyzuj tento sheet a vytvoř PivotTable" — přirozený jazyk
- Model switcher: OpenAI GPT-5.2 nebo Claude Opus přímo v Excelu

## Architecture

### Vrstva 1: Příprava dat

- Sloupec A: surová data (feedback, emaily, popisy produktů, CVs...)
- Ujistěte se, že každý řádek je samostatná položka
- Žádné merged cells, žádné prázdné řádky uprostřed

### Vrstva 2: Prompt design

- Jeden jasný prompt per sloupec výstupu
- Příklady promptů:
 - "Shrň tento feedback jednou větou" → Sloupec B
 - "Klasifikuj sentiment: Positive / Negative / Neutral" → Sloupec C
 - "Extrahuj akční položky, vrať prázdné pokud žádné" → Sloupec D

### Vrstva 3: Test → Feedback → Scale

1. Spusť na 5 řádcích
2. Zkontroluj výstupy — jsou správné? konzistentní?
3. Uprav prompt podle chyb
4. Spusť na dalších 20
5. Teprve pak pusť na všechny

### Vrstva 4: Výstup a navazující akce

- Filtrujte / třiďte podle AI výstupů
- Pivot tabulka pro souhrn
- Conditional formatting pro vizuální přehled
- Export do dalšího systému (CRM, Slack, email)

## Operations

**Typické use cases:**

| Vstup | Prompt | Výstup |
|-------|--------|--------|
| Zákaznický feedback | "Klasifikuj sentiment a extrahuj hlavní bod" | Sentiment + shrnutí |
| Seznam firem | "Napiš personalizovaný cold email na 2 věty" | Outreach draft |
| Produktové popisy | "Přepiš pro SEO, max 160 znaků" | Meta descriptions |
| Meeting notes | "Extrahuj action items s deadlinem" | Task list |
| CVs / profily | "Ohodnoť fit na pozici X, 1-10 + důvod" | Scoring |

**Workflow v Google Sheets:**
```
=AI("Shrň tento zákaznický feedback jednou větou. Buď konkrétní.", A2)
```

**Workflow v Excelu:**
```
=COPILOT("Klasifikuj každý řádek jako Positive, Negative nebo Neutral", A2:A201)
```

## Tips and tricks

- **Array reference v Excelu šetří limity 200×.** `=COPILOT("prompt", A2:A201)` = 1 volání. Tažení formule = 200 volání. Microsoft to doporučuje oficiálně.
- **Gemini v Sheets je nativní = nejméně tření.** Žádný add-on, žádné API klíče, funguje out-of-the-box pro Google Workspace uživatele. Pro Google-first firmy jasná volba.
- **Iterativní prompt = klíč ke kvalitě.** Nikdy nepouštějte 500 řádků napoprvé. Vždy 5 → kontrola → oprava → 50 → kontrola → všechny.
- **Structured output pro konzistenci.** V promptu řekněte formát: "Odpověz POUZE jedním slovem: Positive / Negative / Neutral". Jinak dostanete "Tento feedback je spíše negativní, protože..."
- **Dva průchody pro komplexní úlohy.** Průchod 1: extrahuj strukturovaná data (JSON). Průchod 2: generuj výstupy z dat. Čistší než mega-prompt.
- **Nekombinujte víc úloh do jedné buňky.** Raději 3 sloupce (sentiment + shrnutí + akce) než jeden "udělej všechno najednou".

## Why this works

Spreadsheet je nejpřirozenější "batch runtime" pro knowledge workers — data už tam jsou, výstupy vidíte okamžitě, filtrování a třídění je nativní. AI jako funkce v buňce je mentálně přístupné i lidem, kteří nikdy nenapíší řádek kódu. S nativním Gemini v Google Sheets a =COPILOT() v Excelu to není experiment — je to mainstream workflow 2026.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context. Works with Google Sheets (nativní Gemini AI) or Microsoft Excel (=COPILOT() function + Agent Mode).
