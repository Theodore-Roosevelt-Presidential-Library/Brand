---
name: design-review
description: "Review a design for the Theodore Roosevelt Presidential Library against its visual identity: logo use, clear space, color pairings and proportions, contrast, typography, imagery lanes, AI-image limits, graphic elements, and the copy on it. Use when someone shares an image, PDF, Canva link, deck, web page or mockup and asks whether it is on brand, or asks for a design review or feedback."
---

# Design review

Read `guide/visual-identity.md` and `guide/imagery-and-media.md` at the plugin
root. The contrast numbers are in `tokens/contrast.md`; color values are in
`tokens/tokens.json`. The Brand Style Guide PDF at trlibrary.com/brand is the
final authority on how things look.

## Get the design in front of you

- Image or PDF: view it directly (render PDF pages to images if needed).
- Canva link: use the Canva connector if available to read or export it;
  otherwise ask for an export.
- Web page: screenshot it at desktop and phone widths.
- If you cannot see it, say so. Never review a design you have not looked at.

## Checklist

Mark each pass, concern or fail, with where it occurs.

**Logo**
- Supplied artwork, not retyped or redrawn; not recolored, stretched, rotated,
  outlined or effected
- Right version (stacked first; horizontal only when needed; boxed for busy backgrounds)
- Clear space (two "T" widths) and minimum size (0.85 in stacked, 1.25 in horizontal)
- Logo color fits the background; enough contrast; not over a busy image
- Co-branding: Library first, divider, equal spacing

**Color**
- One background color (plus white); no Night Sky with Dark Forest
- Two color families at most; proportions roughly 75–85 / 15–25 / 5–10
- Never Deep Orange with Sunset Orange; never Dark Forest with Sunset Pink
- Dark Gray, not black, as the neutral
- Sunset Pink only for the Values or deliberate emphasis
- Deep Orange only on things that act like buttons or links (on screen)
- Photo as background: one grounding **or** one accent color
- **Contrast:** check every text/background pair against `tokens/contrast.md`.
  On white, text only in Dark Gray, Night Sky or Dark Forest

**Type**
- Dharma Gothic for headlines and calls to action, ALL CAPS, never body
- Clearface for body (9–11 pt in print); Frutiger Next for captions (≤10 pt)
- Teddy Regular only with approval, a word or two, never as a signature
- Substitutes (Impact, Georgia, Arial) only if brand fonts were unavailable, and stated
- No hyphenation; left-aligned body; no first-line indents; no widows in headlines
- Pull quotes: hanging quotation marks; T.R. quotes with place and year

**Imagery and graphics**
- Real photographs; no renderings of the Library
- No AI-generated people, buildings or landmarks; no AI image presented as a photo
- Historical images captioned to match the source record and credited
- Contemporary = nature and place; historical = Roosevelt; layering deliberate
- Ephemera, patterns, illustration and icons follow the guide; nothing cartoonish
  or generic Western; no frames around photos without reason
- Text over photos sits on a Night Sky gradient or otherwise has contrast

**Copy on the design**
- Run `trpl-brand:style-review` on all text in the design
- Any historical claim, quote or image identification → `trpl-brand:historian-handoff`

**Accessibility**
- Text contrast (above); minimum sizes readable at the intended viewing distance
- Alt text supplied for digital images

## Output

1. Verdict in one line: ready, ready after small fixes, or needs rework.
2. A table: area · issue · where · fix · guide section. Most important first.
3. What works (two or three lines), so the designer keeps it.

Be specific ("headline on the second slide is Sunset Orange on white: 2.2:1,
fails; use Night Sky"). Don't redesign unless asked; if asked, use
`trpl-brand:design-brief`.
