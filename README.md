# AI Guide (static help)

Public static mirror of GOL IBE help articles (Markdown), with a dark-themed single-page browser, search, and categories.

**Live site:** after GitHub Pages is enabled: `https://danielavokalova.github.io/ai-guide/`

## Regenerate content (local)

Requires the GOL help content export next to this folder on disk:

`../new_help/gitbook_golhelp/content/docs/`

Or set a custom path:

```powershell
$env:AI_GUIDE_DOCS_SOURCE = "C:\path\to\content\docs"
python build_site.py
```

Then commit changes under `docs/` and `manifest.json`.

## GitHub Pages

Repository **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch `main` / root** and save.

Add `.nojekyll` (already in repo) so paths with underscores work as expected.
