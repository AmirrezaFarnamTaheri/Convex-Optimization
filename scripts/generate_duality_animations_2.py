"""
Duality Animations Generator - Part 2
Additional animations for convex optimization duality concepts.
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

print("Generating additional duality animations...")

# ==============================================================
# Animation 6: Farkas infeasibility certificate
# ==============================================================
print("6. Generating duality_farkas_infeasible.gif...")

t_frames = np.linspace(0.0, 2.0, 61)

xv = np.linspace(-1.5, 1.5, 400)
y_line1 = -xv        # x+y=0
y_line2 = 1.0 - xv   # x+y=1

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.set_title("Farkas certificate: no (x,y) satisfies x+y≤0 and x+y≥1")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.fill_between(xv, -1.5, y_line1, alpha=0.2, color='blue', label='x+y ≤ 0')
ax.fill_between(xv, y_line2, 1.8, alpha=0.2, color='red', label='x+y ≥ 1')
ax.plot(xv, y_line1, linestyle="--", color='blue')
ax.plot(xv, y_line2, linestyle="--", color='red')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.8)
ax.legend(loc="lower left")

txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top", fontsize=9)

def update(i):
    t = float(t_frames[i])
    y = np.array([1.0, 1.0]) * t
    yTA_coeff = y[0] - y[1]
    yTb = -y[1]

    txt.set_text(
        "Write as A z ≤ b with z=(x,y):\n"
        "  [ 1  1] z ≤  0   (x+y ≤ 0)\n"
        "  [-1 -1] z ≤ -1   (x+y ≥ 1)\n\n"
        f"Certificate y = t·(1,1),  t={t:.2f}:\n"
        f"  y ≥ 0  ✓\n"
        f"  yᵀA = (y₁-y₂)[1,1],  y₁-y₂={yTA_coeff:.2f}  ✓\n"
        f"  yᵀb = {yTb:.2f}  (negative for t>0) ⇒ infeasible"
    )
    return (txt,)

anim = FuncAnimation(fig, update, frames=len(t_frames), interval=90, blit=True)
anim.save(os.path.join(output_dir, "duality_farkas_infeasible.gif"), writer=PillowWriter(fps=10))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 7: Duality gap convergence
# ==============================================================
print("7. Generating duality_gap_convergence.gif...")

def f0(x):
    return (x - 2.0)**2

def g(lam):
    return lam - (lam**2)/4.0

# Primal-dual iterations
alpha = 0.25
beta = 0.35
T = 50

x_iter = 2.4
lam_iter = 0.0
xs = [x_iter]
lams = [lam_iter]

for _ in range(T):
    grad_x = 2.0*(x_iter - 2.0) + lam_iter
    x_iter = x_iter - alpha * grad_x
    x_iter = min(x_iter, 1.0)
    lam_iter = max(0.0, lam_iter + beta*(x_iter - 1.0))
    xs.append(x_iter)
    lams.append(lam_iter)

primal_values = [f0(val) for val in xs]
dual_values = [g(val) for val in lams]
gaps = [p - d for p, d in zip(primal_values, dual_values)]

fig, ax = plt.subplots(figsize=(6.8, 4.8))
ax.set_title("Duality Gap Convergence: Primal Value vs Dual Bound")
ax.set_xlabel("Iteration k")
ax.set_ylabel("Value")
ax.set_xlim(0, T)
ax.set_ylim(-0.5, 6.0)

(line_primal,) = ax.plot([], [], label="f₀(xₖ) (Primal Value)", color="blue", linewidth=2)
(line_dual,) = ax.plot([], [], label="g(λₖ) (Dual Bound)", color="red", linewidth=2)
(line_gap,) = ax.plot([], [], label="Gap (f₀-g)", color="green", linestyle="--", linewidth=2)
ax.axhline(1.0, color="gray", linestyle=":", label="p*=d*=1")
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")
ax.legend(loc="upper right")

def update_gap(i):
    line_primal.set_data(range(i+1), primal_values[:i+1])
    line_dual.set_data(range(i+1), dual_values[:i+1])
    line_gap.set_data(range(i+1), gaps[:i+1])
    txt.set_text(
        f"iter k={i:02d}\n"
        f"f₀(xₖ)={primal_values[i]:.4f}\n"
        f"g(λₖ)={dual_values[i]:.4f}\n"
        f"Gap={gaps[i]:.4f}"
    )
    return line_primal, line_dual, line_gap, txt

anim = FuncAnimation(fig, update_gap, frames=len(xs), interval=90, blit=True)
anim.save(os.path.join(output_dir, "duality_gap_convergence.gif"), writer=PillowWriter(fps=10))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 8: Lower envelope
# ==============================================================
print("8. Generating duality_lower_envelope.gif...")

x = np.linspace(-1.0, 3.0, 400)
f0 = (x - 2.0)**2

lams_env = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

fig, ax = plt.subplots(figsize=(7.0, 4.8))
ax.set_title("The dual function g(λ) = infₓ L(x,λ) is the lower envelope")
ax.set_xlabel("x")
ax.set_ylabel("value")

ax.plot(x, f0, 'k-', linewidth=2, label="f₀(x)=(x-2)²")
ax.axvline(1.0, linestyle="--", color='gray', label="constraint x=1")

# Create lines for each lambda
lines = []
for lam in lams_env:
    L = (x - 2.0)**2 + lam*(x - 1.0)
    line, = ax.plot(x, L, alpha=0.3, linewidth=1)
    lines.append(line)

(envelope_line,) = ax.plot([], [], 'r-', linewidth=2, label="g(λ) envelope")
txt = ax.text(0.02, 0.98, "", transform=ax.transAxes, va="top")

ax.set_ylim(-0.5, 7.0)
ax.legend(loc="upper right")

# Compute envelope
envelope_x = np.linspace(-0.5, 3.0, 100)
envelope_lams = np.linspace(0.0, 4.0, 100)
envelope_vals = []
for lam in envelope_lams:
    g_val = lam - (lam**2)/4.0
    envelope_vals.append(g_val)

def update_env(i):
    for j, line in enumerate(lines):
        if j <= i:
            line.set_alpha(0.6)
        else:
            line.set_alpha(0.1)
    
    # Show envelope up to current
    env_x = []
    env_y = []
    for j in range(min(i+1, len(lams_env))):
        lam = lams_env[j]
        x_min = 2.0 - lam/2.0
        g_val = lam - (lam**2)/4.0
        env_x.append(x_min)
        env_y.append(g_val)
    
    if env_x:
        envelope_line.set_data(env_x, env_y)
    
    if i < len(lams_env):
        lam = lams_env[i]
        txt.set_text(f"λ = {lam:.1f}\nargmin L = {2.0-lam/2.0:.2f}\ng(λ) = {lam - (lam**2)/4.0:.3f}")
    
    return tuple(lines) + (envelope_line, txt)

frames = len(lams_env) + 10  # Extra frames to show final state
anim = FuncAnimation(fig, update_env, frames=frames, interval=200, blit=True)
anim.save(os.path.join(output_dir, "duality_lower_envelope.gif"), writer=PillowWriter(fps=5))
plt.close(fig)
print("   Done!")

print(f"\nAll additional animations saved to: {output_dir}")
print("Animation generation complete!")

