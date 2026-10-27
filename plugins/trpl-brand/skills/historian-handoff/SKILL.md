---
name: historian-handoff
description: "Pass historical questions and claims to HistorianPanel, the Library's accuracy specialists: any T.R. fact, date, quote, image identification, family relationship, superlative or anecdote in brand work. Use whenever copy or a design contains a historical claim, someone asks 'is this right?' about Roosevelt history, or a quote is needed. Installs or points to HistorianPanel if it is missing."
---

# Hand off to HistorianPanel

Brand skills judge how something sounds and looks. HistorianPanel judges
whether it is true. Repository:
`https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel`.

## 1. Is the panel available?

Look for `historian-panel:accuracy-review` in your available skills.

- **Yes:** go to step 2.
- **No:** tell the person historical claims can't be verified until the panel
  is installed, and offer to set it up with `trpl-brand:brand-setup` (or give
  them the one prompt: *"Set up HistorianPanel for me. Follow the instructions
  at https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel/blob/main/INSTALL.md"*).
  Meanwhile, mark every claim `[VERIFY]` and don't present the copy as final.

## 2. Route the request

| Need | Run |
|------|-----|
| Check copy, a caption, a page, a deck | `historian-panel:accuracy-review review <text or URL>` |
| One factual question | `historian-panel:accuracy-review ask <question>` |
| A T.R. quote on a subject | `historian-panel:sp-quote-finder <subject and use>` |
| Is this quote real / exact? | `historian-panel:accuracy-review review "<quote>"` |
| A quiz, trivia or poll | `historian-panel:quiz-check <quiz>` |
| How to frame a contested subject | `historian-panel:scholarly-debate <question>` |
| How scholars would read a long piece | `historian-panel:review-lenses <text>` |
| An error was found; where else is it? | `historian-panel:error-sweep <wrong> -> <right>` |

Pass the claims, not your conclusions. If you drafted the copy, your draft is a
lead like anyone else's; don't tell the panel what you think the answer is.

## 3. Bring the results back

- Apply every **fix** and **cut**. Apply **hedge** wording as given.
- Keep the panel's sources with the draft (in notes, not in public copy unless
  the format cites sources).
- Re-run `trpl-brand:style-review` on changed wording.
- Anything the panel could not resolve is not published as fact.

## Division of labor

House-style wording (Kettle Hill, buttes, T.R.) belongs to this kit's
`style-review`; whether an event happened at Kettle Hill belongs to the panel.
Indigenous history and MHA Nation content always also needs the Library's human
reviewers; the panel never closes those claims on its own.
