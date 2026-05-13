# 🌐 Personalizovaná webová aplikace s AI

> **Modul:** Modul 5
> Webová aplikace, která z vstupních dat generuje personalizovaný výstup.

---

# Idea File: Personalizovaná webová aplikace s AI

## Co chci udělat
Chci vytvořit webovou aplikaci, která na základě vstupních dat (profil, dotazník, formulář) vygeneruje personalizovaný výstup — report, doporučení, transformaci, vizualizaci.

## Kroky
1. Definujte vstup — co od uživatele potřebujete (URL, formulář, upload souboru)
2. Navrhněte automatický sběr dat — API, scraping, nebo jednoduše formulář
3. Vytvořte systémový prompt — co má AI s daty udělat, jaký je požadovaný výstup (JSON)
4. Napojte na AI model přes API — OpenRouter, OpenAI API, Anthropic API
5. Postavte frontend, který výstup vizuálně zobrazí

## Klíčové principy
- Profile-first approach — nejdřív analyzuj, kdo ten člověk je, pak teprve generuj
- Striktní JSON output — frontend potřebuje strukturovaná data, ne volný text
- Cache + rate limit — AI volání jsou pomalá a drahá, cachujte výsledky
- Lead capture — e-mail nebo registrace jako bonus

## Tipy
- Nemusíte umět programovat — celou aplikaci lze postavit s pomocí AI (Cursor, Lovable)
- Funguje pro jakýkoli transformační program, kurz, službu nebo produkt
- Místo LinkedIn můžete použít jakýkoli veřejný profil nebo dotazník
- Klíčové je mít kvalitní systémový prompt s konkrétními příklady