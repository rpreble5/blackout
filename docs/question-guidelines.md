# Question guidelines

The rules applied every time questions are written for Blackout. This file is
distilled from `question-feedback.md`, the running log of notes left in the
game. When a note changes a rule, the rule changes here and the note is cited.

## Source and grouping

- Questions come from one source article at a time. Every question must be
  answerable from that article alone.
- An article is first reduced to short, standalone, tagged facts. Facts are
  clustered into topics of 10 to 15 questions that share one frame: a
  mechanism, a decision, a patient situation. A cluster that can't reach 10
  strong questions is merged with a neighbour or dropped. Two or three
  topics per single-entity review article is the default.
- A planet draws 7 questions from one topic, preferring ones the player has
  not seen, spread across difficulty and across question tags, so no planet
  asks the same sub-point twice.

## Writing a question

- One correct reading. No question should have an arguable second answer.
- **One idea per option.** An option is a single finding, a single number, a
  single action. Never a number paired with its consequence, never several
  parameters bundled, never several mappings in one line. If the fact has
  three parts, that is three questions. (From notes on as-dx-04, as-dx-09,
  as-mx-04, 2026-09-13.)
- **Numeric options run least to greatest** and are marked
  `"order": "fixed"` so the game does not shuffle them. This applies to
  percentages, thresholds, intervals, doses and INR ranges. Options with a
  natural order (intensity, stage) are also fixed. (From the note on
  as-dx-13, 2026-09-13.)
- Distractors match the correct answer in type, length and specificity. If
  the answer is a number with units, every option is a number with the same
  units in a plausible range.
- No negatives ("which is not"), no "all of the above", no trick wording.
- Questions fit the size range (about 50 to 110 characters reads best).
  Options fit two lines at 17px; about 45 characters, 95 at the outside.
- The explanation adds a fact that is in neither the question nor the
  answer. When a fact is split into several questions, keep each
  explanation from giving away its siblings.
- No leakage: a question must not give away another question in its topic.
- Difficulty mix per topic of roughly 4 easy, 6 medium, 3 hard. "Easy" still
  means easy for a physician, not for a layperson.
- The model of a strong single question is as-dx-01: one finding, one axis of
  comparison, a fact worth carrying into clinic. (Noted as strong,
  2026-09-13.)

## Multiple answer questions

- 4 to 8 options, with 2 or more correct. Never exactly one correct.
- Options are parallel: same grammatical shape, same specificity, one idea
  each.
- **They must need clinical judgement.** Sorting things into categories a
  physician already knows (modifiable versus not, classic versus atypical)
  is too easy and gets retired. Good multi-select material: indications,
  triggers for action, complications by route, which comorbidities
  confound a picture. (From the note on as-dx-07, 2026-09-13.)
- Checked by swipe up. Any error costs one light, so the set should reward
  knowing the whole picture rather than punish one borderline option. Avoid
  options that are "sometimes" correct.

## Clinical content

- Prefer questions about decisions (what to do next, when to refer, when to
  repeat) over recall of isolated numbers, unless the number drives a
  decision.
- Use the article's own thresholds and wording for criteria.
- Keep drug names generic. Include dose only when the article gives one and
  it matters.
- Definitional questions ("which of these is X") are too easy for the
  audience. Ask what the definition changes about care instead.

## Rules added from feedback

- 2026-09-13: one idea per option; numeric options ordered and fixed;
  multi-select needs judgement; definitional questions retired. See the
  first entry in `question-feedback.md`.
