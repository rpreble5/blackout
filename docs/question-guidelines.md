# Question guidelines

The rules applied every time questions are written for Blackout. This file is
distilled from `question-feedback.md`, the running log of notes left in the
game. When a note changes a rule, the rule changes here and the note is cited.

## Source and grouping

- Articles set: questions come from one source article at a time, and every
  question must be answerable from that article alone.
- Foundations set: questions are written from a named standard guideline
  (ACC/AHA, ADA and the like) and the topic file cites it. Only settled,
  guideline-level facts qualify; anything contested or edition-dependent is
  left out. These need the user's review more than article questions do.
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
- **Options are matched in length.** The correct option is never the only
  long one or the only short one; keep every option within about a third of
  the others, and give distractors the same specificity as the answer. (From
  the self-review of the first ITE batch, 2026-10-09.)
- Distractors avoid absolute words (always, never, everyone, only); they
  read as tells.
- **Every question and explanation stands alone.** Never refer to the exam,
  the item, the other options, a sibling question, or what was or was not
  "the answer". The player sees one card at a time with no context. (From
  the user's note on the second ITE batch, 2026-10-09.)
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

## ITE set

- Source is the ABFM in-training exam critique books. The PDFs are
  copyrighted and never enter the repo; `docs/facts/ite-<year>.md` holds
  the lessons in our own words, one entry per exam item, and every
  question carries an `item` field pointing at the item it came from.
- Stems are rewritten, never copied: the two or three facts that drive the
  decision, no vignette.
- One exam item yields one question for the answer and one for each
  distractor the critique gives a real reason for ("why not B"). A
  distractor dismissed without a reason does not earn a question.
- The pivot, when the critique names one (the finding that made A right and
  B wrong), is the best question of the set and is written first.
- The ITE set is a pool: its topic files are authoring batches of any size,
  and every planet is a random hand of ten.
- An ITE question does not re-test a fact Foundations already holds; take the
  item's pivot or a why-not that Foundations lacks instead.
- Aim for a third of each batch at difficulty 3 and at least a fifth
  multi-select; the critiques' lists are the multi-select material.

## Rules added from feedback

- 2026-09-13: one idea per option; numeric options ordered and fixed;
  multi-select needs judgement; definitional questions retired. See the
  first entry in `question-feedback.md`.
