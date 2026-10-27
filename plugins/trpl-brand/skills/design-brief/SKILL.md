---
name: design-brief
description: "Plan or build an on-brand design for the Theodore Roosevelt Presidential Library: social graphics, posters, flyers, slides, email headers, web sections, signage, merchandise. Produces a design spec (colors, type, logo, imagery, layout) and builds it in Canva or another design tool when one is connected, or writes a ready prompt for Claude Design, Canva AI or an agency. Use when someone asks to make, design, mock up or brief a visual piece."
---

# Design brief and build

Read `guide/visual-identity.md`, `guide/imagery-and-media.md` and
`guide/channels.md` at the plugin root, and use the values in
`tokens/tokens.json`. Logos and marks: `https://brand.labs.trlibrary.com/assets/`.

## 1. Brief

From the request, settle: format and size, channel, audience, the one message,
the call to action, and the copy. Draft or check the copy with
`trpl-brand:write-on-brand` first; design follows content.

## 2. Spec

Write a short spec:

- **Background color** (one) and **supporting color** (one; a third only if
  needed), chosen from the approved pairings. Proportions 75–85 / 15–25 / 5–10.
- **Type:** headline in Dharma Gothic (ALL CAPS), body in ITC Clearface,
  captions in Frutiger Next. Sizes for the format.
- **Logo:** version, color, placement, clear space, size above the minimum.
- **Imagery:** a real photograph from the Library's asset library or a
  credited public-domain source (see `find-tr-media`). Never renderings; never
  AI-generated people or buildings. If a photo is the main visual, it is the
  background color: add one grounding **or** one accent color.
- **Graphic elements:** marks, Values texture or ephemera only if they serve
  the piece.
- **Contrast check:** list each text/background pair with its ratio from
  `tokens/contrast.md`.

## 3. Build

Library designs are built in **Canva** with the Library's brand kit, unless
Marketing & Communications says otherwise.

- **Canva connector available:** search the brand templates first (the master
  presentation template for decks); copy a template rather than starting
  blank; apply the spec. Brand fonts come from the brand kit. Leave the design
  for a person to review; do not publish or share it.
- **Claude Design or another AI design tool:** give it the spec plus
  `https://brand.labs.trlibrary.com/llms-full.txt` and the logo files. Tell it
  to use real photos the person supplies, not generated ones.
- **No design tool:** deliver the spec as a brief an agency can follow, with
  links to the assets and the guide.

## 4. Review

Run `trpl-brand:design-review` on the result (or the `brand-design-reviewer`
agent for fresh eyes) and fix what it finds before calling it done.
