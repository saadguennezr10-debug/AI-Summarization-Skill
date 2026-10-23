#!/usr/bin/env python3
"""Small dependency-free sanity checker for this repository's distributable skill."""

from pathlib import Path
import re
import sys


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1] / "ai-summarization-skill"
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.is_file():
        return fail(f"Missing skill file: {skill_file}")

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return fail("SKILL.md must start with YAML frontmatter delimited by ---.")

    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return fail("Could not parse the opening frontmatter block.")

    frontmatter = parts[1]
    body = parts[2].lstrip("\r\n")
    fields = {}
    for line in frontmatter.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*?)\s*$", line)
        if match:
            key, value = match.groups()
            if key in fields:
                return fail(f"Duplicate frontmatter key: {key}")
            fields[key] = value.strip().strip('"').strip("'")

    for key in ("name", "description"):
        if not fields.get(key):
            return fail(f"Missing required frontmatter field: {key}")

    name = fields["name"]
    if len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        return fail("name must be kebab-case, lowercase, and at most 64 characters.")
    if name != skill_dir.name:
        return fail(f"name ({name}) must match skill directory ({skill_dir.name}).")

    description = fields["description"]
    if len(description) > 1024 or "<" in description or ">" in description:
        return fail("description must be at most 1024 characters and contain no angle brackets.")

    if not body.lstrip().startswith("# "):
        return fail("The skill body must start with a level-one Markdown heading.")

    line_count = len(text.splitlines())
    if line_count > 500:
        return fail(f"SKILL.md is {line_count} lines; keep it at 500 lines or fewer.")

    print(f"OK: {skill_file.relative_to(Path(__file__).resolve().parents[1])}")
    print(f"Name: {name}")
    print(f"Lines: {line_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
