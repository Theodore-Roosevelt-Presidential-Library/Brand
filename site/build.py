#!/usr/bin/env python3
"""Build the brand site (brand.labs.trlibrary.com) into _site/.

Single source of truth: the markdown in plugins/trpl-brand/guide/, the root
docs, integrations/, assets/ and tokens. Nothing here is edited by hand on the
site; change the markdown and rebuild.
"""
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent
OUT = ROOT / "_site"
GUIDE = ROOT / "plugins/trpl-brand/guide"
TOK = ROOT / "plugins/trpl-brand/tokens"
BASE_URL = "https://brand.labs.trlibrary.com"
REPO = "https://github.com/Theodore-Roosevelt-Presidential-Library/Brand"

# source path (relative to ROOT) -> (output file, nav title, nav group)
PAGES = {}


def register():
    guides = []
    for p in GUIDE.glob("*.md"):
        fm, _ = split(p)
        guides.append((fm.get("order", 99), p, fm))
    for order, p, fm in sorted(guides, key=lambda x: x[0]):
        slug = "guide" if p.stem == "README" else p.stem
        PAGES[str(p.relative_to(ROOT))] = (f"{slug}.html", fm["title"], "Guide")
    PAGES["assets/README.md"] = ("assets.html", "Logos and marks", "Assets")
    PAGES["assets/fonts/README.md"] = ("fonts.html", "Fonts", "Assets")
    PAGES["INSTALL.md"] = ("install.html", "Install for Claude", "Use with AI")
    for p in sorted((ROOT / "integrations").glob("*.md")):
        fm, body = split(p)
        title = fm.get("title") or re.search(r"^# (.+)$", body, re.M).group(1)
        PAGES[str(p.relative_to(ROOT))] = (f"{p.stem}.html", title, "Use with AI")
    PAGES["CHANGELOG.md"] = ("changelog.html", "Changelog", "About")
    PAGES["LICENSE.md"] = ("license.html", "License and use", "About")


def split(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        return yaml.safe_load(m.group(1)) or {}, text[m.end():]
    return {}, text


def rewrite_links(htm, src):
    src_dir = (ROOT / src).parent

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#|/)", url):
            return m.group(0)
        path, _, frag = url.partition("#")
        target = (src_dir / path).resolve()
        try:
            rel = str(target.relative_to(ROOT))
        except ValueError:
            return m.group(0)
        if rel in PAGES:
            new = "/" + PAGES[rel][0]
        elif target.is_dir() or rel.startswith("assets/"):
            new = "/" + rel + ("/" if target.is_dir() else "")
        else:
            new = f"{REPO}/blob/main/{rel}"
        return f'{attr}="{new}{"#" + frag if frag else ""}"'

    return re.sub(r'(href|src)="([^"]+)"', fix, htm)


def swatches(htm):
    def sw(m):
        hexv = m.group(1)
        return (f'<button class="swatch" data-copy="{hexv}" title="Copy {hexv}">'
                f'<span class="chip" style="background:{hexv}"></span><code>{hexv}</code></button>')
    return re.sub(r"<code>(#[0-9A-Fa-f]{6})</code>", sw, htm)


def md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
                             extension_configs={"toc": {"permalink": False}})


def nav(current):
    groups = {}
    for src, (out, title, group) in PAGES.items():
        groups.setdefault(group, []).append((out, title))
    parts = []
    for group in ["Guide", "Assets", "Use with AI", "About"]:
        items = "".join(
            f'<li><a href="/{o}"{" aria-current=page" if o == current else ""}>{html.escape(t)}</a></li>'
            for o, t in groups.get(group, []))
        parts.append(f'<div class="nav-group"><p class="nav-label">{group}</p><ul>{items}</ul></div>')
    return "".join(parts)


TEMPLATE = (SITE / "templates/page.html").read_text()


def page(out, title, description, body, current, extra_class=""):
    edit = ""
    for src, (o, _, _) in PAGES.items():
        if o == out:
            edit = f'<p class="edit"><a href="{REPO}/blob/main/{src}">View this page on GitHub</a> · <a href="/guide.html#keeping-the-guide-current">Suggest a change</a></p>'
    htm = (TEMPLATE.replace("{{title}}", html.escape(title))
           .replace("{{description}}", html.escape(description))
           .replace("{{canonical}}", f"{BASE_URL}/{out if out != 'index.html' else ''}")
           .replace("{{nav}}", nav(current))
           .replace("{{body}}", body)
           .replace("{{edit}}", edit)
           .replace("{{class}}", extra_class)
           .replace("{{year}}", str(date.today().year)))
    (OUT / out).write_text(htm)


def asset_gallery():
    blocks = []
    groups = [("Logos", "assets/logos", ["stacked", "horizontal", "boxed"]),
              ("Supporting marks", "assets/marks", ["tr-brand", "tr-values", "elkhorn"])]
    for gtitle, base, subs in groups:
        blocks.append(f"<h2>{gtitle}</h2>")
        for sub in subs:
            d = ROOT / base / sub
            stems = sorted({p.name.rsplit(".", 1)[0].replace("-cmyk", "") for p in d.iterdir()})
            cards = []
            for stem in stems:
                files = sorted(p for p in d.iterdir() if p.name.rsplit(".", 1)[0].replace("-cmyk", "") == stem)
                preview = next((p for p in files if p.suffix == ".svg"), None) or next((p for p in files if p.suffix == ".png"), None)
                dark = "white" in stem
                label = stem.replace("trpl-", "").replace("darkgray", "dark gray").replace("-", " ")
                links = " · ".join(f'<a href="/{p.relative_to(ROOT)}" download>{p.suffix[1:].upper()}{" (CMYK)" if "cmyk" in p.name else ""}</a>' for p in files)
                img = f'<img src="/{preview.relative_to(ROOT)}" alt="{html.escape(label)}" loading="lazy">' if preview else ""
                cards.append(f'<figure class="asset{" on-dark" if dark else ""}"><div class="asset-preview">{img}</div>'
                             f'<figcaption><span class="asset-name">{html.escape(label)}</span><span class="asset-links">{links}</span></figcaption></figure>')
            blocks.append(f'<h3>{sub.replace("-", " ").title().replace("Tr ", "TR ")}</h3><div class="asset-grid">{"".join(cards)}</div>')
    return "\n".join(blocks)


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    register()
    shutil.copytree(SITE / "static", OUT / "static")
    shutil.copytree(ROOT / "assets", OUT / "assets")
    shutil.copytree(TOK, OUT / "tokens")
    (OUT / "CNAME").write_text("brand.labs.trlibrary.com\n")
    (OUT / ".nojekyll").write_text("")

    contrast = md((TOK / "contrast.md").read_text())
    full = [f"# Theodore Roosevelt Presidential Library — brand guide (full text)\n\n"
            f"Source: {REPO}\nSite: {BASE_URL}\nGenerated: {date.today().isoformat()}\n"]

    for src, (out, title, group) in PAGES.items():
        fm, body = split(ROOT / src)
        desc = fm.get("description", "")
        if not desc:
            first = re.search(r"^(?!#)(\S.+)$", body, re.M)
            desc = first.group(1)[:155] if first else title
        htm = md(body)
        htm = htm.replace("<p><!-- contrast-table --></p>", contrast).replace("<!-- contrast-table -->", contrast)
        htm = swatches(htm)
        if out == "assets.html":
            htm = asset_gallery() + htm.replace("<h1>Brand assets</h1>", "")
            htm = "<h1>Logos and marks</h1>" + htm
        htm = rewrite_links(htm, src)
        cls = "page-" + out[:-5]
        page(out, title, desc, f'<article class="prose">{htm}</article>', out, cls)
        if src.startswith("plugins/") or src.startswith("assets/fonts"):
            full.append(f"\n\n---\n\n<!-- {src} -->\n\n" + body.replace("<!-- contrast-table -->", (TOK / "contrast.md").read_text()))

    # Home
    home = (SITE / "templates/home.html").read_text()
    page("index.html", "Brand", "Brand guide, logos, fonts and AI tools for the Theodore Roosevelt Presidential Library.",
         home, "index.html", "page-home")

    # Machine-readable
    tokens = json.loads((TOK / "tokens.json").read_text())
    full.append("\n\n---\n\n## Design tokens (tokens.json)\n\n```json\n" + json.dumps(tokens, indent=2) + "\n```\n")
    (OUT / "llms-full.txt").write_text("".join(full))
    llms = ["# Theodore Roosevelt Presidential Library — Brand\n",
            "> Brand standards for the Theodore Roosevelt Presidential Library: voice, editorial style, visual identity, design tokens, logos, fonts, Roosevelt orientation and media sources. Historical facts are verified separately by HistorianPanel.\n",
            "\nFor the whole guide in one file, read /llms-full.txt. To install the Claude plugin, read /install.html.\n",
            "\n## Guide\n"]
    for src, (out, title, group) in PAGES.items():
        fm, _ = split(ROOT / src)
        llms.append(f"- [{title}]({BASE_URL}/{out}): {fm.get('description', '')}\n")
    llms += ["\n## Machine-readable\n",
             f"- [Full guide as text]({BASE_URL}/llms-full.txt)\n",
             f"- [Design tokens, W3C format]({BASE_URL}/tokens/tokens.json)\n",
             f"- [CSS variables]({BASE_URL}/tokens/tokens.css)\n",
             f"- [Tailwind preset]({BASE_URL}/tokens/tailwind.preset.js)\n",
             f"- [Repository]({REPO})\n",
             "\n## Related\n",
             "- [HistorianPanel](https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel): historical accuracy specialists for Theodore Roosevelt history\n"]
    (OUT / "llms.txt").write_text("".join(llms))
    (OUT / "404.html").write_text((OUT / "index.html").read_text())
    print(f"built {len(PAGES) + 1} pages into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
