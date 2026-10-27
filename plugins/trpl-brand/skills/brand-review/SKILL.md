---
name: brand-review
description: "Full pre-publication review of a Library piece — copy, design, historical accuracy and required approvals — in one pass, ending with a ready/not-ready verdict and a fix list. Use for anything going out under the Theodore Roosevelt Presidential Library's name that has both words and visuals, for agency or partner deliverables, or when someone asks 'is this ready to go?' or 'review this before it ships.'"
---

# Brand review

The coordinator. Runs the other checks and brings them together.

## Steps

1. **Collect the piece.** Get the actual text, images, PDF, link or design.
   Note channel, audience and who made it (staff, agency, partner).
2. **Copy.** Run `trpl-brand:style-review` on all text, including headlines,
   captions, alt text and fine print. For long pieces, use the
   `brand-copy-reviewer` agent so the read is independent of whoever drafted it.
3. **Design** (if visual). Run `trpl-brand:design-review`, or the
   `brand-design-reviewer` agent.
4. **History.** Run `trpl-brand:historian-handoff` on every historical claim,
   quote and image identification.
5. **Approvals.** Check `guide/accuracy-and-approvals.md#what-needs-review` and
   list each review the piece needs.
6. **Consolidate.** Remove duplicate findings; order by severity:
   - **Blocking:** factual errors, unverified quotes, logo misuse, failed
     contrast on readable text, AI images of people or buildings, missing
     required approval, partisan framing
   - **Fix before publishing:** terminology, off-palette color, wrong type use,
     missing credits, missing visit link
   - **Polish:** voice, tightening, proportion

## Output

```
VERDICT: Ready | Ready after fixes | Not ready

BLOCKING
1. ...

FIX BEFORE PUBLISHING
1. ...

POLISH
1. ...

APPROVALS NEEDED
- ...

WHAT WORKS
- ...
```

Each item: where, what, the fix, and the guide section. Keep it short enough to
act on. If the person is an agency or partner, phrase fixes as instructions
they can hand to their team.
