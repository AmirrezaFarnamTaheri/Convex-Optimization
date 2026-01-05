import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Ensure output directory exists
OUTPUT_DIR = "."

def save_anim(anim, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    print(f"Saving {filepath}...")
    anim.save(filepath, writer=PillowWriter(fps=10))
    print(f"Saved {filepath}")

# ------------------------------
# GIF 1: Saddle-point dynamics
# ------------------------------
def make_saddle_path_gif():
    def f0(x):
        return (x - 2.0)**2

    def g(lam):
        return lam - (lam**2)/4.0

    # Grid for contouring L(x,λ)
    x_grid = np.linspace(-0.5, 2.5, 220)
    lam_grid = np.linspace(0.0, 4.0, 220)
    X, Lam = np.meshgrid(x_grid, lam_grid)
    L_grid = (X - 2.0)**2 + Lam*(X - 1.0)

    # Simple projected primal-dual iterations (toy demonstration)
    alpha = 0.25  # primal step
    beta  = 0.35  # dual step
    T = 50

    x = 2.4
    lam = 0.0
    xs = [x]
    lams = [lam]

    for _ in range(T):
        # Primal step: x <- x - alpha * ∂L/∂x, with ∂L/∂x = 2(x-2) + λ
        grad_x = 2.0*(x - 2.0) + lam
        x = x - alpha * grad_x

        # Project to feasible set x <= 1 (hard projection for demonstration)
        x = min(x, 1.0)

        # Dual ascent: λ <- [λ + beta*(x-1)]_+, since constraint is x-1 <= 0
        lam = max(0.0, lam + beta*(x - 1.0))

        xs.append(x)
        lams.append(lam)

    # Plot + animate
    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    ax.set_title("Saddle-point view: L(x,λ) contours + primal-dual path (x<=1, λ>=0)")
    ax.set_xlabel("x")
    ax.set_ylabel("λ")
    ax.set_xlim(x_grid.min(), x_grid.max())
    ax.set_ylim(lam_grid.min(), lam_grid.max())

    levels = np.linspace(np.percentile(L_grid, 5), np.percentile(L_grid, 95), 14)
    ax.contour(X, Lam, L_grid, levels=levels)

    # Boundary x=1 and saddle point (1,2)
    ax.axvline(1.0, linestyle="--", label="constraint boundary x=1")
    ax.plot([1.0], [2.0], marker="o", linestyle="", label="saddle (x*=1, λ*=2)")

    (path_line,) = ax.plot([], [], linewidth=2, label="iterates")
    (pt_now,) = ax.plot([], [], marker="o", linestyle="")
    txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
    ax.legend(loc="lower left")

    def update(i):
        path_line.set_data(xs[:i+1], lams[:i+1])
        pt_now.set_data([xs[i]], [lams[i]])
        txt.set_text(
            f"iter k={i:02d}\n"
            f"x_k={xs[i]:.4f}\n"
            f"λ_k={lams[i]:.4f}\n"
            f"f0(x_k)={f0(xs[i]):.4f}\n"
            f"g(λ_k)={g(lams[i]):.4f}"
        )
        return path_line, pt_now, txt

    anim = FuncAnimation(fig, update, frames=len(xs), interval=90, blit=True)
    save_anim(anim, "duality_saddle_path.gif")
    plt.close(fig)

# ------------------------------
# GIF 2: Complementary slackness switch
# ------------------------------
def make_comp_slack_switch_gif():
    def f0(x):
        return (x - 2.0)**2

    def x_star(u):
        return min(2.0, 1.0 + u)

    def lam_star(u):
        # valid when constraint binds; clamp at 0
        return max(0.0, 2.0*(1.0 - u))

    u_frames = np.linspace(-0.5, 1.5, 61)

    x_plot = np.linspace(-0.5, 2.5, 500)
    f_plot = f0(x_plot)

    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    ax.set_title("Complementary slackness: λ*(u) drops to 0 when constraint becomes inactive")
    ax.set_xlabel("x")
    ax.set_ylabel("value")

    ax.plot(x_plot, f_plot, label="f0(x)=(x-2)^2")
    (boundary_line,) = ax.plot([1.0, 1.0], [-1, 10], linestyle="--", label="boundary x=1+u")
    (pt,) = ax.plot([1.0], [1.0], marker="o", linestyle="")
    txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")

    ax.set_ylim(-0.5, 6.5)
    ax.legend(loc="upper right")

    def update(i):
        u = float(u_frames[i])
        xb = 1.0 + u

        # move boundary
        boundary_line.set_data([xb, xb], [-0.5, 6.5])

        # optimal x, objective
        xs = x_star(u)
        pt.set_data([xs], [f0(xs)])

        # multiplier behavior
        lam = lam_star(u) if u < 1.0 else 0.0
        active = "ACTIVE" if u < 1.0 else "INACTIVE"

        txt.set_text(
            f"u = {u:.2f}   (constraint: x ≤ 1+u)\n"
            f"boundary: 1+u = {xb:.2f}\n"
            f"x*(u) = {xs:.3f}\n"
            f"λ*(u) = {lam:.3f}   ({active})\n"
            f"p(u) = {f0(xs):.3f}"
        )
        return boundary_line, pt, txt

    anim = FuncAnimation(fig, update, frames=len(u_frames), interval=90, blit=True)
    save_anim(anim, "duality_comp_slack_switch.gif")
    plt.close(fig)

# ------------------------------
# GIF 3: Farkas infeasibility certificate
# ------------------------------
def make_farkas_gif():
    # Infeasible system:
    #   x + y <= 0
    #   x + y >= 1
    #
    # Convert to A z <= b with z=(x,y):
    #   [ 1  1] z <=  0
    #   [-1 -1] z <= -1
    #
    # Farkas-style certificate:
    #   y = t*(1,1) >= 0
    #   y^T A = 0    (because (1,1) times rows sum to zero)
    #   y^T b = -t < 0 for t>0
    # => infeasible.

    t_frames = np.linspace(0.0, 2.0, 61)

    xv = np.linspace(-1.5, 1.5, 400)
    y_line1 = -xv        # x+y=0
    y_line2 = 1.0 - xv   # x+y=1

    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    ax.set_title("Farkas certificate: no (x,y) satisfies x+y≤0 and x+y≥1")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.plot(xv, y_line1, linestyle="--", label="boundary x+y=0")
    ax.plot(xv, y_line2, linestyle="--", label="boundary x+y=1")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.8)
    ax.legend(loc="lower left")

    txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")

    def update(i):
        t = float(t_frames[i])
        y = np.array([1.0, 1.0]) * t

        # A = [[1,1],[-1,-1]], b=[0,-1]
        # y^T A = y1*[1,1] + y2*[-1,-1] = (y1-y2)[1,1]
        yTA_coeff = y[0] - y[1]   # should be 0 since y1=y2
        yTb = -y[1]               # equals -t

        txt.set_text(
            "Write as A z ≤ b with z=(x,y):\n"
            "  [ 1  1] z ≤  0   (x+y ≤ 0)\n"
            "  [-1 -1] z ≤ -1   (x+y ≥ 1)\n\n"
            f"Certificate y = t·(1,1),  t={t:.2f}:\n"
            f"  y ≥ 0  ✓\n"
            f"  yᵀA = (y1-y2)[1,1],  y1-y2={yTA_coeff:.2f}  (0 here) ✓\n"
            f"  yᵀb = {yTb:.2f}  (negative for t>0) ⇒ infeasible ✓"
        )
        return (txt,)

    anim = FuncAnimation(fig, update, frames=len(t_frames), interval=90, blit=True)
    save_anim(anim, "duality_farkas_xy_infeasible.gif")
    plt.close(fig)

# ------------------------------
# GIF 4: Duality gap convergence
# ------------------------------
def make_gap_convergence_gif():
    # Uses the SAME primal-dual iteration rule as the saddle-path GIF:
    #   Primal: min (x-2)^2  s.t. x<=1
    #   Dual bound: g(λ)=λ-λ^2/4
    # Then plots sequences f0(x_k), g(λ_k), and gap=f0-g.

    def f0(x):
        return (x - 2.0)**2

    def g(lam):
        return lam - (lam**2)/4.0

    # Recreate the same iterates
    alpha = 0.25
    beta  = 0.35
    T = 50

    x = 2.4
    lam = 0.0
    xs = [x]
    lams = [lam]

    for _ in range(T):
        grad_x = 2.0*(x - 2.0) + lam
        x = x - alpha * grad_x
        x = min(x, 1.0)
        lam = max(0.0, lam + beta*(x - 1.0))
        xs.append(x)
        lams.append(lam)

    ks = np.arange(len(xs))
    f_vals = np.array([f0(v) for v in xs])
    g_vals = np.array([g(v) for v in lams])
    gap = f_vals - g_vals

    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    ax.set_title("Convergence: primal value f0(x_k), dual bound g(λ_k), and gap")
    ax.set_xlabel("iteration k")
    ax.set_ylabel("value")
    ax.set_xlim(0, len(xs)-1)

    ymin = min(g_vals.min(), f_vals.min()) - 0.5
    ymax = max(f_vals.max(), 1.2) + 0.5
    ax.set_ylim(ymin, ymax)

    (line_f,)   = ax.plot([], [], linewidth=2, label="primal value f0(x_k)")
    (line_g,)   = ax.plot([], [], linewidth=2, label="dual bound g(λ_k)")
    (line_gap,) = ax.plot([], [], linewidth=2, label="gap = f0 - g")
    ax.axhline(1.0, linestyle="--", label="p*=d*=1")

    txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
    ax.legend(loc="upper right")

    def update(i):
        line_f.set_data(ks[:i+1], f_vals[:i+1])
        line_g.set_data(ks[:i+1], g_vals[:i+1])
        line_gap.set_data(ks[:i+1], gap[:i+1])
        txt.set_text(
            f"k={i:02d}\n"
            f"x_k={xs[i]:.4f},  λ_k={lams[i]:.4f}\n"
            f"f0(x_k)={f_vals[i]:.4f}\n"
            f"g(λ_k)={g_vals[i]:.4f}\n"
            f"gap={gap[i]:.4f}"
        )
        return line_f, line_g, line_gap, txt

    anim = FuncAnimation(fig, update, frames=len(xs), interval=90, blit=True)
    save_anim(anim, "duality_gap_convergence.gif")
    plt.close(fig)

# ------------------------------
# GIF 5: Duality Lagrangian Demo
# ------------------------------
def make_lagrangian_demo_gif():
    # Primal: min (x-2)^2 s.t. x <= 1
    x = np.linspace(-1.0, 3.0, 600)
    f0 = (x - 2.0) ** 2

    lams = np.linspace(0.0, 4.0, 41)

    def g(lam):
        return lam - (lam**2)/4.0

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.set_title("Duality demo: L(x, λ) lower-bounds the constrained optimum (x ≤ 1)")
    ax.set_xlabel("x")
    ax.set_ylabel("value")

    (line_f0,) = ax.plot(x, f0, label="f0(x)=(x-2)^2")
    (line_L,)  = ax.plot(x, f0 + lams[0]*(x-1), label="L(x,λ)=f0(x)+λ(x-1)")
    ax.axvline(1.0, linestyle="--", label="constraint boundary x=1")

    # primal optimum
    ax.plot([1.0], [(1.0-2.0)**2], marker="o", linestyle="", label="primal optimum (x*=1,f*=1)")

    # minimizer of L for a given λ: x(λ)=2-λ/2
    point_star, = ax.plot([2.0], [0.0], marker="o", linestyle="")
    txt = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

    ax.set_ylim(-0.5, 7.0)
    ax.legend(loc="upper right")

    def update(i):
        lam = float(lams[i])
        L = (x - 2.0)**2 + lam*(x - 1.0)
        line_L.set_ydata(L)
        x_star = 2.0 - lam/2.0
        y_star = (x_star - 2.0)**2 + lam*(x_star - 1.0)
        point_star.set_data([x_star], [y_star])
        txt.set_text(f"λ={lam:.2f}\nargmin_x L=2-λ/2={x_star:.2f}\ng(λ)={g(lam):.3f}")
        return line_L, point_star, txt

    anim = FuncAnimation(fig, update, frames=len(lams), interval=80, blit=True)
    save_anim(anim, "duality_lagrangian_demo.gif")
    plt.close(fig)

# ------------------------------
# GIF 6: 2D KKT Geometry
# ------------------------------
def make_kkt_2d_gif():
    lam_frames = np.linspace(0.0, 2.0, 31)

    def g2(lam):
        return lam - 0.5*lam**2

    xx = np.linspace(-0.2, 1.6, 140)
    yy = np.linspace(-0.2, 1.6, 140)
    X, Y = np.meshgrid(xx, yy)
    F0 = X**2 + Y**2

    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    ax.set_title("2D KKT: argmin of L(x,y,λ) moves; hits boundary at λ*=1")
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_xlim(-0.2, 1.6); ax.set_ylim(-0.2, 1.6)

    ax.contour(X, Y, F0, levels=np.linspace(0.1, 2.0, 8))
    ax.plot([0, 1.8], [1, -0.8], linestyle="--", label="x+y=1")
    ax.plot([0.5], [0.5], marker="o", linestyle="", label="primal optimum (0.5,0.5)")
    pt, = ax.plot([0.0], [0.0], marker="o", linestyle="")
    txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
    ax.legend(loc="lower right")

    def update_kkt(i):
        lam = float(lam_frames[i])
        xs = lam/2.0; ys = lam/2.0
        pt.set_data([xs], [ys])
        txt.set_text(
            f"λ = {lam:.2f}\n"
            f"argmin L = (λ/2, λ/2)=({xs:.2f},{ys:.2f})\n"
            f"g(λ)=inf L = {g2(lam):.3f}\n"
            f"p* = 0.500"
        )
        return pt, txt

    anim1 = FuncAnimation(fig, update_kkt, frames=len(lam_frames), interval=90, blit=True)
    save_anim(anim1, "duality_kkt_2d_fast.gif")
    plt.close(fig)

# ------------------------------
# GIF 7: Sensitivity
# ------------------------------
def make_sensitivity_gif():
    u = np.linspace(-1.0, 2.0, 500)
    p_u = np.where(u <= 1.0, (1.0 - u)**2, 0.0)
    lam_frames2 = np.linspace(0.0, 4.0, 41)

    fig2, ax2 = plt.subplots(figsize=(6.6, 4.6))
    ax2.set_title("Sensitivity: p(u) and ℓ_λ(u)=1-λu (true λ*=2)")
    ax2.set_xlabel("u (relax constraint: x ≤ 1+u)")
    ax2.set_ylabel("p(u)")
    ax2.plot(u, p_u, label="p(u)")
    ax2.axvline(0.0, linestyle="--", label="u0=0")
    ax2.axvline(1.0, linestyle="--", label="kink u=1")
    lineL, = ax2.plot(u, 1.0 - lam_frames2[0]*u, label="ℓ_λ(u)=1-λu")
    txt2 = ax2.text(0.02, 0.98, "", transform=ax2.transAxes, va="top")
    ax2.set_ylim(-1.0, 3.2)
    ax2.legend(loc="upper right")

    def update_sens(i):
        lam = float(lam_frames2[i])
        lineL.set_ydata(1.0 - lam*u)
        txt2.set_text(f"λ = {lam:.2f}\nline: ℓ_λ(u)=1-λu\n(subgradient at u=0 is λ*=2)")
        return lineL, txt2

    anim2 = FuncAnimation(fig2, update_sens, frames=len(lam_frames2), interval=90, blit=True)
    save_anim(anim2, "duality_sensitivity_supporting_line_fast.gif")
    plt.close(fig2)

if __name__ == "__main__":
    make_saddle_path_gif()
    make_comp_slack_switch_gif()
    make_farkas_gif()
    make_gap_convergence_gif()
    make_lagrangian_demo_gif()
    make_kkt_2d_gif()
    make_sensitivity_gif()
