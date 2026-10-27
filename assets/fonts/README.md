# Brand fonts

> **These are licensed commercial fonts. Downloading them from this repository
> does not give you a license to use them.**
>
> The Theodore Roosevelt Presidential Library holds licenses for its own use.
> Anyone else (agencies, partners, freelancers, vendors) must either buy their
> own license from the foundry, or confirm in writing with the Library's
> Marketing & Communications team that their work for the Library is covered.
> Each font's license terms, embedded in the font files, govern. If you are
> unsure, ask before installing.

| Family | Use | Files | Foundry / license |
|--------|-----|-------|-------------------|
| **Dharma Gothic** (E Bold, E ExBold, M Bold, M ExBold) | Headlines, titles, calls to action. ALL CAPS only | `desktop/dharma-gothic/` · `web/DharmaGothic*.woff2` | Dharma Type ([MyFonts](https://www.myfonts.com/fonts/flat-it/dharma-gothic/)) |
| **ITC Clearface** (Regular, Italic, Bold, Heavy, Black + italics) | Body copy, subheads, pull quotes | `desktop/itc-clearface/` | Monotype / ITC |
| **Frutiger Next** (Light, Regular, Italic, Bold + italics) | Captions, credits, labels, footnotes | `desktop/frutiger-next/` · `web/FrutigerNextCom-*.woff2` | Linotype / Monotype |
| **Teddy Regular** | From T.R.'s handwriting. One or two words at a time | `desktop/teddy/` | Custom face. **Use requires Marketing & Communications approval in every case** |

**Not here:** TRPL Gothic, the custom signage face, and Frutiger Next Medium.
Marketing & Communications supplies them for signage work.

## Desktop fonts (`desktop/`)

For design and office apps. Install the `.otf` files. In Canva, use the
Library's brand kit, which already carries these fonts, rather than uploading
them to a personal account.

## Web fonts (`web/`)

Licensed for the Library's own websites, including sites agencies build for the
Library. Do not use them on other organizations' sites or in apps. [`fonts.css`](web/fonts.css) has the `@font-face` rules and the
approved fallbacks:

```html
<link rel="stylesheet" href="https://brand.labs.trlibrary.com/assets/fonts/web/fonts.css">
```

```css
h1 { font-family: var(--trpl-font-display); text-transform: uppercase; }
body { font-family: var(--trpl-font-body); }
figcaption { font-family: var(--trpl-font-caption); }
```

ITC Clearface has no web license in this kit, so Georgia is the standard web
body face. It needs no substitution note.

## When you can't use the brand fonts

Use the approved substitutes and say that you substituted them:

| Brand font | Substitute |
|------------|------------|
| Dharma Gothic | Impact |
| ITC Clearface | Georgia |
| Frutiger Next | Arial |
