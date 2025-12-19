# Lecture Structure Audit

Generated from: `.`

## [00-linear-algebra-basics] 00. Linear Algebra Basics
*File: `topics/00-linear-algebra-basics/index.html`*

### Sections
- **Learning Objectives**
- **1. Mathematical Atoms: Sets, Functions, and Combinations**
  - 1.1 The Geometric "Atoms" of Optimization
  - 1.2 Scalars, Vectors, and Matrices
  - 1.3 Preliminaries: Lines and Line Segments
  - 1.4 Functions and Preimages
  - 1.5 Combinations and Hulls
- **2. Subspaces and the Four Fundamental Spaces**
  - Rank and Rank–Nullity Theorem
  - Interactive Visualizer: Rank & Nullspace
- **3. Algebraic Invariants: Determinant, Trace, and Eigenvalues**
  - 3.1 The "Big Three" Invariants
  - 3.2 The "Isotropic Scaling" Lemma
  - 3.3 Algebraic Properties
  - 3.4 Similarity and Basis Independence
  - 3.5 Spectral Shift
- **4. Inner Products, Norms, and Angles**
  - Inner Products
  - Norms and Convexity
  - Interactive Visualizer: The Geometry of Norms
  - The Euclidean Geometry ($\ell_2$)
  - Dual Norms and Polar Sets
  - Spectral Norm and Convexity
  - Matrix Inner Product and Frobenius Norm
- **5. Orthogonality and Orthonormal Bases**
  - Orthonormal Sets
  - Angle Preservation and Orthogonal Matrices
  - The Gram-Schmidt Process
  - The QR Decomposition
  - Interactive Explorer: Orthogonality & Projections
- **6. Positive Semidefinite Matrices**
  - 6.1 The Space of Symmetric Matrices ($\mathbb{S}^n$)
  - 6.2 Positive Semidefinite (PSD) Matrices
  - 6.3 Geometry of PSD Matrices: Ellipsoids
  - 6.4 The Rayleigh Quotient and Eigenvalues
  - 6.5 The Schur Complement Lemma
  - Interactive Explorer: Matrix Geometry & Definiteness
  - Interactive: Hessian Landscape Visualizer
  - 6.6 The Loewner Order
- **7. Projections onto Subspaces and Affine Sets**
  - 7.1 Projection onto a Line (1D Case)
  - 7.2 Orthogonal Projection onto a General Subspace
  - Projection via a Basis
  - Projection onto $\mathcal{R}(A)$ using $A$
  - Projection onto an Affine Set
  - Example 1: Projection onto a Line
- **8. The Method of Least Squares**
  - The Problem: Overdetermined Systems
  - Geometric Interpretation: Projection
  - The Normal Equations
  - Interactive Visualizer: Least Squares Projection
  - Uniqueness of the Solution
  - Example 2: Solving Least Squares with Normal Equations
  - Example 3: Rank-Deficient Case
  - 8.4 Variants: Weighted and Constrained Least Squares
  - (a) Weighted Least Squares (WLS)
  - (b) Constrained to an Affine Set
- **9. Review & Cheat Sheet**
  - Definitions
  - Key Theorems
  - Standard Formulas
- **11. Exercises**
  - P0.1 — Linear Independence
  - P0.2 — The Rank-Nullity Theorem
  - P0.3 — Orthogonal Complements
  - P0.4 — Norm Equivalence
  - P0.5 — Frobenius Norm Submultiplicativity
  - P0.6 — Spectral Norm Properties
  - P0.7 — Isometries
  - P0.8 — Weighted Inner Product
  - P0.9 — Characterization of Projectors
  - P0.10 — Projection onto a Line
  - P0.11 — Projection onto a Hyperplane
  - P0.12 — Trace and Determinant
  - P0.13 — Matrix Calculus Practice
  - P0.14 — Testing Positive Semidefiniteness
  - P0.15 — Schur Complement Application
  - P0.16 — Loewner Order Transitivity
  - P0.17 — PSD Cone in 2D
  - P0.18 — Hessian of a Cubic
  - P0.19 — Least Squares from Scratch
  - P0.20 — General Quadratic Minimization
- **11. Readings & Resources**

### Key Elements
- **Theorems/Definitions**: 3
  - Lemma: Scalar Matrices
  - Theorem: Invariance under Similarity
  - Lemma: Conjugate of a Norm
- **Proofs**: 26
  - Proof: Preimage Laws
  - Proof: $\mathcal{R}(A) \perp \mathcal{N}(A^\top)$
  - Proof of the Rank-Nullity Theorem
  - Proof of the Isotropic Scaling Lemma
  - Proof
  - Proof: $\mathrm{tr}(AB) = \mathrm{tr}(BA)$
  - Proof: Dot Product is an Inner Product
  - Proof: Triangle Inequalities for $\ell_1$ and $\ell_\infty$
  - Proof: Unit Ball Convexity
  - Proof: Cauchy-Schwarz Inequality ($|x^\top y| \le \|x\|_2 \|y\|_2$)
  - Proof: Triangle Inequality for $\ell_2$
  - Theorem: The Dual Norm is a Norm
  - Proof: $\|X\|_2 = \sqrt{\lambda_{\max}(X^\top X)}$
  - Derivation: Trace and Frobenius Norm
  - Proof via Column/Row Factorization
  - Proof of Orthogonality
  - Proof: Equivalence of Definitions
  - 1. Block Matrix Setup and Dimensions
  - Line-by-Line Verification of Block Multiplication
  - Detailed Derivation: From Rank-1 to Scalar
  - Key Properties of the Loewner Order
  - Derivation via Lagrange Multipliers
  - Geometric Interpretation and Derivation
  - Example 1: Projection onto a Line
  - Example 2: Solving Least Squares with Normal Equations
  - Example 3: Rank-Deficient Case
- **Examples**: 4
  - Geometric Example: $\mathbb{R}^3$
  - Worked Example: Trace and Determinant Caveats
  - Numerical Example (Sanity Check)
  - Example: Determinant of Symmetric Block Matrix
- **Interactive Widgets**: 6
  - Interactive Visualizer: Rank & Nullspace
  - Interactive Visualizer: The Geometry of Norms
  - Interactive Explorer: Orthogonality & Projections
  - Interactive Explorer: Matrix Geometry & Definiteness
  - Interactive: Hessian Landscape Visualizer
  - Interactive Visualizer: Least Squares Projection

### Broken Links Check
- All local links appear valid.

---

## [01-linear-algebra-advanced] 01. Linear Algebra Advanced
*File: `topics/01-linear-algebra-advanced/index.html`*

### Sections
- **Learning Objectives**
- **1. Bases, Coordinates, and Change of Basis**
  - 0. The Core Strategy: Change of Coordinates
  - 1. Span and Independence
  - 2. Basis and Dimension
  - 3. Coordinates: The Dictionary
  - 4. Change of Basis: The Deep Dive
  - 5. Orthonormal Bases
- **2. Linear Maps, Image/Kernel, and Rank-Nullity**
  - 1. The Geometry of Linear Maps
  - 2. The "Conservation of Dimension"
  - 3. Anatomy of $Ax=b$ (Geometric View)
- **3. Eigenvalues and the Rayleigh Quotient**
  - 3.1 Eigenvalues and Eigenvectors
  - 3.2 Spectral Theorem for Symmetric Matrices
  - 3.3 The Rayleigh Quotient
- **4. Induced Matrix Norms**
  - 4.1 The $\ell_1$ Operator Norm (Max Column Sum)
  - 4.2 The $\ell_\infty$ Operator Norm (Max Row Sum)
  - 4.3 The $\ell_2$ Operator Norm (Spectral Norm)
  - 4.4 Convexity of Induced Norms (Deep Dive)
- **5. The QR Decomposition**
  - 5.1 Motivation: Numerical Stability
  - 5.2 Definition and Existence
  - 5.3 Solving Least Squares with QR
- **6. The Singular Value Decomposition (SVD)**
  - 6.1 Geometric Intuition
  - 6.2 Theorem: Existence of SVD
  - 6.3 SVD vs. Eigendecomposition (Conceptual Contrast)
  - 6.4 Matrix Norms via SVD
  - 6.5 Low-Rank Approximation (Eckart-Young-Mirsky)
  - Interactive Demo: SVD for Image Compression
- **7. The Pseudoinverse and Condition Number**
  - 7.1 The Moore-Penrose Pseudoinverse ($A^+$)
  - 7.2 Condition Number
  - Interactive: Condition Number & Stability
- **8. Review & Cheat Sheet**
  - Key Identities
- **9. Exercises**
  - P1.1 — Dual of $\ell_p$ Norm
  - P1.2 — Frobenius Cauchy–Schwarz
  - P1.3 — SVD Computation
  - P1.4 — Normal Equations vs. QR
  - P1.5 — Pseudoinverse Projectors
  - P1.4 — Projector Formula
  - P1.5 — Hyperplane Projection
  - P1.6 — Condition Number Calculation
  - P1.7 — Pseudoinverse of Rank-1 Matrix
  - P1.8 — Operator Norm Properties
  - P1.9 — Orthogonal Invariance
  - P1.10 — The Orthogonal Group
- **10. Readings & Resources**

### Key Elements
- **Theorems/Definitions**: 4
  - Variational Characterization of Eigenvalues
  - Theorem: QR Factorization
  - Theorem: Eckart-Young-Mirsky
- **Proofs**: 8
  - Steinitz Exchange Lemma
  - Derivation
  - Proof: Convexity via Dual Norms
  - Construction via Gram-Schmidt
  - Constructive Proof via Spectral Theorem (Detailed)
  - Sketch of Proof (Spectral Norm)
  - Proof: Uniqueness of the Pseudoinverse
  - Proof: $x_{LS} = A^+b$ minimizes norm
- **Examples**: 2
  - A Tiny 2D Concrete Picture
  - Numerical Example: SVD in 2D
- **Interactive Widgets**: 2
  - Interactive Demo: SVD for Image Compression
  - Interactive: Condition Number & Stability

### Broken Links Check
- All local links appear valid.

---

## [02-introduction] 02. Introduction: What Makes a Problem Convex?
*File: `topics/02-introduction/index.html`*

### Sections
- **Learning Objectives**
- **1. What is a Convex Optimization Problem?**
  - 1.1 A Historical Perspective
  - 1.2 The Landscape of Optimization
  - 1.3 Formal Definition
  - 1.4 The Feasible Set
  - 1.5 The Meta-Skill: Converting Language
  - 1.6 Optimal Value and Optimal Points
  - Interactive Visualizer: Convex Hull Explorer
- **2. The Fundamental Theorem: Local = Global**
  - 2.1 Global Optimality
  - 2.2 Practical Implications
  - Interactive Laboratory: Convexity & Landscapes
  - Interactive Demo: Convergence Rate Comparison
- **3. Why Convexity Matters: Practical Implications**
  - 3.1 Computational Complexity
  - 3.2 Real-World Impact
  - 3.3 When Convexity is Lost
- **4. The Hierarchy of Convex Problem Families**
  - 4.1 Linear Programming (LP)
  - 4.2 Quadratic Programming (QP)
  - 4.3 Second-Order Cone Programming (SOCP)
  - 4.4 Semidefinite Programming (SDP)
  - 4.5 Summary: The Complexity Hierarchy
  - Interactive Tool: Problem Classification Flowchart
- **5. The Loss + Regularizer Modeling Paradigm**
  - 5.1 The Fundamental Template
  - 5.2 Common Loss Functions
  - 5.3 Common Regularizers
  - 5.4 Why LASSO Promotes Sparsity
- **6. Standard Form Transformations and Rewrites**
  - 6.1 Absolute Value Elimination
  - 6.2 Infinity Norm Transformations
  - 6.3 Euclidean Norm (SOCP Form)
  - 6.4 Maximum Function (Epigraph Form)
  - 6.5 Quadratic-Over-Linear (Perspective Form)
  - 6.6 Quick Reference Table
- **7. Disciplined Convex Programming (DCP)**
  - 7.1 The DCP Philosophy
  - 7.2 DCP Rules
- **8. Verifying Convexity: A Practical Checklist**
  - 8.1 Pre-Solver Sanity Checks
  - 8.2 Common Pitfalls
- **9. The Convex Optimization Workflow**
  - 9.1 The Five-Step Process
- **10. Course Roadmap: The Journey Ahead**
- **11. Review & Cheat Sheet**
  - Convex vs. Non-Convex: The Litmus Test
  - Standard Problem Forms
  - Common Reformulation Tricks
- **12. Exercises**
  - P2.1 — Classify as Convex / Not Convex
  - P2.2 — Real-World Modeling: Warehouse Location
  - P2.3 — Reformulation: $\ell_1$ Regression as LP
  - P2.4 — Prove: Feasible Set is Convex
  - P2.5 — Proving Uniqueness
  - P2.6 — Modeling: Maximum Likelihood Estimation
  - P2.7 — Proving Convexity from First Principles
  - P2.8 — Strict vs. Strong Convexity
- **13. Readings & Resources**

### Key Elements
- **Theorems/Definitions**: 1
  - Theorem (Fundamental Property of Convex Optimization)
- **Proofs**: 5
  - Proof of Global Optimality (Narrative Walkthrough)
  - Analytical Reason: Subgradients at Zero
  - Derivation of Robust Least Squares SOCP
  - Derivation: Equivalence
  - Step-by-Step Reformulation
- **Examples**: 17
  - 🚫 Counter-Example: The Circle Boundary
  - Example: Large-Scale Machine Learning
  - Example 1: Resource Allocation (Production Planning)
  - Example 2: Network Flow
  - Example 1: Markowitz Portfolio Optimization
  - Example 2: Least Squares with Constraints
  - Example 1: Robust Least Squares
  - Example 2: Antenna Array Weight Design
  - Example: Minimum Volume Enclosing Ellipsoid (Löwner-John)
  - Example: LASSO Regression
  - Example: $\ell_1$-Norm Minimization
  - Example: Chebyshev Approximation
  - Example: Robust Least Squares (Walkthrough)
  - Example: Minimax Linear Program
  - Example: Linear-Fractional Programming
  - Pitfall 1: Nonconvex Equality Constraints
  - Pitfall 2: Maximizing a Convex Function
- **Exercises**: 8
  - P2.1 — Classify as Convex / Not Convex
  - P2.2 — Real-World Modeling: Warehouse Location
  - P2.3 — Reformulation: $\ell_1$ Regression as LP
  - P2.4 — Prove: Feasible Set is Convex
  - P2.5 — Proving Uniqueness
  - P2.6 — Modeling: Maximum Likelihood Estimation
  - P2.7 — Proving Convexity from First Principles
  - P2.8 — Strict vs. Strong Convexity
- **Interactive Widgets**: 4
  - Interactive Visualizer: Convex Hull Explorer
  - Interactive Laboratory: Convexity & Landscapes
  - Interactive Demo: Convergence Rate Comparison
  - Interactive Tool: Problem Classification Flowchart

### Broken Links Check
- All local links appear valid.

---

## [03-convex-sets-geometry] 03. Convex Sets: Geometry
*File: `topics/03-convex-sets-geometry/index.html`*

### Sections
- **Learning Objectives**
- **1. Affine and Convex Sets: Definitions and Basic Properties**
  - 1.1 Affine Combinations and Affine Sets
  - 1.2 Convex Combinations and Convex Sets
  - 1.3 Convex Hull
  - 1.4 Sets Defined by Functions
  - 1.5 Key Properties
  - Interactive Tool: Convex Set Checker
- **2. Canonical Convex Sets: Building Blocks**
  - 2.1 Hyperplanes and Halfspaces
  - 2.2 Norm Balls and Ellipsoids
  - Interactive Explorer: Ellipsoid Geometry
  - 2.3 Polyhedra
  - Polytope vs. Polyhedron: H-Rep and V-Rep
  - Interactive Visualizer: Polyhedron Builder
  - 2.4 The Positive Semidefinite (PSD) Cone
- **3. Operations that Preserve Convexity**
  - 3.1 Intersection
  - 3.2 Affine Functions Preserve Convexity
  - 3.3 Perspective and Linear-Fractional Functions
  - 3.4 Minkowski Sum
  - 3.5 Cartesian Product
  - Interactive Laboratory: Convex Geometry
- **4. Topological Toolkit: Closure, Interior, Relative Interior**
  - 4.1 Basic Topological Definitions
  - 4.2 Key Properties for Convex Sets
  - 4.3 Why Relative Interior Matters
- **5. Separating and Supporting Hyperplane Theorems**
  - 5.1 The Separating Hyperplane Theorem
  - 5.2 The Supporting Hyperplane Theorem
  - 5.3 The Support Function
  - 5.4 Theorems of the Alternative (Farkas' Lemma)
  - Interactive Explorer: Separating Hyperplanes
- **6. Review & Cheat Sheet**
  - Key Definitions
  - Operations Preserving Convexity
- **7. Exercises**
  - P3.1 — Voronoi Regions
  - P3.2 — Midpoint Convexity
  - P3.3 — Convex Hull of a Union
  - P3.4 — Linear-Fractional Functions
  - P3.5 — Convexity of Quadratic Sublevel Set
  - P3.6 — Relative Interior of the Simplex
  - P3.7 — Convex Hull Characterizations
  - P3.8 — Minkowski Sum of Sets
  - P3.9 — Convexity of Thickened Sets
  - P3.10 — Closure of a Convex Set
  - P3.11 — Product of Convex Sets
  - P3.12 — Finite Convex Combinations (Jensen's for Sets)
  - P3.13 — Convexity via Line Intersections
  - P3.14 — Hyperbolic Sets
  - P3.15 — Set Classification Challenge
  - P3.16 — Partial Sum of Convex Sets
  - P3.17 — Perspective of Polyhedral Sets
  - P3.18 — Invertible Linear-Fractional Functions
  - P3.19 — Projection onto a Convex Set
  - P3.20 — Preimages under Linear-Fractional Maps
  - P3.21 — Projection onto the Probability Simplex
  - P3.22 — Separation by Projection
  - P3.23 — Support Function Determines Set
  - P3.24 — Converse Supporting Hyperplane Theorem
- **7. Recap & What's Next**

### Key Elements
- **Theorems/Definitions**: 19
  - Definition (Affine Set)
  - Theorem: Affine Set $\iff$ Translated Subspace
  - Definition (Convex Set)
  - Theorem (Carathéodory's Theorem)
  - Theorem
  - Fundamental Bridge Theorem
  - Geometric Interpretation
  - Proof: Norm Balls are Convex
  - Minkowski-Weyl Theorem
  - Theorem (Intersection Preserves Convexity)
  - Theorem (Affine Image and Preimage)
  - Theorem
  - Theorem
  - Convexity of Minkowski Difference (when nonempty)
  - Facts About Convex Sets
  - Theorem (Separating Hyperplane)
  - Theorem (Supporting Hyperplane)
  - Definition (Support Function)
  - Theorem (Farkas' Lemma)
- **Proofs**: 13
  - Proof: The Geometric Shift
  - Proof of Carathéodory's Theorem
  - Proof: Hyperplanes and Halfspaces are Convex
  - Convexity of Polyhedra
  - Proof: The PSD Cone is Convex
  - Proof
  - Proof
  - Proof: Perspective Preserves Convexity (Step-by-Step)
  - Proof
  - Proof
  - Proof (Constructive via Projection)
  - Proof (Limit Argument)
  - Proof via Separation
- **Examples**: 9
  - Examples of Affine Sets
  - Example: $\mathbb{R}^2$
  - Spectrahedra: The Shape of SDP
  - Advanced Example: Trigonometric Polynomials
  - Application: Ellipsoids are Convex
  - Visualizing Projective Geometry
  - Example 1: Line Segment in $\mathbb{R}^2$
  - Example 1b: A Flat Disk in 3D (The "Frisbee" Intuition)
  - Example 2: Standard Simplex
- **Exercises**: 24
  - P3.1 — Voronoi Regions
  - P3.2 — Midpoint Convexity
  - P3.3 — Convex Hull of a Union
  - P3.4 — Linear-Fractional Functions
  - P3.5 — Convexity of Quadratic Sublevel Set
  - P3.6 — Relative Interior of the Simplex
  - P3.7 — Convex Hull Characterizations
  - P3.8 — Minkowski Sum of Sets
  - P3.9 — Convexity of Thickened Sets
  - P3.10 — Closure of a Convex Set
  - P3.11 — Product of Convex Sets
  - P3.12 — Finite Convex Combinations (Jensen's for Sets)
  - P3.13 — Convexity via Line Intersections
  - P3.14 — Hyperbolic Sets
  - P3.15 — Set Classification Challenge
  - P3.16 — Partial Sum of Convex Sets
  - P3.17 — Perspective of Polyhedral Sets
  - P3.18 — Invertible Linear-Fractional Functions
  - P3.19 — Projection onto a Convex Set
  - P3.20 — Preimages under Linear-Fractional Maps
  - P3.21 — Projection onto the Probability Simplex
  - P3.22 — Separation by Projection
  - P3.23 — Support Function Determines Set
  - P3.24 — Converse Supporting Hyperplane Theorem
- **Interactive Widgets**: 5
  - Interactive Tool: Convex Set Checker
  - Interactive Explorer: Ellipsoid Geometry
  - Interactive Visualizer: Polyhedron Builder
  - Interactive Laboratory: Convex Geometry
  - Interactive Explorer: Separating Hyperplanes

### Broken Links Check
- All local links appear valid.

---

## [04-convex-sets-cones] 04. Convex Sets: Cones and Generalized Inequalities
*File: `topics/04-convex-sets-cones/index.html`*

### Sections
- **Learning Objectives**
- **1. Separating and Supporting Hyperplane Theorems**
  - 1.1 The Separating Hyperplane Theorem
  - 1.2 The Supporting Hyperplane Theorem
  - 1.3 The Support Function
  - 1.4 Theorems of the Alternative (Farkas' Lemma)
  - Interactive Explorer: Separating Hyperplanes
- **2. Cones, Proper Cones, and Dual Cones**
  - 2.1 Cones and Convex Cones
  - 2.2 Proper Cones
  - 2.3 Generalized Inequalities
  - 2.4 The Dual Cone
  - 1.5 Calculus of Cones
- **2. Review & Cheat Sheet**
  - Separation Theorems
  - Cones and Duality
- **3. Exercises**
  - P4.1 — Dual of a Subspace
  - P4.2 — Self-Duality of Second-Order Cone
  - P4.3 — Dual Cone Identities
  - P4.4 — Generalized Inequality Properties
  - P4.5 — Norm Cone (Epigraph of Norm)
  - P4.6 — Cones in $\mathbb{R}^2$
  - P4.7 — Properties of Dual Cones
  - P4.8 — Dual Cone of Generated Cone
  - P4.9 — The Monotone Nonnegative Cone
  - P4.10 — The Lexicographic Cone
  - P4.11 — Dual of Intersection
  - P4.12 — Euclidean Distance Matrices (EDM)
  - P4.13 — SOCP Canonical Dual
  - P4.14 — Homogeneous Envelope and Directional Derivatives
- **5. Readings & Resources**
- **6. Recap & What's Next**

### Key Elements
- **Theorems/Definitions**: 7
  - Theorem (Separating Hyperplane)
  - Theorem (Supporting Hyperplane)
  - Definition (Support Function)
  - Theorem (Farkas' Lemma)
  - Deep Dive: Polyhedral Cones and Weyl-Minkowski
  - Theorem (Bipolar Theorem)
  - Important Dualities
- **Proofs**: 6
  - Proof (Constructive via Projection)
  - Proof (Limit Argument)
  - Proof via Separation
  - Proof Sketch
  - Proof: Self-Duality of the PSD Cone
  - Rigorous Proof that the SOC is self-dual ($\mathcal{Q}^* = \mathcal{Q}$)
- **Examples**: 1
  - Examples of Convex Cones
- **Exercises**: 14
  - P4.1 — Dual of a Subspace
  - P4.2 — Self-Duality of Second-Order Cone
  - P4.3 — Dual Cone Identities
  - P4.4 — Generalized Inequality Properties
  - P4.5 — Norm Cone (Epigraph of Norm)
  - P4.6 — Cones in $\mathbb{R}^2$
  - P4.7 — Properties of Dual Cones
  - P4.8 — Dual Cone of Generated Cone
  - P4.9 — The Monotone Nonnegative Cone
  - P4.10 — The Lexicographic Cone
  - P4.11 — Dual of Intersection
  - P4.12 — Euclidean Distance Matrices (EDM)
  - P4.13 — SOCP Canonical Dual
  - P4.14 — Homogeneous Envelope and Directional Derivatives
- **Interactive Widgets**: 1
  - Interactive Explorer: Separating Hyperplanes

### Broken Links Check
- All local links appear valid.

---

## [05-convex-functions-basics] 05. Convex Functions: Basics
*File: `topics/05-convex-functions-basics/index.html`*

### Sections
- **Learning Objectives**
- **1. Definition and Basic Properties**
  - 1.1 Convex Functions: The Core Definition
  - 1.2 Jensen's Inequality: The General Form
  - 1.3 Applications of Jensen's Inequality
  - 1.4 Integral Characterization of Convexity
  - 1.5 Strict and Strong Convexity
  - 1.6 Concave Functions
  - 1.7 Restriction to a Line
  - Interactive Inspector: Understanding Convexity
- **2. Epigraph Characterization**
  - 2.1 The Epigraph
  - 2.2 Convexity via Epigraph
  - 2.3 Convex Hull of a Function
- **3. First-Order Conditions (Tangent Line Property)**
  - 3.1 The First-Order Characterization
  - 3.2 Monotonicity of the Gradient
  - 3.3 Consequences and Applications
- **4. Second-Order Conditions (Hessian Test)**
  - 4.1 The Second-Order Characterization
  - 4.2 Strict and Strong Convexity via Hessian
  - 4.3 Practical Verification
  - Interactive Heatmap: Hessian Eigenvalue Analyzer
- **5. Operations Preserving Convexity**
  - 5.1 Nonnegative Weighted Sum
  - 5.2 Pointwise Maximum of Convex Functions
  - 5.3 Pointwise Supremum over an Index Set
  - 5.4 Partial Minimization
  - 5.5 Composition Rules: The Algebra of Convexity
  - 5.6 Perspective Function
  - 5.7 Power Functions and Homogeneity
  - 5.8 The Minkowski Functional (3.34)
  - 5.9 Pitfalls: What Doesn't Preserve Convexity?
  - 5.10 Summary: Mental Checklist
  - Interactive Builder: Operations Preserving Convexity
- **6. Review & Cheat Sheet**
  - Definitions
  - Conditions for Differentiable $f$
  - Operations Preserving Convexity
- **7. Exercises**
  - P5.1 — Convexity of Basic Functions
  - P5.2 — Arithmetic-Geometric Mean Inequality
  - P5.3 — Log-Sum-Exp
  - P5.4 — Quadratic-over-Linear
  - P5.5 — Distance to a Set
  - P5.6 — Entropy
  - P5.7 — Convexity of Log-Sum-Exp via Cauchy-Schwarz
  - P5.8 — Sensitivity Analysis using Subgradients
  - P5.9 — Advanced Composition Rules (3.22)
  - P5.10 — Perspective Examples (3.23)
- **8. Recap & What's Next**

### Key Elements
- **Theorems/Definitions**: 14
  - Theorem
  - Theorem (Restriction to a Line)
  - Theorem (Epigraph Characterization)
  - Theorem (First-Order Condition for Convexity)
  - Theorem (Second-Order Condition for Convexity)
  - Theorem
  - Claim
  - Theorem
  - Theorem
  - 1. Affine Composition
  - 2. Scalar Composition Rule ($f=h\circ g$) in Depth
  - 3. Vector Composition Rule ($f=h\circ g$) in Depth
  - Definition and Property
  - When is $M_C$ a Norm?
- **Proofs**: 31
  - Proof: Norms are Convex
  - Proof of Jensen's Inequality
  - Proof Breakdown
  - Proof
  - Proof
  - Proof: Largest Convex Underestimator
  - Example: Homogeneous Envelope (Exercise 3.31)
  - Proof: Convexity $\iff$ First-Order Condition
  - Proof: Convexity $\iff$ Monotone Gradient
  - Proof: Convexity $\iff$ PSD Hessian
  - Example 1: Quadratic Function $f(x) = \|Ax - b\|_2^2$
  - Example 2: Log-Sum-Exp (Full Derivation)
  - Deep Dive: Matrix Cauchy-Schwarz & Hilbert-Schmidt Inequality
  - Deep Dive: Hessian of $\ell_p$ Quasi-Norm ($0 < p \le 1$)
  - Deep Dive: Hessian of Geometric Mean
  - Deep Dive: Hessian of $\ell_p$ Quasi-Norm ($0 < p \le 1$)
  - Deep Dive: Hessian of Geometric Mean
  - Proof
  - Algebraic Proof
  - Geometric Proof (Epigraph)
  - Detailed Proof: Representation as Max of Linear Functionals
  - Proof
  - Algebraic Proof
  - Alternative Proof: Distance to Convex Set (Epsilon-Delta)
  - Check via Quadratic Forms
  - Proof: Scalar Composition Rules
  - Proof (Convex + Non-decreasing Case)
  - Direct Proof of Convexity
  - Alternative Proof: Epigraph Mapping
  - Theorem: Log-Concavity + Homogeneity $\implies$ Concavity
  - Properties: Homogeneity and Convexity
- **Examples**: 24
  - 1. Arithmetic-Geometric Mean (AM-GM)
  - 2. From AM-GM to Hölder's Inequality
  - Application 1: Proving a Function is Convex
  - Application 2: Optimality Condition
  - Example 3: Trace of Inverse
  - Example 4: Geometric Mean of Eigenvalues
  - Example 1: Piecewise-Linear (Max of Affine Functions)
  - Example 2: The $\ell_p$-type Mean ($p < 1$)
  - Example 3: Sum of the $r$ Largest Components (Ky Fan Norm)
  - 1. Support Function
  - 2. Distance to Farthest Point
  - 3. Maximum Eigenvalue
  - 4. Induced Matrix Norms
  - 1. Distance to a Convex Set
  - 2. Schur Complement via Quadratic Minimization
  - 3. Infimum over an Affine Constraint
  - Example: Log-Log-Sum-Exp
  - Example 1: Sum of Logs (Concave)
  - Example 2: Log-Sum-Exp of Convex Functions (Detailed Check)
  - Example 3: $p$-Means ($h(z) = (\sum z_i^p)^{1/p}$)
  - Example 4: Geometric Mean ($h(z) = (\prod z_i)^{1/k}$)
  - Example: Relative Entropy
  - Example: Power-over-Linear
  - Example: Quadratic-over-Linear
- **Exercises**: 10
  - P5.1 — Convexity of Basic Functions
  - P5.2 — Arithmetic-Geometric Mean Inequality
  - P5.3 — Log-Sum-Exp
  - P5.4 — Quadratic-over-Linear
  - P5.5 — Distance to a Set
  - P5.6 — Entropy
  - P5.7 — Convexity of Log-Sum-Exp via Cauchy-Schwarz
  - P5.8 — Sensitivity Analysis using Subgradients
  - P5.9 — Advanced Composition Rules (3.22)
  - P5.10 — Perspective Examples (3.23)
- **Interactive Widgets**: 3
  - Interactive Inspector: Understanding Convexity
  - Interactive Heatmap: Hessian Eigenvalue Analyzer
  - Interactive Builder: Operations Preserving Convexity

### Broken Links Check
- All local links appear valid.

---

## [06-convex-functions-advanced] 06. Convex Functions: Advanced Topics
*File: `topics/06-convex-functions-advanced/index.html`*

### Sections
- **Learning Objectives**
- **1. Subgradients and Subdifferentials**
  - 1.1 Definition
  - 1.2 Properties
  - 1.3 Calculus of Subgradients
- **2. The Convex Conjugate (Fenchel Conjugate)**
  - 1.1 Definition and Geometric Meaning
  - Supporting Hyperplane Viewpoint
  - 1.2 Why $f^*$ is Always Convex
  - 1.3 1D Examples in Detail
  - 1.4 Quadratic and Matrix Examples
  - 1.5 Algebra Rules for Conjugates
  - 1.6 Fenchel Inequality and Biconjugate
  - 1.7 Legendre Transform: Smooth Case
- **3. Strong Convexity and Smoothness**
  - 3.1 Strong Convexity
  - 3.2 Lipschitz Smoothness
  - 3.3 The Condition Number
- **4. Quasiconvex Functions**
  - 2.1 Definition: Sublevel Sets
  - 2.2 Simple 1D Examples
  - 2.3 Vector Examples
  - 2.4 Second-Order Condition
  - 2.5 Operations Preserving Quasiconvexity
  - 2.6 Worked Example: Classification Challenge
- **5. Log-Concave and Log-Convex Functions**
  - 3.1 Definitions
  - 3.2 Examples
  - 3.3 Integration Rules
  - 3.4 Probability Examples
- **6. Review & Cheat Sheet**
  - Conjugate Transformations
  - Key Concepts
- **7. Exercises**
  - P6.1 — Conjugate of Norm Squared
  - P6.2 — Quasi-Convexity of Ceiling
  - P6.3 — Softmax Analysis
  - P6.4 — Concavity of Geometric Mean
  - P6.5 — Geometric Mean Cone
  - P6.6 — Matrix Fractional Function
  - P6.7 — Fenchel's Inequality & Biconjugate
  - P6.8 — Quasiconvexity of Distance Ratio
  - P6.9 — Log-Concavity of Probability Measures
- **6. Recap & What's Next**

### Key Elements
- **Theorems/Definitions**: 6
  - Definition (Subgradient)
  - Deep Dive: Biconjugate and Convex Hulls
  - Gradient Condition (3.47)
  - Second-Order Characterization
  - (a) Integrals of Log-Convex Functions
  - (b) Integrals of Log-Concave Functions (Prékopa-Leindler)
- **Proofs**: 2
  - Proof
  - Detailed Proof
- **Examples**: 28
  - Example: Absolute Value
  - (a) Affine function $f(x) = ax + b$
  - (b) Negative Log: $f(x) = -\log x$ on $(0,\infty)$
  - (c) Exponential: $f(x) = e^x$ on $\mathbb{R}$
  - (d) Reciprocal: $f(x) = 1/x$ on $(0,\infty)$
  - (a) Quadratic: $f(x) = \frac{1}{2} x^\top Q x$ with $Q \succ 0$
  - (b) Log-Determinant: $f(X) = -\log \det X$ on $\mathbb{S}^n_{++}$
  - (c) Indicator $\leftrightarrow$ Support Function
  - (d) Norm $\leftrightarrow$ Indicator of Dual Ball
  - (e) Negative Entropy & Log-Sum-Exp
  - (f) Geometric Mean via Conjugates
  - (a) Logarithm: $f(x) = \log x$
  - (b) Ceiling: $f(x) = \lceil x \rceil$
  - 1. Length of a Vector
  - 2. Bilinear: $f(x_1, x_2) = x_1 x_2$ on $\mathbb{R}^2_{++}$
  - 3. Linear-Fractional: $f(x) = \frac{a^\top x + b}{c^\top x + d}$
  - 4. Distance Ratio (Rigorous Analysis)
  - 7. Internal Rate of Return (IRR)
  - (a) $f(x) = e^x - 1$ on $\mathbb{R}$
  - (b) $f(x_1, x_2) = x_1 x_2$ on $\mathbb{R}^2_{++}$
  - (c) $f(x_1, x_2) = 1/(x_1 x_2)$ on $\mathbb{R}^2_{++}$
  - (d) $f(x_1, x_2) = x_1 / x_2$ on $\mathbb{R}_{++}^2$
  - (e) $f(x_1, x_2) = x_1^2 / x_2$ on $\mathbb{R} \times \mathbb{R}_{++}$
  - (f) $f(x_1, x_2) = x_1^\alpha x_2^{1-\alpha}$ on $\mathbb{R}^2_{++}$ for $\alpha \in [0,1]$
  - 1. Uniform Distribution on Convex Set
  - 2. Wishart Distribution
  - (a) Hitting a Convex Set with Log-Concave Noise
  - (b) Cumulative Distribution Function (CDF)
- **Exercises**: 31
  - P6.1 — Conjugate of Norm Squared
  - P6.2 — Quasi-Convexity of Ceiling
  - P6.3 — Softmax Analysis
  - P6.4 — Concavity of Geometric Mean
  - P6.5 — Geometric Mean Cone
  - P6.6 — Matrix Fractional Function
  - P6.7 — Fenchel's Inequality & Biconjugate
  - P6.8 — Quasiconvexity of Distance Ratio
  - P6.9 — Log-Concavity of Probability Measures
  - P6.10 — Log-Concavity of Gaussian
  - P6.11 — Legendre Transform of Quadratic
  - P6.12 — Log-Concavity Examples (3.49)
  - P6.13 — Log-Convexity of the Gamma Function
  - P6.14 — Log-Sum-Exp Conjugate
  - P6.15 — Norm Conjugate
  - P6.16 — Convex Hull of a Function
  - P6.17 — Log-Concavity Characterization (Breakdown of 3.47)
  - P6.18 — Convexity of Maximum Eigenvalue (3.10)
  - P6.19 — Convexity of Induced Matrix Norms (3.11)
  - P6.20 — Vector Composition Rules (3.14)
  - P6.21 — Perspective of Affine Composition (3.20)
  - P6.22 — Convexity Drills (3.22)
  - P6.23 — Perspective Practice (3.23)
  - P6.24 — Shifting Log-Concavity (3.48)
  - P6.25 — Cardinality on $\mathbb{R}_+^n$ (3.35)
  - P6.26 — Rank on PSD Cone (3.36)
  - P6.27 — Homogenization (3.31)
  - P6.28 — Strong Convexity of Quadratic
  - P6.29 — Dual of a Strictly Convex Function
  - P6.30 — Dual via Conjugates
  - P6.31 — Derivation: Dual of QP

### Broken Links Check
- All local links appear valid.

---

## [07-convex-problems-standard] 07. Convex Optimization Problems: Standard Forms
*File: `topics/07-convex-problems-standard/index.html`*

### Sections
- **Learning Objectives**
- **1. The Standard Form of Convex Optimization**
  - 1.1 Definition
  - 1.2 The Feasible Set
  - 1.3 Optimal Value and Optimal Points
- **2. Linear Programs (LP)**
  - 2.1 Definition and Geometry
  - 2.2 Key Properties
  - 2.3 Standard LP Examples
  - 2.4 Piecewise-Linear Minimization
  - 2.5 Matrix Norm Approximation (LP)
  - 2.6 Minimum Fuel Optimal Control (LP)
  - 2.7 Hierarchy of Convex Problems
- **3. Quadratic Programs (QP)**
  - 3.1 Definition
  - 3.2 Geometry and Convexity
  - 3.3 Least-Squares as a QP
  - 3.4 Application: Mean-Variance Analysis
  - 3.5 Application: Distance Between Polyhedra
  - 3.6 Robust Least Squares and the Huber Penalty
  - 3.7 Quadratically Constrained Quadratic Programs (QCQP)
- **4. Linear-Fractional Programming**
  - 4.1 The Geometric Perspective
  - 4.2 Linear-Fractional Programs (LFP)
  - 4.3 Reformulation as an LP
  - 4.4 Recovering the Solution and the Case $z=0$
  - 4.5 Generalized Linear-Fractional Programming (GLFP)
  - 4.6 Convex-Concave Fractional Programming
- **5. Geometric Programming (GP)**
  - 5.1 Monomials and Posynomials
  - 5.2 Standard GP Form
  - 5.3 Convex Reformulation via Log-Transform
- **6. Summary: The Convex Optimization Pattern Library**
- **7. Matrix Viewpoint: The Algebra of QPs**
  - 7.1 Congruence and PSD Matrices
  - 7.2 Similarity and Eigenvalues
- **8. Problem Reformulation**
  - 8.1 Equivalent Problems
  - Interactive: Problem Reformulation Tool
- **9. Exercises**
  - P7.1 — Diet Problem (LP)
  - P7.2 — Transportation Problem (LP)
  - P7.3 — PSD Block Matrix (Matrix Viewpoint)
  - P7.4 — L1 Reformulation
  - P7.5 — LP Reformulation: Piecewise Linear Objective
  - P7.6 — The Log-Barrier Problem
  - P7.7 — LASSO Primal
  - P7.8 — Soft-Margin SVM Primal
  - P7.9 — Robust Least Squares (Huber Penalty) Formulation
  - P7.10 — Matrix Norm Approximation (4.14)
  - P7.11 — Minimum Fuel Optimal Control (4.16)
  - P7.12 — Convex-Concave Fractional Programming (4.7)
- **10. Readings & Resources**
- **11. Recap & What's Next**

### Key Elements
- **Theorems/Definitions**: 1
  - Deep Dive: Slack Variables and Standard Forms
- **Proofs**: 17
  - Theorem: Convexity of Feasible Set
  - Fundamental Property: Local = Global
  - Proof Sketch: Why Vertices?
  - Derivation of the Chebyshev LP
  - The Epigraph Trick: Reformulation as LP
  - Deep Dive: The "Lifting" Technique for Norms
  - LP Formulation Summary
  - LP Formulation
  - Algebraic Expansion
  - Mapping to Standard QP Form
  - Derivation
  - Derivation of Charnes-Cooper Transformation
  - Convex Reformulation (Single Shot)
  - Pattern 1: The Epigraph Trick
  - Pattern 2: Robustness via Dual Norms
  - Pattern 3: The Perspective Transform
  - Pattern 4: Geometric Programming
- **Examples**: 3
  - Example: Trust-Region QCQP
  - Case Study: Von Neumann Growth Model
  - Example: Box Volume Maximization
- **Exercises**: 12
  - P7.1 — Diet Problem (LP)
  - P7.2 — Transportation Problem (LP)
  - P7.3 — PSD Block Matrix (Matrix Viewpoint)
  - P7.4 — L1 Reformulation
  - P7.5 — LP Reformulation: Piecewise Linear Objective
  - P7.6 — The Log-Barrier Problem
  - P7.7 — LASSO Primal
  - P7.8 — Soft-Margin SVM Primal
  - P7.9 — Robust Least Squares (Huber Penalty) Formulation
  - P7.10 — Matrix Norm Approximation (4.14)
  - P7.11 — Minimum Fuel Optimal Control (4.16)
  - P7.12 — Convex-Concave Fractional Programming (4.7)
- **Interactive Widgets**: 1
  - Interactive: Problem Reformulation Tool

### Broken Links Check
- All local links appear valid.

---

## [08-convex-problems-conic] 08. Convex Optimization Problems: Conic Programming
*File: `topics/08-convex-problems-conic/index.html`*

### Sections
- **Learning Objectives**
- **1. Second-Order Cone Programs (SOCP)**
  - 1.1 Definition
  - 1.2 The Second-Order Cone (Lorentz Cone)
  - 1.3 Key Properties
  - 1.4 Standard SOCP Examples
- **2. Robust Linear Programming**
  - 2.1 Deterministic Robust LP
  - 2.2 Stochastic Robust LP (Chance Constraints)
- **3. Semidefinite Programs (SDP)**
  - 3.1 Definition
  - 3.2 The PSD Cone
  - 3.3 Key Properties
  - 3.4 Standard SDP Examples
  - Interactive: SDP Visualizer
  - 3.5 The Hierarchy: LP ⊆ QP ⊆ SOCP ⊆ SDP
- **4. Exponential Cone Programming**
  - 4.1 The Exponential Cone
  - 4.2 Applications
- **5. Quasiconvex Optimization**
  - 4.1 Quasiconvex Functions
  - 4.2 Quasiconvex Optimization Problems
  - 4.3 Solution via Bisection (Convex Feasibility)
- **5. Disciplined Convex Programming (DCP)**
  - 5.1 Motivation
  - 5.2 DCP Rules (a practical checklist)
  - 5.3 DCP in Practice: CVXPY
  - Interactive: Solver Selection Guide
- **6. Review & Cheat Sheet**
  - Meta-Patterns: Convexification Recipes
  - Problem Classes Reference
  - Hierarchy
- **7. Exercises**
  - P8.1 — Classify and Reformulate: Minimizing Maximum Absolute Deviation
  - P8.2 — QP Formulation: Constrained Least Squares
  - P8.3 — SOCP Reformulation: $\ell_2$ Regularized Least Squares
  - P8.4 — SDP Example: Largest Eigenvalue Minimization
  - P8.5 — Problem Classification: Portfolio Optimization with Risk Constraint
  - P8.6 — Equivalence: $\ell_1$ Minimization and LP
  - P8.7 — Quasiconvex Optimization: Bisection Algorithm
  - P8.8 — Minimum Enclosing Ellipsoid as SDP
  - P8.9 — Resource Allocation Formulation
  - P8.10 — Standard Form Transformation: Linear-Fractional Programming
  - P8.11 — Vector Optimization (Pareto Optimality)
  - P8.12 — Matrix Fractional Minimization
  - P8.13 — SOCP Canonical Form (Primal)
  - P8.14 — SDP Canonical Form (Primal)
  - P8.15 — Entropy Maximization via Exponential Cone
  - P8.16 — Dual of the Exponential Cone
- **10. Readings & Resources**
- **11. Recap & What's Next**

### Key Elements
- **Theorems/Definitions**: 2
  - Deep Dive: Value-at-Risk (VaR) vs. Conditional Value-at-Risk (CVaR)
- **Proofs**: 10
  - Convexity of the Second-Order Cone
  - Derivation of Robust Least Squares SOCP (Unstructured Uncertainty)
  - Derivation: Robust to SOCP
  - Derivation: Chance to SOCP
  - Derivation via Loewner Order
  - Derivation via Schur Complement
  - Proof: Embedding SOCP into SDP
  - Mapping Entropy to $K_{\exp}$
  - Recipe 1: Robustness $\to$ Norms $\to$ SOCP
  - Recipe 2: Eigenvalues $\to$ LMIs $\to$ SDP
- **Exercises**: 16
  - P8.1 — Classify and Reformulate: Minimizing Maximum Absolute Deviation
  - P8.2 — QP Formulation: Constrained Least Squares
  - P8.3 — SOCP Reformulation: $\ell_2$ Regularized Least Squares
  - P8.4 — SDP Example: Largest Eigenvalue Minimization
  - P8.5 — Problem Classification: Portfolio Optimization with Risk Constraint
  - P8.6 — Equivalence: $\ell_1$ Minimization and LP
  - P8.7 — Quasiconvex Optimization: Bisection Algorithm
  - P8.8 — Minimum Enclosing Ellipsoid as SDP
  - P8.9 — Resource Allocation Formulation
  - P8.10 — Standard Form Transformation: Linear-Fractional Programming
  - P8.11 — Vector Optimization (Pareto Optimality)
  - P8.12 — Matrix Fractional Minimization
  - P8.13 — SOCP Canonical Form (Primal)
  - P8.14 — SDP Canonical Form (Primal)
  - P8.15 — Entropy Maximization via Exponential Cone
  - P8.16 — Dual of the Exponential Cone

### Broken Links Check
- All local links appear valid.

---

## [09-duality] 09. Duality Theory
*File: `topics/09-duality/index.html`*

### Sections
- **Learning Objectives**
- **1. The Engine of Duality: Conjugates and Support Functions**
  - 1.1 The Fenchel Conjugate
  - 1.2 The Fenchel-Young Inequality
  - 1.3 Support Functions and Indicator Functions
- **2. The Lagrangian**
  - 2.1 Standard Form Primal Problem
  - 2.2 The Lagrangian Function
  - 2.3 The Minimax (Saddle Point) Interpretation
- **3. The Lagrange Dual Function**
  - 3.1 Definition
  - 3.2 Lower Bound on Optimal Value
  - 3.3 Examples of Dual Functions
- **4. The Dual Problem**
  - 4.1 Definition
  - 4.2 Weak Duality
  - 4.3 Strong Duality and Slater's Condition
- **5. KKT Conditions**
- **6. Perturbation and Sensitivity Analysis**
  - 6.1 The Value Function (Perturbation Function)
  - 6.2 Convexity of the Value Function
  - 6.3 Global Inequality (Subgradient Interpretation)
  - 6.4 Local Sensitivity
- **7. Examples of Dual Problems**
  - 6.1 Linear Programming
  - 7.2 Quadratic Programming
  - 7.3 Semidefinite Programming
- **8. Generalized Inequalities and Conic Duality**
  - 8.1 The Standard Conic Form
- **9. Review & Cheat Sheet**
  - Key Definitions
  - KKT Conditions (Convex + Slater $\iff$ Optimal)
- **10. Canonical Duals: A Problem Pack**
  - Problem 1: Least Squares (Residual Form)
  - Problem 2: Ridge Regression
  - Problem 3: LASSO
  - Problem 4: Basis Pursuit
  - Problem 5: Support Vector Machine (Hinge Loss)
  - Problem 6: Trust-Region QCQP
  - Problem 7: Simplex Projection
  - Problem 8: Logistic Regression
- **11. Exercises**
  - P9.1 — Deriving the Dual of a Quadratic Program
  - P9.2 — KKT Conditions for Entropy Maximization
  - P9.3 — Sensitivity Analysis and Shadow Prices
  - P9.4 — Dual of a Linear Program
  - P9.5 — Farkas' Lemma
  - P9.6 — KKT for Water-filling
  - P9.7 — KKT for Standard QP
  - P9.8 — Certificates of Infeasibility (Gordan's Theorem)
  - P9.9 — The Gap Certificate Cookbook
  - P9.10 — SDP Duality: Max Cut Relaxation
  - P9.11 — SOCP Duality: Robust Least Squares

### Key Elements
- **Theorems/Definitions**: 5
  - Deep Dive: Minimax Theorem and Zero-Sum Games
  - Key Property: Concavity
  - Theorem (Slater's Condition)
  - Theorem (KKT Conditions)
  - Theorem: Optimal Multipliers as Subgradients
- **Proofs**: 7
  - Proof
  - Proof
  - Geometric Proof via Separation
  - Derivation from Strong Duality
  - Proof: Epigraph as Projection
  - Derivation via Perturbed Lagrangian
  - Appendix: Gap Certificate Cookbook
- **Examples**: 5
  - 1. Least Squares (Quadratic)
  - 2. Linear Program (Standard Form)
  - 3. Conjugate Functions
  - Example: Non-Convex Problem with Duality Gap
  - Application: Water-Filling (Channel Capacity)
- **Exercises**: 19
  - Problem 1: Least Squares (Residual Form)
  - Problem 2: Ridge Regression
  - Problem 3: LASSO
  - Problem 4: Basis Pursuit
  - Problem 5: Support Vector Machine (Hinge Loss)
  - Problem 6: Trust-Region QCQP
  - Problem 7: Simplex Projection
  - Problem 8: Logistic Regression
  - P9.1 — Deriving the Dual of a Quadratic Program
  - P9.2 — KKT Conditions for Entropy Maximization
  - P9.3 — Sensitivity Analysis and Shadow Prices
  - P9.4 — Dual of a Linear Program
  - P9.5 — Farkas' Lemma
  - P9.6 — KKT for Water-filling
  - P9.7 — KKT for Standard QP
  - P9.8 — Certificates of Infeasibility (Gordan's Theorem)
  - P9.9 — The Gap Certificate Cookbook
  - P9.10 — SDP Duality: Max Cut Relaxation
  - P9.11 — SOCP Duality: Robust Least Squares

### Broken Links Check
- All local links appear valid.

---

## [10-approximation-fitting] 06. Applications I: Approximation & Fitting
*File: `topics/10-approximation-fitting/index.html`*

### Sections
- **Learning Objectives**
- **Key Concepts**
  - 1. Least Squares Problems
  - 2. Weighted Least Squares
  - 3. Regularization Techniques
  - 4. Robust Regression
  - 5. Sparse Signal Recovery
  - 6. Total Variation Denoising
  - 7. Basis Pursuit and Variants
  - 8. Matrix Approximation
  - 9. Polynomial and Function Fitting
- **Interactive Widgets**
  - Least Squares Regularization
  - Robust Regression
  - Sparse Recovery Demo
  - Matrix Completion Visualizer
  - Regularization Theory Tool
- **Readings & Resources**
- **Example Problems**
  - Example 6.1: Ridge Regression with Explicit Solution
  - Example 6.2: LASSO Path and Sparsity Pattern
  - Example 6.3: Weighted Least Squares for Heteroscedastic Data
  - Example 6.4: Robust Regression with Huber Loss
  - Example 6.5: Sparse Signal Recovery via Basis Pursuit
  - Example 6.6: Total Variation Denoising of Piecewise Constant Signal
  - Example 6.7: Low-Rank Matrix Approximation via SVD
  - Example 6.8: Polynomial Fitting with Regularization
- **Exercises**

### Key Elements
- **Examples (Heuristic)**: 8
  - Example 6.1: Ridge Regression with Explicit Solution
  - Example 6.2: LASSO Path and Sparsity Pattern
  - Example 6.3: Weighted Least Squares for Heteroscedastic Data
  - Example 6.4: Robust Regression with Huber Loss
  - Example 6.5: Sparse Signal Recovery via Basis Pursuit
  - Example 6.6: Total Variation Denoising of Piecewise Constant Signal
  - Example 6.7: Low-Rank Matrix Approximation via SVD
  - Example 6.8: Polynomial Fitting with Regularization

### Broken Links Check
- All local links appear valid.

---

## [11-statistical-estimation] 07. Applications II: Statistical Estimation & Machine Learning
*File: `topics/11-statistical-estimation/index.html`*

### Sections
- **Learning Objectives**
- **Key Concepts**
  - 1. Maximum Likelihood Estimation (MLE)
  - 2. Logistic Regression
  - 3. Support Vector Machines (SVMs)
  - 4. Regularized Maximum Likelihood
  - 5. Exponential Family and GLMs
  - 6. Multi-Class Classification
  - 7. Robust Estimation
  - 8. Empirical Risk Minimization (ERM)
  - 9. Regularization Paths and Model Selection
- **Interactive Widgets**
  - Classification Boundary
  - SVM Margin Visualizer
  - Logistic Regression Solver
- **Readings & Resources**
- **Example Problems**
  - Example 7.1: MLE for Gaussian Distribution
  - Example 7.2: Logistic Regression for Binary Classification
  - Example 7.3: Hard-Margin SVM
  - Example 7.4: Soft-Margin SVM with Hinge Loss
  - Example 7.5: Poisson Regression for Count Data
  - Example 7.6: Softmax Regression for Multi-Class Classification
  - Example 7.7: Regularized Logistic Regression
  - Example 7.8: Robust MLE with Huber Loss
- **Exercises**

### Key Elements
- **Examples (Heuristic)**: 8
  - Example 7.1: MLE for Gaussian Distribution
  - Example 7.2: Logistic Regression for Binary Classification
  - Example 7.3: Hard-Margin SVM
  - Example 7.4: Soft-Margin SVM with Hinge Loss
  - Example 7.5: Poisson Regression for Count Data
  - Example 7.6: Softmax Regression for Multi-Class Classification
  - Example 7.7: Regularized Logistic Regression
  - Example 7.8: Robust MLE with Huber Loss

### Broken Links Check
- All local links appear valid.

---

## [12-geometric-problems] 08. Applications III: Geometric Problems
*File: `topics/12-geometric-problems/index.html`*

### Sections
- **Learning Objectives**
- **Key Concepts**
  - 1. Distance Between Convex Sets
  - 2. Euclidean Projection onto Convex Sets
  - 3. Minimum Volume Enclosing Ellipsoid (MVEE)
  - 4. Chebyshev Center and Maximum Inscribed Ball
  - 5. Separating and Supporting Hyperplanes
  - 6. Extremal Volume Ellipsoids
  - 7. Placement and Location Problems
  - 8. Shape Fitting and Geometric Approximation
  - 9. Floor Planning and Geometric Design
- **Interactive Widgets**
  - MVEE Visualizer
  - Chebyshev Center
  - Distance Between Convex Sets
  - Best-Fit Shape Finder
  - Matrix Rank Minimization
  - Robust Geometry Optimizer
- **Readings & Resources**
- **Example Problems**
  - Example 8.1: Euclidean Projection onto a Simplex
  - Example 8.2: Distance Between Two Polyhedra
  - Example 8.3: Chebyshev Center of Triangle
  - Example 8.4: MVEE for 2D Point Set
  - Example 8.5: Separating Hyperplane for Two Sets
  - Example 8.6: Optimal Placement of Facility
  - Example 8.7: Best-Fit Line to Points
  - Example 8.8: Maximum Volume Inscribed Ellipsoid
- **Exercises**

### Key Elements
- **Examples (Heuristic)**: 8
  - Example 8.1: Euclidean Projection onto a Simplex
  - Example 8.2: Distance Between Two Polyhedra
  - Example 8.3: Chebyshev Center of Triangle
  - Example 8.4: MVEE for 2D Point Set
  - Example 8.5: Separating Hyperplane for Two Sets
  - Example 8.6: Optimal Placement of Facility
  - Example 8.7: Best-Fit Line to Points
  - Example 8.8: Maximum Volume Inscribed Ellipsoid

### Broken Links Check
- All local links appear valid.

---

## [13-unconstrained-minimization] 09. Algorithms I: Unconstrained Minimization
*File: `topics/13-unconstrained-minimization/index.html`*

### Sections
- **Learning Objectives**
- **Key Concepts**
  - 1. Gradient Descent (GD)
  - 2. Step Size Selection
  - 3. Newton's Method
  - 4. Quasi-Newton Methods
  - 5. Conjugate Gradient Method
  - 6. Accelerated Gradient Methods
  - 7. Convergence Analysis and Rates
  - 8. Self-Concordance and Damped Newton
  - 9. Preconditioning and Scaling
- **Interactive Widgets**
  - Gradient Descent Visualizer
  - GD vs. Newton Race
  - Convergence Rate Comparison
- **Readings & Resources**
- **Example Problems**
  - Example 9.1: Gradient Descent on Quadratic Function
  - Example 9.2: Newton's Method for Logistic Regression
  - Example 9.3: Backtracking Line Search
  - Example 9.4: Conjugate Gradient for Linear System
  - Example 9.5: BFGS Update
  - Example 9.6: Convergence Rate Comparison
  - Example 9.7: Nesterov Acceleration
  - Example 9.8: Newton Decrement and Stopping Criterion
- **Exercises**

### Key Elements
- **Examples (Heuristic)**: 8
  - Example 9.1: Gradient Descent on Quadratic Function
  - Example 9.2: Newton's Method for Logistic Regression
  - Example 9.3: Backtracking Line Search
  - Example 9.4: Conjugate Gradient for Linear System
  - Example 9.5: BFGS Update
  - Example 9.6: Convergence Rate Comparison
  - Example 9.7: Nesterov Acceleration
  - Example 9.8: Newton Decrement and Stopping Criterion

### Broken Links Check
- All local links appear valid.

---

## [14-equality-constrained-minimization] 10. Algorithms II: Equality-Constrained Minimization
*File: `topics/14-equality-constrained-minimization/index.html`*

### Sections
- **Learning Objectives**
- **Key Concepts**
  - 1. KKT System for Equality-Constrained Problems
  - 2. Feasible Start Newton Method
  - 3. Infeasible Start Newton Method
  - 4. Elimination via Null-Space Methods
  - 5. Elimination via Explicit Solution
  - 6. Augmented Lagrangian and Penalty Methods
  - 7. Projected Gradient Descent
  - 8. Range-Space vs. Null-Space Methods
  - 9. Sequential Quadratic Programming (SQP)
- **Interactive Widgets**
  - Null-Space Visualizer
  - Projected Gradient Descent
  - Feasible vs. Interior-Point Methods
- **Readings & Resources**
- **Example Problems**
  - Example 10.1: QP with Equality Constraints via KKT System
  - Example 10.2: Null-Space Elimination
  - Example 10.3: Projected Gradient Descent
  - Example 10.4: Augmented Lagrangian Method
  - Example 10.5: Feasible vs. Infeasible Start
  - Example 10.6: Analytic Center of Linear Inequalities
  - Example 10.7: Explicit QP Solution
  - Example 10.8: Range-Space vs. Null-Space Complexity
- **Exercises**

### Key Elements
- **Examples (Heuristic)**: 8
  - Example 10.1: QP with Equality Constraints via KKT System
  - Example 10.2: Null-Space Elimination
  - Example 10.3: Projected Gradient Descent
  - Example 10.4: Augmented Lagrangian Method
  - Example 10.5: Feasible vs. Infeasible Start
  - Example 10.6: Analytic Center of Linear Inequalities
  - Example 10.7: Explicit QP Solution
  - Example 10.8: Range-Space vs. Null-Space Complexity

### Broken Links Check
- All local links appear valid.

---

## [15-interior-point-methods] 11. Algorithms III: Interior-Point Methods
*File: `topics/15-interior-point-methods/index.html`*

### Sections
- **Learning Objectives**
- **Key Concepts**
  - 1. Logarithmic Barrier Function
  - 2. Central Path and Optimality
  - 3. Barrier Method Algorithm
  - 4. Self-Concordance and Complexity
  - 5. Primal-Dual Interior-Point Methods
  - 6. Path-Following vs. Potential Reduction
  - 7. Homogeneous Self-Dual Embedding
  - 8. Conic Optimization: LP, SOCP, SDP
  - 9. Warm-Starting and Practical Considerations
- **Interactive Widgets**
  - Barrier Method Path Tracer
  - LP Simplex vs. Interior-Point
  - Newton Step in IPM
- **Readings & Resources**
- **Example Problems**
  - Example 11.1: Log-Barrier for Simple LP
  - Example 11.2: Central Path for 2D LP
  - Example 11.3: Barrier Method Iteration
  - Example 11.4: Complementary Slackness Gap
  - Example 11.5: Primal-Dual KKT System
  - Example 11.6: SDP via Barrier Method
  - Example 11.7: Geometric Program Transformation
  - Example 11.8: Complexity Analysis
- **Exercises**

### Key Elements
- **Examples (Heuristic)**: 8
  - Example 11.1: Log-Barrier for Simple LP
  - Example 11.2: Central Path for 2D LP
  - Example 11.3: Barrier Method Iteration
  - Example 11.4: Complementary Slackness Gap
  - Example 11.5: Primal-Dual KKT System
  - Example 11.6: SDP via Barrier Method
  - Example 11.7: Geometric Program Transformation
  - Example 11.8: Complexity Analysis

### Broken Links Check
- All local links appear valid.

---
