# Install the TRPL Brand Kit

## The one prompt

Open Claude (the desktop app or Claude Code) and paste:

> Set up the TRPL Brand Kit for me. Follow the instructions at
> https://github.com/Theodore-Roosevelt-Presidential-Library/Brand/blob/main/INSTALL.md
> and walk me through anything I need to click.

Claude installs the brand kit and HistorianPanel (historical accuracy), checks
both work, and tells you what to try. In the desktop app it will ask you to
click through a few menus; it can't click them for you.

If your organization manages Claude for you, the kit may already be there.

---

## For Claude: carrying out the prompt

Tell the person in one line what you are about to do, then do it. Ask before
installing anything or changing settings.

### Step 1. Already installed?

If your skills include `trpl-brand:write-on-brand`, the kit is installed. Skip
to Step 4. If it is listed as `trpl-brand@synced`, the organization manages it;
skip to Step 4.

### Step 2. Which app?

If `claude --version` runs in a shell, you are in **Claude Code**: Step 3a.
Otherwise you are in the **Claude desktop app**: Step 3b.

### Step 3a. Claude Code

With the person's go-ahead:

```
claude plugin marketplace add Theodore-Roosevelt-Presidential-Library/Brand
claude plugin install trpl-brand@trpl-brand
claude plugin marketplace add Theodore-Roosevelt-Presidential-Library/HistorianPanel
claude plugin install historian-panel@trpl-historian
```

Offer automatic updates. With a yes, merge into `~/.claude/settings.json`,
keeping everything already there:

```json
{
  "extraKnownMarketplaces": {
    "trpl-brand": {
      "source": {"source": "github", "repo": "Theodore-Roosevelt-Presidential-Library/Brand"},
      "autoUpdate": true
    },
    "trpl-historian": {
      "source": {"source": "github", "repo": "Theodore-Roosevelt-Presidential-Library/HistorianPanel"},
      "autoUpdate": true
    }
  }
}
```

Ask them to run `/reload-plugins` or start a new session, then Step 4.

### Step 3b. Claude desktop app

Give these one at a time and wait for each:

1. In the left sidebar, open **Customize**, then **Plugins**.
2. Choose **Add marketplace** and paste
   `Theodore-Roosevelt-Presidential-Library/Brand`.
3. Choose **Browse plugins**, find **TRPL Brand Kit**, and click **Install**.
4. Choose **Add marketplace** again and paste
   `Theodore-Roosevelt-Presidential-Library/HistorianPanel`, then install
   **HistorianPanel**.
5. Start a new conversation and paste the setup prompt again to finish with Step 4.

No **Add marketplace** option means the organization manages plugins; suggest
they ask their IT contact.

### Step 4. Check, without questions

Run `trpl-brand:brand-setup` section 4. Then report in one or two sentences and
list what they can ask for: write on brand, check copy, review a design, find
an image of T.R.

## Updating

- Organization-managed: automatic.
- Desktop app: **Customize** → **Plugins** → the `trpl-brand` marketplace → **Update**.
- Claude Code: `claude plugin marketplace update trpl-brand`, then `/reload-plugins`.

Or ask Claude: "Update the brand kit."

## Not using Claude?

- Read the guide at [brand.labs.trlibrary.com](https://brand.labs.trlibrary.com).
- Give any AI tool [`llms-full.txt`](https://brand.labs.trlibrary.com/llms-full.txt).
- See [Canva](integrations/canva.md), [Claude Design](integrations/claude-design.md)
  and [other AI tools](integrations/other-ai-tools.md).
