#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - only used in minimal environments
    yaml = None


SUPPORTED_SECTIONS = {
    "profile_headline",
    "about",
    "experience_description",
    "project_title",
    "project_description",
    "post",
    "comment",
    "article_title",
    "article_body",
}

COMPRESSION_HINT = """Compression priorities:
Preserve:
1. quantified hook
2. reader benefit
3. proof metrics
4. mechanism/framework
5. CTA

Remove first:
1. filler words
2. repeated qualifiers
3. duplicated concepts
4. excessive internal details
5. weak adjectives
6. redundant setup"""


@dataclass(frozen=True)
class MarkdownDocument:
    path: Path
    frontmatter: dict[str, Any]
    body: str


def load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise SystemExit("Install PyYAML to read YAML config files: pip install pyyaml")
    text = path.read_text(encoding="utf-8")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if normalized.startswith("---\n"):
        end = normalized.find("\n---\n", 4)
        if end != -1:
            normalized = normalized[4:end]
    data = yaml.safe_load(normalized) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be an object: {path}")
    return data


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {path}")
    end = normalized.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"Unclosed YAML frontmatter: {path}")
    raw_frontmatter = normalized[4:end]
    body = normalized[end + len("\n---\n") :]
    if yaml is None:
        raise SystemExit("Install PyYAML to parse Markdown frontmatter: pip install pyyaml")
    frontmatter = yaml.safe_load(raw_frontmatter) or {}
    if not isinstance(frontmatter, dict):
        raise ValueError(f"Frontmatter must be a YAML object: {path}")
    return frontmatter, body


def markdown_documents(paths: list[Path]) -> list[MarkdownDocument]:
    docs: list[MarkdownDocument] = []
    for root in paths:
        candidates = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for path in candidates:
            if path.suffix.lower() != ".md":
                continue
            frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"), path)
            if frontmatter.get("platform") != "linkedin":
                continue
            docs.append(MarkdownDocument(path=path, frontmatter=frontmatter, body=body))
    return docs


def yaml_asset_specs(paths: list[Path]) -> list[tuple[Path, dict[str, Any]]]:
    specs: list[tuple[Path, dict[str, Any]]] = []
    for root in paths:
        candidates = [root] if root.is_file() else sorted(root.rglob("*"))
        for path in candidates:
            if path.suffix.lower() not in {".yaml", ".yml"}:
                continue
            data = load_yaml(path)
            if data.get("platform") == "linkedin" and data.get("asset_type"):
                specs.append((path, data))
    return specs


def raw_count(text: str) -> int:
    return len(text)


def utf16_count(text: str) -> int:
    return len(text.encode("utf-16-le")) // 2


def count_text(text: str, mode: str) -> int:
    if mode == "raw_unicode_codepoints":
        return len(text)
    if mode == "non_newline_unicode_codepoints":
        return len(text.replace("\n", "").replace("\r", ""))
    if mode == "non_whitespace_unicode_codepoints":
        return len(re.sub(r"\s+", "", text))
    if mode == "utf16_code_units":
        return utf16_count(text)
    raise ValueError(f"Unsupported count mode: {mode}")


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


def validate_markdown(docs: list[MarkdownDocument], config: dict[str, Any]) -> bool:
    ok = True
    limits = config.get("character_limits", {})
    soft_targets = config.get("soft_targets", {})

    for doc in docs:
        section = doc.frontmatter.get("section")
        if section not in SUPPORTED_SECTIONS:
            print(f"LINKEDIN_VALIDATION_ERROR file={relative(doc.path)} section={section} error=unsupported_section")
            ok = False
            continue
        if section not in limits:
            print(f"LINKEDIN_VALIDATION_ERROR file={relative(doc.path)} section={section} error=missing_limit")
            ok = False
            continue

        section_config = limits[section]
        max_chars = int(section_config["max_chars"])
        count_mode = section_config.get("count_mode", "non_newline_unicode_codepoints")
        actual = count_text(doc.body, count_mode)
        raw = raw_count(doc.body)
        utf16 = utf16_count(doc.body)

        if actual > max_chars:
            over_by = actual - max_chars
            print(
                "LINKEDIN_VALIDATION_ERROR "
                f"file={relative(doc.path)} section={section} actual={actual} max={max_chars} "
                f"over_by={over_by} count_mode={count_mode} raw_count={raw} "
                f"utf16_code_units_count={utf16}"
            )
            print()
            print(COMPRESSION_HINT)
            ok = False
            continue

        target = soft_targets.get(section)
        if target:
            ideal_min = target.get("ideal_min_chars")
            ideal_max = target.get("ideal_max_chars")
            if ideal_min is not None and actual < int(ideal_min):
                print(
                    "LINKEDIN_SOFT_TARGET_WARNING "
                    f"file={relative(doc.path)} section={section} actual={actual} ideal_min={ideal_min}"
                )
            if ideal_max is not None and actual > int(ideal_max):
                print(
                    "LINKEDIN_SOFT_TARGET_WARNING "
                    f"file={relative(doc.path)} section={section} actual={actual} ideal_max={ideal_max}"
                )

        print(
            "LINKEDIN_VALIDATION_OK "
            f"file={relative(doc.path)} section={section} actual={actual} max={max_chars} "
            f"count_mode={count_mode} raw_count={raw} utf16_code_units_count={utf16}"
        )

    return ok


def image_size_with_pillow(path: Path) -> tuple[int, int] | None:
    try:
        from PIL import Image
    except ImportError:
        return None
    with Image.open(path) as image:
        return image.size


def declared_size(spec: dict[str, Any]) -> tuple[int, int] | None:
    if "width" in spec and "height" in spec:
        return int(spec["width"]), int(spec["height"])
    return None


def validate_image_specs(specs: list[tuple[Path, dict[str, Any]]], config: dict[str, Any]) -> bool:
    ok = True
    image_specs = config.get("image_specs", {})

    for spec_path, spec in specs:
        asset_type = str(spec.get("asset_type", ""))
        spec_config = image_specs.get(asset_type, {})
        asset_path = spec.get("path")
        size = declared_size(spec)

        if asset_type not in {"profile_banner", "profile_photo"} and size is None:
            print(f"LINKEDIN_IMAGE_VALIDATION_OK file={relative(spec_path)} asset_type={asset_type} check=metadata_only")
            continue

        if asset_path and size is None:
            image_path = Path(asset_path)
            if not image_path.is_absolute():
                image_path = spec_path.parent / image_path
            if not image_path.exists():
                print(
                    "LINKEDIN_IMAGE_VALIDATION_ERROR "
                    f"file={relative(spec_path)} asset_type={asset_type} path={asset_path} error=missing_image_file"
                )
                ok = False
                continue
            size = image_size_with_pillow(image_path)
            if size is None:
                print("Install pillow to validate image dimensions: pip install pillow")
                print(
                    "LINKEDIN_IMAGE_VALIDATION_ERROR "
                    f"file={relative(spec_path)} asset_type={asset_type} path={asset_path} error=pillow_missing"
                )
                ok = False
                continue

        if size is None:
            print(f"LINKEDIN_IMAGE_VALIDATION_OK file={relative(spec_path)} asset_type={asset_type} check=metadata_only")
            continue

        width, height = size
        if asset_type == "profile_banner":
            expected_width = int(spec_config["width"])
            expected_height = int(spec_config["height"])
            allow_scaled = bool(spec.get("allow_scaled", False))
            if allow_scaled:
                if width < expected_width or height < expected_height or width * expected_height != height * expected_width:
                    print(
                        "LINKEDIN_IMAGE_VALIDATION_ERROR "
                        f"file={relative(spec_path)} asset_type={asset_type} width={width} height={height} "
                        f"expected_aspect_ratio={spec_config.get('aspect_ratio')} min_width={expected_width} "
                        f"min_height={expected_height}"
                    )
                    ok = False
                    continue
            elif width != expected_width or height != expected_height:
                print(
                    "LINKEDIN_IMAGE_VALIDATION_ERROR "
                    f"file={relative(spec_path)} asset_type={asset_type} width={width} height={height} "
                    f"expected_width={expected_width} expected_height={expected_height}"
                )
                ok = False
                continue

        elif asset_type == "profile_photo":
            min_width = int(spec_config["min_width"])
            min_height = int(spec_config["min_height"])
            require_square = bool(spec_config.get("require_square", True))
            if width < min_width or height < min_height or (require_square and width != height):
                print(
                    "LINKEDIN_IMAGE_VALIDATION_ERROR "
                    f"file={relative(spec_path)} asset_type={asset_type} width={width} height={height} "
                    f"min_width={min_width} min_height={min_height} require_square={str(require_square).lower()}"
                )
                ok = False
                continue

        print(f"LINKEDIN_IMAGE_VALIDATION_OK file={relative(spec_path)} asset_type={asset_type} width={width} height={height}")

    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate LinkedIn Markdown content and image specs.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--config", type=Path, default=Path("config/linkedin_limits.yaml"))
    args = parser.parse_args()

    config = load_yaml(args.config)
    docs = markdown_documents(args.paths)
    specs = yaml_asset_specs(args.paths)

    text_ok = validate_markdown(docs, config)
    image_ok = validate_image_specs(specs, config)
    return 0 if text_ok and image_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
