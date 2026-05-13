# AI studijní portál (statický web)

Přehled materiálů v `docs/` — dlaždice na `index.html`, každý návod na samostatné stránce `viewer.html?p=…` s tlačítkem **Zpět**.

## Obsah

- `docs/dokumenty/`
- `docs/idea-files/`
- `docs/prompty/`
- `docs/prehled-portal-ai.md` — rejstřík odkazů

## Obnovení `manifest.json`

```powershell
python build_site.py
```

## Import ze složky (rozbalený ZIP)

Složka musí obsahovat `dokumenty`, `idea-files`, `prompty`:

```powershell
$env:AI_MATERIAL_IMPORT = "C:\cesta\k\rozbalenemu-zipu"
python build_site.py --import
```

(Podporováno je i dřívější název proměnné prostředí pro import — viz `build_site.py`.)

Pak znovu `python build_site.py` a commit.

## Publikace

GitHub Pages z větve `main`, kořen repozitáře. Soubor `.nojekyll` je v repu.
