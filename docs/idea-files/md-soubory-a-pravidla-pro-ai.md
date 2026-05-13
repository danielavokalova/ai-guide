# MD soubory a pravidla pro AI

> **Modul:** Session 4
> Jak dát AI pravidla, aby nedělala věci po svém — plan.md, design.md, rules.md.

---

# MD soubory a pravidla pro AI

Jak dát AI pravidla, aby nedělala věci po svém — jednou napíšete, platí pro celý projekt.

This is an idea file — it communicates a concept, not an implementation. Share it with your AI assistant and build it together.

## Start here

1. **V čem vibe kóduješ?** (Cursor, Claude Code, Codex, Lovable, jiné...)
2. **Máš existující projekt, nebo začínáš nový?**
3. **Co tě trápí?** (nekonzistentní design, AI dělá pokaždé něco jiného, opakuješ stejné instrukce...)
4. **Máš vizuální vzor?** (screenshot aplikace, web, který se ti líbí)

Based on answers, help create the right .md files for their tool and situation.

## The core idea

Bez pravidel AI jednou použije modré tlačítko, podruhé zelené, jednou píše "Tisk", podruhé "Tisknout". **MD soubory jsou instrukce, které AI čte automaticky na začátku každé konverzace.** Zapíšete jednou, platí pro celý projekt.

Tři základní soubory:

**plan.md** — co stavím, pro koho, jaké funkce. AI chápe kontext celého projektu.

**design.md** — barvy, fonty, styl komponent. AI dodržuje konzistentní vizuál.

**rules.md** — pojmenování, jazyk UI, bezpečnostní pravidla, co AI nesmí dělat.

## How to create them

**Prompt pro plan.md:** "Popíšu ti svůj projekt — ty z toho udělej plan.md s cíli, funkcemi a architekturou."

**Prompt pro design.md:** "Podívej se na mou aplikaci [nebo: tady je screenshot webu, který se mi líbí] a vytvoř design.md se všemi vizuálními pravidly."

**Prompt pro rules.md:** "Vytvoř rules.md — chci české UI, bezpečnostní pravidla, konzistentní pojmenování souborů."

**Za běhu:** "Tohle se mi líbí. Zapiš to do design.md, ať to příště děláš stejně."

## Where they live

- **Cursor** — kořen projektu (.cursorrules nebo .md soubory)
- **Claude Code** — CLAUDE.md v kořeni
- **Lovable** — Settings → instrukce
- **Codex** — AGENTS.md

## Tips

- Začněte s plan.md — nechte AI navrhnout design.md a rules.md z toho.
- Méně je víc: 10 jasných pravidel > 50 vágních.
- MD soubory se dají kopírovat mezi projekty — hotový design.md přenesete do nového projektu jedním kopírováním.
- Plan režim v Cursoru: AI nejdřív navrhne plán, vy potvrdíte, pak teprve staví.

## Note

This document is intentionally abstract. Share it with your AI and adapt it to your tools, preferences, and context.
