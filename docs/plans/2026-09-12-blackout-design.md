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

Planet colours are procedural, generated fresh for every run (since
2026-09-13). Palettes are built in OKLCH so lightness and chroma behave the
same at every hue, then converted to hex. The rule is unchanged: c1 and c2
are neighbouring hues (18 to 40 degrees apart) and carry the sphere, c3 is a
free accent 60 to 150 degrees away, c4 is c2 deepened. Chroma is reduced
until the colour is inside sRGB. About one palette in eight is pale, like an
opal. A run's eight base hues are spread evenly around the wheel with jitter
and then shuffled, skipping the olive band (about 80 to 140 degrees) that
looks muddy at mid lightness. Shape compositions are also generated per
sphere, jittering position, size, rotation and corner radii within the
light-top-left, accent-right, dark-bottom structure. The hand-picked
palettes that preceded this are in git history.

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
   are hidden until travelled: choosing a planet draws its path in (0.7 s)
   before the quiz fades in, and the travelled route stays lit. Showing all
   paths at once was rejected.
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

## Question formats

Single answer: tap one row, it resolves at once.

Multiple answer ("select all that apply"): four to eight rows. Tapping a row
holds it (a faint wash of the planet fill). A swipe up checks the answer. The
swipe only counts if the answer list was already scrolled to its end when the
finger went down, so scrolling a long list can never check by accident. On a
mouse the same gesture is a quick upward drag or a burst of downward wheel.
Any error on the question (a missed correct or a wrong pick) costs one light,
never more than one. After checking: correct rows fill fully whether picked
or not, wrong picks stay at 60% with a grey circle, unpicked wrong rows fade
to 22%. Six or more rows switch to a dense layout (46px rows, 24px circles).
A "Check" button and tap-outside-to-check were considered and rejected.

Questions live in `blackout/topics/*.json`, one file per topic, listed in
`topics/index.json`. A topic has id, title, short (the label shown on the
map and in the quiz header), specialty, tags, source, and 10 to 15
questions. A question has id, type (single or multi), difficulty 1 to 3, q,
a (a string, or a list for multi), d (distractors), why, tags. Each planet
is one visit to a topic and shows 7 questions (the boss shows 8 from every
topic). Draws prefer questions this device has seen least, tracked in local
storage, so a revisit repeats as little as the bank allows. Topics are
assigned to map nodes by cycling a shuffled list, so with few topics a run
revisits them.

## Notes on questions

Swipe left on any question, before or after answering, to write a note. The
answers slide aside and a single text field takes their place with the
question still visible; "Save note" or "Cancel" slides them back. Notes are
stored in the browser (local storage) with the question id, planet, category,
what was answered, whether it was right, and a timestamp. The title and end
screens show "Copy N notes" and "Clear" whenever notes exist; copy puts a
markdown list on the clipboard to paste into chat. Delivery by GitHub issue
and by share sheet were considered and rejected in favour of clipboard.
Pasted notes are logged in `docs/question-feedback.md` and distilled into
`docs/question-guidelines.md`.

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
- `blackout/topics/*.json` and `topics/index.json`: the question banks.
- `tools/check-topics.py`: validates every topic file and regenerates the
  review sheets in `docs/review/`. Run it before committing a topic.
- `index.html` at the repo root redirects to `blackout/` for GitHub Pages.
- Live at https://rpreble5.github.io/blackout/ from the main branch.
- `.claude/launch.json`: serves the folder on port 8765 for the preview pane.

## Content direction

Sources are clinical review articles (first one: American Family Physician,
Aortic Stenosis, August 2026, uploaded as PDF). Questions are board style.
Workflow: article to a fact sheet in `docs/facts/`, reviewed, then topics of
10 to 15 questions, checked with `tools/check-topics.py`. Second article
(HFrEF medical management, AFP 2025) became three topics on 2026-09-13. The aortic stenosis article became two topics (diagnosis;
management) on 2026-09-13, with a one-line review sheet in `docs/review/`.
Five topics and one topic were considered; two or three per article is the
agreed default for a single-entity review.

## Not built yet

- Persisted best run, more questions per category, sound, haptics.
- Rewards between planets (relics, second chances). Kept out on purpose until
  the core loop feels right.
