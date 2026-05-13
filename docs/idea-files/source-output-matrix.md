# 🔀 Source → Output Matrix

> **Modul:** Modul 9
> Jeden zdroj, maximální hodnota. Systém, který z jednoho vstupu vytvoří 5–15 výstupů.

---

# Source → Output Matrix

Jeden zdroj, maximální hodnota. Jak navrhnout systém, který z jednoho vstupu vytvoří 5-15 výstupů — ne kopírováním, ale designem.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — help the user identifikovat jejich nejčastější zdroj (meeting, prezentace, podcast, customer call), zmapovat všechny možné výstupy, a navrhnout postupný build-up.
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — vytvořte Source → Output Matrix jako tabulku, definujte extrakční schéma a formátové šablony pro každý výstup.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — pokud uživatel chce automatizaci, postavte orchestrovaný pipeline s agenty per výstup a review pointy.

## The core idea

Většina lidí vytvoří jeden výstup z jednoho zdroje: zapíšou meeting, pošlou zápis, konec. Nebo nahrají podcast a dají ho na Spotify. A tím to končí.

**Klíčový insight: každý kvalitní zdroj obsahuje 5-15 různých výstupů — jen je nikdo nedesignoval.** Z jednoho 60minutového podcastu můžete mít: přepis, blog článek, 3 LinkedIn posty, newsletter sekci, YouTube popisek, audiogram pro Reels, citáty pro grafiky, knowledge base entry, follow-up email hostovi, pitch pro potenciální hosty. Z jednoho meetingu: zápis, action items v Jira, follow-up emaily účastníkům, update do Slacku, dashboard update, personalizované doporučení per účastník.

Rozdíl oproti "content repurposing": to řeší jenom marketingové formáty. Source → Output Matrix je **designový přístup** — systematicky mapujete, jaké výstupy mají hodnotu pro jakou audience, a stavíte systém, který je produkuje s minimální friction.

Reálný příklad: profesionální podcast pipeline, který z jednoho video záznamu automaticky generuje 10 výstupů — audio soubor, surový přepis, vyčištěný přepis, popis pro web, YouTube description s timestamps, HTML pro hosting platformu, blog článek v autorově hlasu, LinkedIn post, newsletter draft, a knowledge base záznam. Celý systém běží orchestrovaně, s review pointy po klíčových krocích.

## Architecture

### Vrstva 1: Identifikace zdroje (Source)

Každý profesionál má 2-3 "zlaté zdroje" — vstupy, které obsahují nejvíc hodnoty:

| Role | Zlatý zdroj | Proč je zlatý |
|------|-------------|---------------|
| Konzultant | Klientský call / workshop | Insights, doporučení, příběhy |
| Manažer | Týmový meeting / 1:1 | Rozhodnutí, kontext, feedback |
| Tvůrce obsahu | Podcast / přednáška | Myšlenky, stories, citáty |
| Sales | Discovery call | Pain points, námitky, potřeby |
| Výzkumník | Rozhovor / panel | Data, perspektivy, vzory |
| Školitel | Workshop / školení | Principy, příklady, Q&A |

**Klíčová otázka: "Který jeden vstup, kdybych z něj vytěžil maximum, by mi přinesl nejvíc hodnoty?"**

### Vrstva 2: Output Matrix (mapování výstupů)

Pro každý zdroj navrhněte matici:

```
SOURCE: [váš zlatý zdroj]
─────────────────────────────────────────────────────
VÝSTUP              │ PRO KOHO        │ FORMÁT       │ HODNOTA
────────────────────┼─────────────────┼──────────────┼────────
Strukturovaný zápis │ Účastníci       │ Markdown     │ Reference
Action items        │ Tým             │ Jira/Notion  │ Execution
Follow-up email     │ Každý účastník  │ Personalized │ Vztahy
Knowledge base      │ Já + tým        │ Wiki entry   │ Memory
Social post         │ Audience        │ LinkedIn     │ Reach
Newsletter sekce    │ Subscribers     │ Email        │ Engagement
Interní update      │ Management      │ Slack/Teams  │ Visibility
Training material   │ Nováčci         │ How-to       │ Onboarding
...                 │ ...             │ ...          │ ...
```

### Vrstva 3: Extrakce (Extract)

Podobně jako v programování — nejdřív parsujete, pak renderujete. Nesnažte se generovat všechny výstupy najednou. Nejdřív extrahujte "jádro":

- Klíčová rozhodnutí / teze
- Přesné citáty (kdo co řekl)
- Data a čísla
- Příběhy a příklady
- Action items / next steps
- Otevřené otázky
- Emocionální momenty (překvapení, nesouhlas, aha)

Tento strukturovaný extrakt je základ pro VŠECHNY výstupy. Extrahujte jednou, generujte mnohokrát.

### Vrstva 4: Generování (Generate per output)

Každý výstup má vlastní:
- **Formát** — délka, struktura, médium
- **Audience** — kdo to čte, co potřebuje vědět
- **Tone** — formální vs. casual, osobní vs. firemní
- **Template** — opakovaná struktura, kterou jen naplníte

Klíčový princip: **jeden výstup = jeden agent/prompt.** Ne mega-prompt "udělej všechno najednou". Kvalita klesá exponenciálně s počtem úkolů v jednom promptu.

### Vrstva 5: Orchestrace

Výstupy nejsou nezávislé — mají závislosti:

```
Zdroj → Přepis → Extrakt ─┬─→ Zápis pro účastníky
                           ├─→ Action items (závisí na zápisu)
                           ├─→ Blog článek
                           ├─→ LinkedIn post (závisí na blogu)
                           ├─→ Newsletter (závisí na blogu)
                           └─→ Knowledge base entry
```

Review pointy po klíčových krocích: po přepisu (je přesný?), po extraktu (nic nechybí?), po finálních výstupech (kvalita?).

## Operations

**Krok 1: Zmapujte svůj zlatý zdroj (30 minut)**

Řekněte AI: "Dělám [váš zlatý zdroj] pravidelně. Jaké výstupy bych z toho mohl generovat? Navrhni Source → Output Matrix."

AI vám navrhne 10-20 možných výstupů. Vy vyberete 5-8, které mají reálnou hodnotu.

**Krok 2: Navrhněte extrakční schéma (15 minut)**

"Z [zdroj] potřebuji vytáhnout tyto typy informací: [výčet z matice]. Navrhni extrakční schéma — jakou strukturu má mít meziprodukt."

**Krok 3: Vytvořte šablonu pro každý výstup (po 10 minut)**

Pro každý výstup z matice:
- Definujte formát a délku
- Napište 2-3 příklady dobrého výstupu
- Uložte jako Custom GPT / Claude Project / asistenta

**Krok 4: Otestujte na posledním zdroji (45 minut)**

Vezměte poslední meeting / podcast / call. Projděte celý pipeline ručně:
1. Extrakt
2. Každý výstup zvlášť
3. Co funguje? Co ne? Upravte šablony.

**Krok 5: Postupně automatizujte (ongoing)**

- Týden 1-2: ručně, laďte šablony
- Týden 3-4: polo-automaticky (extrakt + generování v jednom projektu)
- Měsíc 2+: plně orchestrovaně (trigger → pipeline → review → publikace)

## Tips and tricks

- **Začněte třemi výstupy, ne patnácti.** Tři kvalitní > patnáct průměrných. Přidávejte postupně, až když předchozí fungují na 8/10.
- **Extrakt je investice, ne overhead.** Jeden dobrý extrakt použijete 3× — tento týden pro LinkedIn, příští týden pro newsletter, za měsíc jako základ pro workshop. Ukládejte extrakty.
- **Personalizace je superpower.** Nejhodnotnější výstupy nejsou generické (zápis pro všechny), ale personalizované (follow-up pro Petra, jiný pro Janu). AI tohle zvládá triviálně — stačí říct "pro každého účastníka napiš personalizovaný follow-up na základě toho, co říkal".
- **Review pointy šetří čas.** Přeskočíte-li review po extraktu a extrakce je špatná, všechny výstupy budou špatné. 2 minuty kontroly ušetří 30 minut předělávání.
- **Reálný benchmark:** 60minutový podcast → 10 výstupů za ~45 minut (s review). Bez systému: 6-8 hodin, nebo — reálněji — se to nikdy neudělá.
- **Nemusíte použít všechny výstupy pokaždé.** Matrix je menu, ne checklist. Tento týden potřebuji blog + LinkedIn. Příští týden jenom zápis + follow-up.

## Why this works

Lidé netvoří málo obsahu proto, že nemají co říct — ale proto, že **nemají systém na transformaci myšlenek do formátů**. Jeden kvalitní meeting obsahuje materiál na týden tvorby. Jeden podcast je základ pro měsíc marketingu. Ale bez designu pipeline se stane: nahraju, archivuju, zapomenu.

Source → Output Matrix mění přístup z "musím tvořit obsah" na "musím jenom vytěžit to, co už dělám". A AI je perfektní na tuto transformaci — stále stejný extrakt, stále stejné šablony, stále stejná kvalita. Vy děláte jen review a strategické rozhodnutí "co dnes publikuji".

Hlubší princip: **hodnota nežije v jednom formátu — žije v myšlence. Formát je jen balení.** Jeden insight funguje jako tweet, jako slide, jako newsletter hook, jako blog sekce. Systém, který tohle automaticky dělá, je multiplicator vaší hodnoty.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context. Funguje s jakýmkoli AI nástrojem — od jednoduchého Claude Project, kde ručně vkládáte přepisy, až po plně orchestrovaný pipeline s agenty a automatickým triggerem.
