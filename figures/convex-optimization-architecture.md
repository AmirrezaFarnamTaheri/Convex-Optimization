# Convex Optimization — Complete System Architecture & Curriculum Pipeline

This diagram formalizes the rigorous 4-phase theoretical pipeline of Convex Optimization, connecting rigorous mathematical foundations through duality theory and computational solvers to the interactive WebGL/D3/Pyodide visual simulation stack.

```mermaid
flowchart TB
    %% ─────────────────────────────────────────────────────────────
    %% STYLES & DEFINITIONS
    %% ─────────────────────────────────────────────────────────────
    classDef foundation fill:#EFF6FF,stroke:#3B82F6,stroke-width:2px,color:#1E3A8A;
    classDef geometry fill:#F5F3FF,stroke:#8B5CF6,stroke-width:2px,color:#4C1D95;
    classDef duality fill:#FDF2F8,stroke:#EC4899,stroke-width:2px,color:#831843;
    classDef algos fill:#ECFDF5,stroke:#10B981,stroke-width:2px,color:#064E3B;
    classDef apps fill:#FFFBEB,stroke:#F59E0B,stroke-width:2px,color:#78350F;
    classDef lab fill:#F8FAFC,stroke:#64748B,stroke-width:2px,color:#0F172A;

    subgraph SEC_FOUNDATION ["📐 Phase I: Mathematical Foundations"]
        LA["$$\text{Linear Algebra: } V, \langle u, v \rangle, \text{SVD, } A = U \Sigma V^T$$"]:::foundation
        ANA["$$\text{Real Analysis: } \text{cl}(S), \text{int}(S), \partial S, \text{Weierstrass Theorem}$$"]:::foundation
    end

    subgraph SEC_GEOMETRY ["🧊 Phase II: Convex Geometry & Cones"]
        SETS["$$\text{Convex Sets: } \theta x + (1-\theta)y \in C, \ \forall \theta \in [0, 1]$$"]:::geometry
        CONES["$$\text{Cones & Dual Cones: } \mathcal{K}^* = \{y \mid x^T y \ge 0, \ \forall x \in \mathcal{K}\}$$"]:::geometry
        FUNCS["$$\text{Convex Functions: } f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$"]:::geometry
        OPER["$$\text{Calculus & Operations: } f^*, \ \text{epi}(f), \ \nabla^2 f(x) \succeq 0$$"]:::geometry
    end

    subgraph SEC_DUALITY ["⚖️ Phase III: Duality Theory & Optimality"]
        LAGR["$$\text{Lagrangian: } L(x, \lambda, \nu) = f_0(x) + \sum \lambda_i f_i(x) + \sum \nu_i h_i(x)$$"]:::duality
        DUAL["$$\text{Dual Function: } g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$"]:::duality
        SLATER["$$\text{Slater's Condition: } \exists x \in \text{relint}(D) \implies p^* = d^*$$"]:::duality
        KKT["$$\text{KKT Conditions: } \nabla f_0(x^*) + \sum \lambda_i^* \nabla f_i(x^*) + \sum \nu_i^* \nabla h_i(x^*) = 0$$"]:::duality
    end

    subgraph SEC_ALGORITHMS ["⚡ Phase IV: Computational Algorithms"]
        UNCON["$$\text{Unconstrained: Gradient Descent & Newton-Raphson}$$"]:::algos
        CONIC["$$\text{Conic Formulations: LP, QP, SOCP, SDP}$$"]:::algos
        INTERIOR["$$\text{Barrier & Primal-Dual Interior-Point Methods}$$"]:::algos
        FIRST_ORDER["$$\text{Proximal Splitting, ADMM & Operator Splitting}$$"]:::algos
        STOCHASTIC["$$\text{Stochastic & Online Convex Optimization (SGD, Adam)}$$"]:::algos
    end

    subgraph SEC_LAB ["🧪 Visual & Interactive Simulation Stack"]
        D3["$$\text{D3.js 2D Invariant Manipulators (Supporting Hyperplanes)}$$"]:::lab
        THREE["$$\text{Three.js 3D Epigraphs & Second-Order Lorentz Cones}$$"]:::lab
        PYODIDE["$$\text{Pyodide In-Browser CVXPY Optimization Engine}$$"]:::lab
    end

    %% Flow Connections
    LA --> SETS
    ANA --> FUNCS
    SETS --> CONES
    CONES --> FUNCS
    FUNCS --> OPER
    OPER --> LAGR
    LAGR --> DUAL
    DUAL --> SLATER
    SLATER --> KKT
    KKT --> UNCON
    KKT --> CONIC
    UNCON --> INTERIOR
    CONIC --> INTERIOR
    INTERIOR --> FIRST_ORDER
    FIRST_ORDER --> STOCHASTIC

    %% Interactivity mappings
    SETS -.-> D3
    CONES -.-> THREE
    FUNCS -.-> THREE
    CONIC -.-> PYODIDE
    FIRST_ORDER -.-> PYODIDE
```

## Structural Summary

1. **Phase I (Foundations)**: Establishes inner product spaces, Spectral Theorem, SVD, and point-set topology.
2. **Phase II (Geometry & Cones)**: Explores convex sets, proper cones, dual cones $\mathcal{K}^*$, epigraphs, and convex calculus.
3. **Phase III (Duality Theory)**: Derives Lagrange dual problems, weak duality, Slater's constraint qualifications for strong duality, and full Karush-Kuhn-Tucker (KKT) optimality systems.
4. **Phase IV (Algorithms)**: Covers classical descent, Interior-Point methods with self-concordant barriers, ADMM operator splitting, and modern Stochastic Online Convex Optimization.
5. **Interactive Laboratory Layer**: Direct real-time bindings to D3.js geometric manipulators, Three.js 3D PBR epigraph manifolds, and in-browser Pyodide CVXPY solver engines.
