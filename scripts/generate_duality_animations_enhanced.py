# -*- coding: utf-8 -*-
"""
Enhanced Duality Animations Generator
Fixes logical errors and improves visualizations for convex optimization duality concepts.
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

# Also save to topics folder for direct use
topics_dir = os.path.join(os.path.dirname(__file__), '..', 'topics', '09-duality', 'assets')
os.makedirs(topics_dir, exist_ok=True)

print("Generating enhanced duality animations...")
print("=" * 60)

# ==============================================================
# Animation 1: FIXED 2D KKT geometry
# ==============================================================
print("\n1. Generating duality_kkt_2d.gif (FIXED)...")
print("   Problem: min x^2 + y^2  s.t. x + y >= 1")
print("   Lagrangian: L = x^2 + y^2 + lam(1 - x - y)")
print("   Optimal: lam* = 1, (x*, y*) = (0.5, 0.5)")

# Key insight: lam ranges from 0 to lam* = 1
# At lam = 0: unconstrained min is (0,0), which violates x+y>=1
# At lam = 1: unconstrained min of L is (0.5, 0.5), exactly on constraint
# For lam > 1: dual value decreases, so we stop at lam* = 1

lam_frames = np.linspace(0.0, 1.5, 46)  # Go slightly beyond lam*=1 to show decline

def g2(lam):
    """Dual function: g(lam) = lam - lam^2/2"""
    return lam - 0.5 * lam**2

xx = np.linspace(-0.3, 1.8, 160)
yy = np.linspace(-0.3, 1.8, 160)
X, Y = np.meshgrid(xx, yy)
F0 = X**2 + Y**2

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: Geometry
ax = axes[0]
ax.set_title("2D KKT Geometry: argmin of L(x,y,lam)", fontsize=11)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(-0.3, 1.4)
ax.set_ylim(-0.3, 1.4)

# Contours of objective
contour = ax.contour(X, Y, F0, levels=np.linspace(0.1, 2.0, 10), colors='lightblue', alpha=0.7)
ax.clabel(contour, inline=True, fontsize=8, fmt='%.1f')

# Feasible region (x + y >= 1)
ax.fill_between(xx, 1 - xx, 2.0, alpha=0.15, color='green', label='Feasible: x+y >= 1')
ax.plot(xx, 1 - xx, 'g--', linewidth=2, label='Constraint: x+y = 1')

# Origin and optimum
ax.plot([0], [0], 'ko', markersize=8, label='Unconstrained min (0,0)')
ax.plot([0.5], [0.5], 'r*', markersize=15, label='Constrained opt (0.5, 0.5)')

# Moving point (argmin of Lagrangian)
pt, = ax.plot([0.0], [0.0], 'bo', markersize=10, zorder=5)

ax.legend(loc='upper right', fontsize=8)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Right plot: Dual function
ax2 = axes[1]
ax2.set_title("Dual Function g(lam) = lam - lam^2/2", fontsize=11)
ax2.set_xlabel("lam (dual variable)")
ax2.set_ylabel("g(lam)")

lam_plot = np.linspace(0, 2.0, 200)
g_plot = g2(lam_plot)
ax2.plot(lam_plot, g_plot, 'b-', linewidth=2, label='g(lam)')
ax2.axhline(0.5, color='red', linestyle=':', label='d* = p* = 0.5')
ax2.axvline(1.0, color='orange', linestyle=':', label='lam* = 1')
ax2.plot([1.0], [0.5], 'r*', markersize=15)

dual_pt, = ax2.plot([0], [0], 'bo', markersize=10)
ax2.legend(loc='lower right', fontsize=9)
ax2.set_xlim(-0.1, 2.1)
ax2.set_ylim(-0.3, 0.7)
ax2.grid(True, alpha=0.3)

# Text annotation
txt = fig.text(0.5, 0.02, "", ha='center', fontsize=10, 
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout(rect=[0, 0.08, 1, 1])

def update_kkt(i):
    lam = float(lam_frames[i])
    
    # Unconstrained minimizer of Lagrangian
    xs = lam / 2.0
    ys = lam / 2.0
    
    pt.set_data([xs], [ys])
    dual_pt.set_data([lam], [g2(lam)])
    
    # Check constraint satisfaction
    constraint_val = xs + ys
    
    # Status messages
    if lam < 0.99:
        status = "lam < lam*=1: Point VIOLATES constraint (x+y < 1)"
        color = 'blue'
    elif lam < 1.01:
        status = "lam = lam*: OPTIMAL! Point ON constraint"
        color = 'green'
    else:
        status = "lam > lam*: Dual DECREASING (past optimum)"
        color = 'red'
    
    txt.set_text(
        f"lam = {lam:.2f}  |  argmin L = ({xs:.2f}, {ys:.2f})  |  "
        f"x+y = {constraint_val:.2f}  |  g(lam) = {g2(lam):.3f}  |  {status}"
    )
    txt.set_color(color)
    
    return pt, dual_pt, txt

anim = FuncAnimation(fig, update_kkt, frames=len(lam_frames), interval=120, blit=True)
anim.save(os.path.join(output_dir, "duality_kkt_2d.gif"), writer=PillowWriter(fps=8))
anim.save(os.path.join(topics_dir, "duality_kkt_2d.gif"), writer=PillowWriter(fps=8))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 2: FIXED Farkas Infeasibility Certificate  
# ==============================================================
print("\n2. Generating duality_farkas_infeasible.gif (FIXED)...")
print("   System: x + y <= 0  AND  x + y >= 1  (INFEASIBLE)")
print("   Farkas certificate: y = [t, t] with t > 0")
print("   y^T A = [0, 0], y^T b = -t < 0")

t_frames = np.linspace(0.0, 2.0, 51)

xv = np.linspace(-2.0, 2.0, 400)
y_line1 = -xv        # x+y=0
y_line2 = 1.0 - xv   # x+y=1

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Geometric view
ax = axes[0]
ax.set_title("Farkas' Lemma: Infeasible System", fontsize=11)
ax.set_xlabel("x")
ax.set_ylabel("y")

# Region 1: x + y <= 0 (below the line y = -x)
ax.fill_between(xv, -2.5, y_line1, alpha=0.3, color='blue', label='x + y <= 0')
ax.plot(xv, y_line1, 'b-', linewidth=2)

# Region 2: x + y >= 1 (above the line y = 1 - x)
ax.fill_between(xv, y_line2, 2.5, alpha=0.3, color='red', label='x + y >= 1')
ax.plot(xv, y_line2, 'r-', linewidth=2)

# Gap region (infeasible)
ax.fill_between(xv, y_line1, y_line2, alpha=0.2, color='gray', 
                label='Gap: NO intersection!')

# Normal direction arrow (certificate direction)
arrow, = ax.plot([], [], 'g-', linewidth=3, label='Certificate direction')
arrow_head, = ax.plot([], [], 'g>', markersize=10)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.0)
ax.legend(loc='lower left', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# Right: Mathematical explanation
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title("Farkas' Lemma Certificate", fontsize=11)

# Static text box
math_text = ax2.text(0.5, 0.95, "", transform=ax2.transAxes, fontsize=10,
                     verticalalignment='top', fontfamily='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

def update_farkas(i):
    t = float(t_frames[i])
    
    # Certificate y = [t, t]
    y_cert = np.array([t, t])
    
    # A matrix and b vector
    # A = [[1, 1], [-1, -1]], b = [0, -1]
    A = np.array([[1, 1], [-1, -1]])
    b = np.array([0, -1])
    
    # Compute y^T A and y^T b
    yTA = y_cert @ A  # = [t-t, t-t] = [0, 0]
    yTb = y_cert @ b  # = t*0 + t*(-1) = -t
    
    # Draw arrow in normal direction [1,1] (pointing into gap)
    if t > 0.1:
        # Arrow from origin in direction [1,1], scaled by t
        scale = 0.3 * t
        arrow.set_data([0, scale], [0, scale])
        arrow_head.set_data([scale], [scale])
    else:
        arrow.set_data([], [])
        arrow_head.set_data([], [])
    
    # Mathematical explanation
    infeas_msg = "  => SYSTEM IS INFEASIBLE!" if t > 0.1 else ""
    math_text.set_text(
        f"Write system as Az <= b with z = (x, y):\n"
        f"-------------------------------------------\n"
        f"  Row 1: [ 1,  1] z <=  0   (x + y <= 0)\n"
        f"  Row 2: [-1, -1] z <= -1   (x + y >= 1)\n\n"
        f"         [ 1   1]         [ 0]\n"
        f"  A  =   [-1  -1],   b =  [-1]\n\n"
        f"===========================================\n"
        f"FARKAS CERTIFICATE: y = [{t:.2f}, {t:.2f}]\n"
        f"===========================================\n\n"
        f"  [OK] y >= 0:  [{t:.2f}, {t:.2f}] >= 0\n\n"
        f"  [OK] y'A = [{t:.2f}, {t:.2f}] @ A = [{yTA[0]:.2f}, {yTA[1]:.2f}]\n"
        f"         = [0, 0]  (rows cancel!)\n\n"
        f"  [OK] y'b = [{t:.2f}, {t:.2f}] @ [0, -1]' = {yTb:.2f}\n"
        f"         = {yTb:.2f} < 0  for t > 0\n\n"
        f"{infeas_msg}"
    )
    
    return arrow, arrow_head, math_text

anim = FuncAnimation(fig, update_farkas, frames=len(t_frames), interval=100, blit=True)
plt.tight_layout()
anim.save(os.path.join(output_dir, "duality_farkas_infeasible.gif"), writer=PillowWriter(fps=10))
anim.save(os.path.join(topics_dir, "duality_farkas_infeasible.gif"), writer=PillowWriter(fps=10))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 3: Enhanced Saddle-Point Path with Arrows
# ==============================================================
print("\n3. Generating duality_saddle_path.gif (ENHANCED)...")
print("   Problem: min (x-2)^2  s.t. x <= 1")
print("   Saddle point: (x*, lam*) = (1, 2)")

def f0_saddle(x):
    return (x - 2.0)**2

def g_saddle(lam):
    return lam - (lam**2) / 4.0

# Grid for contouring L(x,lam) = (x-2)^2 + lam(x-1)
x_grid = np.linspace(-0.5, 2.8, 250)
lam_grid = np.linspace(-0.3, 4.5, 250)
X_s, Lam_s = np.meshgrid(x_grid, lam_grid)
L_grid = (X_s - 2.0)**2 + Lam_s * (X_s - 1.0)

# Improved primal-dual iterations with momentum
alpha = 0.18
beta = 0.25
T = 60

x_iter = 2.5
lam_iter = 0.1
xs_list = [x_iter]
lams_list = [lam_iter]

for _ in range(T):
    # Primal: gradient descent on x
    grad_x = 2.0 * (x_iter - 2.0) + lam_iter
    x_new = x_iter - alpha * grad_x
    x_new = min(x_new, 1.0)  # Project to feasible
    
    # Dual: gradient ascent on lam  
    grad_lam = x_new - 1.0  # dL/dlam = x - 1
    lam_new = max(0.0, lam_iter + beta * grad_lam)
    
    x_iter = x_new
    lam_iter = lam_new
    xs_list.append(x_iter)
    lams_list.append(lam_iter)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Saddle surface with path
ax = axes[0]
ax.set_title("Saddle-Point Dynamics: L(x,lam) = (x-2)^2 + lam(x-1)", fontsize=10)
ax.set_xlabel("x (primal)")
ax.set_ylabel("lam (dual)")
ax.set_xlim(x_grid.min(), x_grid.max())
ax.set_ylim(lam_grid.min(), lam_grid.max())

# Contours with better coloring
levels = np.linspace(-2, 6, 20)
contour = ax.contourf(X_s, Lam_s, L_grid, levels=levels, cmap='RdYlBu_r', alpha=0.7)
plt.colorbar(contour, ax=ax, label='L(x,lam)')
ax.contour(X_s, Lam_s, L_grid, levels=levels, colors='gray', alpha=0.3, linewidths=0.5)

# Constraint and saddle point
ax.axvline(1.0, color='green', linestyle='--', linewidth=2, label='Constraint x=1')
ax.plot([1.0], [2.0], 'w*', markersize=20, markeredgecolor='black', label='Saddle (1, 2)')

# Path with arrows
path_line, = ax.plot([], [], 'b-', linewidth=2, alpha=0.8, label='Iterates')
pt_now, = ax.plot([], [], 'ro', markersize=10, zorder=5)
ax.legend(loc='lower left', fontsize=8)

# Right: Convergence plots
ax2 = axes[1]
ax2.set_title("Primal-Dual Convergence", fontsize=10)
ax2.set_xlabel("Iteration k")

primal_line, = ax2.plot([], [], 'b-', linewidth=2, label='x_k (primal)')
dual_line, = ax2.plot([], [], 'r-', linewidth=2, label='lam_k (dual)')
ax2.axhline(1.0, color='blue', linestyle=':', alpha=0.5, label='x* = 1')
ax2.axhline(2.0, color='red', linestyle=':', alpha=0.5, label='lam* = 2')
ax2.set_xlim(0, T)
ax2.set_ylim(-0.5, 3.5)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

txt = fig.text(0.5, 0.02, "", ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout(rect=[0, 0.08, 1, 1])

def update_saddle(i):
    # Path up to current point
    path_line.set_data(xs_list[:i+1], lams_list[:i+1])
    pt_now.set_data([xs_list[i]], [lams_list[i]])
    
    # Convergence lines
    primal_line.set_data(range(i+1), xs_list[:i+1])
    dual_line.set_data(range(i+1), lams_list[:i+1])
    
    # Gap calculation
    primal_val = f0_saddle(xs_list[i])
    dual_val = g_saddle(lams_list[i])
    gap = primal_val - dual_val
    
    txt.set_text(
        f"iter k={i:02d}  |  x_k={xs_list[i]:.4f}  |  lam_k={lams_list[i]:.4f}  |  "
        f"f0(x_k)={primal_val:.4f}  |  g(lam_k)={dual_val:.4f}  |  Gap={gap:.4f}"
    )
    
    return path_line, pt_now, primal_line, dual_line, txt

anim = FuncAnimation(fig, update_saddle, frames=len(xs_list), interval=80, blit=True)
anim.save(os.path.join(output_dir, "duality_saddle_path.gif"), writer=PillowWriter(fps=12))
anim.save(os.path.join(topics_dir, "duality_saddle_path.gif"), writer=PillowWriter(fps=12))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 4: Enhanced Duality Gap Convergence with Shading
# ==============================================================
print("\n4. Generating duality_gap_convergence.gif (ENHANCED)...")
print("   Showing gap shading and convergence to p* = d* = 1")

def f0(x):
    return (x - 2.0)**2

def g(lam):
    return lam - (lam**2) / 4.0

# Reuse iterations from saddle path
primal_values = [f0(val) for val in xs_list]
dual_values = [g(val) for val in lams_list]
gaps = [p - d for p, d in zip(primal_values, dual_values)]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Value convergence with gap shading
ax = axes[0]
ax.set_title("Duality Gap Convergence", fontsize=11)
ax.set_xlabel("Iteration k")
ax.set_ylabel("Value")
ax.set_xlim(0, T)
ax.set_ylim(-0.3, 2.5)

# Optimal value line
ax.axhline(1.0, color='gray', linestyle=':', linewidth=2, label='p* = d* = 1')

# Fill between (gap region) - will be updated
gap_fill = ax.fill_between([], [], [], alpha=0.3, color='green', label='Duality Gap')

line_primal, = ax.plot([], [], 'b-', linewidth=2.5, label='f0(x_k) (Primal)')
line_dual, = ax.plot([], [], 'r-', linewidth=2.5, label='g(lam_k) (Dual)')

ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)

# Right: Gap vs iteration (log scale option)
ax2 = axes[1]
ax2.set_title("Duality Gap: f0(x_k) - g(lam_k)", fontsize=11)
ax2.set_xlabel("Iteration k")
ax2.set_ylabel("Gap")
ax2.set_xlim(0, T)
ax2.set_ylim(-0.1, max(gaps) * 1.1)

line_gap, = ax2.plot([], [], 'g-', linewidth=2.5, label='Gap')
ax2.axhline(0, color='gray', linestyle=':', label='Zero gap (strong duality)')
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

txt = fig.text(0.5, 0.02, "", ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

plt.tight_layout(rect=[0, 0.08, 1, 1])

def update_gap(i):
    global gap_fill
    
    iters = list(range(i+1))
    
    line_primal.set_data(iters, primal_values[:i+1])
    line_dual.set_data(iters, dual_values[:i+1])
    line_gap.set_data(iters, gaps[:i+1])
    
    # Update gap fill region
    gap_fill.remove()
    gap_fill = axes[0].fill_between(iters, dual_values[:i+1], primal_values[:i+1], 
                                     alpha=0.3, color='green')
    
    # Status text
    txt.set_text(
        f"Iteration k = {i}  |  "
        f"f0(x_k) = {primal_values[i]:.4f}  |  "
        f"g(lam_k) = {dual_values[i]:.4f}  |  "
        f"Gap = {gaps[i]:.4f}  |  "
        f"Relative Gap = {gaps[i]/max(1e-8, primal_values[i])*100:.2f}%"
    )
    
    return line_primal, line_dual, line_gap, gap_fill, txt

anim = FuncAnimation(fig, update_gap, frames=len(xs_list), interval=80, blit=False)
anim.save(os.path.join(output_dir, "duality_gap_convergence.gif"), writer=PillowWriter(fps=12))
anim.save(os.path.join(topics_dir, "duality_gap_convergence.gif"), writer=PillowWriter(fps=12))
plt.close(fig)
print("   Done!")

# ==============================================================
# Animation 5: Enhanced Lower Envelope (bonus)
# ==============================================================
print("\n5. Generating duality_lower_envelope.gif (ENHANCED)...")

x = np.linspace(-0.5, 3.5, 500)
f0_env = (x - 2.0)**2

lams_env = np.linspace(0.0, 4.0, 21)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: x-space view
ax = axes[0]
ax.set_title("Lagrangian L(x,lam) = (x-2)^2 + lam(x-1)", fontsize=10)
ax.set_xlabel("x")
ax.set_ylabel("value")

ax.plot(x, f0_env, 'k-', linewidth=3, label="f0(x) = (x-2)^2")
ax.axvline(1.0, linestyle='--', color='green', linewidth=2, label="Constraint x = 1")

# Lines for each lambda (will fade in)
L_lines = []
for lam in lams_env:
    L = (x - 2.0)**2 + lam * (x - 1.0)
    line, = ax.plot(x, L, alpha=0.0, linewidth=1, color='blue')
    L_lines.append(line)

# Minimum points
min_pts, = ax.plot([], [], 'ro', markersize=8, label='Minima (envelope)')
active_line, = ax.plot([], [], 'r-', linewidth=2, alpha=0.8)

ax.set_ylim(-1.5, 8)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)

# Right: lam-space (dual function)
ax2 = axes[1]
ax2.set_title("Dual Function g(lam) = lam - lam^2/4", fontsize=10)
ax2.set_xlabel("lam")
ax2.set_ylabel("g(lam)")

lam_plot = np.linspace(0, 4.5, 200)
g_plot = lam_plot - (lam_plot**2) / 4.0
ax2.plot(lam_plot, g_plot, 'b-', linewidth=3, label='g(lam)')
ax2.axhline(1.0, color='red', linestyle=':', label='max g(lam) = d* = 1')
ax2.axvline(2.0, color='orange', linestyle=':', label='lam* = 2')
ax2.plot([2.0], [1.0], 'r*', markersize=15)

dual_trace, = ax2.plot([], [], 'ro', markersize=6)
ax2.legend(loc='lower left', fontsize=9)
ax2.set_xlim(-0.2, 4.5)
ax2.set_ylim(-1.5, 1.5)
ax2.grid(True, alpha=0.3)

txt = fig.text(0.5, 0.02, "", ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

plt.tight_layout(rect=[0, 0.08, 1, 1])

def update_env(i):
    idx = min(i, len(lams_env) - 1)
    
    # Fade in Lagrangian lines
    for j, line in enumerate(L_lines):
        if j <= idx:
            alpha = 0.3 + 0.4 * (j == idx)  # Current line brighter
            line.set_alpha(alpha)
    
    # Collect all minima up to current frame
    min_x_list = []
    min_y_list = []
    dual_lam_list = []
    dual_g_list = []
    
    for j in range(idx + 1):
        lam = lams_env[j]
        x_min = 2.0 - lam / 2.0
        g_val = lam - (lam**2) / 4.0
        min_x_list.append(x_min)
        min_y_list.append(g_val)
        dual_lam_list.append(lam)
        dual_g_list.append(g_val)
    
    min_pts.set_data(min_x_list, min_y_list)
    
    # Draw envelope curve through points
    if len(min_x_list) > 1:
        active_line.set_data(min_x_list, min_y_list)
    
    dual_trace.set_data(dual_lam_list, dual_g_list)
    
    lam = lams_env[idx]
    txt.set_text(
        f"lam = {lam:.2f}  |  "
        f"argmin_x L(x,lam) = 2 - lam/2 = {2.0 - lam/2.0:.2f}  |  "
        f"g(lam) = inf_x L(x,lam) = {lam - (lam**2)/4.0:.3f}"
    )
    
    return tuple(L_lines) + (min_pts, active_line, dual_trace, txt)

anim = FuncAnimation(fig, update_env, frames=len(lams_env) + 10, interval=150, blit=True)
anim.save(os.path.join(output_dir, "duality_lower_envelope.gif"), writer=PillowWriter(fps=6))
anim.save(os.path.join(topics_dir, "duality_lower_envelope.gif"), writer=PillowWriter(fps=6))
plt.close(fig)
print("   Done!")

print("\n" + "=" * 60)
print(f"All enhanced animations saved to:")
print(f"  1. {output_dir}")
print(f"  2. {topics_dir}")
print("=" * 60)
print("\nEnhanced animation generation complete!")
