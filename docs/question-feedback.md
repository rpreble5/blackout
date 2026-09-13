# Question feedback log

Notes left in the game by swiping left on a question, pasted here from the
"Copy notes" control on the title or end screen. Each entry keeps the
question id so it can be traced back. Rules that come out of these notes go
into `question-guidelines.md`.

Format per entry: date, then the pasted list, then what changed.

## Entries

### 2026-09-13, first play of the aortic stenosis topics

Pasted (six distinct notes, duplicates from cumulative copies removed):

- [as-dx-07] "Which risk factors for aortic stenosis are nonmodifiable?" |
  answered: Age over 65; Male sex; Prior thoracic radiation (wrong) | note:
  This is a bit too easy for physicians. It's not hard to know the things
  that can't be changed.
- [as-dx-13] "What is the estimated two-year mortality of untreated
  symptomatic severe aortic stenosis?" | answered: About 10% (wrong) | note:
  Number questions like this should always be in order from least to
  greatest.
- [as-mx-04] "In an asymptomatic patient, which echo surveillance intervals
  are correct?" | answered all three correctly | note: This is a super
  annoying question to think about. Would be better broken down into
  separate questions.
- [as-dx-04] "Which set of echo findings defines severe aortic stenosis?" |
  answered correctly | note: Way too many things to compare. Perhaps this
  question would work better as separate questions?
- [as-dx-01] "Which examination finding most raises the likelihood of aortic
  stenosis?" | answered correctly | note: This is a strong question.
- [as-dx-09] "About what share of patients with aortic stenosis also have
  atrial fibrillation, and how does that affect valve replacement?" |
  answered correctly | note: I don't think these combo questions are useful.
  It's too hard to think through the combo answers.

What changed:

- New rule: numeric options are listed least to greatest and never shuffled.
  Topic files mark these with `"order": "fixed"` and the game respects it.
  Applied to as-dx-13, as-mx-13, and every new numeric question.
- New rule: one idea per option. No option pairs a number with a consequence
  or bundles several parameters or several mappings. Split instead.
  Rewritten: as-dx-04 (now Vmax and valve area as two questions), as-dx-06,
  as-dx-09, as-dx-11, as-dx-12, as-mx-04 (now moderate and severe intervals
  as two questions), as-mx-12.
- New rule: multiple-answer questions must need clinical judgement, not
  categorisation a physician already knows. as-dx-07 retired (replaced by
  a bicuspid outlook question); as-dx-02 (classic symptoms) replaced by a
  question on which comorbidities confound symptom attribution.
- as-dx-01 kept as the model for a strong single question: one finding, one
  axis of comparison, a fact worth knowing.
- Bank sizes stay at 15 and 15; as-mx-01 (which treatment reverses stenosis)
  was dropped as too easy under the same reasoning.
