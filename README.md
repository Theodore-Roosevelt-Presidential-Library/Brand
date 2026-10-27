# Theodore Roosevelt Presidential Library — Brand

Everything an agency, partner or staff member needs to work on the Library's
brand: the guide, logos, marks, fonts, design tokens, and a Claude plugin that
writes, reviews and designs to the standards.

**Website:** [brand.labs.trlibrary.com](https://brand.labs.trlibrary.com)

> **Claude:** start with [CLAUDE.md](CLAUDE.md). To install for someone, follow
> [INSTALL.md](INSTALL.md).

## Get started with Claude

Paste this into Claude (desktop app or Claude Code):

> Set up the TRPL Brand Kit for me. Follow the instructions at
> https://github.com/Theodore-Roosevelt-Presidential-Library/Brand/blob/main/INSTALL.md
> and walk me through anything I need to click.

In Claude Code you can also install directly:

```
/plugin install trpl-brand --marketplace Theodore-Roosevelt-Presidential-Library/Brand
```

The prompt installs the brand kit and [HistorianPanel](https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel),
the Library's historical-accuracy specialists. Then ask in plain words:

- "Write an Instagram post about the Elkhorn Ranch."
- "Check this press release against our style guide."
- "Review this poster." (attach it)
- "Where can I find a photo of T.R. at Sagamore Hill?"
- "Add a rule to the style guide: ..."

## What's here

| Folder | What |
|--------|------|
| [`plugins/trpl-brand/guide/`](plugins/trpl-brand/guide/README.md) | The brand guide in plain text: foundation, voice, **editorial style guide**, visual identity, imagery and media sources, T.R. essentials, accuracy and approvals, channels |
| [`plugins/trpl-brand/skills/`](plugins/trpl-brand/skills/) | Claude skills: write on brand, style review, design review, design brief, T.R. orientation, find T.R. media, HistorianPanel hand-off, full brand review, update the style guide, setup |
| [`plugins/trpl-brand/agents/`](plugins/trpl-brand/agents/) | Independent reviewers: copy, design, and a steward for guide changes |
| [`plugins/trpl-brand/tokens/`](plugins/trpl-brand/tokens/) | Design tokens (W3C format), CSS variables, Tailwind preset, contrast table |
| [`assets/`](assets/README.md) | Logos, supporting marks and **licensed** fonts |
| [`integrations/`](integrations/) | Using the brand with Canva, Claude Design and other AI tools |
| [`site/`](site/) | Builds the website from the files above |

## Without Claude

Read the guide on the [website](https://brand.labs.trlibrary.com), download
assets from [Logos and marks](https://brand.labs.trlibrary.com/assets.html), or
point any AI tool at
[`llms-full.txt`](https://brand.labs.trlibrary.com/llms-full.txt), the whole
guide in one file.

## The authoritative documents

- [Brand Style Guide](https://www.trlibrary.com/brand) (v0.1): everything visual
- [Story Guide](https://www.trlibrary.com/storyguide): tone, terminology, naming

This repository distills both. Where they disagree, they win.

## Fonts are licensed

The brand fonts in [`assets/fonts/`](assets/fonts/README.md) are commercial
fonts. **Having the files does not give you a license.** Read the font README
before installing.

## Changing the guide

See [CONTRIBUTING.md](CONTRIBUTING.md). Staff using Claude can say "add a rule to
the style guide" and the kit opens a pull request. Every change is logged in
[CHANGELOG.md](CHANGELOG.md).

## License

See [LICENSE.md](LICENSE.md). In short: code is MIT; the Library's name, logos,
marks and guide content are the Library's and are for authorized Library work;
fonts are licensed separately.
