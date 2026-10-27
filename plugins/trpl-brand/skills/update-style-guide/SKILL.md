---
name: update-style-guide
description: "Add, change or retire a rule in the Theodore Roosevelt Presidential Library's brand and editorial style guide through a reviewed pull request. Use when someone says 'add this to the style guide', 'make this a rule', 'we always/never write X', 'update the brand guide', when a style question comes up that the guide doesn't answer, or when the same correction keeps being made."
---

# Update the style guide

The guide lives in
`https://github.com/Theodore-Roosevelt-Presidential-Library/Brand`, under
`plugins/trpl-brand/guide/`. Changes reach everyone through a pull request a
person merges, then the next plugin update and site build.

## 1. Pin down the rule

From the request, write:

- **Rule:** one sentence, with its level: **Always**, **Never** or **Prefer**.
- **Why:** one sentence.
- **Example:** before and after, if it helps.
- **Scope:** all copy, or a channel.
- **Who decided it:** the person and date, if a decision was made. Staff only
  in the pull request description, never in the guide (the repository is
  public; use roles).

If it is unclear whether this is a standing rule or a one-off preference for
one piece, ask.

## 2. Check it against the guide

Read every file in `guide/`. Then:

- **Duplicate?** Strengthen the existing entry instead of adding another.
- **Conflict?** If it contradicts the guide, the Brand Style Guide v0.1 or the
  Story Guide, say so and propose how to resolve it. Visual rules can't
  override the Brand Style Guide; tone and terminology rules can't override the
  Story Guide without saying so explicitly (as the "Teddy" rule does).
- **Placement:** the right page and, in the editorial guide, the right
  alphabetical entry. Add it to the quick-reference table if it is a word swap.
- **Open questions:** if it settles one listed under "Open questions," remove
  it from that list.

## 3. Make the change

1. Clone the repository (or use an existing clone), and create a branch named
   `guide/<short-name>-<yyyymmdd>`.
2. Edit the guide file(s). Match the existing format: entry heading, bold rule
   level, short reason, example.
3. Add a line to `CHANGELOG.md` under today's date: `- <Rule> (<page>)`.
4. Run the checks:

   ```
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   python scripts/check_repo.py
   python site/build.py
   ```

5. Ask the `brand-guide-steward` agent to review the diff. Address what it finds.
6. Commit, push and open a pull request with the rule, the reason, who decided,
   and the steward's recommendation. Label it `style-guide`.

Never push to `main`, merge or approve. A member of Marketing & Communications
merges.

## 4. Without repository access

Draft the change as above and give it to the person to send to Marketing &
Communications, or open a GitHub issue with it if they can.

## Never put in the guide

Staff names or contact details, internal system links, figures that need
approval, licensed text, or anything historical stated as fact (historical
rules say where to verify, not what is true).
