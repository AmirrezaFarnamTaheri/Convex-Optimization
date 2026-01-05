import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

# Common settings for "slow motion"
FPS = 8
INTERVAL = 120

print("Generating duality_lagrangian_demo.gif...")
# 1. Lagrangian Demo
# Primal: min (x-2)^2 s.t. x <= 1
x = np.linspace(-1.0, 3.0, 600)
f0 = (x - 2.0) ** 2
lams = np.linspace(0.0, 4.0, 61) # More frames for smoothness

def g(lam):
    return lam - (lam**2)/4.0

fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.set_title("Duality demo: L(x, λ) lower-bounds the constrained optimum (x ≤ 1)")
ax.set_xlabel("x")
ax.set_ylabel("value")

(line_f0,) = ax.plot(x, f0, label="f0(x)=(x-2)^2", color="blue", alpha=0.6)
(line_L,)  = ax.plot(x, f0 + lams[0]*(x-1), label="L(x,λ)=f0(x)+λ(x-1)", color="red")
ax.axvline(1.0, linestyle="--", color="black", label="constraint x=1")

# primal optimum
ax.plot([1.0], [(1.0-2.0)**2], marker="o", color="gold", linestyle="", label="primal optimum")

# minimizer of L
point_star, = ax.plot([], [], marker="o", color="red", linestyle="")
txt = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

ax.set_ylim(-0.5, 7.0)
ax.legend(loc="upper right")

def update_lag(i):
    lam = float(lams[i])
    L = (x - 2.0)**2 + lam*(x - 1.0)
    line_L.set_ydata(L)
    x_star = 2.0 - lam/2.0
    y_star = (x_star - 2.0)**2 + lam*(x_star - 1.0)
    point_star.set_data([x_star], [y_star])
    txt.set_text(f"λ={lam:.2f}\nargmin L = {x_star:.2f}\ng(λ)={g(lam):.3f}")
    return line_L, point_star, txt

anim = FuncAnimation(fig, update_lag, frames=len(lams), interval=INTERVAL, blit=True)
anim.save("assets/duality_lagrangian_demo.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)


print("Generating duality_saddle_path.gif...")
# 2. Saddle Path (Enhanced)
def f0_sp(x): return (x - 2.0)**2
def g_sp(lam): return lam - (lam**2)/4.0

x_grid = np.linspace(-0.5, 2.5, 220)
lam_grid = np.linspace(0.0, 4.0, 220)
X, Lam = np.meshgrid(x_grid, lam_grid)
L_grid = (X - 2.0)**2 + Lam*(X - 1.0)

# Iterates
alpha, beta = 0.2, 0.25 # Slower learning rate for smoother path
x_curr, lam_curr = 2.4, 0.0
xs, lams_list = [x_curr], [lam_curr]
for _ in range(60):
    grad_x = 2.0*(x_curr - 2.0) + lam_curr
    x_curr = min(x_curr - alpha * grad_x, 1.0) # Projection
    lam_curr = max(0.0, lam_curr + beta*(x_curr - 1.0))
    xs.append(x_curr); lams_list.append(lam_curr)

fig, ax = plt.subplots(figsize=(6.8, 5.0))
ax.set_title("Saddle-point dynamics: min_x max_λ L(x,λ)")
ax.set_xlabel("x (primal)"); ax.set_ylabel("λ (dual)")
ax.set_xlim(-0.5, 2.5); ax.set_ylim(0.0, 4.0)

cntr = ax.contour(X, Lam, L_grid, levels=20, cmap="viridis", alpha=0.5)
ax.axvline(1.0, linestyle="--", color="k", label="Feasible x≤1")
ax.plot([1.0], [2.0], marker="*", markersize=15, color="gold", label="Saddle (1, 2)")

(path_line,) = ax.plot([], [], 'r-', linewidth=2, label="Iterates")
(pt_now,) = ax.plot([], [], 'ro')
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.legend(loc="lower left")

def update_saddle(i):
    path_line.set_data(xs[:i+1], lams_list[:i+1])
    pt_now.set_data([xs[i]], [lams_list[i]])
    txt.set_text(f"Step {i}\nx={xs[i]:.2f}\nλ={lams_list[i]:.2f}")
    return path_line, pt_now, txt

anim = FuncAnimation(fig, update_saddle, frames=len(xs), interval=INTERVAL, blit=True)
anim.save("assets/duality_saddle_path.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)


print("Generating duality_gap_convergence.gif...")
# 3. Gap Convergence
ks = np.arange(len(xs))
f_vals = np.array([f0_sp(v) for v in xs])
g_vals = np.array([g_sp(v) for v in lams_list])
gap = f_vals - g_vals

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.set_title("Duality Gap Convergence")
ax.set_xlabel("Iteration")
ax.set_ylabel("Value")
ax.set_xlim(0, len(xs)-1)
ax.set_ylim(min(g_vals.min(), f_vals.min())-0.5, max(f_vals.max(), 1.2)+0.5)

(line_f,) = ax.plot([], [], 'b-', linewidth=2, label="Primal f0(x)")
(line_g,) = ax.plot([], [], 'r-', linewidth=2, label="Dual g(λ)")
(line_gap,) = ax.plot([], [], 'g--', linewidth=2, label="Gap")
ax.axhline(1.0, color='k', linestyle=':', label="Optimal=1")
txt = ax.text(0.5, 0.5, "", transform=ax.transAxes, ha="center")
ax.legend()

def update_gap(i):
    line_f.set_data(ks[:i+1], f_vals[:i+1])
    line_g.set_data(ks[:i+1], g_vals[:i+1])
    line_gap.set_data(ks[:i+1], gap[:i+1])
    txt.set_text(f"Gap: {gap[i]:.4f}")
    return line_f, line_g, line_gap, txt

anim = FuncAnimation(fig, update_gap, frames=len(ks), interval=INTERVAL, blit=True)
anim.save("assets/duality_gap_convergence.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)


print("Generating duality_kkt_2d_fast.gif...")
# 4. KKT 2D
lam_frames = np.linspace(0.0, 2.0, 41)
xx = np.linspace(-0.2, 1.6, 100)
yy = np.linspace(-0.2, 1.6, 100)
X, Y = np.meshgrid(xx, yy)
F0 = X**2 + Y**2

fig, ax = plt.subplots(figsize=(6.6, 4.8))
ax.set_title("KKT Stationarity: argmin L(x,λ) meets boundary")
ax.contour(X, Y, F0, levels=10, cmap="Blues")
ax.plot([0, 1.8], [1, -0.8], 'k--', label="x+y=1")
ax.plot([0.5], [0.5], 'g*', markersize=10, label="Optimum")
pt, = ax.plot([], [], 'ro', label="argmin L")
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.legend(loc="upper right")

def update_kkt(i):
    lam = lam_frames[i]
    xs = lam/2.0; ys = lam/2.0
    pt.set_data([xs], [ys])
    txt.set_text(f"λ={lam:.2f}\nargmin L=({xs:.2f},{ys:.2f})")
    return pt, txt

anim = FuncAnimation(fig, update_kkt, frames=len(lam_frames), interval=INTERVAL, blit=True)
anim.save("assets/duality_kkt_2d_fast.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)


print("Generating duality_comp_slack_switch.gif...")
# 5. Comp Slack
u_frames = np.linspace(-0.5, 1.5, 61)
x_plot = np.linspace(-0.5, 2.5, 500)
f_plot = (x_plot - 2.0)**2

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.set_title("Complementary Slackness: λ drops to 0 when inactive")
ax.plot(x_plot, f_plot, 'b-', label="f0(x)")
(bound_line,) = ax.plot([], [], 'k--', label="x <= 1+u")
(pt,) = ax.plot([], [], 'ro')
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.set_ylim(-0.5, 6.5)
ax.legend()

def update_cs(i):
    u = u_frames[i]
    xb = 1.0 + u
    bound_line.set_data([xb, xb], [-0.5, 6.5])
    xs = min(2.0, xb)
    pt.set_data([xs], [(xs-2)**2])
    lam = 2*(1-u) if u < 1 else 0
    state = "Active" if u < 1 else "Inactive"
    txt.set_text(f"u={u:.2f}\nλ*={lam:.2f} ({state})")
    return bound_line, pt, txt

anim = FuncAnimation(fig, update_cs, frames=len(u_frames), interval=INTERVAL, blit=True)
anim.save("assets/duality_comp_slack_switch.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)


print("Generating duality_sensitivity_supporting_line_fast.gif...")
# 6. Sensitivity
u = np.linspace(-1.0, 2.0, 500)
p_u = np.where(u <= 1.0, (1.0 - u)**2, 0.0)
lam_frames2 = np.linspace(0.0, 4.0, 41)

fig, ax = plt.subplots(figsize=(6.6, 4.6))
ax.set_title("Sensitivity: Dual variable is slope of p(u)")
ax.plot(u, p_u, 'b-', label="p(u)")
(lineL,) = ax.plot([], [], 'r--', label="Support")
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.set_ylim(-1.0, 3.5)
ax.legend()

def update_sens(i):
    lam = lam_frames2[i]
    lineL.set_data(u, 1.0 - lam*u)
    txt.set_text(f"λ={lam:.2f}\nSlope = -{lam:.2f}")
    return lineL, txt

anim = FuncAnimation(fig, update_sens, frames=len(lam_frames2), interval=INTERVAL, blit=True)
anim.save("assets/duality_sensitivity_supporting_line_fast.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)


print("Generating duality_farkas_xy_infeasible.gif...")
# 7. Farkas (Enhanced Visuals)
# System: x+y <= 0, x+y >= 1.
# Farkas vector y connects the two separated sets.
t_frames = np.linspace(0.0, 2.0, 61)
xv = np.linspace(-2, 2, 400)

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.set_title("Farkas Certificate: Separating Hyperplane Normal")
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
ax.set_xlabel("x"); ax.set_ylabel("y")

# Feasible regions (empty intersection)
# Region 1: x+y <= 0
ax.fill_between(xv, -2, -xv, color='blue', alpha=0.1, label="x+y <= 0")
ax.plot(xv, -xv, 'b--')
# Region 2: x+y >= 1
ax.fill_between(xv, 1-xv, 2, color='red', alpha=0.1, label="x+y >= 1")
ax.plot(xv, 1-xv, 'r--')

(vec,) = ax.plot([], [], 'k-', linewidth=2, marker='>')
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.legend(loc="lower right")

def update_farkas(i):
    t = t_frames[i]
    # The certificate vector y is normal to the hyperplanes
    # In this case y = (t, t).
    # It demonstrates the direction of contradiction.
    vec.set_data([0, t], [0, t])
    txt.set_text(f"Certificate y = ({t:.1f}, {t:.1f})\n Proves separation")
    return vec, txt

anim = FuncAnimation(fig, update_farkas, frames=len(t_frames), interval=INTERVAL, blit=True)
anim.save("assets/duality_farkas_xy_infeasible.gif", writer=PillowWriter(fps=FPS))
plt.close(fig)

print("All GIFs generated successfully.")
