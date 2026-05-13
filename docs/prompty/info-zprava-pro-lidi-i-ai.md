# 💬 Info zpráva pro lidi i AI

> **Modul:** Modul 6
> Filipův prompt z modulu 6 — vezme kontext konverzace a napíše krátkou zprávu, která funguje jak pro člověka, tak pro jeho AI. Plus návod, jak ho nastavit jako klávesovou zkratku na všech platformách.

---

## Jak to použít

### 1. Zkopírujte prompt níže do své AI (ChatGPT, Claude, Cursor…)
### 2. Doplňte jméno příjemce a krátký kontext, případně rovnou pokračujte v probíhající konverzaci
### 3. AI vám vyplivne zprávu, která funguje pro člověka i pro jeho AI

> **Princip:** Vaše zpráva by měla fungovat dvakrát — člověk ji přečte a pochopí, AI ji pochopí a bude vědět, co dělat. Idea file v miniatuře.

---

```
Vezmi kontext této konverzace a napiš to jako krátkou zprávu pro [jméno příjemce].

Zpráva musí fungovat dvakrát:
1. Jako lidská zpráva — příjemce ji přečte, hned pochopí o co jde a co po něm chci.
2. Jako vstup pro jeho AI — pokud si ji hodí do ChatGPT/Claude/Cursoru, AI bude mít všechen kontext a ví, jak mu pomoct s realizací.

Zahrň všechny relevantní detaily:
- O co jde a proč to píšu
- Co od příjemce potřebuju (nebo co nabízím)
- Odkazy, dokumenty, deadlines, čísla
- Sugesce akce, pokud dává smysl ("zkus si to projet s AI a vrátit se s návrhem…")

Formát: jasná struktura, snadno parsovatelná, lidský tón. Žádné corporate buzzwords. Markdown OK.
```

---

## Jak si to nastavit jako klávesovou zkratku

Cílem je, aby stačilo někde napsat `/msg` a celý prompt se rozbalil. Pak ho jen pošlete do své AI s konkrétním jménem.

- **macOS**: `System Settings` → `Keyboard` → `Text Replacements` → `+` → do **Replace** dejte `/msg`, do **With** vložte prompt → zavřete (uloží automaticky). Bonus: pokud máte iCloud, zkratka se vám sama nasynchronizuje na iPhone i iPad.

- **iPhone / iPad**: `Settings` → `General` → `Keyboard` → `Text Replacement` → `+` → do **Phrase** vložte prompt, do **Shortcut** napište `/msg` → `Save`.

- **Android (Gboard)**: `Gboard Settings` → `Dictionary` → `Personal dictionary` → vyberte jazyk → `+` → do **prvního pole** vložte prompt, do **Shortcut** napište `/msg` → `OK`.

- **Windows**: nativní text replacement chybí — nainstalujte si zdarma [Espanso](https://espanso.org) → v terminálu spusťte `espanso edit base` → přidejte:

```yaml
matches:
  - trigger: "/msg"
    replace: "Vezmi kontext této konverzace a napiš to jako krátkou zprávu pro [jméno]…"
```

→ uložte a zavřete editor (Espanso si pravidlo ihned načte). Bonus: Espanso funguje i na Macu/Linuxu, pokud chcete jednu konfiguraci napříč zařízeními.

> **Tip:** Pokud používáte Raycast (Mac), TextExpander, aText nebo Alfred, mají vlastní snippet manažery — fungují stejně, často s víc featurami (proměnné, datum, schránka).

---

### Kdy se hodí

- Píšete kolegovi/klientovi po hodině brainstormingu s AI a potřebujete to shrnout do zprávy
- Chcete delegovat úkol na člověka, který sám pracuje s AI (idea file v miniatuře)
- Posíláte zadání externímu dodavateli — ať si ho hodí do své AI a začne pracovat
- Vystupujete z konverzace s AI a chcete ji „přepóstnout" někomu dalšímu
