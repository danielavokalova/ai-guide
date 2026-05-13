# AI Guide

Samostatný statický web: články v `docs/`, rozhraní v `index.html`, seznam v `manifest.json`, obrázky v `images/`.

Tento repozitář je jediný zdroj toho, co se na webu zobrazuje — není spojený s žádným jiným veřejným projektem ani stránkou.

## Obnovení obsahu (volitelné)

Skript jen zkopíruje Markdown a obrázky ze složek, které nastavíš v proměnných prostředí, a znovu vygeneruje `manifest.json`.

```powershell
$env:AI_GUIDE_DOCS_SOURCE = "C:\cesta\k\markdown-slozce"
$env:AI_GUIDE_PUBLIC = "C:\cesta\k\public-obrazkum"
python build_site.py
```

Potom commitni změny v `docs/`, `images/` a `manifest.json`.

## Publikace

V nastavení repozitáře na GitHubu zapni Pages z větve `main` z kořene projektu. V repu je soubor `.nojekyll`.
