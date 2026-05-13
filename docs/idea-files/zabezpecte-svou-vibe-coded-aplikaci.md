# Zabezpečte svou vibe-coded aplikaci

> **Modul:** Session 4
> Přihlašování a ochrana dat — RLS, autentizace a bezpečnostní checklist.

---

# Zabezpečte svou vibe-coded aplikaci

Přihlašování a ochrana dat — aby vaše aplikace nebyla mezi těmi 10 %, kterým unikají data na internet.

This is an idea file — it communicates a concept, not an implementation. Share it with your AI assistant and build it together.

## Start here

1. **Jakou aplikaci zabezpečuješ?** (popiš krátce, co dělá)
2. **Používáš Supabase?** (ano / ne — pokud ne, jakou databázi?)
3. **Má tvoje aplikace přihlašování?** (ano / ne / nevím)
4. **Kdo k ní má přistupovat?** (jen já, můj tým, veřejnost)
5. **Pracuješ s citlivými daty?** (osobní údaje, finanční data, firemní data)

Based on answers, focus on what's most urgent — if no auth exists, start there. If auth exists but no RLS, that's the priority.

## The core idea

AI generuje kód, kterému nerozumíte. **Bez správného nastavení jsou data volně přístupná komukoli.** V roce 2025 sken 1 645 aplikací zjistil, že 10 % mělo plně čitelná data přes veřejný klíč.

Dva klíčové pojmy:
- **Autentizace** = kdo jste (přihlášení)
- **RLS (Row Level Security)** = kdo vidí jaká data

**Pravidlo: žádná aplikace s daty nesmí jít ven bez auth + RLS.**

## What to tell your AI

### Při startu nového projektu
"Chci Supabase Auth s přihlašováním přes email/heslo. Zapni RLS na všech tabulkách. Každý uživatel vidí jen svá data přes auth.uid() = user_id."

### Při zabezpečení existujícího projektu
"Přidej přihlašování přes Supabase Auth. Zapni RLS na všech tabulkách. Přidej user_id sloupec. Uživatele řeš přes authentification modul, ne přes klasickou tabulku."

### Checklist před sdílením
- [ ] RLS zapnutý na všech tabulkách
- [ ] Žádný service_role klíč ve frontendu
- [ ] .env v .gitignore
- [ ] Test v anonymním okně: bez přihlášení nevidím data
- [ ] Systémové emaily přeložené do češtiny (Authentication → Email Templates)

## Tips

- **"Zapni RLS" nestačí** — musíte vytvořit i politiky (SELECT/INSERT/UPDATE/DELETE). Bez politik nikdo nevidí nic.
- **Supabase free tier posílá max 3 emaily/hodinu.** Pro produkci napojte Resend nebo SendGrid.
- **AI občas obchází bezpečnost kvůli jednoduchosti.** Pokud vidíte service_role klíč v kódu — okamžitě opravte.
- Nastavte rate limiting: max 5 přihlášení za 30 sekund (Settings → Auth).

## Note

This document is intentionally abstract. Share it with your AI and adapt it to your tools, preferences, and context.
