# Contributing

## Who decides

Marketing & Communications owns the brand. Anyone can propose a change; a
member of that team reviews and merges it.

## Proposing a change

- **With Claude:** say "add a rule to the style guide: ..." or "change the rule
  on ...". The `update-style-guide` skill drafts the change, checks it against
  the rest of the guide, gets an independent review from the
  `brand-guide-steward` agent, and opens a pull request.
- **By hand:** branch, edit the markdown in `plugins/trpl-brand/guide/`, add a
  line to `CHANGELOG.md`, run the checks, open a pull request.
- **Not on GitHub:** send the rule, the reason and an example to your Marketing
  & Communications contact.

## What a good rule looks like

- One sentence with a level: **Always**, **Never** or **Prefer**
- One sentence of why
- A before-and-after example when it helps
- In the right alphabetical place, and in the quick-reference table if it is a
  word swap

## Hierarchy

The [Brand Style Guide](https://www.trlibrary.com/brand) governs visual rules.
The [Story Guide](https://www.trlibrary.com/storyguide) governs tone,
terminology and naming. A rule here that departs from either must say so
explicitly.

## Checks

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_repo.py
python site/build.py
```

CI runs the same checks on every pull request and publishes the site when
`main` changes.

## Never commit

Staff names or contact details (use roles), internal links or file paths,
credentials, unapproved figures, licensed text, or new licensed files without
a license notice.

## Agents

Agents work on branches and open pull requests. They never push to `main`,
merge or approve.
