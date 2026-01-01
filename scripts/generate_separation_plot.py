import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Set the style
plt.figure(figsize=(8, 5))
ax = plt.gca()

# Create two convex sets
# Set 1: A blue circle
circle = patches.Circle((2, 3), 1, edgecolor='blue', facecolor='blue', alpha=0.6, label='C (Convex Set)')
ax.add_patch(circle)

# Set 2: A red square (rotated for interest)
# Square center at (6, 2), size 1.5
square = patches.Rectangle((5, 1), 1.5, 1.5, edgecolor='red', facecolor='red', alpha=0.6, label='D (Convex Set)')
ax.add_patch(square)

# Define the separating hyperplane (line)
# Slope approx -0.5, passing through (4, 2.5)
# Normal vector a = (1, 2) -> slope = -0.5
# a^T x = b
# Let a = [1, 2].
# Point between sets: (3.5, 2.5) -> 1*3.5 + 2*2.5 = 3.5 + 5 = 8.5
# Line: x + 2y = 8.5 => 2y = -x + 8.5 => y = -0.5x + 4.25

x_vals = np.linspace(0, 8, 100)
y_vals = -0.5 * x_vals + 4.25
plt.plot(x_vals, y_vals, 'k-', linewidth=2, label='Separating Hyperplane ($a^T x = b$)')

# Draw the normal vector a
# Origin on line: (4.5, 2)
origin_x, origin_y = 4.5, 2.0
# Vector direction (1, 2) normalized
a_vec = np.array([1, 2])
a_vec = a_vec / np.linalg.norm(a_vec)
plt.arrow(origin_x, origin_y, a_vec[0], a_vec[1], head_width=0.2, head_length=0.2, fc='black', ec='black')
plt.text(origin_x + a_vec[0] + 0.1, origin_y + a_vec[1], r'$a$', fontsize=12)

# Annotations
plt.text(2, 3, r'$C$', fontsize=14, ha='center', va='center', color='white', fontweight='bold')
plt.text(5.75, 1.75, r'$D$', fontsize=14, ha='center', va='center', color='white', fontweight='bold')

plt.xlim(0, 8)
plt.ylim(0, 5)
plt.axis('off') # Remove axes for cleaner look
plt.legend(loc='upper right')
plt.title('Separating Hyperplane Theorem', fontsize=14)

# Save
plt.tight_layout()
plt.savefig('topics/03-convex-sets-geometry/assets/separating-hyperplane.png', dpi=150)
print("Image generated successfully.")
