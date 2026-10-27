---
name: write-on-brand
description: "Draft or rewrite any copy for the Theodore Roosevelt Presidential Library in its voice and editorial style: web pages, social posts, emails, newsletters, press releases, letters, thank-yous, captions, scripts, signage, grant and sponsor copy. Use whenever someone asks to write, draft, rewrite, polish or shorten something that will carry the Library's name, even if they don't mention the brand."
---

# Write on brand

Read these at the plugin root before drafting:

- `guide/voice-and-tone.md`
- `guide/editorial-style-guide.md`
- `guide/channels.md` (the section for this channel)
- `guide/brand-foundation.md` if the piece touches mission, values or pillars

If the files are missing, fetch `https://brand.labs.trlibrary.com/llms-full.txt`.

## 1. Settle the brief

Work out audience, channel, goal and length from the request. Ask one short
question only if the channel or audience is genuinely unclear; otherwise state
your reading in one line and draft.

## 2. Draft

- Lead with story, place or the participant, not the institution.
- Concrete, checkable detail. No filler ("world-class," "transformative").
- Apply the editorial rules as you write: participants, Trustees, Benefactors,
  T.R., buttes, Kettle Hill, "pursuing," the Library capitalized, no "Teddy,"
  no throat-clearing, minimal "we/our."
- Gratitude: once, plainly, specifically. See `#gratitude` in the editorial guide.
- Visitor copy: no current or future years; visit about three and a half hours;
  link hours, don't restate them.
- Every social post or email carries a way to visit (except press-coverage posts).
- **Quotes:** never write a T.R. quotation from memory. If a quote would help,
  leave a placeholder `[VERIFIED QUOTE ON <idea> — see historian-handoff]` or
  ask HistorianPanel's quote finder.
- **Facts:** your draft is a lead, not a source. Mark every historical claim you
  are not sure of with `[VERIFY]`.
- **Images:** suggest real photographs, never renderings or AI images of people
  or buildings.

## 3. Check before showing it as final

1. Run `trpl-brand:style-review` on your draft (or use the
   `brand-copy-reviewer` agent for a fresh-eyes read on longer pieces). Fix
   every hit.
2. If the draft contains any historical claim, run `trpl-brand:historian-handoff`.
3. Check `guide/accuracy-and-approvals.md#what-needs-review` and list any
   reviews the piece needs (for example, financial figures → Development).

## 4. Deliver

The draft, then at most three short lines:

- what was verified, hedged or still needs verification
- which reviews it needs before publishing, if any
- one alternative angle, only if the request was strategic

For social, give the platform set the channel guide calls for (long-form plus
short-form under 300 characters) unless asked for one platform.
