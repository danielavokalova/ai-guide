"""
Rebuild the AI Guide static site: copy Markdown + images into this repo and regenerate manifest.json.
Run from repo root: python build_site.py

Paths default to optional local sibling folders; override with AI_GUIDE_DOCS_SOURCE and AI_GUIDE_PUBLIC.
"""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

DEST = Path(__file__).resolve().parent
DOCS = DEST / "docs"

# Optional: when unset, try common local layout (repo on Desktop).
_default_source = DEST.parent / "new_help" / "gitbook_golhelp" / "content" / "docs"
_default_public = DEST.parent / "new_help" / "gitbook_golhelp" / "public"
SOURCE = Path(os.environ.get("AI_GUIDE_DOCS_SOURCE", str(_default_source)))
PUBLIC = Path(os.environ.get("AI_GUIDE_PUBLIC", str(_default_public)))

CATEGORY_LABELS = {
    "getting-started": "Getting started",
    "configuration": "Configuration",
    "operations": "Operations",
    "release-notes": "Release notes",
    "troubleshooting": "Troubleshooting",
}


def title_from_md(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main() -> None:
    if not SOURCE.is_dir():
        raise SystemExit(f"Missing source tree: {SOURCE}")

    if DOCS.exists():
        shutil.rmtree(DOCS)
    shutil.copytree(SOURCE, DOCS)

    imgs = DEST / "images"
    if imgs.exists():
        shutil.rmtree(imgs)
    pub_img = PUBLIC / "images"
    if pub_img.is_dir():
        shutil.copytree(pub_img, imgs)

    entries: list[dict[str, str]] = []
    for md in sorted(DOCS.rglob("*.md")):
        rel = md.relative_to(DOCS).as_posix()
        parts = rel.split("/")
        category = parts[0] if len(parts) > 1 else "docs"
        raw = md.read_text(encoding="utf-8")
        raw = raw.replace("](/images/", "](images/")
        raw = raw.replace("![](/images/", "![](images/")
        md.write_text(raw, encoding="utf-8")
        stem_title = md.stem.replace("-", " ").replace("_", " ").title()
        title = title_from_md(raw, stem_title)
        entries.append(
            {
                "id": rel[:-3] if rel.endswith(".md") else rel,
                "path": f"docs/{rel}",
                "title": title,
                "category": category,
                "categoryLabel": CATEGORY_LABELS.get(
                    category, category.replace("-", " ").title()
                ),
            }
        )

    (DEST / "manifest.json").write_text(
        json.dumps({"articles": entries}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote manifest with {len(entries)} articles.")


if __name__ == "__main__":
    main()
