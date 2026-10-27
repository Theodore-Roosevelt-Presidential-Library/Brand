---
name: brand-setup
description: "Install, update, check or troubleshoot the TRPL Brand Kit, and install HistorianPanel alongside it. Use when someone asks to set up the brand kit, the Library's brand tools, the style guide plugin, or asks whether it is up to date, or when brand skills seem missing or stale. Configures itself without questions."
---

# Brand kit setup, updates and health check

The repository is `https://github.com/Theodore-Roosevelt-Presidential-Library/Brand`.
The marketplace is `trpl-brand` and the plugin is `trpl-brand@trpl-brand`.
HistorianPanel (historical accuracy) is a companion plugin:
`historian-panel@trpl-historian` from
`Theodore-Roosevelt-Presidential-Library/HistorianPanel`.

Tell the person in one line what you are about to do, then do it. Ask before
installing anything or changing settings.

## 1. Where are you running?

- **Organization-managed:** the plugin shows as `trpl-brand@synced`, or the
  person says IT installed it. Skip to section 4.
- **Claude Code:** the `claude` command runs in a shell. Use section 2.
- **Claude desktop app:** use section 3. You cannot click the app's menus;
  walk the person through them one step at a time.

## 2. Claude Code

With the person's go-ahead:

```
claude plugin marketplace add Theodore-Roosevelt-Presidential-Library/Brand
claude plugin install trpl-brand@trpl-brand
claude plugin marketplace add Theodore-Roosevelt-Presidential-Library/HistorianPanel
claude plugin install historian-panel@trpl-historian
```

Offer automatic updates. With a yes, merge into `~/.claude/settings.json`
(keep everything already there):

```json
{
  "extraKnownMarketplaces": {
    "trpl-brand": {"source": {"source": "github", "repo": "Theodore-Roosevelt-Presidential-Library/Brand"}, "autoUpdate": true},
    "trpl-historian": {"source": {"source": "github", "repo": "Theodore-Roosevelt-Presidential-Library/HistorianPanel"}, "autoUpdate": true}
  }
}
```

To update by hand: `claude plugin marketplace update trpl-brand`, then
`claude plugin update trpl-brand@trpl-brand`. Then `/reload-plugins`.

## 3. Desktop app

One step at a time; wait for each:

1. In the sidebar, open **Customize**, then **Plugins**.
2. Choose **Add marketplace** and paste `Theodore-Roosevelt-Presidential-Library/Brand`.
3. **Browse plugins**, find **TRPL Brand Kit**, click **Install**.
4. Repeat steps 2–3 with `Theodore-Roosevelt-Presidential-Library/HistorianPanel`
   and install **HistorianPanel**.
5. Start a new conversation so both load.

To update: **Customize** → **Plugins** → the `trpl-brand` marketplace → **Update**.
If there is no **Add marketplace**, the organization manages plugins; suggest
they ask IT.

## 4. Check, silently

1. You can see `trpl-brand:write-on-brand` and `trpl-brand:style-review`.
2. The guide files are present at the plugin root under `guide/`. If not,
   the plugin is damaged: reinstall.
3. HistorianPanel: you can see `historian-panel:accuracy-review`. If not, offer
   to install it (section 2 or 3). The kit works without it, but historical
   claims then cannot be verified, and you must say so whenever copy contains
   them.
4. Brand fonts: if the person will design, mention once that the fonts are in
   the repository's `assets/fonts/` and **need their own license**.

## 5. Report

One or two plain sentences, then the four things they can now ask for:

- "Write a post about ..." (on-brand drafting)
- "Check this copy against our style guide"
- "Review this design" (paste an image, PDF or link)
- "Where can I find a photo or film of T.R. ...?"

## Maintaining the kit

Never edit the installed copy; updates overwrite it. To change a rule, use
`trpl-brand:update-style-guide`, which opens a pull request on the repository.
