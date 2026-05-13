# FAIL Portal (statický web)

Veřejný přehled materiálů **Future AI Leader 2026** — prompty, idea files a dokumenty. Všechno leží v `docs/`; rozhraní je `index.html` + `manifest.json`.

## Obsah

- `docs/dokumenty/` — návody (včetně exportu zadání z Wordu `fail-13-3-zadani.md`)
- `docs/idea-files/`
- `docs/prompty/`
- `docs/prehled-portal-fail.md` — rejstřík odkazů (převzat z původního README balíčku)

## Obnovení `manifest.json`

Po úpravě Markdownů v `docs/`:

```powershell
python build_site.py
```

## Jednorázový import ze složky (rozbalený ZIP)

Složka musí obsahovat přímo podsložky `dokumenty`, `idea-files`, `prompty`:

```powershell
$env:FAIL_PORTAL_IMPORT = "C:\cesta\k\rozbalenemu-zipu"
python build_site.py --import
```

Pak zkontroluj `docs/`, případně doplněné soubory (např. export z Wordu), znovu spusť `python build_site.py` bez `--import` a commitni.

## Publikace

GitHub Pages z větve `main`, kořen repozitáře. Soubor `.nojekyll` je v repu.
