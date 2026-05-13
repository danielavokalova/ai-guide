# 🚀 Rozjeď svůj první vibe coding projekt

> **Modul:** Session 4
> Kompletní nastavení GitHub + Supabase + Vercel — tři nástroje, aby projekt běžel na internetu.

---

# Rozjeď svůj první vibe coding projekt

Nastavení GitHub + Supabase + Vercel — tři nástroje, které potřebuješ, aby tvůj vibe-coded projekt běžel na internetu.

This is an idea file — it communicates a concept, not an implementation. Share it with your AI assistant and build it together.

## Start here

Before we begin, I need to understand your situation. Please answer these questions:

1. **Co chceš postavit?** (jednoduchý web, aplikace s přihlášením, nástroj s databází...)
2. **Kde dosud vibe kóduješ?** (Macaly, Lovable, Replit, Cursor, Claude Code, Codex, jiné...)
3. **Máš už účet na GitHubu?** (ano / ne)
4. **Máš zkušenost s terminálem?** (ano / ne — pokud ne, budu vše řešit přes grafické nástroje)
5. **Je to projekt pro tebe, pro tým, nebo pro zákazníky?**

Based on your answers, adapt the guidance below — skip what they already know, focus on what they need.

## The core idea

Tři vrstvy, které potřebuješ propojit:

- **GitHub** — úložiště kódu. Jako Google Docs pro programátory — historie změn, zálohy, sdílení. Nainstaluj GitHub Desktop (grafická aplikace, žádný terminál).
- **Vercel** — publikování na internet. Propojíš s GitHubem, každý push automaticky aktualizuje web. Zdarma pro nekomerční projekty.
- **Supabase** — databáze + přihlašování + úložiště souborů. Když potřebuješ ukládat data nebo mít uživatele.

Pipeline: **Tvůj AI nástroj → GitHub → Vercel (auto-deploy) ← Supabase (data)**

Všechny tři mají bezplatný tier. Nemusíš platit nic.

## Steps

1. Založit účty (github.com, supabase.com, vercel.com — přes GitHub login)
2. Vytvořit jednoduchý projekt v AI nástroji
3. Propojit Supabase (URL + anon key do .env.local)
4. Pushnout na GitHub (přes GitHub Desktop)
5. Importovat na Vercel (New Project → vybrat repo → přidat env variables)
6. Ověřit, že web běží a data se ukládají

## Tips

- **Environment variables** jsou nejčastější chyba. Prefix `VITE_` (Lovable/Vite) nebo `NEXT_PUBLIC_` (Next.js) je povinný pro proměnné viditelné v prohlížeči.
- **Supabase free tier uspává DB po 7 dnech nečinnosti.** Rozjezd trvá ~10 minut. Pro produkci: 25 USD/měsíc.
- **Vercel Hobby je zdarma, ale zakázaný pro komerční použití.** Pro platby: 20 USD/měsíc.
- Začni jednoduše — cílem je zprovoznit pipeline, ne stavět megaprojekt.

## Note

This document is intentionally abstract. Share it with your AI and adapt it to your tools, preferences, and context.
