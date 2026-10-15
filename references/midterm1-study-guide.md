# Study guide for weeks 1–7 (Aug 25 – Oct 8, 2026)

Written 2026-10-11. Companion to `external-resources.md`, which has the page-level references for
most lectures; this file adds the lectures it skips (Sep 8, 10, 15, 17, Oct 8) and the exam view.

Not known from anything in this repo: the midterm date, its exact scope, and its format. The
syllabus only says "Midterm exam 1: 25%". The likely-question list in section 3 is inference from
what was assigned in class, not information from the professor.

Week-by-week recap with figures, timed blocks and self-checks:
<https://claude.ai/artifact/2ogYiEzX2Ln3MxYxbD5gBi> (private; open it while signed in). One week per
sitting. After each sitting, do that week's section of `weeklypackets/weeklypackets.pdf`: the
scribe results to have open (number and page in `scribes/main.pdf`), then likely questions with
full solutions.

| Week | Lectures | Topic | Time |
|---|---|---|---|
| 1 | Aug 25, 27 | Expectation, geometric variable, deterministic search lower bound | 60 min |
| 2 | Sep 1, 3 | Coupon collector, Yao, Markov / Chebyshev / Chernoff, birthday, collision bound | 90 min |
| 3 | Sep 8, 10 | Leader election, weak law, random walks and stationary distribution | 90 min |
| 4 | Sep 15, 17 | Qubits, unitaries, H and CNOT, entanglement (`ad = bc`), rank | 60 min |
| 5 | Sep 24 | `U_f`, phase kickback, Deutsch, Hadamard transform, Deutsch–Jozsa | 75 min |
| 6 | Sep 29, Oct 1 | Bernstein–Vazirani, Simon (quantum and classical bounds) | 120 min |
| 7 | Oct 6, 8 | Grover, number of iterations, random `k`, amplitude amplification | 120 min |

## 1. What the seven weeks cover

Syllabus topics 1–3 and 5–8 are done. Topic 4 (superdense coding, teleportation) has no scribe.

| Block | Lectures | What you need to be able to do |
|---|---|---|
| Probability tools | Aug 25, Sep 1, Sep 3 | Expectation by indicators and linearity; geometric random variable; union bound; `1 − x ≤ e^(−x)`; Markov, Chebyshev, Chernoff (which one to use when); "with high probability"; coupon collector (`n H_n`, and `3n ln n` w.h.p.); birthday paradox by first and second moment |
| Query complexity, classical | Aug 25, Sep 1, Sep 3, Oct 1 | Adversary argument for deterministic lower bounds; Las Vegas vs Monte Carlo; Yao's minmax principle (pick a hard input distribution, bound the best deterministic algorithm); collision lower bound `Ω(√n)` |
| Distributed computing | Sep 8 | Anonymous nodes: no deterministic leader election (symmetry); the randomized algorithm (candidates, referees), at least one / at most one leader, message and round counts |
| Markov chains | Sep 8, Sep 10 | Transition matrix `P`, `p_(t+1) = p_t P`, row stochastic preserves probability vectors, stationary distribution `π_v = d(v)/2m`, convergence iff connected and non-bipartite, the eigenvalue proof; weak and strong law of large numbers |
| Quantum basics | Sep 15, Sep 17 | Kets, bras, dagger; unitary iff norm preserving; `H`, `X`, `Z`, CNOT as matrices; `HH = I`; tensor products; proving a state is entangled; rank, linear independence, orthogonal implies independent |
| Query algorithms | Sep 24, Sep 29, Oct 1 | `U_f` and why it is unitary; phase kickback; `H^(⊗n)∣x⟩ = 2^(−n/2) Σ_y (−1)^(x·y) ∣y⟩`; the sum-of-signs lemma; Deutsch, Deutsch–Jozsa, Bernstein–Vazirani, Simon (one run, then linear algebra over GF(2)), probability that the `y`'s are independent |
| Grover | Oct 6, Oct 8 | `Z_f`, `Z_0`, `D = 2∣h⟩⟨h∣ − I`; the plane spanned by `∣A⟩`, `∣B⟩`; `sin θ = √(a/N)`; state after `k` iterations `sin((2k+1)θ)∣A⟩ + cos((2k+1)θ)∣B⟩`; choice of `k`; overshooting; random `k` when `a` is unknown; amplitude amplification `Q = −A Z_0 A^(−1) Z_f` |

Query counts to have in one place (all are in the scribes):

| Problem | Deterministic | Randomized | Quantum |
|---|---|---|---|
| Search, one marked item of `N` | `Ω(N)` | `Ω(N)` (Yao) | `Θ(√N)` |
| Deutsch | 2 | 2 | 1 |
| Deutsch–Jozsa | `2^(n−1) + 1` | `O(1)` with bounded error | 1 |
| Bernstein–Vazirani | `n` | `n` | 1 |
| Simon | `Θ(√(2^n))` | `Θ(√(2^n))` | `O(n)` |
| Collision in a random function to `[n]` | — | `Θ(√n)` | not covered yet (Sep 3 says "later in the course") |

## 2. Which parts of the two syllabus references to use

### Pandurangan, randalgos page (15 slide decks)

Use these eight; links for the first seven are in `external-resources.md` section 2.

| Deck (number on the page) | For |
|---|---|
| 1 Introduction | Aug 25 |
| 2 Probability and Randomization I | Aug 25 (sample spaces, amplification), Sep 3 (birthday, slides 27–29) |
| 3 Probability and Randomization II | Aug 25–Sep 1 (expectation, geometric variable, Las Vegas / Monte Carlo) |
| 6 Deviations | Sep 3 (Markov, Chebyshev, variance), Sep 8 (Chebyshev step of the weak law) |
| 7 Chernoff Bounds | Sep 1 (slides 3–7 have the proof the scribe omits; slide 10 compares the three inequalities) |
| 10 Balls into Bins Paradigm | Sep 1 (coupon collector, slides 15–17; max load) |
| 12 Probabilistic Method | Sep 3 (slide 17, first and second moment method) |
| 15 Markov Chains and Random Walks | Sep 8, Sep 10. <https://drive.google.com/file/d/1OOBseTZQyn3r-8XQW6vKCYjWnuzVQ_YR/view>. Not opened yet, so no slide numbers. `external-resources.md` lists Markov chains as "not covered"; that is wrong for Sep 8 and 10 |

Skip: 4 MIS, 5 MST, 8 Packet Routing, 9 Randomized Rounding, 11 Two Choices, 13 Lovász Local
Lemma, 14 Martingales.

### Watrous, QC-notes (22 lectures)

| Lecture | For |
|---|---|
| 1, 2 Overview of quantum information | Sep 15 (qubits, unitaries, Hadamard, measurement; tensor products, entanglement, Dirac notation) |
| 3 Superdense coding; circuits; partial measurements | Sep 15 (CNOT, circuit conventions), Sep 22, and the partial-measurement rule used in Simon |
| 4 Teleportation; Deutsch | Sep 22 (p1–3, teleportation), Sep 24 (p3–6) |
| 5 Simple searching; Deutsch–Jozsa | Sep 24 (p3–6), Oct 6 two-qubit example (p1–3) |
| 6 Simon | Sep 29, Oct 1 |
| 12 Grover | Oct 6 (`Z_f`, `Z_0`, reflections, with figures) |
| 13 Grover (continued) | Oct 6 and Oct 8 (rotation by `2θ` as a squared matrix, p2–3; number of iterations and overshooting, p3–4; unknown number of solutions with random `k`, p4–5, stated without proof) |

Skip for now: 7–11 (phase estimation, QFT, order finding: syllabus topic 9, not reached) and
14–22.

### In the scribes but in neither reference

For these the scribe is the only course source, so read them closely.

| Topic | Scribe | Outside source |
|---|---|---|
| Deterministic search lower bound | Aug 25, `thm:detsearch-0825` | — |
| Yao's principle, randomized search lower bound | Sep 1, Oct 1 | Motwani–Raghavan; Karger lecture 4 |
| Collision lower bound | Sep 3, `thm:collision-lb-0903` | — |
| Leader election | Sep 8 | not on the randalgos page |
| Linear algebra review | Sep 17 | any linear algebra text |
| Bernstein–Vazirani | Sep 29 | de Wolf §2.4; Watrous IBM lesson |
| Classical lower bound for Simon | Oct 1 | Cleve's 2-page note; de Wolf §3.3.2 |
| `Pr[independent] ≥ 1/4` | Oct 1, `thm:indep-1001` | Watrous L6 p5 states it without proof |
| Random `k`, proof | Oct 8, `thm:randomk-1008` | Watrous L13 p4–5 states it without proof |
| Amplitude amplification | Oct 8, `thm:ampamp-1008` | de Wolf §7.3; Brassard–Høyer–Mosca–Tapp (paper 8 of the final project list) |

## 3. Likely exam questions (inference)

With the scribes open, copying a proof earns nothing, so expect the in-class results with something
changed: a concrete instance, a different parameter, or one step turned into a new statement.
The 26 exercises he assigned in class are the best evidence of what he thinks you should be able
to do; the list below is those, varied.

Most likely, one or two from each line:

1. **Run an algorithm on a concrete function.** Deutsch–Jozsa or Bernstein–Vazirani on a given
   `f` on 2–3 bits: write the state after each gate. Simon with `n = 3` and a given table: find the
   possible `y`'s, set up the equations, solve for `s`.
2. **Grover with numbers.** Given `N` and `a` (for example `N = 4, a = 1`; `N = 8, a = 2`;
   `a = N/4`): compute `θ`, the best `k`, the success probability, and what one extra iteration
   does. What happens for `a = N/2`, or `a > N/2`?
3. **Grover structure.** Show `D = 2∣h⟩⟨h∣ − I` from `H^(⊗n) Z_0 H^(⊗n)`; show two reflections
   give a rotation by `2θ`; inversion about the mean on a given amplitude vector.
4. **Amplitude amplification applied.** Given a procedure that succeeds with probability `p`
   (for example `p = 1/100`), how many applications are needed classically and quantumly, and why
   `A` must have no measurements.
5. **Entangled or product.** Decide for a given two-qubit state (not the Bell state from class),
   with proof. Check that a given 2×2 or 4×4 matrix is unitary. Compute a small circuit
   (`H` then CNOT, or CNOT in the Hadamard basis).
6. **Random walk on a small graph.** Write `P`, find `π`, say whether `p_t → π` and why (a path or
   an even cycle is bipartite; the triangle is not). Compute `p_1, p_2` from a given start.
7. **Tail bounds in a new setting.** Coupon collector or balls into bins with a different number of
   trials; "show that w.h.p. ..." by Chernoff plus union bound; a problem where you must choose
   between Markov, Chebyshev and Chernoff.
8. **Birthday and collisions with new parameters.** Expected number of collisions for `m` samples;
   how large `m` must be for a constant collision probability; why the same count gives the
   `√(2^n)` bound for Simon.
9. **Lower bounds.** An adversary argument for a deterministic bound on a variant problem; state
   Yao's principle and name a hard distribution for search or for Simon.
10. **Leader election.** Change the number of referees or the candidate probability and redo
    "at least one" and "at most one" leader; count messages.
11. **Compare models.** Fill in or justify rows of the query table in section 1; explain why
    Deutsch–Jozsa is not an exponential separation against randomized algorithms while Simon is.
12. **Linear algebra used by Simon.** Probability that `n − 1` random vectors orthogonal to `s`
    are independent; why `n − 1` independent equations determine `s`; orthogonal implies
    independent.

Less likely but cheap to prepare: why XOR is not reversible and how `U_f` fixes that; the
sum-of-signs lemma `Σ_y (−1)^(x·y)`; the weak law from Chebyshev.

## 4. Holes to close before an open-scribes exam

1. **Sep 22 has no scribe and no photos** (`main.tex` line 81). If superdense coding or
   teleportation was taught that day, it is examinable and you have nothing to open. Get notes from
   a classmate; until then Watrous lectures 3 and 4 (p1–3) are the stand-in.
2. **Chernoff has no proof in the scribe** (`thm:chernoff-0901`). Read Chernoff deck slides 3–7
   once so you can adapt it.
3. **Max-load exercise.** The scribe proves the lower tail (`lem:maxload-lower-0901`, 24 n log n
   queries) and gets the upper tail only as a remark with `c = 144`. His own notes state the upper
   tail with `3n ln n` trials and `9 ln n` (Balls into Bins, Theorem 7.3). Know that version.
4. **Markov chains deck** has not been compared against the Sep 8 and Sep 10 scribes.
5. The scribes contain no worked numeric examples for Simon or for Deutsch–Jozsa; Watrous L6 p1–2
   (`n = 3`, `s = 110`) and de Wolf Ch. 3 have one each. Working one by hand is the best single
   preparation for question 1.
