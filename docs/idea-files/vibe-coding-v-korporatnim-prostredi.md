# Vibe coding v korporátním prostředí

> **Modul:** Session 4
> Jak prosadit vibe coding ve velké firmě — argumenty pro IT/management a bezpečný sandbox.

---

# Vibe coding v korporátním prostředí

Jak prosadit vibe coding ve velké firmě — argumenty, bezpečné prostředí a konkrétní kroky.

This is an idea file — it communicates a concept, not an implementation. Share it with your AI assistant and build it together.

## Start here

1. **Jaká je tvoje role?** (manažer, specialista, IT, jiné)
2. **Jaké AI nástroje máte ve firmě schválené?** (Copilot, ChatGPT Enterprise, žádné, nevím)
3. **Co bys chtěl vyřešit?** (konkrétní proces, reporting, automatizace, prototyp)
4. **Máš podporu vedení/IT?** (ano / ne / ještě jsem nezkusil)
5. **Pracuješ s firemními daty?** (ano — jaký typ / ne)

Based on answers, help craft either a business case for leadership, a safe sandbox setup, or a pilot project plan.

## The core idea

IT nestíhá, byznys čeká, nápady umírají ve frontě. **Vibe coding dává byznysovým lidem možnost digitalizovat procesy sami — ale bez systému to vytvoří víc problémů, než vyřeší.**

Dva osvědčené principy:
- Produkťáci generují kód, IT zajišťuje bezpečnost
- Nic nejde ven bez review programátora

## Three paths

### Path A: Máte Copilot / ChatGPT Enterprise
Nejsnazší cesta. Zažádejte o přístup ke Codex nebo Copilot Workspace. Bezpečnostní model je schválený, data zůstávají ve firemním tenantu.

### Path B: Chcete sandbox mimo firemní systémy
Oddělený prostor: Cursor + Supabase + Vercel. Žádné napojení na produkční data. Anonymizované nebo testovací datasety. Vibe-coded aplikace žije mimo firemní síť.

### Path C: Napojení na firemní systémy
Osvědčený vzorec (SAP + vibe coding z praxe):
```
Firemní systém → export dat (CSV/API/FTP) → Make/n8n → Supabase → vibe app
```
Data se anonymizují při exportu. Do firemního systému se nic neposílá zpět. IT nemusí nic instalovat do produkce.

## How to start

1. **Najděte konkrétní problém** — kolik hodin týdně tráví tým manuální prací?
2. **Udělejte prototyp** — sami, za 1–2 dny. Fungující demo > prezentace.
3. **Ukažte vedení výsledek** — ne "chci povolení", ale "podívejte, co jsem udělal za víkend".
4. **Navrhněte pravidla** — co je povoleno, co vyžaduje review, co je zakázáno.

## Tips

- **Neříkejte "vibe coding".** V korporátu funguje líp "citizen development" nebo "rapid prototyping".
- **Jeden power user per oddělení** může digitalizovat víc než měsíce čekání na IT.
- IT nepotřebuje nic instalovat — export dat přes existující kanály stačí.
- Začněte prototypem, ne žádostí o povolení.

## Note

This document is intentionally abstract. Share it with your AI and adapt it to your tools, preferences, and context.
