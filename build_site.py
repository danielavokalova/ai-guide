"""
Regenerate manifest.json from all Markdown files under docs/.

Run from repo root: python build_site.py

Optional one-off import (složka musí obsahovat podsložky dokumenty, idea-files, prompty):

  set AI_MATERIAL_IMPORT=C:\\cesta\\k\\rozbalenemu-zipu
  python build_site.py --import
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path

DEST = Path(__file__).resolve().parent
DOCS = DEST / "docs"

CATEGORY_LABELS = {
    "dokumenty": "Dokumenty & návody",
    "idea-files": "Idea files",
    "prompty": "Prompty & šablony",
}


def title_from_md(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def category_for(rel: str) -> tuple[str, str]:
    parts = rel.split("/")
    if len(parts) >= 2:
        key = parts[0]
        return key, CATEGORY_LABELS.get(key, key.replace("-", " ").title())
    return "prehled", "Přehled portálu"


def do_import(root: Path) -> None:
    required = ("dokumenty", "idea-files", "prompty")
    for name in required:
        if not (root / name).is_dir():
            raise SystemExit(f"Import: missing folder {name!r} under {root}")

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    for name in required:
        shutil.copytree(root / name, DOCS / name)

    imgs = DEST / "images"
    if imgs.exists():
        shutil.rmtree(imgs)


def write_manifest() -> int:
    if not DOCS.is_dir():
        raise SystemExit(f"Missing {DOCS}")

    entries: list[dict[str, str]] = []
    for md in sorted(DOCS.rglob("*.md")):
        rel = md.relative_to(DOCS).as_posix()
        raw = md.read_text(encoding="utf-8")
        stem_title = md.stem.replace("-", " ").replace("_", " ").title()
        title = title_from_md(raw, stem_title)
        cat_key, cat_label = category_for(rel)
        entries.append(
            {
                "id": rel[:-3] if rel.endswith(".md") else rel,
                "path": f"docs/{rel}",
                "title": title,
                "category": cat_key,
                "categoryLabel": cat_label,
            }
        )

    (DEST / "manifest.json").write_text(
        json.dumps({"articles": entries}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return len(entries)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--import",
        dest="do_import",
        action="store_true",
        help="Copy dokumenty/, idea-files/, prompty/ from AI_MATERIAL_IMPORT before manifest.",
    )
    args = parser.parse_args()

    if args.do_import:
        root = (
            os.environ.get("AI_MATERIAL_IMPORT", "").strip()
            or os.environ.get("FAIL_PORTAL_IMPORT", "").strip()
        )
        if not root:
            raise SystemExit(
                "Set AI_MATERIAL_IMPORT to the extracted zip folder (dokumenty, idea-files, prompty)."
            )
        do_import(Path(root))

    n = write_manifest()
    print(f"Wrote manifest with {n} articles.")


if __name__ == "__main__":
    main()
