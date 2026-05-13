# Email Triage Agent

> **Modul:** Modul 9
> AI automaticky třídí inbox, klasifikuje priority a draftuje odpovědi — vy jen schvalujete.

---

# Email Triage Agent

AI automaticky třídí váš inbox, klasifikuje priority a draftuje odpovědi — vy jen schvalujete.

This is an idea file — it communicates a concept, not an implementation.
Share it with your AI assistant and build it together.

## How to use this

If you're a chat assistant (e.g. ChatGPT, Copilot, Gemini) — help the user navrhnout kategorie, pravidla třídění, a zvolit platformu (Make/n8n/Relay/Power Automate).
If you're a cowork tool (e.g. Claude Cowork, Microsoft Cowork) — naplánujte workflow: trigger, klasifikace, routing, odpovědi, eskalace.
If you're a code agent (e.g. Cursor, Claude Code, Codex) — pokud uživatel chce vlastní řešení (Python + Gmail API), postavte email parser s LLM klasifikací.

## The core idea

Průměrný knowledge worker stráví 2.5 hodiny denně emailem. Většina emailů patří do 4-5 kategorií a vyžaduje předvídatelnou reakci. Přesto je čteme a řešíme jeden po druhém.

**Klíčový posun: AI přečte všechny, vy řešíte jen ty důležité.** Agent klasifikuje příchozí emaily, draftuje odpovědi na rutinní dotazy, eskaluje důležité — a vy jen schválíte nebo upravíte.

Reálná data: implementace emailového triage agenta (quellant.com case study) snížila čas na inbox o 60 % bez ztráty důležitých zpráv.

## Architecture

### Vrstva 1: Trigger

- Gmail/Outlook webhook nebo polling (nový email → spuštění)
- Webhook je lepší než polling (žádné zbytečné běhy = úspora kreditů)

### Vrstva 2: Klasifikace

AI přečte email a rozhodne:
- **Kategorie:** Sales / Support / Interní / Newsletter / Spam
- **Priorita:** Urgent / Normal / Low / Ignore
- **Confidence score:** 0-1 (jak si je AI jistá)

Tip: Použijte levný model (GPT-4o-mini, Gemini Flash) pro klasifikaci — je to jednoduché rozhodnutí, nepotřebujete drahý reasoning model.

### Vrstva 3: Routing + akce

| Kategorie | Priorita | Akce |
|-----------|----------|------|
| Sales + Urgent | High | Slack notifikace + draft odpovědi → human review |
| Support + High confidence | Normal | Auto-draft z knowledge base → human review |
| Newsletter | Low | Archivuj + shrň do týdenního digestu |
| Spam / Promo | Ignore | Smaž / archivuj automaticky |
| Cokoli s low confidence | - | Eskaluj bez akce → human rozhodne |

### Vrstva 4: Human-in-the-loop

- Drafty odpovědí jdou do Slack/Teams k review
- Jedno kliknutí: Schválit / Upravit / Odmítnout
- Zpětná vazba se učí (vector store s historií → lepší klasifikace)

### Vrstva 5: Learning loop (volitelné)

- PostgreSQL / Pinecone vector store ukládá lidská rozhodnutí
- Klasifikátor se zlepšuje na základě zpětné vazby
- Thresholdy se přizpůsobují (0.95 pro auto-send, 0.20 pro ignore)

## Operations

**Setup:**
1. Definujte 4-6 kategorií (specifické pro vaši roli)
2. Napište 10-20 příkladů "tento email = tato kategorie + tato akce" (golden dataset)
3. Nastavte workflow v Make/n8n/Relay
4. Zapněte human-in-the-loop na VŠECHNY akce (první 2 týdny)
5. Postupně uvolňujte: low-risk akce → auto, high-risk → vždy review

**Denní provoz:**
- Ráno: místo 50 emailů vidíte 5-10 v Slacku s draftem odpovědi
- Schválíte, upravíte, nebo řeknete "tohle řeším sám"
- Zbytek je zpracovaný automaticky

## Tips and tricks

- **Kombinace modelů šetří 70 % nákladů.** GPT-4o-mini/Gemini Flash pro klasifikaci ($0.001/email), Claude/GPT-5 jen pro drafting odpovědí na complex emaily.
- **Reasoning effort: low pro klasifikaci.** V o3-mini nastavte `reasoningEffort: low` — pro binární rozhodnutí nepotřebujete hluboké uvažování.
- **Thresholdy místo binárních rozhodnutí.** AI nikdy nemá 100% jistotu. Confidence > 0.95 → auto. Confidence 0.50-0.95 → human review. Confidence < 0.50 → přeposlat bez akce.
- **Filtrujte vlastní odpovědi.** Klasická chyba: agent odpoví → přijde notifikace → agent odpoví znovu → loop. Vždy filtrujte zprávy, které jste sami poslali.
- **Golden dataset = kvalita.** 10-20 reálných příkladů s vaším ručním roztříděním. Bez toho agent hádá.

## Why this works

Email je strukturovaný vstup (odesílatel, předmět, obsah) s předvídatelnými výstupy (odpověď, přeposlání, archivace). To je přesně typ úlohy, kde AI exceluje — pattern matching na škále, kterou člověk nezvládne udržet konzistentně po 50. emailu dne.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. Share it with your AI and adapt it to your tools, preferences, and context. Realizovatelné v Make.com, n8n, Relay.app, Power Automate, nebo jako vlastní Python script.
