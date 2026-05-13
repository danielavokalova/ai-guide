# 🧭 Jak Designovat AI Automatizaci

> **Modul:** Modul 9
> Rozhodovací framework: kdy uložený prompt, kdy orchestrace, kdy vibe coding.

---

# Jak Designovat AI Automatizaci

Rozhodovací framework: kdy uložený prompt, kdy orchestrace, kdy vibe coding — a 5 pravidel, která vás ochrání před nejčastějšími chybami.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — help the user identifikovat jejich opakované úkoly, zvolit správnou úroveň automatizace, a navrhnout první kroky.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — vytvořte rozhodovací dokument pro tým: které procesy automatizovat, jak, a v jakém pořadí.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — toto není coding task. Pomozte jen pokud uživatel potřebuje implementovat zvolenou automatizaci.

## The core idea

Největší chyba v AI automatizaci není špatný nástroj — je to **automatizace špatné věci, nebo na špatné úrovni**. Někdy stačí uložený prompt. Někdy potřebujete orchestrační platformu. Někdy je nejlepší odpověď "počkej měsíc".

**Klíčový framework: 4 úrovně × 5 pravidel.** Zvolte úroveň podle complexity a frekvence. Pak aplikujte 5 pravidel, která odliší úspěšnou automatizaci od té, co tiše selhává.

## Architecture

### 4 úrovně automatizace (od jednoduché po pokročilou)

```
┌─────────────────────────────────────────────────────────────────┐
│ ÚROVEŇ 4: Vibe Coding                                          │
│ Cursor 3, Claude Code, Codex                                    │
│ → Vlastní nástroje, scripty, aplikace                           │
├─────────────────────────────────────────────────────────────────┤
│ ÚROVEŇ 3: Vestavěné funkce AI nástrojů                         │
│ Claude Routines, Cursor Agents, ChatGPT Tasks                   │
│ → Autonomní agenti uvnitř nástrojů, které už používáte          │
├─────────────────────────────────────────────────────────────────┤
│ ÚROVEŇ 2: Orchestrační platformy                               │
│ Make, n8n, Relay.app, Power Automate                            │
│ → Propojení systémů, workflow s AI krokem                       │
├─────────────────────────────────────────────────────────────────┤
│ ÚROVEŇ 1: Polo-automatizace                                    │
│ Custom GPT, Claude Project, Gemini Gem, uložený prompt          │
│ → Konzistentní výstupy bez opakovaného vysvětlování             │
└─────────────────────────────────────────────────────────────────┘
```

### Rozhodovací strom: Kdy co

| Potřebuji... | Úroveň | Nástroj |
|--------------|---------|---------|
| Konzistentní výstupy na opakovaný úkol | 1 | Custom GPT / Claude Project / Gem |
| Zpracovat 50-500 položek najednou | 1 | GPT for Sheets / =COPILOT() |
| Propojit 2+ systémy automaticky | 2 | Make / Relay / n8n / Power Automate |
| AI rozhodování uvnitř workflow | 2 | Orchestrace + AI agent krok |
| Reagovat na event (nový PR, email, deploy) | 3 | Claude Routines / GitHub Copilot Agent |
| Pravidelný autonomní běh (denně/týdně) | 3 | Scheduled Task / Routine |
| Vlastní nástroj přesně pro moje potřeby | 4 | Cursor / Claude Code |
| Komplex automatizaci s mnoha edge cases | 4 | Vibe coding + orchestrace |

### Kdy NEAUTOMATIZOVAT

- Děláte to méně než 1× týdně → nestojí za investici
- Vyžaduje to hluboký úsudek pokaždé jiný → nechte na sobě
- Cena chyby je katastrofální a nereverzibilní → human only
- Technologie se zlepší za měsíc → počkejte

## Operations

### 5 pravidel pro design AI automatizací

**Pravidlo 1: Cíle, ne kroky.**

Starý přístup (cron job): "1. stáhni data 2. filtruj 3. formátuj 4. pošli"
Nový přístup (AI agent): "Každé ráno mi připrav přehled klíčových metrik. Zaměř se na anomálie. Pod 150 slov."

AI si cestu najde — a když jeden krok selže, zkusí alternativu. Deterministický script při prvním selhání zamrzne.

**Pravidlo 2: Nejdřív jeden, dva týdny kalibrace, pak druhý.**

Nespouštějte 5 automatizací najednou. Začněte jedinou nejvíc repetitivní. Nechte 14 dní běžet. Kalibrujte prompt podle reálných výstupů. "Set and forget" automatizace, která tiše posílá špatná data, je horší než žádná.

**Pravidlo 3: Vzorek → zpětná vazba → batch.**

Nikdy nespouštějte na 1000 záznamech napoprvé:
1. Spusťte na 5
2. Zkontrolujte výstup
3. Dejte zpětnou vazbu (co bylo špatně?)
4. Opravte prompt
5. Spusťte na 50
6. Pak teprve na všechny

**Pravidlo 4: Human-in-the-loop u high-stakes akcí.**

Matrice:
- Cena chyby nízká + reversibilní → plně automaticky (archivace, labeling)
- Cena chyby střední → auto-draft + lidský review (emaily zákazníkům)
- Cena chyby vysoká + ireversibilní → vždy lidský souhlas (platby, mazání, právní)

**Pravidlo 5: Spend limity od dne 1.**

Dokumentované případy: 47 000 USD za 3 dny (Claude), roční subscription za den (Cursor). Nastavte hard limits v Settings → Billing OKAMŽITĚ po subscribu. Monitorujte cost-per-task, ne cost-per-token.

### Staged akční plán

| Fáze | Kdy | Co udělat | Benchmark pro postup |
|------|-----|-----------|---------------------|
| 1 | Tento týden | Jedna saved config (Custom GPT / Project / Gem) | 8/10 výstupů použitelných |
| 2 | Týden 2-3 | Batch přes spreadsheet | Rework < 25 % |
| 3 | Měsíc 2 | Přidat trigger (scheduled task) | Neignorujete output 2× za sebou |
| 4 | Měsíc 3+ | Cross-app workflow (Make/n8n) | Šetříte > 2h/týden per workflow |

## Tips and tricks

- **Elon Musk algoritmus:** 1) Zpochybni požadavek 2) Smaž zbytečné kroky 3) Zjednoduš 4) Zrychli 5) TEPRVE PAK automatizuj. Automatizace zbytečného procesu = amplifikace plýtvání.
- **Denní otázka:** "Co můžu udělat dnes proto, abych měl zítra jednodušší práci?"
- **Vestavěná funkce vs. orchestrátor:** Pokud úloha je reasoning-heavy a vstupy nestrukturované → vestavěná AI funkce. Pokud workflow deterministický a propojuje 5+ aplikací → orchestrátor. Nejlepší týmy kombinují obojí.
- **Konektory na minimum.** Každý konektor = attack surface + token s expirací. Jeden routine = nejmenší možná množina přístupů.
- **Webhooky místo polling.** Polling ("checkni každých 5 minut") = stovky zbytečných kreditů. Webhook ("řekni mi, když se něco stane") = platíte jen za skutečnou práci.

## Why this works

Automatizace s AI není technický problém — je to designový problém. Správná úroveň + správný scope + disciplína (test-feedback-scale) = úspora 5-15 hodin týdně. Špatná úroveň + příliš široký scope + "set and forget" = utopené náklady a tiše degradující výstupy. Tento framework odděluje jedno od druhého.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context. Use it as a decision-making guide before starting any automation project.
