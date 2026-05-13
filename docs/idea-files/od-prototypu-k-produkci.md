# Od prototypu k produkci

> **Modul:** Session 4
> Jak dotáhnout projekt k aplikaci pro reálné uživatele — test/produkce, zálohy a pre-launch checklist.

---

# Od prototypu k produkci

Jak dotáhnout vibe-coded projekt k aplikaci, kterou používají reální lidé — bezpečně a bez nečekaných účtů.

This is an idea file — it communicates a concept, not an implementation. Share it with your AI assistant and build it together.

## Start here

1. **Co jsi postavil?** (popiš krátce svůj projekt)
2. **Kde to běží?** (lokálně, Lovable, Vercel, jiné)
3. **Kolik lidí to bude používat?** (já, tým 5–20, stovky)
4. **Přijímáš platby nebo pracuješ s citlivými daty?**
5. **Co tě nejvíc trápí?** (bojím se něco rozbít, nevím jak aktualizovat, nechci nečekaný účet)

Based on answers, prioritize — someone with 5 users needs different advice than someone expecting hundreds.

## The core idea

Udělat první verzi je nejjednodušší část. **Skutečná práce začíná, když to chcete dát lidem.** Tři věci, které musíte vyřešit: jak aktualizovat bez rozbití, jak se chránit před výpadky, jak nekrvácet penězi.

## Three essentials

### 1. Oddělte test od produkce
- Stáhněte projekt přes GitHub Desktop → otevřete v Cursoru → dělejte změny lokálně
- Pushněte do nové větve (ne do main) → Vercel vytvoří preview URL → otestujte
- Až je vše OK → merge do main → automatický deploy
- Něco se pokazí → Vercel: Instant Rollback jedním klikem

### 2. Nastavte spend management
Případ z praxe: aplikace Cara — 96 280 USD za týden na Vercelu.
- **Vercel:** Settings → Billing → Spend Management → hard cap 20–50 USD
- **Supabase:** kontrolujte compute v dashboardu, zapněte spend cap
- **Předřaďte Cloudflare (zdarma)** — ořeže bot traffic

### 3. Zálohy
- GitHub Desktop = lokální kopie kódu na vašem počítači
- Supabase = automatické zálohy na placeném tieru
- Vercel = rollback na libovolnou předchozí verzi

## Pre-launch checklist

- [ ] Auth + RLS funguje (viz idea file #2)
- [ ] Žádné API klíče v kódu
- [ ] Spend management nastaven
- [ ] Testováno v anonymním okně
- [ ] Testováno na telefonu
- [ ] `npm run build` projde lokálně bez chyb

## Tips

- **Vercel Hobby je zdarma, ale bez analytik a zakázaný pro komerční projekty.** Pro reálné nasazení: Pro 20 USD/měsíc.
- **Supabase Pro (25 USD/měsíc):** žádné uspávání, zálohy, vyšší limity.
- Spusťte `npm run build` lokálně před pushem — dev server toleruje chyby, které produkce neodpustí.
- Vlastní doména zvyšuje důvěru a je na Vercelu zdarma.

## Note

This document is intentionally abstract. Share it with your AI and adapt it to your tools, preferences, and context.
