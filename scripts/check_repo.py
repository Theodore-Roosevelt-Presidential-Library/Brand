#!/usr/bin/env python3
"""Repository checks for the TRPL Brand Kit.

- Skills and agents have valid frontmatter
- Guide pages have frontmatter and their relative links resolve
- Nothing private slips into this public repository
- Generated token files are current
"""
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins/trpl-brand"
errors = []


def front(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


# Skills
for skill in sorted((PLUGIN / "skills").glob("*/SKILL.md")):
    fm, body = front(skill)
    name = skill.parent.name
    if fm.get("name") != name:
        errors.append(f"{skill.relative_to(ROOT)}: name must be '{name}'")
    desc = fm.get("description", "")
    if not 40 <= len(desc) <= 1024:
        errors.append(f"{skill.relative_to(ROOT)}: description must be 40-1024 characters")
    if "claude" in name or "anthropic" in name:
        errors.append(f"{skill.relative_to(ROOT)}: skill names may not contain 'claude' or 'anthropic'")
    for ref in re.findall(r"`(guide/[\w\-./]+\.md)", body):
        if not (PLUGIN / ref).exists():
            errors.append(f"{skill.relative_to(ROOT)}: points at missing {ref}")
    for ref in re.findall(r"`trpl-brand:([\w-]+)`", body):
        if not (PLUGIN / "skills" / ref).exists():
            errors.append(f"{skill.relative_to(ROOT)}: points at missing skill trpl-brand:{ref}")

# Agents
for agent in sorted((PLUGIN / "agents").glob("*.md")):
    fm, _ = front(agent)
    if fm.get("name") != agent.stem or not fm.get("description"):
        errors.append(f"{agent.relative_to(ROOT)}: needs name '{agent.stem}' and a description")

# Guide pages and links
md_files = list((PLUGIN / "guide").glob("*.md")) + list(ROOT.glob("*.md")) + \
    list((ROOT / "integrations").glob("*.md")) + list((ROOT / "assets").rglob("README.md"))
for page in (PLUGIN / "guide").glob("*.md"):
    fm, _ = front(page)
    if not fm.get("title") or not fm.get("description"):
        errors.append(f"{page.relative_to(ROOT)}: needs title and description")
for page in md_files:
    text = page.read_text()
    for link in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|mailto:|#)", link):
            continue
        target = (page.parent / link.split("#")[0]).resolve()
        if not target.exists():
            errors.append(f"{page.relative_to(ROOT)}: broken link {link}")

# Public-repository safety
PRIVATE = [
    (r"\b\d{3}[-.]\d{3}[-.]\d{4}\b", "phone number"),
    (r"\b192\.168\.\d+\.\d+\b|\b10\.\d+\.\d+\.\d+\b", "private IP address"),
    (r"briney\.me|mcp\.\w+\.\w+/mcp", "internal host"),
    (r"/Users/\w+|~/TRPL|OneDrive-", "personal file path"),
    (r"(api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}", "credential"),
]
ALLOWED_EMAILS = {"hello@trlibrary.com", "noreply@anthropic.com"}
scan = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix in {".md", ".json", ".yml", ".yaml", ".py", ".html", ".css", ".js", ".txt"}
        and ".git" not in p.parts and ".venv" not in p.parts and "_site" not in p.parts]
for p in scan:
    text = p.read_text(errors="ignore")
    for pat, what in PRIVATE:
        if p.name == "check_repo.py":
            continue
        if re.search(pat, text, re.I):
            errors.append(f"{p.relative_to(ROOT)}: looks like a {what}")
    for email in re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text):
        if email.lower() not in ALLOWED_EMAILS and not email.endswith("@users.noreply.github.com"):
            errors.append(f"{p.relative_to(ROOT)}: email address {email} (use roles, not personal contacts)")

# Tokens
r = subprocess.run([sys.executable, str(ROOT / "scripts/build_tokens.py"), "--check"], capture_output=True, text=True)
if r.returncode:
    errors.append(r.stdout.strip())

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("all checks passed")
