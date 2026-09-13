# Blackout: design

Date: 2026-09-12

## What it is

A roguelike quiz game for the phone, web based. You climb a branching star map,
planet to planet, answering three questions per planet. Four lights are your
health. A wrong answer puts one out. When the last goes out, the run ends in a
blackout. Clearing a planet with no misses relights one. The top of the map is
the Eclipse, a boss planet that draws four questions from every category.

## Decisions made with the client

- Health is a row of four small lights, not a dimming interface (rejected).
- The question screen stays black. The planet's gradient lives in small
  circles beside each answer, not in a big planet at the top (rejected).
  Organic blob shapes were tried and rejected in favour of plain circles.
- Selecting a planet is a plain crossfade. A fly-up transition was rejected.
- On any pick, every wrong answer fades at the same moment the correct one
  fills, whether or not the pick was right.
- Each planet is one category. Its three gradient stops supply every colour
  on that planet's question screen.

## Tokens

| Token | Value | Role |
|---|---|---|
| Black | `#000000` | Ground. True black. |
| Ink | `#ECEBE6` | Text, lights, primary button |
| Dust | `#6A6A72` | Secondary text |
| Hair | `rgba(236,235,230,.14)` | Outlines, rings |

Planets. Rule: c1 and c2 sit next to each other on the spectrum and carry
the sphere. c3 is the free accent, kept small. c4 is c2 deepened, never a new
hue. So each sphere reads as one colour family with a hint of something else.

| Planet | Category | c1 light | c2 base | c3 accent | c4 dark |
|---|---|---|---|---|---|
| Sol | Music | `#FFE24A` | `#FF8A1F` | `#FF3D3D` | `#8A1C1C` |
| Vesper | Astronomy | `#B49BFF` | `#7B5CFF` | `#4FA3FF` | `#2A1A6E` |
| Halide | Science | `#7FF0D8` | `#1FB5A3` | `#2E7BFF` | `#0B4A48` |
| Meridian | Geography | `#C9FF5E` | `#3ED47A` | `#FFD84A` | `#146B3A` |
| Cinder | History | `#FFB061` | `#FF5A2E` | `#C1123A` | `#4A0F14` |
| Umbra | Film and art | `#8F7BFF` | `#4B3FCC` | `#FF9A4A` | `#1B1650` |
| Opal | Words | `#FFFFFF` | `#C6CFDC` | `#8FA4C4` | `#4E6282` |
| Eclipse | Everything (boss) | `#C9A2FF` | `#7C3FB5` | `#FF8A5B` | `#0A0510` |

Type: Sora only. Weight 200 for the title and end-screen headline, 300 for
questions, 400 for answers, 500 for buttons and planet names. Sentence case
everywhere. No all-caps labels.

## Screens

1. Title. Wordmark top-left, one sentence, one primary button. A large planet
   sits low on the screen, half off the bottom edge, like a horizon.
2. Map. Vertical, climbed upward. Eight planets in tiers of 2, 3, 2, 1 joined
   by curved paths. Each path is an S-curve that leaves and arrives
   vertically with a small sideways lean, stroked with a gradient from one
   planet's average colour to the other's (mean of its four colours). Paths
   out of the current planet are at full opacity; the rest sit at 28%.
   Reachable planets are full colour and grow slightly on hover. Locked ones
   are desaturated. Visited ones stay at full colour (fading them was
   rejected). No rings (tried and rejected).
   Lights top-right.
3. Question. Planet name and category top-left, lights top-right. Under the
   head row a 3px full-width band carries the planet's gradient (the same
   blurred-shapes technique sliced into a strip, drifting sideways slowly).
   The band is also the progress bar: the unearned part sits under a 72%
   black scrim whose left edge slides right after each answer (0.9 s). There
   is no "Question x of y" text and no tap hint (both tried and rejected).
   Question in light type. Four full-width
   answer rows, each with a 30px circle carrying the planet's gradient with
   its colours rotated. A small planet in the header was tried and rejected.
   Correct row fills with the two light colours. All wrong rows fade to 22%
   at the same moment. A wrong pick also puts one light out. A one-sentence
   explanation then crossfades into the question's slot. A tap anywhere on
   the screen moves on, with no hint text. Nothing
   auto-advances, and there is no button (one was tried and rejected).
   Question size scales with length from 27px (50 characters or fewer) down
   to 20px (110 or more). Explanations scale from 21px to 16px over 60 to
   150 characters. Answers stay 17px and may wrap to two lines.
4. End. Black. "Blackout." or "Past the eclipse." with one sentence, the four
   lights in their final state, and "Run again".

## Motion

- Screens crossfade in 500 ms. No flying elements.
- Continuous but slow: planets have a drifting highlight over 22 s.
- Everything is disabled under prefers-reduced-motion.

## Gradient recipe

Not radial gradients. Each sphere is a square sheet, 22% larger than the
circle on every side, holding four solid-colour shapes: rotated rounded
rectangles and ellipses in the planet's four colours. The sheet is blurred as
a group (blur radius is 13% of the sphere's diameter, so it looks the same at
30px and 500px) and the parent crops it to a circle. Four shape layouts are
defined in `LAYOUTS`; the map uses a different one per planet and each answer
circle uses a different one, so no two spheres share a composition. Stacking
puts the accent on top, then the light colour, then the dark, with the mid
colour as the base. Over the sheet: only a soft-light grain layer. The look
is flat on purpose. A lighting layer (highlight, shadow, rim) was tried and
rejected. The sheet rotates once every 140 seconds so the colours drift.

## Full screen

`manifest.webmanifest` declares display fullscreen and portrait, so an
installed copy on Android runs without the status or navigation bars. In a
browser tab, "Begin a run" also requests the Fullscreen API with navigation
UI hidden and tries to lock portrait; platforms that refuse (iOS Safari) just
carry on. Icons are `icon-192.png` and `icon-512.png`, generated by script.

## Files

- `blackout/index.html`: the whole prototype, no build step.
- `blackout/manifest.webmanifest`, `blackout/icon-*.png`: install metadata.
- `index.html` at the repo root redirects to `blackout/` for GitHub Pages.
- Live at https://rpreble5.github.io/blackout/ from the main branch.
- `.claude/launch.json`: serves the folder on port 8765 for the preview pane.

## Not built yet

- Persisted best run, more questions per category, sound, haptics.
- Rewards between planets (relics, second chances). Kept out on purpose until
  the core loop feels right.
