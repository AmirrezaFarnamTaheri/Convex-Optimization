"""
Duality Animations Generator
Generates educational GIF animations for convex optimization duality concepts.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Ensure output directory exists
output_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'assets', 'topics', 'duality')
os.makedirs(output_dir, exist_ok=True)

print("Generating duality animations...")

# ==============================================================
# Animation 1: Lagrangian Demo
# ==============================================================
print("1. Generating duality_lagrangian_demo.gif...")

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

(line_f0,) = ax.plot(x, f0, label="f0(x)=(x-2)²")
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
anim.save(os.path.join(output_dir, "duality_lagrangian_demo.gif"), writer=PillowWriter(fps=12))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 2: 2D KKT geometry
# ==============================================================
print("2. Generating duality_kkt_2d.gif...")

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
anim1.save(os.path.join(output_dir, "duality_kkt_2d.gif"), writer=PillowWriter(fps=10))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 3: Sensitivity / supporting line
# ==============================================================
print("3. Generating duality_sensitivity.gif...")

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
anim2.save(os.path.join(output_dir, "duality_sensitivity.gif"), writer=PillowWriter(fps=10))
plt.close(fig2)
print("   Done!")

# ==============================================================
# Animation 4: Saddle-point path
# ==============================================================
print("4. Generating duality_saddle_path.gif...")

def f0_saddle(x):
    return (x - 2.0)**2

def g_saddle(lam):
    return lam - (lam**2)/4.0

# Grid for contouring L(x,λ)
x_grid = np.linspace(-0.5, 2.5, 220)
lam_grid = np.linspace(0.0, 4.0, 220)
X_s, Lam_s = np.meshgrid(x_grid, lam_grid)
L_grid = (X_s - 2.0)**2 + Lam_s*(X_s - 1.0)

# Simple projected primal-dual iterations
alpha = 0.25
beta = 0.35
T = 50

x_iter = 2.4
lam_iter = 0.0
xs_list = [x_iter]
lams_list = [lam_iter]

for _ in range(T):
    grad_x = 2.0*(x_iter - 2.0) + lam_iter
    x_iter = x_iter - alpha * grad_x
    x_iter = min(x_iter, 1.0)
    lam_iter = max(0.0, lam_iter + beta*(x_iter - 1.0))
    xs_list.append(x_iter)
    lams_list.append(lam_iter)

fig, ax = plt.subplots(figsize=(6.8, 5.0))
ax.set_title("Saddle-point view: L(x,λ) contours + primal-dual path")
ax.set_xlabel("x")
ax.set_ylabel("λ")
ax.set_xlim(x_grid.min(), x_grid.max())
ax.set_ylim(lam_grid.min(), lam_grid.max())

levels = np.linspace(np.percentile(L_grid, 5), np.percentile(L_grid, 95), 14)
ax.contour(X_s, Lam_s, L_grid, levels=levels)

ax.axvline(1.0, linestyle="--", label="constraint x=1")
ax.plot([1.0], [2.0], marker="o", linestyle="", label="saddle (x*=1, λ*=2)")

(path_line,) = ax.plot([], [], linewidth=2, label="iterates")
(pt_now,) = ax.plot([], [], marker="o", linestyle="")
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.legend(loc="lower left")

def update_saddle(i):
    path_line.set_data(xs_list[:i+1], lams_list[:i+1])
    pt_now.set_data([xs_list[i]], [lams_list[i]])
    txt.set_text(
        f"iter k={i:02d}\n"
        f"x_k={xs_list[i]:.4f}\n"
        f"λ_k={lams_list[i]:.4f}\n"
        f"f0(x_k)={f0_saddle(xs_list[i]):.4f}\n"
        f"g(λ_k)={g_saddle(lams_list[i]):.4f}"
    )
    return path_line, pt_now, txt

anim = FuncAnimation(fig, update_saddle, frames=len(xs_list), interval=90, blit=True)
anim.save(os.path.join(output_dir, "duality_saddle_path.gif"), writer=PillowWriter(fps=10))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 5: Complementary slackness switch
# ==============================================================
print("5. Generating duality_comp_slack.gif...")

def f0_comp(x):
    return (x - 2.0)**2

def x_star_comp(u):
    return min(2.0, 1.0 + u)

def lam_star_comp(u):
    return max(0.0, 2.0*(1.0 - u))

u_frames_comp = np.linspace(-0.5, 1.5, 61)

x_plot_comp = np.linspace(-0.5, 2.5, 500)
f_plot_comp = f0_comp(x_plot_comp)

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.set_title("Complementary slackness: λ*(u) drops to 0 when constraint inactive")
ax.set_xlabel("x")
ax.set_ylabel("value")

ax.plot(x_plot_comp, f_plot_comp, label="f0(x)=(x-2)²")
(boundary_line,) = ax.plot([1.0, 1.0], [-1, 10], linestyle="--", label="boundary x=1+u")
(pt,) = ax.plot([1.0], [1.0], marker="o", linestyle="")
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")

ax.set_ylim(-0.5, 6.5)
ax.legend(loc="upper right")

def update_comp(i):
    u = float(u_frames_comp[i])
    xb = 1.0 + u
    boundary_line.set_data([xb, xb], [-0.5, 6.5])
    xs = x_star_comp(u)
    pt.set_data([xs], [f0_comp(xs)])
    lam = lam_star_comp(u) if u < 1.0 else 0.0
    active = "ACTIVE" if u < 1.0 else "INACTIVE"
    txt.set_text(
        f"u = {u:.2f}   (constraint: x ≤ 1+u)\n"
        f"boundary: 1+u = {xb:.2f}\n"
        f"x*(u) = {xs:.3f}\n"
        f"λ*(u) = {lam:.3f}   ({active})\n"
        f"p(u) = {f0_comp(xs):.3f}"
    )
    return boundary_line, pt, txt

anim = FuncAnimation(fig, update_comp, frames=len(u_frames_comp), interval=90, blit=True)
anim.save(os.path.join(output_dir, "duality_comp_slack.gif"), writer=PillowWriter(fps=10))
plt.close(fig)
print("   Done!")

print(f"\nAll animations saved to: {output_dir}")
print("Animation generation complete!")

