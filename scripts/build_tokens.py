#!/usr/bin/env python3
"""Generate token outputs from plugins/trpl-brand/tokens/tokens.json.

Writes tokens.css, tailwind.preset.js and contrast.md next to tokens.json.
Run with --check to fail if the generated files are out of date.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOK = ROOT / "plugins/trpl-brand/tokens"


def load():
    return json.loads((TOK / "tokens.json").read_text())


def flat_colors(t):
    out = []
    for group, items in t["color"].items():
        for key, e in items.items():
            if key.startswith("$"):
                continue
            out.append((group, key, e["$value"], e["$extensions"]["org.trlibrary"]["name"]))
    return out


def lum(hexv):
    h = hexv.lstrip("#")
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def grade(r):
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA"
    if r >= 3:
        return "AA large"
    return "Fail"


def css(t):
    lines = ["/* Generated from tokens.json by scripts/build_tokens.py. Do not edit. */", ":root {"]
    for group, key, hexv, name in flat_colors(t):
        lines.append(f"  --trpl-{key}: {hexv}; /* {name} ({group}) */")
    for key, e in t["font"].items():
        if key.startswith("$"):
            continue
        fam = ", ".join(f'"{f}"' if " " in f else f for f in e["$value"])
        lines.append(f"  --trpl-font-{key}: {fam};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def tailwind(t):
    colors = {key: hexv for _, key, hexv, _ in flat_colors(t)}
    fonts = {k: e["$value"] for k, e in t["font"].items() if not k.startswith("$")}
    body = json.dumps({"theme": {"extend": {"colors": {"trpl": colors}, "fontFamily": fonts}}}, indent=2)
    return "// Generated from tokens.json by scripts/build_tokens.py. Do not edit.\n" \
           "// Usage: presets: [require('./tailwind.preset.js')]\nmodule.exports = " + body + ";\n"


def contrast(t):
    cols = flat_colors(t)
    bgs = [c for c in cols if c[0] == "background"]
    head = "| Text color | " + " | ".join(f"on {b[3]}" for b in bgs) + " |"
    sep = "|" + "---|" * (len(bgs) + 1)
    rows = [head, sep]
    for _, _, hexv, name in cols:
        cells = []
        for _, _, bhex, bname in bgs:
            if bname == name:
                cells.append("—")
            else:
                r = ratio(hexv, bhex)
                cells.append(f"{r:.1f} {grade(r)}")
        rows.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(rows) + "\n"


def main():
    t = load()
    outputs = {"tokens.css": css(t), "tailwind.preset.js": tailwind(t), "contrast.md": contrast(t)}
    stale = []
    for name, content in outputs.items():
        p = TOK / name
        if "--check" in sys.argv:
            if not p.exists() or p.read_text() != content:
                stale.append(name)
        else:
            p.write_text(content)
    if stale:
        print("Out of date: " + ", ".join(stale) + ". Run python scripts/build_tokens.py")
        sys.exit(1)
    print("tokens ok")


if __name__ == "__main__":
    main()
