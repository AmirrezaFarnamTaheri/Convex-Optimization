import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def save_gif(anim, path, fps=12):
    anim.save(path, writer=PillowWriter(fps=fps))
    print(f"Saved: {path} (FPS: {fps})")

# -----------------------------
# Helpers
# -----------------------------
def quad_levelset_points_diag(gamma, c, n=400):
    """
    Level set for f(x)=0.5(x1^2 + gamma x2^2) = c
    => x1^2 + gamma x2^2 = 2c (ellipse).
    """
    theta = np.linspace(0, 2*np.pi, n)
    x1 = np.sqrt(2*c) * np.cos(theta)
    x2 = np.sqrt(2*c/gamma) * np.sin(theta)
    return x1, x2

def gd_exact_diag(gamma, x0, K):
    """
    GD + exact line search on f(x)=0.5(x1^2+gamma x2^2).
    H = diag(1, gamma), g = Hx.
    Exact line search along -g: t = (g^T g)/(g^T H g).
    """
    x = np.array(x0, dtype=float)
    xs = [x.copy()]
    for _ in range(K):
        g = np.array([x[0], gamma*x[1]])
        gtg = g @ g                       # x1^2 + gamma^2 x2^2
        gHg = g[0]**2 + gamma*(g[1]**2)   # x1^2 + gamma^3 x2^2
        t = gtg / gHg if gHg > 0 else 0.0
        x = x - t*g
        xs.append(x.copy())
    return np.array(xs)

def quad_levelset_points(H, c, n=400):
    """
    Level set for 0.5 x^T H x = c in R^2 with SPD H.
    If H = Q diag(lam) Q^T, then x = Q diag(sqrt(2c/lam)) [cos; sin].
    """
    lam, Q = np.linalg.eigh(H)
    theta = np.linspace(0, 2*np.pi, n)
    circle = np.vstack([np.cos(theta), np.sin(theta)])  # 2 x n
    scales = np.sqrt((2*c)/lam)
    x = Q @ (scales[:, None] * circle)
    return x[0], x[1]

def gd_exact_quad(H, b, x0, K):
    """
    GD + exact line search on f(x)=0.5 x^T H x + b^T x (H SPD).
    g = Hx + b, d = -g
    t = (g^T g)/(g^T H g).
    """
    x = np.array(x0, dtype=float)
    xs = [x.copy()]
    for _ in range(K):
        g = H @ x + b
        Hg = H @ g
        gtg = g @ g
        gHg = g @ Hg
        t = gtg / gHg if gHg > 0 else 0.0
        x = x - t*g
        xs.append(x.copy())
    return np.array(xs)

def precond_gd_exact_quad(H, b, P, x0, K):
    """
    Steepest descent in P-norm => direction d = -P^{-1} g, exact line search.
    Quadratic line search: t = -(g^T d)/(d^T H d).
    """
    Pinv = np.linalg.inv(P)
    x = np.array(x0, dtype=float)
    xs = [x.copy()]
    for _ in range(K):
        g = H @ x + b
        d = -Pinv @ g
        denom = d @ (H @ d)
        t = -(g @ d) / denom if denom > 0 else 0.0
        x = x + t*d
        xs.append(x.copy())
    return np.array(xs)

def l1_steepest_exact_quad(H, b, x0, K):
    """
    ℓ1-steepest descent:
      pick i maximizing |g_i|
      exact minimization along coordinate i:
        x -> x + s e_i,  s* = -g_i/H_ii
    """
    x = np.array(x0, dtype=float)
    xs = [x.copy()]
    for _ in range(K):
        g = H @ x + b
        i = int(np.argmax(np.abs(g)))
        s = -g[i] / H[i, i]
        step = np.zeros(2)
        step[i] = s
        x = x + step
        xs.append(x.copy())
    return np.array(xs)

# ============================================================
# 1) Gradient descent zig-zag on an ill-conditioned quadratic
#    f(x)=1/2(x1^2 + gamma x2^2), exact line search along -grad.
# ============================================================
def make_gif_gradient_zigzag(path="gd_zigzag.gif", gamma=30.0, K=40):
    H = np.diag([1.0, gamma])

    def grad(x):
        return np.array([x[0], gamma * x[1]])

    # exact line search for quadratic along -g:
    # t = (g^T g)/(g^T H g)
    def step_size(x):
        g = grad(x)
        return float((g @ g) / (g @ (H @ g)))

    x = np.array([gamma, 1.0], dtype=float)
    xs = [x.copy()]
    for _ in range(K):
        g = grad(x)
        t = step_size(x)
        x = x - t * g
        xs.append(x.copy())
    xs = np.array(xs)

    lim = max(2.5, float(np.max(np.abs(xs))) * 1.1)
    grid = np.linspace(-lim, lim, 250)
    X, Y = np.meshgrid(grid, grid)
    F = 0.5 * (X**2 + gamma * Y**2)

    fig, ax = plt.subplots(figsize=(5.6, 5.6))
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Gradient descent (exact line search) on ill-conditioned quadratic")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")

    positive = F[F > 0]
    lo = float(np.min(positive)) if positive.size else 1e-3
    levels = np.geomspace(lo, float(np.max(F)), 14)
    ax.contour(X, Y, F, levels=levels)

    (path_line,) = ax.plot([], [], marker="o", markersize=3)
    (pt,) = ax.plot([], [], marker="o", markersize=6)

    def init():
        path_line.set_data([], [])
        pt.set_data([], [])
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        return path_line, pt

    def update(i):
        path_line.set_data(xs[: i + 1, 0], xs[: i + 1, 1])
        pt.set_data([xs[i, 0]], [xs[i, 1]])
        return path_line, pt

    # Slower FPS for path visualization
    anim = FuncAnimation(fig, update, frames=len(xs), init_func=init, blit=True)
    save_gif(anim, path, fps=5)
    plt.close(fig)

# ============================================================
# 2) Steepest descent direction depends on norm geometry:
#    show unit balls of l2 and l1, rotate gradient, show
#    steepest direction under each norm.
# ============================================================
def make_gif_norm_geometry(path="steepest_descent_norms.gif", frames=140):
    fig, ax = plt.subplots(figsize=(6.2, 6.2))
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Steepest direction depends on geometry: $\\ell_2$ vs $\\ell_1$")
    ax.set_xlabel("$v_1$")
    ax.set_ylabel("$v_2$")

    th = np.linspace(0, 2 * np.pi, 400)
    ball_l2 = np.c_[np.cos(th), np.sin(th)]
    ball_l1 = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]], dtype=float)

    ax.plot(ball_l2[:, 0], ball_l2[:, 1])
    ax.plot(ball_l1[:, 0], ball_l1[:, 1])

    (g_line,) = ax.plot([], [])
    (sd_l2_line,) = ax.plot([], [])
    (sd_l1_line,) = ax.plot([], [])
    txt = ax.text(0.02, 0.02, "", transform=ax.transAxes)

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)

    def init():
        g_line.set_data([], [])
        sd_l2_line.set_data([], [])
        sd_l1_line.set_data([], [])
        txt.set_text("")
        return g_line, sd_l2_line, sd_l1_line, txt

    def update(i):
        theta = 2 * np.pi * (i / frames)
        g = np.array([np.cos(theta), 0.65 * np.sin(theta)])

        # l2 steepest: v = -g/||g||
        v_l2 = -g / np.linalg.norm(g)

        # l1 steepest: put all mass on max-|g_i| coordinate
        j = int(np.argmax(np.abs(g)))
        v_l1 = np.zeros(2)
        v_l1[j] = -np.sign(g[j]) if g[j] != 0 else -1.0

        g_line.set_data([0, g[0]], [0, g[1]])
        sd_l2_line.set_data([0, v_l2[0]], [0, v_l2[1]])
        sd_l1_line.set_data([0, v_l1[0]], [0, v_l1[1]])

        txt.set_text("Gradient $g$ rotates.\nL2 steepest follows $-g$.\nL1 steepest snaps to an axis.")
        return g_line, sd_l2_line, sd_l1_line, txt

    # Smooth rotation, 15 FPS
    anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
    save_gif(anim, path, fps=15)
    plt.close(fig)

# ============================================================
# 3) Backtracking line search (Armijo) along a 1D slice:
#    show phi(t)=f(x+t d), show Armijo line, animate candidate t.
# ============================================================
def make_gif_backtracking(path="backtracking_armijo.gif", alpha=0.2, beta=0.6):
    def f(z):
        return (z - 2.0) ** 2 + np.exp(0.5 * z)

    def fp(z):
        return 2.0 * (z - 2.0) + 0.5 * np.exp(0.5 * z)

    x = 0.0
    d = -fp(x)              # descent direction in 1D
    phi0 = f(x)
    phip0 = fp(x) * d       # phi'(0)

    ts = [1.0]
    t = 1.0
    while f(x + t * d) > phi0 + alpha * t * phip0:
        t = beta * t
        ts.append(t)
        if len(ts) > 30:
            break

    tmax = max(1.2, 1.1 * ts[0])
    T = np.linspace(0.0, tmax, 400)
    PHI = f(x + T * d)

    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    ax.set_title("Backtracking line search (Armijo) on a 1D slice")
    ax.set_xlabel("$t$")
    ax.set_ylabel("$\\phi(t)=f(x+t\\Delta)$")

    ax.plot(T, PHI)
    ax.plot(T, phi0 + alpha * T * phip0)

    (vline,) = ax.plot([], [])
    (pt,) = ax.plot([], [], marker="o", markersize=6)
    status = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

    ax.set_xlim(0, tmax)
    ymin = min(float(PHI.min()), float((phi0 + alpha * T * phip0).min()))
    ymax = max(float(PHI.max()), float((phi0 + alpha * T * phip0).max()))
    ax.set_ylim(ymin - 0.05 * (ymax - ymin), ymax + 0.05 * (ymax - ymin))

    def init():
        vline.set_data([], [])
        pt.set_data([], [])
        status.set_text("")
        return vline, pt, status

    def update(i):
        tc = ts[i]
        yc = f(x + tc * d)
        vline.set_data([tc, tc], [ax.get_ylim()[0], yc])
        pt.set_data([tc], [yc])
        ok = yc <= phi0 + alpha * tc * phip0
        status.set_text(f"candidate t={tc:.4f}  |  Armijo {'PASS' if ok else 'FAIL'}")
        return vline, pt, status

    # Very slow FPS to show thinking process
    anim = FuncAnimation(fig, update, frames=len(ts), init_func=init, blit=True)
    save_gif(anim, path, fps=2)
    plt.close(fig)

# ============================================================
# 4) Newton step as minimizer of local quadratic model (1D demo):
#    show f(x), quadratic model at x_k, and Newton jump to its minimizer.
# ============================================================
def make_gif_newton_quadratic_model(path="newton_quadratic_model.gif", K=10):
    def f(x):
        return np.exp(x) + 0.5 * (x - 1.0) ** 2

    def fp(x):
        return np.exp(x) + (x - 1.0)

    def fpp(x):
        return np.exp(x) + 1.0

    x = 1.5
    xs = [x]
    for _ in range(K):
        x = x - fp(x) / fpp(x)   # full Newton step in 1D
        xs.append(x)
    xs = np.array(xs)

    xmin = float(np.min(xs) - 1.0)
    xmax = float(np.max(xs) + 1.0)
    X = np.linspace(xmin, xmax, 500)
    Y = f(X)

    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    ax.set_title("Newton step = minimizer of local quadratic model (1D)")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$f(x)$")
    ax.plot(X, Y)

    (pt,) = ax.plot([], [], marker="o", markersize=7)
    (next_pt,) = ax.plot([], [], marker="o", markersize=7)
    (quad_line,) = ax.plot([], [])
    (seg,) = ax.plot([], [])
    txt = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(float(Y.min()) - 0.1 * float(Y.max() - Y.min()),
                float(Y.max()) + 0.1 * float(Y.max() - Y.min()))

    def init():
        pt.set_data([], [])
        next_pt.set_data([], [])
        quad_line.set_data([], [])
        seg.set_data([], [])
        txt.set_text("")
        return pt, next_pt, quad_line, seg, txt

    def update(k):
        xk = float(xs[k])
        g = float(fp(xk))
        h = float(fpp(xk))

        # quadratic model: f(xk) + g (z-xk) + 0.5 h (z-xk)^2
        Z = np.linspace(xk - 1.0, xk + 1.0, 200)
        Q = f(xk) + g * (Z - xk) + 0.5 * h * (Z - xk) ** 2

        xnext = float(xs[min(k + 1, len(xs) - 1)])
        pt.set_data([xk], [f(xk)])
        next_pt.set_data([xnext], [f(xnext)])
        quad_line.set_data(Z, Q)
        seg.set_data([xk, xnext], [f(xk), f(xnext)])

        # in 1D: Newton decrement^2 = g^2/h
        lam2 = g * g / h
        txt.set_text(f"k={k}\nNewton decrement^2: {lam2:.3e}\nupdate: x <- x - f'/f''")
        return pt, next_pt, quad_line, seg, txt

    # Slow steps
    anim = FuncAnimation(fig, update, frames=len(xs), init_func=init, blit=True)
    save_gif(anim, path, fps=2)
    plt.close(fig)

# ============================================================
# GIF 5: Conditioning makes zig-zag worse
# ============================================================
def make_gif_kappa_effect(path="kappa_effect_paths.gif"):
    gamma_min, gamma_max = 1.0, 200.0
    frames1 = 45
    K_path = 14
    x0 = (1.0, 1.0)

    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    ax.set_aspect('equal', adjustable='box')

    def update1(i):
        ax.clear()
        ax.set_aspect('equal', adjustable='box')

        gamma = gamma_min * (gamma_max/gamma_min)**(i/(frames1-1))
        kappa = max(gamma, 1/gamma)

        for c in [0.05, 0.15, 0.35]:
            x1, x2 = quad_levelset_points_diag(gamma, c)
            ax.plot(x1, x2, lw=1)

        xs = gd_exact_diag(gamma, x0, K_path)
        ax.plot(xs[:,0], xs[:,1], marker='o', ms=3, lw=1)
        ax.plot([0],[0], marker='x', ms=7, lw=0)

        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_title("Condition number tax: GD path worsens as κ grows")
        ax.text(0.02, 0.98, f"γ = {gamma:6.2f}\nκ ≈ {kappa:6.2f}",
                transform=ax.transAxes, va="top")
        return ax.lines

    anim1 = FuncAnimation(fig, update1, frames=frames1, interval=70, blit=False)
    save_gif(anim1, path, fps=10) # 45 frames / 10 fps = 4.5 sec
    plt.close(fig)

# ============================================================
# GIF 6: Preconditioning comparison on a rotated quadratic
# ============================================================
def make_gif_precond(path="preconditioning_comparison.gif"):
    H = np.array([[1.0, 0.9],
                  [0.9, 80.0]])
    b = np.array([1.0, -5.0])
    x_star = -np.linalg.solve(H, b)

    x0 = np.array([2.5, -1.5])
    K2 = 25

    xs_gd = gd_exact_quad(H, b, x0, K2)
    P_jacobi = np.diag(np.diag(H))
    xs_pc = precond_gd_exact_quad(H, b, P_jacobi, x0, K2)
    xs_nt = np.vstack([x0, x_star])  # Newton solves quadratic in 1 step

    all_pts = np.vstack([xs_gd, xs_pc, xs_nt, x_star[None,:]])
    xmin, xmax = all_pts[:,0].min()-0.6, all_pts[:,0].max()+0.6
    ymin, ymax = all_pts[:,1].min()-0.6, all_pts[:,1].max()+0.6
    ellipses = [quad_levelset_points(H, c) for c in [0.5, 2.0, 6.0, 14.0]]

    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.set_aspect('equal', adjustable='box')

    def update2(k):
        ax.clear()
        ax.set_aspect('equal', adjustable='box')

        for (x1, x2) in ellipses:
            ax.plot(x_star[0] + x1, x_star[1] + x2, lw=1)
        ax.plot([x_star[0]], [x_star[1]], marker='x', ms=7, lw=0)

        k = min(k, K2)
        ax.plot(xs_gd[:k+1,0], xs_gd[:k+1,1], marker='o', ms=3, lw=1)
        ax.plot(xs_pc[:k+1,0], xs_pc[:k+1,1], marker='o', ms=3, lw=1)
        ax.plot(xs_nt[:,0], xs_nt[:,1], marker='o', ms=3, lw=1)

        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        ax.set_title("Same f, different geometry: GD vs precond vs Newton")
        ax.legend(["Level sets", "x*", "GD (ℓ2)", "Precond (P=diag(H))", "Newton"],
                  loc="lower left", fontsize=8, frameon=True)
        ax.text(0.02, 0.98, f"iter k = {k}", transform=ax.transAxes, va="top")
        return ax.lines

    anim2 = FuncAnimation(fig, update2, frames=K2+1, interval=90, blit=False)
    save_gif(anim2, path, fps=5) # 25 frames / 5 fps = 5 sec
    plt.close(fig)

# ============================================================
# GIF 7: ℓ1-steepest vs GD on same quadratic
# ============================================================
def make_gif_l1_vs_gd(path="l1_coordinate_descent_vs_gd.gif"):
    H = np.array([[1.0, 0.9],
                  [0.9, 80.0]])
    b = np.array([1.0, -5.0])
    x_star = -np.linalg.solve(H, b)
    x0 = np.array([2.5, -1.5])
    ellipses = [quad_levelset_points(H, c) for c in [0.5, 2.0, 6.0, 14.0]]

    K3 = 30
    xs_cd = l1_steepest_exact_quad(H, b, x0, K3)
    xs_gd3 = gd_exact_quad(H, b, x0, K3)

    all_pts = np.vstack([xs_cd, xs_gd3, x_star[None,:]])
    xmin, xmax = all_pts[:,0].min()-0.6, all_pts[:,0].max()+0.6
    ymin, ymax = all_pts[:,1].min()-0.6, all_pts[:,1].max()+0.6

    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.set_aspect('equal', adjustable='box')

    def update3(k):
        ax.clear()
        ax.set_aspect('equal', adjustable='box')

        for (x1, x2) in ellipses:
            ax.plot(x_star[0] + x1, x_star[1] + x2, lw=1)
        ax.plot([x_star[0]], [x_star[1]], marker='x', ms=7, lw=0)

        ax.plot(xs_gd3[:k+1,0], xs_gd3[:k+1,1], marker='o', ms=3, lw=1)
        ax.plot(xs_cd[:k+1,0], xs_cd[:k+1,1], marker='o', ms=3, lw=1)

        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        ax.set_title("ℓ1-steepest descent follows axes (coordinate-like)")
        ax.legend(["Level sets", "x*", "GD (ℓ2 steepest)", "ℓ1-steepest"],
                  loc="lower left", fontsize=8, frameon=True)
        ax.text(0.02, 0.98, f"iter k = {k}", transform=ax.transAxes, va="top")
        return ax.lines

    anim3 = FuncAnimation(fig, update3, frames=K3+1, interval=90, blit=False)
    save_gif(anim3, path, fps=5)
    plt.close(fig)

# ============================================================
# GIF 8: Damped Newton + backtracking on BV (9.20)-style exp-sum objective
# ============================================================
def make_gif_damped_newton(path="damped_newton_backtracking_2d.gif"):
    A = np.array([[1.0,  3.0],
                  [1.0, -3.0],
                  [-1.0, 0.0]])
    c_vec = np.array([-0.1, -0.1, -0.1])

    def f_exp(x):
        z = A @ x + c_vec
        return np.sum(np.exp(z))

    def grad_exp(x):
        z = A @ x + c_vec
        w = np.exp(z)
        return A.T @ w

    def hess_exp(x):
        z = A @ x + c_vec
        w = np.exp(z)
        return A.T @ (w[:, None] * A)

    def damped_newton_backtracking(x0, K=18, alpha=0.25, beta=0.5):
        x = np.array(x0, dtype=float)
        xs, ts, lams = [x.copy()], [], []
        for _ in range(K):
            g = grad_exp(x)
            Hx = hess_exp(x)
            d = -np.linalg.solve(Hx, g)

            lam2 = -g @ d                   # Newton decrement squared
            lams.append(np.sqrt(max(lam2, 0.0)))

            t = 1.0
            fx = f_exp(x)
            while f_exp(x + t*d) > fx + alpha*t*(g @ d):
                t *= beta
                if t < 1e-12:
                    break

            x = x + t*d
            xs.append(x.copy())
            ts.append(t)

            if lam2/2 <= 1e-10:
                break
        return np.array(xs), np.array(ts), np.array(lams)

    x0N = np.array([0.0, 1.0])
    xsN, tsN, lamsN = damped_newton_backtracking(x0N)

    # Precompute contour background
    x1 = np.linspace(-1.5, 1.5, 230)
    x2 = np.linspace(-1.5, 1.5, 230)
    X1, X2 = np.meshgrid(x1, x2)
    pts = np.stack([X1.ravel(), X2.ravel()], axis=1)
    Z = np.exp(pts @ A.T + c_vec).sum(axis=1).reshape(X1.shape)
    Zlog = np.log(Z)
    levels = np.quantile(Zlog.ravel(), [0.05, 0.15, 0.3, 0.5, 0.7, 0.85, 0.95])

    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    ax.set_aspect('equal', adjustable='box')

    def update4(k):
        ax.clear()
        ax.set_aspect('equal', adjustable='box')
        ax.contour(X1, X2, Zlog, levels=levels, linewidths=1)

        k = min(k, len(xsN)-1)
        ax.plot(xsN[:k+1,0], xsN[:k+1,1], marker='o', ms=3, lw=1)

        if k > 0:
            t = tsN[k-1]
            lam = lamsN[k-1]
            ax.text(0.02, 0.98, f"iter k = {k}\nstep t = {t:.3g}\nNewton decrement λ ≈ {lam:.3g}",
                    transform=ax.transAxes, va="top")
        else:
            ax.text(0.02, 0.98, f"iter k = {k}", transform=ax.transAxes, va="top")

        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_title("Damped Newton (Armijo backtracking): step sizes + λ(x)")
        return ax.lines

    anim4 = FuncAnimation(fig, update4, frames=len(xsN), interval=130, blit=False)
    save_gif(anim4, path, fps=4) # 18 frames / 4 fps = 4.5 sec
    plt.close(fig)

if __name__ == "__main__":
    os.makedirs("topics/13-unconstrained-minimization/assets", exist_ok=True)
    base = "topics/13-unconstrained-minimization/assets"

    make_gif_gradient_zigzag(f"{base}/gd_zigzag.gif")
    make_gif_norm_geometry(f"{base}/steepest_descent_norms.gif")
    make_gif_backtracking(f"{base}/backtracking_armijo.gif")
    make_gif_newton_quadratic_model(f"{base}/newton_quadratic_model.gif")

    make_gif_kappa_effect(f"{base}/kappa_effect_paths.gif")
    make_gif_precond(f"{base}/preconditioning_comparison.gif")
    make_gif_l1_vs_gd(f"{base}/l1_coordinate_descent_vs_gd.gif")
    make_gif_damped_newton(f"{base}/damped_newton_backtracking_2d.gif")

    print("Done generating all GIFs.")
