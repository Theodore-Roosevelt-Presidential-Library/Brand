# TRPL Brand Kit: instructions for Claude

You are working with the brand kit of the Theodore Roosevelt Presidential
Library in Medora, North Dakota. This file says what the kit is, when to use
it, how to install and update it, and how to maintain it. It applies in Claude
Code, the Claude desktop app, and any session with this repository open.

## What it is

A Claude plugin (`plugins/trpl-brand`) plus the brand's source files:

- **`guide/`**: the brand guide in markdown. It is the source of truth for the
  skills and the website. Read the relevant page before writing or reviewing.
- **Skills** (`skills/`): `write-on-brand`, `style-review`, `design-review`,
  `design-brief`, `tr-knowledge`, `find-tr-media`, `historian-handoff`,
  `brand-review`, `update-style-guide`, `brand-setup`.
- **Agents** (`agents/`): `brand-copy-reviewer` and `brand-design-reviewer`
  (independent reviews), `brand-guide-steward` (reviews guide changes).
- **Tokens** (`tokens/`): colors and fonts as W3C design tokens, CSS and Tailwind.
- **Assets** (`assets/`, repository root): logos, marks, licensed fonts.

## When to use it

Use the kit **every time** you write, edit, design or review anything that will
carry the Library's name, whether or not the person mentions the brand:

| Request | Skill |
|---------|-------|
| Write, draft, rewrite, shorten | `trpl-brand:write-on-brand` |
| Check, proof, edit for style | `trpl-brand:style-review` |
| "Is this design on brand?" | `trpl-brand:design-review` |
| Make a graphic, slide, poster, flyer | `trpl-brand:design-brief` |
| Background on T.R. for creative work | `trpl-brand:tr-knowledge` |
| A photo or film of T.R., or the Library | `trpl-brand:find-tr-media` |
| Any historical fact, quote or image ID | `trpl-brand:historian-handoff` |
| "Is this ready to ship?" | `trpl-brand:brand-review` |
| "Add a rule," "we always/never..." | `trpl-brand:update-style-guide` |
| Install, update, "is it working?" | `trpl-brand:brand-setup` |

## Non-negotiables

1. **Historical accuracy.** Two independent sources for every historical claim.
   Your own output is never a source. Hand off to HistorianPanel.
2. **T.R. is quoted verbatim, or not at all.** Never write a Roosevelt quote
   from memory.
3. **Nonpartisan.** Shared values, never current political debates.
4. **Real photographs.** No renderings; no AI images of people, the Library or
   any identifiable building.
5. **Terminology:** participants, Trustees, Benefactors, T.R. (never "Teddy"
   except #TeddyRoosevelt), buttes, Kettle Hill / San Juan Heights, the Library,
   "pursuing" certification, "independently operated."
6. **Design in Canva** with the Library's brand kit unless told otherwise.

## Installing and updating

See [INSTALL.md](INSTALL.md). Marketplace `trpl-brand`, plugin
`trpl-brand@trpl-brand`. Companion: `historian-panel@trpl-historian`. The plugin
has no pinned version, so every merged commit is a new version; updates come
through marketplace update or auto-update.

## Maintaining the kit (you may and should do this)

- Change rules only through `trpl-brand:update-style-guide`: branch
  `guide/<name>-<yyyymmdd>`, edit the guide, add a CHANGELOG line, run the
  checks, get the `brand-guide-steward` review, open a pull request.
- Never push to `main`, merge or approve. A person in Marketing &
  Communications merges.
- Never edit an installed copy of the plugin.
- After changing `tokens/tokens.json`, run `python scripts/build_tokens.py`.

## This repository is public

Never commit: staff names or contact details (use roles; the only address in
the repo is hello@trlibrary.com), internal hostnames or file paths,
credentials, unapproved figures (finance, attendance, sustainability
performance), licensed text, or claim-ledger contents. Fonts are here by the
Library's decision, with a license notice; don't add other licensed files
without the same notice.

## Checks

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_repo.py
python site/build.py
claude plugin validate .
```

## Map

```
.claude-plugin/marketplace.json   marketplace "trpl-brand"
.claude/settings.json             enables this kit and HistorianPanel in this repo
plugins/trpl-brand/
  .claude-plugin/plugin.json      plugin "trpl-brand"
  guide/                          the brand guide (source of truth)
  skills/  agents/                Claude skills and agents
  tokens/                         design tokens and generated CSS/Tailwind
assets/                           logos, marks, fonts (served by the site)
integrations/                     Canva, Claude Design, other AI tools
site/                             website builder and templates
scripts/                          checks and token builder
```
