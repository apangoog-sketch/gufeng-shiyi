#!/usr/bin/env python3
"""Offline structural validation; does not perform image generation or model evaluation."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "README.md", "README.en.md", "LICENSE", "skill.json",
    "agents/openai.yaml", "references/look.md", "references/params.md",
    "references/recipes.md", "anti-slop-system.md", "adapters/general.md",
    "scripts/validate_skill.py", "tests/cases.json",
]
ZH_SECTIONS = ["功能", "范围", "安装", "使用方法", "LOOK", "项目结构", "验证", "许可证"]
EN_SECTIONS = ["Features", "Scope", "Installation", "Usage", "LOOK", "Project structure", "Validation", "License"]

def validate():
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append("Missing: " + relative)
    if errors:
        return errors
    meta = json.loads((ROOT / "skill.json").read_text(encoding="utf-8"))
    slug, name = meta["name"], meta["display_name"]
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n([\s\S]*?)\n---\n", skill)
    if not front or "name: " + slug not in front.group(1):
        errors.append("Invalid frontmatter/name")
    if ROOT.name != slug or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        errors.append("Folder and invocation name must agree")
    if meta["look_count"] != 1 or meta["license"] != "LicenseRef-AP-Image-Personal-Study-1.0":
        errors.append("Expected one LOOK and personal-study license")
    look = (ROOT / "references/look.md").read_text(encoding="utf-8")
    if not look.startswith("# " + name + "\n") or re.search(r"^## \d{2} ", look, re.M):
        errors.append("Expected exactly one unnumbered LOOK")
    for carrier in ["Identity:", "Framing:", "Texture:", "Mood:", "Avoid:"]:
        if carrier not in look:
            errors.append("Missing LOOK carrier: " + carrier)
    ui = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if 'display_name: "' + name + '"' not in ui or "$" + slug not in ui:
        errors.append("UI identity/invocation mismatch")
    for doc, headings in [("README.md", ZH_SECTIONS), ("README.en.md", EN_SECTIONS)]:
        text = (ROOT / doc).read_text(encoding="utf-8")
        for heading in headings:
            if "## " + heading + "\n" not in text:
                errors.append(doc + ": missing " + heading)
        if "$" + slug not in text or "LICENSE" not in text:
            errors.append(doc + ": missing invocation/license")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "仅许可自然人为个人、非商业" not in license_text or "No commercial use" not in license_text:
        errors.append("License is missing personal-study/non-commercial terms")
    cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
    if {c["kind"] for c in cases} != {"prompt", "reference", "render", "conflict", "bare", "unavailable-tool"}:
        errors.append("Behavior fixtures are incomplete")
    if any("$" + slug not in c["input"] for c in cases):
        errors.append("Fixture invocation mismatch")
    forbidden = ["ap-image-stylization", "references/presets.md", "prompt-workflow.md", "MIT License"]
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".mp4", ".mov", ".mkv", ".avi", ".zip"}:
            errors.append("Unexpected media/archive: " + str(path.relative_to(ROOT)))
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for term in forbidden:
            if term in text:
                errors.append(str(path.relative_to(ROOT)) + ": stale reference " + term)
        if re.search(r"[A-Z]:[\\/]Users[\\/]", text, re.I):
            errors.append("Local user path: " + str(path.relative_to(ROOT)))
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "#")):
                continue
            relative = target.split("#")[0]
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                errors.append("Broken/external local link: " + target)
    return errors

if __name__ == "__main__":
    try:
        issues = validate()
    except (KeyError, ValueError, OSError) as exc:
        issues = [str(exc)]
    if issues:
        print("FAIL\n" + "\n".join(issues))
        sys.exit(1)
    print("PASS: standalone single LOOK, bilingual docs, links, license, and behavior fixtures")
    print("Structural checks only; model behavior and image quality are not evaluated.")

