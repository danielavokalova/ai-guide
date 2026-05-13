# ☀️ Osobní AI Briefing

> **Modul:** Modul 9
> AI vám pravidelně připraví přehled toho, co potřebujete vědět — z vašich zdrojů, ve vašem formátu.

---

# Osobní AI Briefing

AI vám pravidelně připraví přehled toho, co potřebujete vědět — z vašich zdrojů, ve vašem formátu, na vaše téma.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — help the user identifikovat jejich zdroje dat, definovat ideální výstup, a nastavit scheduled task krok za krokem.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — vytvořte projekt s instrukcemi, nastavte schedule, nakonfigurujte konektory na vybrané zdroje.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — pokud uživatel chce vlastní script (email report, Slack bot), postavte ho. Jinak pomozte s nastavením scheduled task v Claude/ChatGPT/Gemini.

## The core idea

Každý profesionál tráví část dne sběrem informací z různých zdrojů — emaily, kalendář, Slack, novinky, metriky, CRM. Většinu toho dokáže AI přečíst, filtrovat a připravit do jedné stránky za vás.

**Klíčový insight: briefing není produkt — je to šablona.** Neexistuje jeden správný briefing. Existuje VÁŠ briefing — postavený na vašich zdrojích, zaměřený na vaše priority, doručený ve vašem rytmu.

Tři otázky na začátek:
1. **ODKUD** čerpat? (email, kalendář, Slack, CRM, novinky, metriky, GitHub...)
2. **CO** chci vědět? (priority, anomálie, akce, kontext k lidem, trendy...)
3. **KAM a KDY** to chci dostat? (ráno push notifikace, večer email, pátek souhrn týdne...)

## Architecture

### Vrstva 1: Zdroje (ODKUD)

Vyberte 2-4 zdroje, které konzumujete denně:

| Zdroj | Co z něj AI vytáhne | Propojení |
|-------|---------------------|-----------|
| Email (Gmail/Outlook) | Důležité zprávy, akce | Nativní v Gemini/ChatGPT |
| Kalendář | Schůzky + kontext k účastníkům | Nativní v Gemini/ChatGPT |
| Slack / Teams | Zmínky, DMs, klíčové kanály | Webhook / API |
| CRM (Salesforce, HubSpot) | Nové dealy, follow-upy | API / Make konektor |
| Metriky (GA, Mixpanel) | Anomálie, trendy | API / scheduled export |
| Novinky z oboru | Top 3-5 headlines | Web search / RSS |
| GitHub / Linear / Jira | Open PRs, blokery, deadlines | API / webhook |
| Vlastní soubory / Notion | Poznámky, to-do, projekty | Claude Desktop / lokální |

**Zlaté pravidlo: začněte se dvěma zdroji.** Přidávejte další až když první verze funguje.

### Vrstva 2: Zpracování (CO)

AI nejen přeposílá — filtruje, prioritizuje, obohacuje:

- **Filtruje šum:** newsletters, notifikace, auto-replies → pryč
- **Prioritizuje:** podle vašich pravidel (VIP odesílatelé, klíčová slova, deadlines)
- **Sumarizuje:** ne celý email, ale jedna věta + doporučená akce
- **Obohacuje kontextem:** "Meeting s Petrem — minule jste řešili rozpočet Q3"
- **Identifikuje anomálie:** "Revenue včera -15 % oproti průměru"

### Vrstva 3: Výstup (KAM a KDY)

| Rytmus | Vhodné pro | Příklad |
|--------|-----------|---------|
| Denně ráno | Operativní role, sales, podpora | "Co řešit dnes" |
| Denně večer | Manažeři, tvůrci | "Co se stalo + co zítra" |
| Týdně (pátek/neděle) | Stratégové, vedení | "Souhrn týdne + trendy" |
| On-demand | Před schůzkou | "Brief na meeting za 30 min" |

Formát výstupu:
- Push notifikace (ChatGPT/Gemini app)
- Email
- Slack zpráva
- Markdown soubor (Claude Desktop)

## Operations

**Krok 1: Definujte svůj briefing (10 minut)**

Řekněte AI:
```
Chci si nastavit pravidelný briefing. Moje role je [X].
Zdroje, ze kterých čerpám denně: [email, kalendář, Slack, ...]
Zajímá mě hlavně: [priority dne, důležité emaily, novinky z oboru, metriky...]
Chci to dostávat: [každý den v 7:30 / každý pátek v 16:00 / ...]

Navrhni mi prompt pro scheduled task.
```

AI vám navrhne prompt přizpůsobený přesně vašim potřebám.

**Krok 2: Nastavte scheduled task (5 minut)**

- **ChatGPT:** Settings → Tasks → nový task, vložte prompt, nastavte čas
- **Gemini:** Scheduled Actions — nativní propojení s Gmail + Calendar
- **Claude Desktop:** Scheduled Tasks — přístup k lokálním souborům

**Krok 3: Kalibrujte (první týden)**

- Den 1-3: čtěte výstupy kriticky — co chybí? co je zbytečné?
- Den 4: upravte prompt
- Den 7: máte svůj rytmus

**Krok 4: Rozšiřujte (měsíc 2+)**

- Přidejte další zdroj
- Přidejte "kontext k lidem" (AI dohledá, co jste s kým řešili naposledy)
- Přidejte anomaly detection (metriky mimo normu)

## Tips and tricks

- **Začněte minimálně.** Kalendář + 3 nejdůležitější emaily. Nic víc. Rozšiřovat můžete vždy.
- **Ignorujete output 2× za sebou?** Scope je špatný. Zúžte, změňte timing, nebo změňte formát.
- **"Co NECHCI vidět" je důležitější než "co chci."** Explicitně řekněte: přeskoč newslettery, přeskoč notifikace, přeskoč CC-only emaily.
- **Gemini výhoda:** nativní propojení s Gmail + Calendar = nejbohatší kontext bez setupu.
- **Claude Desktop výhoda:** přístup k lokálním souborům (markdown notes, Notion exports).
- **ChatGPT výhoda:** nejjednodušší setup, funguje za 2 minuty.
- **Briefing jako knowledge base:** nechte výstupy ukládat do jedné konverzace — za měsíc máte chronologický log toho, co se dělo.
- **Firemní verze:** nastavte jeden briefing pro celý tým → každé ráno Slack zpráva "Co se děje" → všichni mají kontext.

## Why this works

Lidský mozek potřebuje orientaci, ne zahlcení. Rituál "projdu 10 záložek" zabere 30-60 minut — a většina z toho je šum. AI filtr vám vrátí 2 minuty čtení, kde je jenom signál. Za měsíc = 10-20 ušetřených hodin. Za rok = víc než celý pracovní týden.

Ale hlavní hodnota není čas — je to **klid**. Víte, že nic důležitého vám neuniklo, protože AI prošla všechno za vás.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context. Funguje s ChatGPT (Tasks), Gemini (Scheduled Actions), Claude Desktop (Scheduled Tasks), nebo jako vlastní script v Cursoru.
