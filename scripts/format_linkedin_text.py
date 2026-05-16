#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n?", re.DOTALL)
NUMBERED_STEP_RE = re.compile(r"^\d+\.\s+\S+")
BULLET_RE = re.compile(r"^\s*(?:[-*+] |• )")
HEADING_RE = re.compile(r"^#{1,6}\s+")


def split_frontmatter(text: str) -> tuple[str, str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    match = FRONTMATTER_RE.match(normalized)
    if not match:
        return "", normalized
    return match.group(0).rstrip("\n") + "\n\n", normalized[match.end() :]


def collapse_blank_lines(lines: list[str]) -> list[str]:
    result: list[str] = []
    blank_count = 0
    for line in lines:
        if line == "":
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
            continue
        blank_count = 0
        result.append(line)
    return result


def ensure_blank_before(result: list[str]) -> None:
    if result and result[-1] != "":
        result.append("")


def format_body(body: str) -> str:
    raw_lines = [line.rstrip() for line in body.split("\n")]
    raw_lines = collapse_blank_lines(raw_lines)

    result: list[str] = []
    previous_was_numbered = False
    previous_was_bullet = False

    for line in raw_lines:
        stripped = line.strip()
        is_blank = stripped == ""
        is_heading = bool(HEADING_RE.match(stripped))
        is_numbered = bool(NUMBERED_STEP_RE.match(stripped))
        is_bullet = bool(BULLET_RE.match(line))

        if is_blank:
            result.append("")
            previous_was_numbered = False
            previous_was_bullet = False
            continue

        if is_heading:
            ensure_blank_before(result)
        elif is_numbered:
            ensure_blank_before(result)
        elif previous_was_numbered and not is_numbered:
            ensure_blank_before(result)
        elif is_bullet and not previous_was_bullet:
            ensure_blank_before(result)

        result.append(line)
        previous_was_numbered = is_numbered
        previous_was_bullet = is_bullet

    result = collapse_blank_lines(result)
    while result and result[0] == "":
        result.pop(0)
    while result and result[-1] == "":
        result.pop()
    return "\n".join(result) + "\n"


def format_text(text: str) -> str:
    frontmatter, body = split_frontmatter(text)
    return frontmatter + format_body(body)


def markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Format LinkedIn Markdown text without semantic rewriting.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    changed: list[Path] = []
    for path in markdown_files(args.paths):
        original = path.read_text(encoding="utf-8")
        formatted = format_text(original)
        if original == formatted:
            continue
        changed.append(path)
        if args.write:
            path.write_text(formatted, encoding="utf-8")

    if changed and args.check:
        for path in changed:
            print(f"LINKEDIN_FORMATTING_ERROR file={path}")
        return 1

    if changed:
        for path in changed:
            print(f"LINKEDIN_FORMATTED file={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
