# Theodore Roosevelt Presidential Library — Brand Assets

This repository is the authoritative source for TRPL's visual identity system. It is structured to support design tooling, AI-assisted design (including Claude Design), and consistent brand application across all channels.

---

## Repository Structure

```
Brand/
├── brand-guidelines/       Core brand documentation (colors, type, voice, usage rules)
├── logos/                  All logo marks, wordmarks, monograms, and lockups
│   ├── primary/            Main horizontal/stacked logo variants
│   ├── secondary/          Alternate approved logo versions
│   ├── wordmarks/          Text-only wordmark treatments
│   ├── monograms/          TR monogram and icon-only marks
│   └── lockups/            Logo + tagline or logo + partner combinations
├── design-examples/        Finished, approved design work organized by channel
│   ├── print/              Brochures, ads, direct mail, event programs
│   ├── digital/            Web graphics, display ads, digital signage
│   ├── social-media/       Organized by platform (instagram, facebook, linkedin, x-threads)
│   ├── email/              Email campaign designs and templates
│   └── signage/            Physical and environmental signage examples
├── templates/              Editable/reusable templates by channel
│   ├── social-media/
│   ├── print/
│   └── email/
├── photography/            Photography style guide and representative image examples
│   └── examples/
├── assets/                 Supporting graphic elements
│   ├── icons/              Custom iconography system
│   ├── patterns/           Brand patterns and textures
│   └── textures/
├── brand.json              Machine-readable brand token spec (colors, fonts, voice)
└── README.md               This file
```

---

## Naming Conventions

Consistent file naming is critical for AI tooling and human navigation alike. Follow these conventions for every file added to this repo.

**Format:** `[scope]_[descriptor]_[variant]_[size-or-format].[ext]`

**Examples:**
- `trpl_logo_primary_horizontal_rgb.svg`
- `trpl_logo_monogram_white_300px.png`
- `trpl_social_instagram_square_opening-announcement.jpg`
- `trpl_print_brochure_visitor-guide_2026.pdf`
- `trpl_email_header_grand-opening_1200w.png`

**Rules:**
- Lowercase only, hyphens within descriptor phrases, underscores between fields
- No spaces, no special characters
- Always include color space in logo filenames: `rgb` (screen), `cmyk` (print), `mono` (single-color)
- Include year for date-sensitive materials (e.g., `_2026`)
- Use `@2x` suffix for retina/high-DPI variants

---

## Accepted File Formats

| Category | Preferred | Also Accepted |
|---|---|---|
| Logos | SVG, EPS, AI | PNG (with transparency) |
| Photography | JPG (high-res) | TIFF |
| Illustrations / Icons | SVG | PNG |
| Brand guidelines | MD, PDF | DOCX |
| Templates | Canva export, AI, INDD | PDF |
| Print-ready | PDF (press-quality) | EPS |

Source files (AI, INDD, Canva links) are preferred alongside exports when available.

---

## Brand Essentials

The full brand system is documented in [`/brand-guidelines/`](./brand-guidelines/). Key reference points:

- **Voice:** Action-oriented, decisive, inspiring, earnest. Not casual or ad-copy clever.
- **Brand arc:** Story → Connection → Visit
- **Typeface:** ITC Clearface (body); refer to typography guide for full hierarchy
- **Terminology:** "participants" (not visitors), "Trustees" (not board), "benefactors" (not donors), "the Library" (always capitalized)
- **TR quotes:** Verbatim only, with source attribution. Never paraphrased.
- **No "Teddy" in prose** (hashtag exception only: #TeddyRoosevelt)

---

## Contributing Assets

1. Place files in the correct folder following the naming conventions above
2. Add a one-line entry to the folder's `README.md` describing the new asset
3. For any asset that introduces a new color, font, or usage pattern, update the relevant file in `/brand-guidelines/` and `brand.json`
4. For questions on brand standards, contact: Matt Briney — matt@trlibrary.com

---

## About TRPL

The Theodore Roosevelt Presidential Library opens July 4, 2026 in Medora, North Dakota — timed to America's 250th anniversary. Designed by Snøhetta and pursuing triple sustainability certification (LBC Full, LEED Platinum, SITES Platinum), the Library is dedicated to TR's enduring legacy of conservation, civic leadership, and the strenuous life.

[trlibrary.com](https://trlibrary.com)
