#!/usr/bin/env python3
"""Hide GitBook's right-hand page outline on every page in SUMMARY.md
except those in the Reference group, where long API pages need it.

Safe to re-run: pages that already have a `layout:` block are left alone.
Run from the repo root: python3 scripts/hide-outline.py
"""
import re
from pathlib import Path

KEEP_OUTLINE_GROUPS = {"Reference"}

LAYOUT = """layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
"""


def pages():
    group = None
    for line in Path("SUMMARY.md").read_text().splitlines():
        if line.startswith("## "):
            group = line[3:].strip()
            continue
        m = re.search(r"\]\(([^)]+\.md)\)", line)
        if m and group not in KEEP_OUTLINE_GROUPS:
            yield Path(m.group(1))


def hide(path: Path) -> bool:
    text = path.read_text()
    if text.startswith("---\n"):
        end = text.index("\n---", 3)
        front = text[4:end + 1]
        if re.search(r"^layout:", front, re.M):
            return False
        text = "---\n" + front + LAYOUT + text[end + 1:]
    else:
        text = "---\n" + LAYOUT + "---\n\n" + text
    path.write_text(text)
    return True


if __name__ == "__main__":
    changed = [p for p in dict.fromkeys(pages()) if p.exists() and hide(p)]
    print(f"Outline hidden on {len(changed)} pages")
