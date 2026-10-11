# External cross-reference for the scribes (Aug 25 – Oct 6, 2026)

Scanned on 2026-10-11 against the two syllabus reference sites:

- Pandurangan, *Randomized Algorithms and Probabilistic Techniques*: <https://sites.google.com/site/gopalpandurangan/home/randalgos>
- Watrous, *Quantum Computation* lecture notes (Calgary 2006): <https://cs.uwaterloo.ca/~watrous/QC-notes/>

Nothing in `scribes/` was changed. This file is a study aid and a list of things to check; the
course rule is that scribes contain only what was covered in class.

How to read the confidence of an entry:

- Page numbers are PDF pages that were actually opened. For Pandurangan's decks PDF page = slide
  number (Introduction: slide + 1). For his book, PDF page = printed page + 13; both are given.
- "(text only)" means the page was read from extracted text, which drops ≤, ≥, δ, μ. Check the
  sign in the PDF before relying on it.
- Video and course links were loaded and matched unless marked otherwise.

## 1. Findings that matter most

Update, 2026-10-11: findings 3, 4 and 5 were fixed in the scribes after checking the photos
(Chernoff lower tail is now `<` everywhere, as on the Sep 3 board; line 201 now ends in
m²/(2n) = Θ(m²/n); the "next lecture" sentences are gone from Aug 25). Finding 6 needs no
change: the Oct 1 board itself rewrites the state with the registers swapped ("rearrange").

1. **Max-load exercise direction (`ex:maxload-0901`).** The scribe states the exercise as
   "any slot is accessed ≤ c log n times" with probability ≤ 1/n². Both of the professor's own
   written versions are the upper tail: Balls-into-Bins p15, Theorem 7.3, "with probability at
   least 1 − 1/n no coupon is collected more than 9 ln n number of times", and book Exercise
   8.26(3). `lem:maxload-upper-0901` is that reading. `lem:maxload-lower-0901` has no
   counterpart in his notes. Proving both readings is still what the repo rule asks for; this
   tells you which one he most likely meant. The lecture photo was not re-examined.
2. **Max-load constant.** His notes get 9 ln n with 3n ln n trials (p17, "Using the Chernoff
   bound", no computation). The scribe proves 18 log n via the 2^(−R) form. The general form
   (e^δ/(1+δ)^(1+δ))^μ with δ = 2 gives about n^(−3.89), so 9 is provable; that computation is a
   reconstruction, not in the source.
3. **Chernoff lower tail is written two ways in the scribes.** 09-01 line 192 has
   `X ≤ (1−δ)μ`; 09-03 line 87 has `X < (1−δ)μ`. The source (Chernoff p4; book Theorem C.9,
   printed 320) has strict events on both tails: Pr(X > (1+δ)μ) and Pr(X < (1−δ)μ). The
   non-strict forms are true, but `lem:maxload-lower-0901` relies on the ≤ form, which the
   source does not state.
4. **Expected collisions, 09-03 line 201.** The line reads `m(m−1)/(2n) ∼ m²/n`. The asymptotic
   form of the exact value on the same line is m²/(2n).
5. **Promised proof never given.** 08-25 lines 95–96 and 229–230 say the next lecture defines
   expectation and proves E[samples] = n. 09-01 lines 18–22 only assert it from the geometric
   random variable. Source for both: Prob II p10 (definition), book §C.7.2, printed 317–318
   (proof of E[X] = 1/p).
6. **Register order differs between two scribes.** 09-29 line 232 writes `|y⟩|f(x)⟩`;
   10-01 line 311 writes `|f(x)⟩|y⟩` ("target register written first"). Watrous L6 p3 uses the
   first order.
7. **`U_f` is overloaded.** 09-24 line 23 uses it for the XOR oracle and line 150 for the phase
   oracle (the scribe says so at line 151, "instead of the original form"); 10-06 switches to
   `Z_f` at line 121. Watrous keeps `B_f` (XOR) and `Z_f` (phase) apart throughout. This is a
   naming choice, not an error; keep whatever the board used.
8. **Bernstein–Vazirani is not in Watrous's 2006 notes** (searched all 22 lectures). Use his IBM
   lesson or de Wolf §2.4 instead (section 3 below).
9. **Watrous does not prove the classical lower bound for Simon** (L6 p2, "We will not go
   through the proof of this fact"). The Oct 1 scribe goes further than he does. Proofs to
   compare against: Cleve's 2-page note and de Wolf §3.3.2 (section 3, Oct 1).
10. **Neither site has videos, homeworks or exams.** Videos and exercise sets below come from
    other sources. No recordings of either professor's own course were found.

## 2. Source inventory

### Pandurangan (typed slide decks, Google Drive)

| Deck | Pages | Link |
|---|---|---|
| Introduction | 9 | <https://drive.google.com/file/d/1OiD8F3tg_Sp43DiW97yzo17QXIOFlsKs/view> |
| Intro to Probability and Randomization I | 32 | <https://drive.google.com/file/d/1UUGnMwR3s5fxbiXCo7ifdKc_sWpL9gM1/view> |
| Intro to Probability and Randomization II | 23 | <https://drive.google.com/file/d/1dDMgUHNmho8HHRtubVjZ_dl75Y7z6k_Q/view> |
| Deviations | 24 | <https://drive.google.com/file/d/1EjFWIn5GXPwZJPCIyl_u9U5oo-jDHNqz/view> |
| Chernoff Bounds | 23 | <https://drive.google.com/file/d/1nGFAjUFPJm1GlkTmyJR6MHDHUpSGs6_w/view> |
| Balls into Bins Paradigm | 35 | <https://drive.google.com/file/d/1u87qaQDSjb7njlM0WlInhOW16hklrdKU/view> |
| Two Choices Method (skimmed) | 10 | <https://drive.google.com/file/d/1YI54BN2kDyeBAcCm-_8_43VKw-ZNjFJS/view> |
| Probabilistic Method (skimmed) | 20 | <https://drive.google.com/file/d/1uEy6F0Ro8IOuVJwDplIbyqB7eQlMt1ut/view> |

Book: *Algorithms: An Intuitive Approach* (free PDF, dated May 5, 2024, 352 pages), linked from
<https://sites.google.com/site/gopalpandurangan/home/algorithms-design>:
<https://drive.google.com/open?id=1Wf5IKPjagt3uNybXtOjRf0vqDJ-N_gA0>. This is the book already
cited in `scribes/references.bib` (the bib entry says 2025). Relevant parts: Ch. 8 (randomized
algorithms), Appendix C (probability), §10.1 (primality). It has exercises, no solutions.
His newer *Efficient Algorithms, Part 1* has no randomization chapter yet.

Not covered in class, so skipped: MIS, MST, packet routing, randomized rounding, LLL,
martingales, Markov chains.

### Watrous (typed notes, `https://cs.uwaterloo.ca/~watrous/QC-notes/QC-notes.NN.pdf`)

| NN | Title | Pages | Used for |
|---|---|---|---|
| 01 | Overview of quantum information | 5 | Sep 22 (unscribed) |
| 02 | Overview (continued) | 8 | Sep 22 (unscribed) |
| 03 | Superdense coding; quantum circuits; partial measurements | 8 | Sep 22 (unscribed) |
| 04 | Quantum teleportation; Deutsch's algorithm | 6 | Sep 24 |
| 05 | A simple searching algorithm; Deutsch–Jozsa | 6 | Sep 24, Oct 6 |
| 06 | Simon's algorithm | 5 | Sep 29, Oct 1 |
| 12 | Grover's algorithm | 6 | Oct 6 |
| 13 | Grover's algorithm (continued) | 5 | Oct 6 |

Lectures 04, 05, 06, 12, 13 were read in full; 01–03 were skimmed from extracted text.
These notes have no exercise sections.

## 3. Lecture by lecture

### Aug 25 — efficient algorithms, random sampling, deterministic search lower bound, probability basics

| Scribe item | Source | What it adds |
|---|---|---|
| Primality / input size (lines 11–27) | Book §2.2, §2.6 (printed 8–11, 24) | Trial division, input size in bits |
| Miller–Rabin amplification (lines 31–38) | Book §10.1 (printed 210–213); Prob I p8–9, p18 | Second worked example of repeat-to-amplify (polynomial identity checking) |
| Random number in one step (lines 42–51, 79–82) | Book Exercise 8.1 (printed 176) | The scribe handles n a power of 2 only; the exercise asks for general k in O(log k) |
| `thm:detsearch-0825` | none | Not in his notes. Nearest analogue: adversary argument for the repeated-element problem, n/2+2 steps (MAS 720 variant of Prob I, p3) |
| Probability basics (lines 176–187) | Prob I p1–2; Prob II p8 | Same definitions; the source allows countably infinite sample spaces, the scribe says finite |
| E[samples] = n (lines 93–96) | Prob II p10; book §C.7.2 (printed 317–318) | The definition and proof the scribe promises (finding 5) |

Difference to note: the scribe says at least 3/4 of {2, …, n−2} are witnesses, error (1/4)^k.
The book (Lemma 10.2, Theorem 10.5, printed 212–213) uses a Fermat test with "at least half",
error 1/2 per round. Both are standard; they are different tests.

Videos: MIT 6.5220 playlist (Karger), <https://www.youtube.com/playlist?list=PL278F9gM5aZb8HXAh2yT3QmwyYQZrQUNH>.

### Sep 1 — Monte Carlo / Las Vegas, coupon collector, w.h.p., randomized lower bound, Chernoff, max load

| Scribe item | Source | What it adds |
|---|---|---|
| Monte Carlo / Las Vegas (lines 12–24) | Prob II p23 (text only); book §8.5.1 (printed 155); book Exercise 8.16 | One-sided vs two-sided error; the scribe's "error probability > 0" is a stricter paraphrase of "may produce an incorrect solution" |
| `thm:coupon` | Balls-into-Bins p15–16, Theorem 7.1 | Identical proof; sharper final form n H_n = n ln n + O(n) |
| `thm:whp` | Balls-into-Bins p16–17, Theorem 7.2; book Definition 8.1 (printed 148–149) | Identical proof; a formal definition of w.h.p. Note the theorem statement says 2n ln n but its proof uses 3n ln n, as the scribe does |
| `thm:lowerbound`, Yao (lines 133–143) | none | No mention of Yao or any randomized lower bound in his notes. Cite Motwani–Raghavan (see below) |
| `thm:chernoff-0901` | Chernoff p3–7; book Theorem C.9 and §C.9.1 (printed 320) | Full proof (the scribe states it unproved); general form for any δ > 0; hypothesis 0 < p_i < 1 |
| `ex:maxload-0901`, `lem:maxload-upper-0901` | Balls-into-Bins p15, p17 (Theorem 7.3); p2–3; book Theorem 8.10 (printed 163) | Findings 1 and 2. p2–3 gives a proof without Chernoff: C(m,k)(1/n)^k and a union bound |
| `lem:maxload-lower-0901`, `cor:maxload-0901` | none | Closest: Balls-into-Bins p25, Corollary 2 (text only), a lower-tail-plus-union-bound statement about vertex degrees |

Further results in the same deck, beyond what was scribed: max load at least ln n / ln ln n
(p13–14, Theorem 6); sharp threshold for coupon collector (p31–35, Theorem 11).

Exercises with the same content: book Exercise 8.26 (printed 182) restates all three coupon
collector parts as "Show each of the following"; Exercise 8.12 (printed 178), minimum m so every
bin is non-empty with probability 1 − 1/n.

Videos and solved exercises:

- Karger, "6.5220 Lecture 4: Game theory, Lower Bounds 1, Coupon Collecting, Stable Matching", <https://youtu.be/ET8g7RjWn9U> (by its title, the Yao's-principle lecture; not watched).
- Karger, "6.5220 Lecture 7: Chernoff Bound. Randomized routing", <https://youtu.be/ljkB2msfwMc>.
- Stanford CS265 (Wootters/Valiant), <https://web.stanford.edu/class/cs265/>: Class 5 (Chernoff), Class 6 (balls and bins), with posted solutions, e.g. <https://web.stanford.edu/class/cs265/Lectures/Lecture6/class6-sols.pdf>. Best free source of solved exercises for this material.
- Yao's principle: <https://en.wikipedia.org/wiki/Yao%27s_principle>. Textbook: Motwani–Raghavan §2.2 (section number from memory, not checked).

### Sep 3 — Markov, Chebyshev, Chernoff, birthday paradox, collision lower bound

| Scribe item | Source | What it adds |
|---|---|---|
| `thm:markov` | Deviations p2, Theorem 1 | Same statement and proof; example Pr(≥ 3N/4 heads) ≤ 2/3 |
| Variance definition (lines 56–61) | Deviations p3 | Identical |
| `thm:chebyshev` | Deviations p5–6, Theorems 2–4 | Identical; Theorem 4 with ε = 1 is the step at lines 273–274 |
| All three inequalities compared | Chernoff p10 | One example, Pr(X ≥ 3N/4): Markov 2/3, Chebyshev 4/N, Chernoff exponential |
| Birthday product bound (lines 137–159) | Prob I p27–29; book §C.4 | Same derivation, same m = √(2N)+1, same 1/e; p29 names the "Principle of Deferred Decisions" |
| Expected collisions (lines 185–202) | Book Lemma 9.9 (printed 196) | Hashing version of the same indicator count (finding 4) |
| `lem:pairwise-0903` | Deviations p7–8 (text only) | E[XY] = E[X]E[Y] and Var[X+Y] for independent variables, with proofs. Pairwise independence of collision indicators is not discussed. Book Exercise 8.6 asks for a pairwise-but-not-mutually independent example; X_12, X_13, X_23 are one |
| `thm:birthday-0903` | Probabilistic Method p17, Theorem 8; book Theorem C.8 | Named "First and Second Moment Method": Pr(X = 0) ≤ Var(X)/(E X)². Same argument; the source never applies it to birthdays. p18–20 has a second worked example (isolated vertices in G(n,p)) |
| `ex:collision-lb-0903`, `thm:collision-lb-0903` | none | Not in his notes |

No differences found in Markov, Chebyshev, the variance definitions or the birthday bound.

Videos and solved exercises: Karger, "6.5220 Lecture 5: Deviations: Markov, Chebyshev. Balls in
Bins", <https://youtu.be/5n2wzljxeWY>; Stanford CS265 Class 4 solutions,
<https://web.stanford.edu/class/cs265/Lectures/Lecture4/class4-sols.pdf>.

### Sep 22 — quantum circuits (not scribed; pointers only)

| Topic | Watrous | IBM lesson and video (Watrous) |
|---|---|---|
| Qubits, unitaries, Hadamard, measurement | L1 p3–5 | Single Systems, <https://youtu.be/3-c4xJa7Flk> |
| Tensor products, entanglement, Dirac notation | L2 p1–8 | Multiple Systems, <https://youtu.be/DfZZS8Spe7U> |
| Circuit conventions, CNOT, Toffoli, partial measurement | L3 p2–8 | Quantum Circuits, <https://youtu.be/30U2DTfIrOU> |

Course text for the IBM lessons: <https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information>.
Watrous L3 p6–8 has worked examples of the partial-measurement rule that 09-29 lines 208–210
state in one sentence. The Sep 22 scribe still has to come from the lecture photos.

### Sep 24 — Deutsch, phase flip, Walsh–Hadamard, Deutsch–Jozsa

| Scribe item | Watrous | What it adds |
|---|---|---|
| Deutsch's problem (lines 9–15) | L4 p3–4 | Table of the four functions |
| Why U_f (lines 19–26) | L4 p4–5 | Concrete non-unitary matrix for a constant f; B_f is always a permutation matrix (alternate unitarity argument) |
| `thm:deutsch-0924` | L4 p5–6 | Same proof step for step; uses the name "phase kick-back" |
| `lem:wh-0924`, `eq:hadamard-0924` | L5 p4–5 | Same derivation |
| Classical bounds for DJ (lines 190–215) | L5 p3–4 | Same bounds; numeric example (k = 11 gives error below 1/1000) |
| `thm:dj-0924` | L5 p5–6 | Same |

Differences: Watrous applies H and measures the first qubit only and discards the second
("trash"); the scribe applies H to and measures both (lines 80–86, 137–138). The statement about
the first qubit is the same. See also finding 7 on the name `U_f`.

Videos and other notes:

- Watrous, "Quantum Query Algorithms | Lesson 05", <https://youtu.be/2wticzHE1vs>; text at <https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/deutsch-algorithm> (has a section on phase kickback) and `.../deutsch-jozsa-algorithm`.
- de Wolf, *Quantum Computing: Lecture Notes*, Ch. 2, <https://arxiv.org/abs/1907.09415> (exercises at chapter end; hints only, Appendix C).
- Shor, 8.370 Lecture 16, <https://math.mit.edu/~shor/435-LN/Lecture_16.pdf>.
- Aaronson, Lecture 17, <https://www.scottaaronson.com/qclec.pdf> (open in a browser).

### Sep 29 — Walsh–Hadamard recap, Bernstein–Vazirani, Simon's algorithm

| Scribe item | Watrous | What it adds |
|---|---|---|
| `lem:signsum-0929` | none | Not in Watrous |
| `thm:bv-0929` | none (finding 8) | IBM lesson text, sections "The Bernstein-Vazirani problem" and "Classical difficulty", inside `.../quantum-query-algorithms/deutsch-jozsa-algorithm`; de Wolf §2.4; Aaronson Lecture 18 |
| Simon's problem (lines 110–122) | L6 p1–2 | Concrete n = 3 table with s = 110 |
| `thm:simon-run-0929` | L6 p2–4 | Same computation in both cases; he calls the range A where the scribe uses R |
| `alg:simon-0929`, `thm:simon-0929` | L6 p4–5 | Same n − 1 runs and the same f(0ⁿ) = f(s′) check. Amplification is parametrized differently: he repeats 4m times for failure below e^(−m); the scribe uses t = ⌈log_{4/3} n⌉ for 1 − 1/n. Consistent |
| `ex:simon-det-0929` | none | Not in Watrous. de Wolf §3.3.1 has the birthday-style O(√(2ⁿ)) upper bound |

The scribe notes at lines 275–278 that class said "n measurements give n equations"; Watrous
supports n − 1. He leaves "(x_z ⊕ s)·y = (x_z·y) ⊕ (s·y)" to the reader (L6 p4); the scribe
uses it at line 252 and argues bilinearity at lines 43 and 90–91.

Videos and other notes:

- Watrous Lesson 05 (same video as above); Simon text at <https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/quantum-query-algorithms/simon-algorithm>.
- O'Donnell, "Simon's Algorithm: Lecture 13 of Quantum Computation at CMU", <https://youtu.be/tXux8-UMSv8>; notes <https://www.cs.cmu.edu/~odonnell/quantum18/lecture13.pdf>; weekly homeworks on the course page <https://www.cs.cmu.edu/~odonnell/quantum18/> (no solutions).
- de Wolf Ch. 3 (worked 3-qubit instance; exercises with hints).
- Shor, Lecture 18, <https://math.mit.edu/~shor/435-LN/Lecture_18.pdf>.
- MIT OCW 18.435J (Shor, 2003) assignments with posted solutions, <https://ocw.mit.edu/courses/18-435j-quantum-computation-fall-2003/pages/assignments/>. The only quantum course found with full solutions.

### Oct 1 — classical complexity of Simon's problem, Yao, linear independence

| Scribe item | Source | What it adds |
|---|---|---|
| `thm:simon-rand-ub-1001` | de Wolf §3.3.1 | Birthday-paradox upper bound |
| `thm:simon-rand-lb-1001`, `lem:yao-1001`, `lem:collision-1001`, `lem:indist-1001` | Cleve, "Classical Lower Bound for Simon's Problem" (2 pages), <https://cleve.iqc.uwaterloo.ca/resources/QIC-710-F19/SimonClassicalLB.pdf>; de Wolf §3.3.2 | Two independent write-ups of the same Yao-style argument: fix a hard input distribution, analyse deterministic algorithms, bound Pr[collision] by T²/2ⁿ. de Wolf's is the closest match to the lecture |
| same | Watrous IBM text, Simon lesson, section "Classical difficulty" | Explicit constant: fewer than 2^(n/2−1) − 1 queries fails with probability at least 1/2. Statement only was checked |
| `lem:prodsum-1001` | none | Not in Pandurangan's notes or book Appendix G.2 |
| `ex:simon-11-1001` | Watrous L6 p3 | Same argument (replace f(x) by x in the one-to-one case) |
| `ex:indep-1001`, `thm:indep-1001` | Watrous L6 p5; Cleve course notes pp. 137–138, <https://cleve.iqc.uwaterloo.ca/resources/QIC-710-F26/Qic710LectureNotes2026V2.pdf> | Watrous states "at least ∏_{k≥1}(1 − 1/2^k) = 0.288788··· > 1/4" without proof; Cleve derives the row-by-row product and leaves "≥ 1/4" as an exercise. The scribe proves the finite product and adds a separate 1/2 bound for the one-to-one case, which neither has |

An alternative to the independence argument, from the IBM Simon lesson: with n + r runs the
null space is exactly {0, s} with probability at least 1 − 2^(−r).

Book Exercise 8.19 (printed 179) is the averaging fact behind `lem:yao-1001`.

### Oct 6 — Grover's search

| Scribe item | Watrous | What it adds |
|---|---|---|
| Two-qubit example (lines 26–53), `fig:grover4-1006` | L5 p1–3, "simple searching problem" | The same N = 4 algorithm derived as a state-distinguishing problem; his matrix U (−1/2 on the diagonal, 1/2 elsewhere) equals the scribe's D at N = 4, and he gives a gate-level circuit. Also states the classical count: three queries. The identification with Grover is ours; Watrous does not make it |
| Classical bound (lines 20–22) | L12 p2 | Short self-contained argument. Typo there: "Ω(2^N)" should be Ω(2ⁿ) |
| Z_f, Z_0 (lines 120–161), `fig:zf-1006` | L12 p2 | Same; his ancilla starts in ∣0⟩ with NOT gates, the scribe's starts in ∣1⟩. Equivalent |
| `lem:diffusion-1006` | L12 p5 | Same computation for H Z_0 H = I − 2∣h⟩⟨h∣. He never uses the words "diffusion" or "inversion about the mean"; the amplitude form is only in the scribe |
| `lem:giter-1006` | L12 p6 | Same formulas; he attaches the minus sign to Z_f, the scribe to D. Same G = −H Z_0 H Z_f |
| Reflections give a rotation (lines 296–298) | L12 p3–4 | Full geometric explanation with figures, where the scribe has one sentence |
| `eq:gmatrix-1006`, `ex:grover-rotation-1006` | L13 p2–3 | Alternate proof that the matrix is a rotation by 2θ, by squaring R_θ. Same angle (sin θ = √(a/N)) and basis order. He states the state after k iterations without the induction the scribe gives |
| `thm:grover-1006` | L13 p3–4 | For a = 1 he takes k = ⌊(π/4)√N⌋ and says the success probability is "always at least 1/2", with a table for N = 2 to 4096 and no proof. The scribe's k = ⌊π/(4θ)⌋ and bound 1 − a/N are stronger and proved. The two choices of k agree for a = 1, N = 2ⁿ, n = 1..60 (numerical check) |
| "Do not overshoot" (lines 396–401) | L13 p4 | Concrete failure example: a = 4 with the a = 1 iteration count sends the success probability to 0 |

In Watrous and not in the scribe:

- **Unknown number of solutions** (L13 p4–5): choose k at random in {1, …, √N+1}, failure at most
  3/4; then a growing schedule with factor 8/7 giving O(√(N/a)) queries and success at least 1/4.
  Both are stated without proof. As written, m = ⌊(8/7)m⌋ starting from m = 1 never increases;
  a ceiling or real-valued m is presumably intended.
- **a = 0 and a = N** (L13 p5): the output is uniformly distributed. The scribe assumes
  1 ≤ a ≤ N − 1 (line 223), and its problem statement has no "no solution" outcome.

In the scribe and not in Watrous L12–13: the 1/√N, 3/√N, 5/√N amplitude heuristic (lines
103–114) and the remark that Ω(√N) quantum queries are necessary (lines 23–24). For the lower
bound see Shor Lecture 25 or Aaronson Lecture 23 below.

The scribe says at lines 189–190 "The notes write D = I − 2∣h⟩⟨h∣". Watrous has exactly that
expression for H Z_0 H (L12 p5), so that sentence may be referring to him.

Videos and other notes:

- Watrous, "Grover's Algorithm | Lesson 08", <https://youtu.be/hnpjC8WQVrQ>; text at <https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/introduction> (sections `/analysis` with the geometric picture, `/number-of-iterations`).
- O'Donnell, "Grover's Algorithm: Lecture 18", <https://youtu.be/F1p-_Y0xA5I>; notes <https://www.cs.cmu.edu/~odonnell/quantum18/lecture18.pdf>.
- de Wolf Ch. 7 (§7.2 geometric argument, §7.3 amplitude amplification; exercises with hints).
- Shor, Lecture 24, <https://math.mit.edu/~shor/435-LN/Lecture_24.pdf>, and Lecture 25 (optimality) on <https://math.mit.edu/~shor/435-LN/>.
- Aaronson, Lectures 22–23, <https://www.scottaaronson.com/qclec.pdf>.
- Preskill Ph219 (2020), Lecture 16 "Quantum searching", playlist <https://www.youtube.com/playlist?list=PL0ojjrEqIyPy-1RRD8cTD_lF1hflo89Iu>.

## 4. Whole-course resources

| Resource | Type | Link |
|---|---|---|
| Watrous, *Understanding Quantum Information and Computation* (book form of the IBM lessons; Ch. 5 query algorithms, Ch. 8 Grover; no exercises) | book | <https://arxiv.org/abs/2507.11536> |
| Watrous video playlist (Qiskit) | video | <https://www.youtube.com/playlist?list=PLOFEBzvs-VvqKKMXX4vbi4EB1uaErFMSO> |
| de Wolf, *Quantum Computing: Lecture Notes* | notes + exercises (hints) | <https://arxiv.org/abs/1907.09415> |
| O'Donnell, CMU 15-859BB (2018) | video + notes + homeworks | <https://www.cs.cmu.edu/~odonnell/quantum18/> |
| O'Donnell and Wright, 2015 scribe notes in one file | notes | <https://www.cs.cmu.edu/~odonnell/quantum15/QuantumComputationScribeNotesByRyanODonnellAndJohnWright.pdf> |
| Shor, 8.370/18.435 lecture notes (2022) | notes | <https://math.mit.edu/~shor/435-LN/> |
| MIT OCW 18.435J (2003) | homeworks + solutions | <https://ocw.mit.edu/courses/18-435j-quantum-computation-fall-2003/pages/assignments/> |
| Stanford CS265 Randomized Algorithms | video + exercises + solutions | <https://web.stanford.edu/class/cs265/> |
| MIT 6.5220 Randomized Algorithms (Karger) | video | <https://courses.csail.mit.edu/6.856/current/> |

## 5. Not checked

- The lecture photos were not re-read, so finding 1 does not settle what the board said.
- The combined Watrous file `QC-notes.pdf` was not opened; the 22 individual lectures were.
- O'Donnell lectures 11–12 ("Revealing XOR-patterns") are listed on his page but were not opened;
  that they cover Deutsch–Jozsa and Bernstein–Vazirani is an inference from the titles.
- Mitzenmacher–Upfal and Motwani–Raghavan section numbers are from memory.
- Other Pandurangan decks linked from his other course pages ("Search", "Prime number checking",
  "Probabilistic Algorithms", "Fingerprinting, Hashing and Randomization 1–3") were not opened.
  "Search" is the likeliest place for `thm:detsearch-0825`.
