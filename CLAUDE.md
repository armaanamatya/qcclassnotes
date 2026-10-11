# COSC 6397 Quantum Computing: lecture scribes

## Assigned questions in the lecture photos (this is the graded assignment)

Throughout each lecture the professor gives questions to prove, explore, or solve. In the
handwritten photos (`progress/*`, `mynotes/*`) they appear as:

- a bounded box (dashed or solid) drawn around a statement,
- a dash-prefixed or standalone line saying "Show ...", "Prove ...", "Exercise", "HW",
- a "?" at the end of a derivation, a table entry, or a circuit wire,
- a "we will show later / left to you / do this yourself" remark.

Every one of them must appear in the scribe as an `exercise` environment followed by a complete,
human-readable proof or solution (a named `lemma`/`theorem` with `proof`, or `wsolution`).
Flagging it with `\solutionspace` or a TODO is not enough. A box around a definition that is then
used in a proof is not a question; when in doubt, include and solve it. If the handwriting is
ambiguous (for example `<=` vs `>=`), prove the natural reading and say in one sentence whether the
alternative also holds; do not prove both.

Keep the scribes short and plain: no commentary about the notes or the board, no recaps that
restate an earlier lecture (point to it), no remarks that go beyond the lecture, one proof per result.

Workflow:

1. Before transcribing a lecture, list every prompt found in its photos (page, wording).
2. Write the full argument for each in the scribe, next to the exercise statement, or in a
   clearly cross-referenced section if the tools it needs come later in the lecture.
3. Before opening a PR, `grep -rn "solutionspace\|TODO" scribes/tex` must return nothing, and
   the PR description says which questions were found and solved.

## Layout and build

- One file per lecture in `scribes/tex/lecture_YYYY-MM-DD.tex` (copy `lecture_template.tex`),
  wired into `scribes/main.tex` in chronological order with `\newlecture{weekday, date}{topic}`.
- Lectures are grouped by week with `\newweek{number}{dates}` (week 1 is August 24--28, 2026;
  lectures are on Tuesday and Thursday). The table of contents lists weeks, then lecture days, then
  sections. Sections are numbered from 1 inside each lecture; keep them few (three to five per
  lecture) and make short topics a `\subsection` or `\paragraph` of a neighbouring section.
- `scribes/scribe.sty` is the unmodified course style file. Put additions in `scribeextras.sty`.
- Build from `scribes/` with `pdflatex -interaction=nonstopmode main.tex`, three passes
  (table of contents and cross-references). Commit the rebuilt `main.pdf`.
- `main.tex` has a commented-out AI use declaration that must be filled in before each submission.
