# Image Sources & Notes

This repository contains original diagrams/animations as well as third‑party assets.
This document captures image provenance notes and a short “to-add / to-adopt” backlog.

## Planned images to add (descriptions)

### 1) Determinant as volume scaling
- **Left**: unit square spanned by \(e_1, e_2\).
- **Right**: transformed parallelogram spanned by \(Ae_1, Ae_2\), labeled \(|\det(A)|\).
- **Orientation**: indicate sign via orientation (flip → negative determinant).

### 2) Operator norm geometry
- **Input**: unit circle.
- **Output**: ellipse \(A(\mathbb{S}^1)\).
- **Max stretch**: highlight longest semi-axis; label \(\|A\|_2 = \sigma_{\max}\).

### 3) SVD transformation sequence
Visual sequence for \(A = U\Sigma V^\top\): rotate → axis stretch → rotate.

### 4) SVD vs eigendecomposition (non-symmetric)
Contrast “invariant directions” (eigenvectors) vs orthogonal frames mapped by SVD.

### 5) Zig-zag of ill-conditioning
Two contour plots (well conditioned vs ill conditioned) with gradient descent paths.

### 6) Duality: \(\ell_1\) vs \(\ell_\infty\)
Maximizing \(x^\top y\) over the \(\ell_1\) unit ball; show it selects the largest component.

### 7) Least squares as orthogonal projection
Plane = \(\mathcal{R}(A)\), point \(b\), projection \(Ax^\*\), residual orthogonal to plane.

### 8) Projection onto an affine set
Show shift by a particular solution \(x_0\), project \(y-x_0\) onto parallel subspace, shift back.

### 9) Condition number: error amplification in linear systems
Two panels comparing error regions under \(x=A^{-1}b\) for \(\kappa(A)\approx 1\) vs \(\kappa(A)\gg 1\).
Include inequality:
\[
\frac{\|\delta x\|}{\|x\|} \le \kappa(A)\cdot \frac{\|\delta b\|}{\|b\|}.
\]

### 10) Low-rank image approximation
Three reconstructions (rank 500 vs 50 vs 5) with “energy retained” labels.

## Planned images to adopt (descriptions)

| # | Topic | Description | Why |
|---:|---|---|---|
| 1 | Gram–Schmidt Orthogonalization | Geometric illustration of subtracting projections to produce an orthonormal basis. | Fills a gap: orthogonalization is core in LA and later algorithms. |
| 2 | SVD Ellipsoid | Unit sphere mapped to ellipsoid; semi-axes = singular values, directions = singular vectors. | Reinforces geometric meaning of SVD. |
| 3 | Minkowski sum/difference | Two subfigures: Minkowski addition and erosion; annotate definition and basic properties. | Supports convex set intuition in early lectures. |
| 4 | Projection onto a convex set | Nearest-point projection with orthogonality / normal vector intuition. | Projections are foundational (prox methods, feasibility). |


