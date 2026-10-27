---
title: Claude Design
description: Giving Claude's design tools the Library's brand system, so mockups, decks and pages start on brand.
---

# Claude Design

Claude can build designs, decks and pages from a design system. Give it the
Library's brand once, and every design you ask for starts from it.

## Create the Library's design system in Claude

In Claude, say:

> Create a design system for the Theodore Roosevelt Presidential Library from
> https://brand.labs.trlibrary.com/llms-full.txt and the tokens at
> https://brand.labs.trlibrary.com/tokens/tokens.json. Use the logos at
> https://brand.labs.trlibrary.com/assets.html. Headlines in Dharma Gothic (all
> caps), body in ITC Clearface, captions in Frutiger Next; if those aren't
> available, use Impact, Georgia and Arial and say so.

Then ask for designs against it: "Using the TRPL design system, make a one-page
event flyer for ..."

## What to tell it every time

- Use **real photographs** you supply. Never generate people, the Library or
  any building.
- One background color plus white; two color families at most.
- Deep Orange is for buttons and links only.
- Check text contrast against the [contrast table](../plugins/trpl-brand/guide/visual-identity.md#contrast).

## Then review

Ask "Review this design against the TRPL brand" to run the design review, and
send any historical text through the accuracy check.

## When to use Canva instead

Finished Library designs are built in [Canva](canva.md) with the brand kit, so
the real fonts and templates are used. Claude Design is good for exploring
options and mockups; move the chosen direction into Canva for production unless
Marketing & Communications agrees otherwise.
