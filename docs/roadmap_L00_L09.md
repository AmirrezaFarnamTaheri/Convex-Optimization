# Roadmap for Auditing and Improving Lectures 00–09 (Convex Optimization Course)

## Overview

The task covers ten lecture files in the `Convex‑Optimization` repository (`topics/00-linear-algebra-basics/index.html` through `topics/09-duality/index.html`). Each file is a self‑contained module of a wider course, yet they share themes and build on each other. The goal is to audit every lecture thoroughly, verify mathematical accuracy, eliminate redundancies, ensure numbering consistency and improve the explanatory narrative. The final deliverable should preserve existing functionality (widgets, interactive exercises), avoid regressions, and maintain compatibility with the site’s build system. Below is a comprehensive plan broken down by preparatory work, per‑lecture tasks, cross‑lecture integration, and final checks.

### Preparatory Work

1.  **Environment Setup**
    *   Clone or pull the `Convex-Optimization` repository and create a new working branch (e.g., `lecture-audit`). Install dependencies as specified in the project’s README (likely Node.js dependencies for the interactive components and Python packages for pre‑commit hooks).
    *   Build the site locally (e.g., `npm run build` or `make docs`) to get an initial baseline. Take notes of any warnings or broken links.
    *   Run the existing `pre-commit` hooks to see current linting standards. Fix any issues unrelated to lecture content (e.g., formatting) first.
2.  **Reference Material**
    *   Gather authoritative references (e.g., Boyd & Vandenberghe _Convex Optimization_, Rockafellar _Convex Analysis_, Strang _Linear Algebra_) for cross‑checking definitions and proofs. Keep them handy during auditing.
    *   For specific theorems (e.g., Carathéodory’s theorem, fundamental property of convex optimization), cross-check their statements with these sources. The lecture on convex sets already cites Carathéodory’s theorem correctly; use that as a baseline.
3.  **Document Current Structure**
    *   For each lecture, create an outline listing sections, subsections, theorems, proofs, examples and exercises. This outline makes it easier to identify missing concepts, misordered sections, or duplicated topics across lectures.
    *   Note file‑specific features (e.g., interactive widgets, solution toggles) to ensure they remain functional after edits.

## Per‑Lecture Audit and Improvement

For each lecture file `topics/XX.../index.html`, carry out the following steps systematically. Keep a log of identified issues, proposed changes, and implemented fixes. The order of lectures in the list matches their numbering; however, many tasks repeat across lectures.

### 00. Linear Algebra Basics

1.  **Content Audit**
    *   Read the lecture end‑to‑end. Identify definitions (vectors, matrices, subspaces, rank, nullspace), invariants (trace, determinant, eigenvalues), inner products and norms, orthogonality, PSD matrices, projections, least squares, and any exercises. Record the current numbering of sections, theorems and exercises.
    *   Check each explanation for mathematical accuracy. For instance, confirm that the properties of determinants, the statement about eigenvalues summing to the trace, and the proof of the spectral theorem match standard sources.
2.  **Completeness and Redundancy**
    *   Look for missing prerequisite explanations: e.g., does the lecture sufficiently define subspaces before using them in an example? If not, add a brief definition or forward reference.
    *   Remove repeated material (e.g., if the rank–nullity theorem is defined twice). Consolidate scattered explanations about PSD matrices into a single subsection.
3.  **Pedagogical Flow**
    *   Reorder sections so that basic notions precede advanced ones. A typical progression is: scalars and vectors → matrices → operations (addition, multiplication) → subspaces and dimension → eigenvalues/eigenvectors → PSD matrices → projections and least squares.
    *   **Action:** Move "Matrix Calculus Basics" (currently Sec 1.6) to later in the lecture (e.g., Section 5), as it relies on Trace and Inner Products.
    *   Where proofs appear abruptly, preface them with intuition or a motivating example. For example, before deriving the formula for orthogonal projection, remind the reader of the geometric meaning of projecting onto a subspace.
4.  **Writing Style**
    *   Rewrite verbose sentences into clear, concise prose. Avoid jargon and unnatural synonyms; use consistent notation (**bold** for vectors, capital letters for matrices, italic for scalars) throughout the lecture.
    *   Use lists or numbered steps for proofs to guide the reader through the logic.
5.  **Exercises**
    *   Ensure exercises progress logically: simple computational problems first, then conceptual questions, followed by proofs. Merge similar exercises if they test the same concept.
    *   **Action:** Reorder exercises to align with the new content flow (e.g., P0.5 requires Matrix Calculus, so it should come after that section).
    *   Each exercise should clearly state the problem; solutions should be detailed and reference relevant sections. If an exercise solution references an unproven claim, insert that claim into the main text or adjust the problem.
6.  **Numbering and Cross‑References**
    *   Fix section numbering if the current HTML has inconsistent or missing numbers. Use hierarchical numbering (e.g., 1.1, 1.2, etc.).
    *   Check that hyperlinks to other lectures or definitions point to valid anchors.
7.  **Verification**
    *   After edits, build the site locally and verify that all LaTeX expressions render, interactive widgets load, and exercises toggle correctly.

### 01. Linear Algebra Advanced

1.  **Coverage Audit**
    *   Topics include basis change, linear maps, eigenvalues and Rayleigh quotient, induced norms, QR decomposition, SVD, pseudoinverse, condition number, and reviews. Confirm that each concept is defined and derived. Cross-check definitions with references.
    *   Pay particular attention to subtle topics like the induced operator norm and condition number. Provide explicit formulas and examples to illustrate their computation.
2.  **Enhance Intuition**
    *   For SVD and pseudoinverse, include geometric interpretations (e.g., SVD as rotation–scaling–rotation). Provide simple numerical examples demonstrating how the pseudoinverse solves least squares problems.
    *   For the Rayleigh quotient, explain its relationship to eigenvalues and show how it bounds the quadratic form; cite that this is covered in the lecture summary.
3.  **Refactor Redundancies**
    *   Remove repeated definitions that already appear in Lecture 00 (e.g., eigenvalue basics) and instead refer back. Use forward references for concepts that will be explored in Lectures 05 and 06 (e.g., convex conjugates) rather than redefining them here.
4.  **Proofs and Derivations**
    *   Verify each derivation, such as the proof that every matrix has an SVD, and that the pseudoinverse satisfies the Moore–Penrose conditions. Fill in missing steps or supply intuitive explanations.
    *   Where the lecture states results without proof (e.g., the Eckart–Young theorem), either provide a proof or supply an external reference.
5.  **Exercises**
    *   Re‑order exercises to match the lecture flow. For example, practice problems on induced norms should follow the definition of norms. Add new exercises where necessary (e.g., computing the SVD of a 2×2 matrix by hand).
    *   **Action:** Fix the exercise numbering gap (jumps from P1.3 to P1.6).

### 02. Introduction to Convex Optimization

1.  **Content and Flow**
    *   The lecture defines convex optimization problems, proves the fundamental theorem that local minima are global, classifies standard problem families (LP, QP, SOCP, SDP), introduces the loss+regularizer modeling paradigm and DCP rules, and provides comprehensive examples and exercises. Verify the mathematical definitions and theorems. For example, check that the three conditions for convexity (convex objective, convex inequality constraints, affine equality constraints) are correct and clearly stated.
    *   Ensure the historical perspective and complexity discussions are accurate (e.g., interior‑point methods’ development). Update dated statements if necessary.
2.  **Pedagogical Improvements**
    *   Replace general statements with specific examples. For instance, when discussing NP‑hardness of non‑convex problems, cite a concrete NP‑hard problem (e.g., integer programming) and briefly outline why it is hard.
    *   In the loss+regularizer section, include a comparative table of common loss functions and regularizers, as the current file does (least squares, logistic loss, hinge loss, etc.). Ensure each entry mentions its convexity and typical use cases (already present in the lecture but confirm accuracy).
3.  **Clarify Modeling Tricks**
    *   In the standard form transformation section, step through each conversion slowly: e.g., show how introducing slack variables converts an  $\ell_1$  norm minimization into a linear program. Provide pseudo‑code for variable introductions.
    *   Use diagrams to illustrate the epigraph transformation or perspective functions where appropriate.
4.  **Exercises and Solutions**
    *   Audit each exercise to ensure it aligns with the preceding material. Provide complete solutions with reasoning. For proof‑based exercises (e.g., proving that  $\|Ax-b\|_2^2$  is convex), give a step‑by‑step derivation using the definition of convexity rather than only quoting the Hessian condition.
    *   **Action:** De-duplicate Exercise P2.9 (Voronoi Regions) if it appears identically in Lecture 03.

### 03. Convex Sets – Geometry

1.  **Content Review**
    *   Topics include affine sets, convex sets, convex hulls, sublevel sets, epigraphs, canonical convex sets (hyperplanes, halfspaces, balls, ellipsoids, polyhedra, PSD cone), operations preserving convexity (intersection, affine maps, Minkowski sum, perspective and linear fractional functions, Cartesian products), topological concepts (closure, interior, relative interior, boundary), separation theorems, and Carathéodory’s theorem. Verify all definitions and proofs. The lecture currently states Carathéodory’s theorem accurately; ensure the proof is complete and accessible.
    *   **Action:** Move **Separation Theorems** (Separating and Supporting Hyperplanes) from Lecture 04 to Lecture 03. Separation is a fundamental geometric property that belongs with "Geometry".
2.  **Structure and Coherence**
    *   Sequence the material logically: start with definitions and geometric intuition (affine → convex), then move to operations preserving convexity, then explore canonical sets, and finally discuss topological concepts and separation. This helps learners build a mental map.
    *   For each canonical set, include both algebraic and geometric definitions, as well as pictures. Explain the intuition behind why, for example, the PSD cone is convex.
3.  **Examples and Visualizations**
    *   Ensure that interactive widgets (e.g., convex combination visualizer) work correctly. Provide instructions on how to use them and what learners should observe.
    *   Where possible, add diagrams or 2‑D sketches to illustrate abstract concepts like the Minkowski sum or perspective map.
4.  **Exercises**
    *   Group exercises by topic (e.g., convex hulls, separation, topological notions). Provide detailed solutions with references back to the relevant definitions. Remove duplicates if any.
    *   **Action:** Import exercises P4.1, P4.7, and P4.8 (Separation-related) from Lecture 04.

### 04. Convex Sets – Cones

1.  **Focus on Cones**
    *   **Proposal:** Rename lecture to "Convex Sets: Cones and Generalized Inequalities".
    *   Audit definitions of cones (convex cones, pointed cones, proper cones), dual cones, polar cones, and examples such as the positive orthant, Lorentz cone, and PSD cone. Provide geometric interpretations and ensure definitions are correct.
    *   Present the correspondence between cones and generalized inequalities; prove properties of dual cones and self‑dual cones.
2.  **Operations and Constructions**
    *   Discuss cone operations (direct sum, Cartesian product) and how they interact with convexity. Include proofs or intuitive arguments.
    *   Introduce the concept of cone programming and connect to standard forms in Lectures 07–08.
    *   **Action:** Since Separation Theorems are moving to L03, expand this lecture with more content on **Cone Operations** (e.g., dual of a sum, dual of an intersection) to fill the gap.
3.  **Examples and Visual Aids**
    *   Include diagrams of the positive orthant, Lorentz cone, and a PSD cone to aid understanding. Use interactive widgets if available.
4.  **Exercises**
    *   Provide problems requiring computation of dual cones and identifying whether a given set is a cone or convex. Ensure solutions are detailed.
    *   **Action:** Transfer Separation exercises to L03. Add new exercises on cone calculus.

### 05. Convex Functions – Basics

1.  **Core Definitions**
    *   Define convex functions, epigraphs, and sublevel sets. Provide the first principles definition and simple examples (linear, quadratic, exponential). Emphasize the difference between convex and strictly convex functions.
    *   Prove Jensen’s inequality and show how it implies convexity of common functions.
2.  **Operations that Preserve Convexity**
    *   Cover pointwise maxima, sums, nonnegative scaling, composition rules, and perspective functions. Provide formal statements and proofs or intuitive explanations.
3.  **Examples**
    *   Provide both 1‑D and multivariate examples. Use plots or interactive widgets to illustrate convex vs. non‑convex functions. Discuss functions that are convex but not differentiable (e.g., absolute value).
4.  **Refactoring**
    *   **Action:** Move **Strong Convexity** and **Smoothness** sections to Lecture 06 ("Advanced").
5.  **Exercises**
    *   Design problems asking students to prove convexity of functions using the definition rather than Hessian tests. Provide complete solutions.
    *   **Action:** Move Exercises P5.7 (Strong Convexity) and P5.9, P5.10, P5.11 (Conjugates/Duals) to Lecture 06.

### 06. Convex Functions – Advanced

1.  **New Content: Subgradients**
    *   **Action:** Add a new section on **Subgradients and Subdifferentials**. This is currently missing but critical for Duality (L09).
2.  **Subdifferentials and Conjugates**
    *   Introduce subgradients, subdifferentials and the Fenchel conjugate. Provide definitions, examples (e.g., subgradients of  $\|x\|_1$  and indicator functions), and interpretation.
    *   Derive conjugate functions for common examples (quadratic, exponential, indicator of a ball). Show how conjugation relates to duality.
3.  **Smoothness and Strong Convexity**
    *   **Action:** Receive "Strong Convexity" and "Smoothness" content from Lecture 05.
    *   Define Lipschitz continuity, smoothness, and strong convexity. Show how these properties translate into algorithmic convergence rates. Include examples of functions that are strictly convex but not strongly convex (e.g.,  $x^4$ ) and explain why.
4.  **Fenchel Duality**
    *   Present Fenchel’s inequality and Fenchel duality theorem. Work through a complete example (e.g., computing the dual of the LASSO problem). Provide step‑by‑step derivations.
5.  **Exercises**
    *   Design problems involving subgradient computation, conjugates, and checking strong convexity. Include guided solutions.
    *   **Action:** Incorporate the exercises moved from L05. Add new exercises on Subgradients.

### 07. Convex Problems – Standard Forms

1.  **Standard Form Details**
    *   Revisit the definitions of LP, QP, SOCP and SDP from Lecture 02 and provide more depth. For each class, define the objective and constraints formally, discuss the feasible set (polyhedron, ellipsoid, cone, PSD cone), and mention typical algorithms. Ensure that the definitions agree with those given in the introduction (Lecture 02).
2.  **Modeling Examples**
    *   Expand on the examples in Lecture 02 by providing detailed derivations. E.g., fully derive how a portfolio optimization problem fits into a QP, including variable definitions and matrices. For SOCP and SDP, provide at least one non‑trivial example (robust least squares, beamforming) with step‑by‑step reformulation.
3.  **Connections to Geometry**
    *   Relate each standard form to geometric structures from Lectures 03 and 04 (polyhedra, second‑order cones, PSD cones). This helps unify the narrative and fosters understanding of why certain constraints are allowed in a convex problem.
4.  **Exercises**
    *   Provide modeling exercises requiring identification of the correct standard form and reformulation into that form. Include solutions and highlight common pitfalls (e.g., the need for PSD matrices in QPs).

### 08. Convex Problems – Conic Forms

1.  **Conic Programming**
    *   Introduce the general conic form: minimize a linear function subject to the variable lying in an affine set intersected with a convex cone. Explain how LP, QP, SOCP and SDP are special cases of conic programs.
    *   Present dual cone and conic duality. Derive the dual of a general conic problem step by step.
2.  **New Content: Exponential Cone**
    *   **Action:** Add a section on **Exponential Cone Programming**. Define the exponential cone $K_{exp}$ and give examples (Entropy maximization, Geometric Programming in conic form).
3.  **Examples and Transformations**
    *   Provide examples of conic reformulations beyond the standard forms. Show how to express exponential and power functions using conic constraints.
    *   Walk through the derivation of a primal–dual pair for an SDP to illustrate the dual cone concept.
4.  **Exercises**
    *   Create exercises on deriving the dual of a given conic program and identifying the appropriate cone. Provide complete solutions with hints where necessary.
    *   **Action:** Add exercises involving the Exponential Cone.

### 09. Duality

1.  **Lagrangian and Dual Functions**
    *   Define the Lagrangian for a general convex optimization problem and the dual function. Derive the dual problem by maximizing the dual function over dual variables.
    *   Include a step‑by‑step derivation for an example (e.g., equality‑constrained QP). Clarify the roles of inequality multipliers and sign conventions.
2.  **Strong Duality and KKT Conditions**
    *   State conditions (Slater’s condition) under which strong duality holds. Provide proofs or intuitive arguments. Derive Karush–Kuhn–Tucker (KKT) conditions and relate them to optimality.
    *   Connect back to the fundamental theorem of convex optimization from Lecture 02.
3.  **Applications**
    *   Discuss sensitivity analysis (how dual variables measure constraint tightness) and complementary slackness. Provide examples such as deriving the dual of a linear program and interpreting shadow prices.
4.  **Exercises**
    *   Offer problems deriving duals of small problems (LP, QP, SOCP). Include checks for strong duality. Provide full solutions.

## Cross‑Lecture Integration and Consistency

1.  **Consistent Notation and Terminology**
    *   Create a style guide summarizing notation for scalars, vectors, matrices, cones, and functions.
    *   **Strict Rule:** Vectors must be in **boldface lowercase** ($\mathbf{x}$), not italic ($x$). Matrices in Capital ($A$). Sets in calligraphic ($\mathcal{C}$) or blackboard bold ($\mathbb{R}$).
    *   Standardize terminology (e.g., always use “positive semidefinite” rather than mixing “PSD” and “semi‑definite”).
2.  **Inter‑Lecture References**
    *   Update forward and backward connections in each lecture’s summary. For instance, Lecture 02 should link to Lecture 03 for the proof that feasible sets are convex, as it currently does. Ensure these links remain valid after renumbering.
    *   Use a consistent scheme for referring to definitions and theorems across lectures (e.g., “Definition 3.1 (Convex Set)” rather than generic phrases).
3.  **Remove Duplicates, Maintain Necessary Background**
    *   If a concept is introduced in Lecture 00, do not redefine it in Lecture 01; instead, link back. Conversely, ensure that later lectures do not assume knowledge of concepts that were not introduced previously.
    *   Consolidate overlapping exercises. For example, if both Lectures 02 and 03 have exercises on convex hulls, merge or cross‑reference them to avoid repetition.
4.  **Narrative Flow Across the Course**
    *   Revisit the course roadmap section (Lecture 02) and ensure it accurately reflects the improved content. Align the narrative so that the geometry of convex sets (Lectures 03–04) naturally leads into convex functions (Lectures 05–06), which then feeds into standard and conic problem forms (Lectures 07–08), culminating in duality (Lecture 09).
    *   Add summary sections at the end of each lecture summarizing the main takeaways and hinting at the next lecture.
