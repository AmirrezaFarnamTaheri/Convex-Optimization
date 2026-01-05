import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ------------------------------
# GIF 1: 2D KKT geometry
# Primal: min x^2+y^2  s.t. x+y >= 1   (equiv f1=1-x-y<=0)
# L(x,y,λ)=x^2+y^2 + λ(1-x-y), λ>=0
# argmin: (λ/2, λ/2)
# g(λ)=λ-λ^2/2, max at λ*=1 with value 1/2
# ------------------------------
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
anim1.save("topics/09-duality/assets/duality_kkt_2d_fast.gif", writer=PillowWriter(fps=10))
plt.close(fig)

# ------------------------------
# GIF 2: Sensitivity / supporting line
# p(u)=min (x-2)^2 s.t. x<=1+u
# p(u)=(1-u)^2 for u<=1, else 0
# supporting line: ℓ_λ(u)=1-λu; true λ*=2
# ------------------------------
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
anim2.save("topics/09-duality/assets/duality_sensitivity_supporting_line_fast.gif", writer=PillowWriter(fps=10))
plt.close(fig2)

# ------------------------------
# GIF 3: Farkas Certificate (Redesigned)
# Infeasible System: x+y <= 0 AND x+y >= 1
# Certificate: y_vec >= 0 s.t. A^T y = 0, b^T y < 0.
# A = [[1, 1], [-1, -1]], b = [0, -1]
# Cert y = [1, 1] -> A^T y = [0, 0], b^T y = -1 < 0.
# Animation: Rotate a vector 'v' and check if it separates the sets or certifies infeasibility.
# Actually, let's visualize the "Theorem of Alternatives" geometry.
# The set {Ax | x} is a subspace (line x=y). The set {z | z <= b} is a shifted quadrant.
# They don't intersect. The certificate is the separating hyperplane normal.
# ------------------------------

fig3, ax3 = plt.subplots(figsize=(6.0, 5.0))
ax3.set_title("Farkas' Lemma: Separating Hyperplane Certificate")
ax3.set_xlim(-2, 2)
ax3.set_ylim(-2, 2)
ax3.grid(True, alpha=0.3)

# Draw the two conflicting halfspaces in primal space (x, y)
# 1. x + y <= 0
x_vals = np.linspace(-2, 2, 100)
ax3.fill_between(x_vals, -2, -x_vals, color='blue', alpha=0.1, label="x+y <= 0")
# 2. x + y >= 1  =>  -x - y <= -1
ax3.fill_between(x_vals, 1-x_vals, 2, color='red', alpha=0.1, label="x+y >= 1")

# Draw the separating hyperplane (certificate)
# Normal vector c = (1, 1).
# We want to show a vector 'y' that proves disjointness.
# In Farkas for Ax <= b, the cert y >= 0 proves b^T y < 0 while A^T y = 0.
# Here, primal x is unconstrained sign? No, standard Farkas is usually x >= 0 or Ax=b.
# Let's stick to the specific constraints visual:
# The gap is between the lines x+y=0 and x+y=1.
# A separating line is x+y = 0.5.
line_sep, = ax3.plot(x_vals, 0.5 - x_vals, 'k--', linewidth=2, label="Separator")

txt3 = ax3.text(0.02, 0.95, "", transform=ax3.transAxes, va="top", fontsize=10)
# No real animation needed for the static geometry, but let's rotate the normal to show ONLY (1,1) works.

angles = np.linspace(0, 2*np.pi, 60)

# Use a line for the animating vector
vec_line, = ax3.plot([], [], 'g-', linewidth=2)

def update_farkas_safe(i):
    angle = angles[i]
    dx = np.cos(angle)
    dy = np.sin(angle)

    is_separating = abs(angle - np.pi/4) < 0.2

    # Update vector line from (0,0.5) to (dx, dy) scaled
    vec_line.set_data([0, dx], [0.5, 0.5+dy])
    vec_line.set_color('green' if is_separating else 'gray')

    txt3.set_text(f"Normal direction: {np.degrees(angle):.0f}°\n" +
                  ("CERTIFICATE FOUND (y >= 0, separates)" if is_separating else "Invalid direction"))

    return txt3, vec_line

anim3 = FuncAnimation(fig3, update_farkas_safe, frames=len(angles), interval=50, blit=True)
anim3.save("topics/09-duality/assets/duality_farkas_xy_infeasible.gif", writer=PillowWriter(fps=15))
plt.close(fig3)


# ------------------------------
# GIF 4: Saddle Point Path (Enhanced)
# Primal: min (x-1)^2 s.t. x <= 0. (Optimum x*=0, p*=1)
# Lagrangian L(x,λ) = (x-1)^2 + λx.
# Saddle point at x*=0, λ*=2.
# ------------------------------
x_min, x_max = -1.5, 1.5
lam_min, lam_max = 0, 4
X_grid, Lam_grid = np.meshgrid(np.linspace(x_min, x_max, 50), np.linspace(lam_min, lam_max, 50))
L_grid = (X_grid - 1)**2 + Lam_grid * X_grid

fig4, ax4 = plt.subplots(figsize=(6, 5))
ax4.set_title("Primal-Dual Dynamics -> Saddle Point (0, 2)")
ax4.set_xlabel("Primal x")
ax4.set_ylabel("Dual λ")
contour = ax4.contour(X_grid, Lam_grid, L_grid, levels=20, cmap='viridis', alpha=0.5)
ax4.plot(0, 2, 'r*', markersize=15, label="Saddle Point (0,2)")

# Gradient flow path
# dx/dt = -dL/dx = -(2(x-1) + λ)
# dλ/dt = +dL/dλ = x  (projected to λ>=0)
path_x = [1.0]
path_lam = [0.0]
dt = 0.05
for _ in range(100):
    curr_x = path_x[-1]
    curr_lam = path_lam[-1]

    dx = - (2*(curr_x - 1) + curr_lam)
    dlam = curr_x

    new_x = curr_x + dt * dx
    new_lam = max(0, curr_lam + dt * dlam) # Projection

    path_x.append(new_x)
    path_lam.append(new_lam)

line_path, = ax4.plot([], [], 'k.-', linewidth=1, markersize=3, label="Uzawa Iteration")
point_head, = ax4.plot([], [], 'ko', markersize=6)
txt4 = ax4.text(0.02, 0.95, "", transform=ax4.transAxes)

ax4.legend()

def update_saddle(i):
    line_path.set_data(path_x[:i], path_lam[:i])
    point_head.set_data([path_x[i]], [path_lam[i]])
    txt4.set_text(f"Iter {i}: x={path_x[i]:.2f}, λ={path_lam[i]:.2f}")
    return line_path, point_head, txt4

anim4 = FuncAnimation(fig4, update_saddle, frames=len(path_x), interval=50, blit=True)
anim4.save("topics/09-duality/assets/duality_saddle_path.gif", writer=PillowWriter(fps=15))
plt.close(fig4)
