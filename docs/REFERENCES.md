# REFERENCES.md — Canonical Sources & Per-Lecture Mapping

The course's notation, problem taxonomy, and much of its arc follow **Boyd &
Vandenberghe** (see `docs/NOTATION.md`). This file fixes the citation base so
lectures cite consistently and authors verify claims against the right source.

> These are **unofficial study notes** (see README disclaimer). References are
> for verification and further reading; content is written from scratch, never
> copied. Image provenance rules: `docs/IMAGE_SOURCES.md`.

---

## 1. Primary Text

**[BV]** S. Boyd, L. Vandenberghe, *Convex Optimization*, Cambridge University
Press, 2004. ISBN 978-0-521-83378-3.

Verified from the official book page (`https://stanford.edu/~boyd/cvxbook/`):
- The full **book PDF is legitimately free** on that page (Cambridge University
  Press has agreed to web availability) — link it, never mirror it.
- Official **lecture slides** (Boyd, Vandenberghe, Nobel):
  `https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf`.
- An **Additional Exercises** collection exists on the same page (solutions are
  instructor-only — do **not** reproduce their solutions; our banks ship our
  own solutions per `docs/ASSESSMENT.md` §4).
- Source code for Part-II examples exists in CVX / CVXOPT / CVXPY.

Problems in `data/problems-index.json` titled "BV x.y" are re-derivations of
the corresponding [BV] exercise with original solutions written for this site.

## 2. Per-Lecture Mapping to [BV]

| Lecture | Primary [BV] material | Notes |
| :--- | :--- | :--- |
| L00 Linear Algebra Basics | Appendix A (math background), Appendix C (numerical linear algebra) | supplemented by [Str] |
| L01 Linear Algebra Advanced | Appendix A/C | QR/SVD depth beyond [BV] from [TB], [GvL] |
| L02 Introduction | Ch. 1; Ch. 4 §4.1–4.2 | hierarchy preview draws on Ch. 4 |
| L03 Convex Sets & Geometry | Ch. 2 §2.1–2.3, §2.5 topology parts | |
| L04 Cones & Separation | Ch. 2 §2.4–2.6 (cones, generalized inequalities, separation, dual cones) | Farkas via §2.6 / Ch. 5 examples |
| L05 Convex Functions Basics | Ch. 3 §3.1–3.2 | |
| L06 Convex Functions Advanced | Ch. 3 §3.3 (conjugate), §3.4 (quasiconvex), §3.5 (log-concave); subgradients from [BV-slides]/[Beck] (subgradients are *not* in [BV] main text) | strong convexity from Ch. 9 §9.1.2 |
| L07 Standard Problems | Ch. 4 §4.1–4.4 (LP, QP, QCQP), §4.3.2 (LFP), §4.5 (GP) | |
| L08 Conic Problems | Ch. 4 §4.4.2 (SOCP), §4.6 (SDP); §4.2.5 (quasiconvex via bisection) | exponential cone is post-[BV]; cite [MOSEK-cookbook] |
| L09 Duality | Ch. 5 (entire) | the lecture tracks Ch. 5's arc closely |
| L10 Approximation & Fitting | Ch. 6 §6.1–6.3 (approximation, regularization), §6.3.2 (TV) | LASSO/basis-pursuit modern context: [HTW] |
| L11 Statistical Estimation | Ch. 7 §7.1–7.3 (MLE/MAP, detection), §7.5 (experiment design) | |
| L12 Geometric Problems | Ch. 8 §8.1 (distances), §8.4 (extremal ellipsoids), §8.5 (centering), §8.6 (classification), §8.7 (placement) | Löwner–John factor: §8.4.1 |
| L13 Unconstrained Minimization | Ch. 9 (descent, GD rates, steepest descent in norms, Newton) | BFGS/L-BFGS from [NW] Ch. 6–7 ([BV] has no quasi-Newton) |
| L14 Equality-Constrained | Ch. 10 (KKT systems, elimination, feasible/infeasible Newton) | |
| L15 Interior-Point Methods | Ch. 11 (barrier, central path, complexity, generalized inequalities); primal-dual §11.7 | self-concordance §9.6 + §11.5 |

## 3. Secondary Texts (cite for what [BV] doesn't cover)

| Key | Reference | Used for |
| :--- | :--- | :--- |
| [Beck] | A. Beck, *First-Order Methods in Optimization*, SIAM, 2017 | subgradients, proximal/soft-thresholding, rates |
| [NW] | J. Nocedal, S. Wright, *Numerical Optimization*, 2nd ed., Springer, 2006 | BFGS/L-BFGS, line-search theory, KKT-system numerics |
| [Nes] | Y. Nesterov, *Lectures on Convex Optimization*, 2nd ed., Springer, 2018 | lower complexity bounds, self-concordance origins |
| [Roc] | R. T. Rockafellar, *Convex Analysis*, Princeton, 1970 | rel-int calculus, conjugacy edge cases (closed/proper) |
| [BTN] | A. Ben-Tal, A. Nemirovski, *Lectures on Modern Convex Optimization*, SIAM, 2001 | conic duality depth, robust optimization |
| [Str] | G. Strang, *Introduction to Linear Algebra* | L00's four-subspaces narrative |
| [TB] | L. Trefethen, D. Bau, *Numerical Linear Algebra*, SIAM, 1997 | QR stability, conditioning |
| [GvL] | G. Golub, C. Van Loan, *Matrix Computations*, 4th ed., JHU Press, 2013 | SVD/factorization algorithms |
| [HTW] | T. Hastie, R. Tibshirani, M. Wainwright, *Statistical Learning with Sparsity*, CRC, 2015 | LASSO theory & paths (free PDF from authors) |

## 4. Landmark Papers (single-claim citations)

| Claim in course | Cite |
| :--- | :--- |
| MAX-CUT 0.878-approximation from the SDP relaxation | M. Goemans, D. Williamson, *JACM* 42(6), 1995 |
| DCP ruleset | M. Grant, S. Boyd, Y. Ye, "Disciplined Convex Programming," 2006 (in *Global Optimization*, Springer) |
| CVXPY (referenced by `solver-guide.js`) | S. Diamond, S. Boyd, *JMLR* 17(83), 2016 |
| TV denoising dual algorithm (capstone option B) | A. Chambolle, *J. Math. Imaging Vision* 20, 2004 |
| Khachiyan MVEE algorithm (`mvee-visualizer.js`) | L. Khachiyan, *Math. of OR* 21(2), 1996 |
| Löwner–John ellipsoid factor $n$ | F. John, 1948 (via [BV] §8.4.1) |
| Huber loss | P. Huber, *Ann. Math. Statist.* 35(1), 1964 |

## 5. Citation Rules for Authors

1. **Verify against the source before citing a numbered result.** If you can't
   check it, cite the claim generically ("standard; see [NW] Ch. 6") rather
   than inventing a theorem number. Never cite page numbers from memory.
2. [BV] chapter/section citations follow §2's table; if your content departs
   from that mapping, update the table in the same commit.
3. External links: only to official/author-sanctioned pages (the two Stanford
   URLs in §1 are verified live 2026-07). No mirrors, no scans.
4. Notation from a source is **converted** to `docs/NOTATION.md` conventions
   at the boundary — quote results in our notation with a conversion remark
   when signs/orientations differ.
