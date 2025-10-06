import pyvista as pv
import numpy as np
from matplotlib import cm

# ------------------------------
# Parameters
# ------------------------------
num_cells = 200
np.random.seed(42)

# Generate random 3D positions for cells
cell_positions = np.random.rand(num_cells, 3) * 100

# Simulate gene expression (normalized 0-1)
gene_expression = np.random.rand(num_cells)

# Choose a colormap
cmap_name = "coolwarm"
colormap = cm.get_cmap(cmap_name)

# Map gene expression to RGB colors
cell_colors = np.array([colormap(g)[:3] for g in gene_expression])

# ------------------------------
# PyVista Plotter
# ------------------------------
plotter = pv.Plotter(window_size=[1024, 768])
plotter.background_color = 'white'

# Add cells as spheres with colors
sphere_radius = 1.5
for pos, color in zip(cell_positions, cell_colors):
    sphere = pv.Sphere(radius=sphere_radius, center=pos)
    plotter.add_mesh(sphere, color=color, smooth_shading=True)

# ------------------------------
# Camera & Aesthetics
# ------------------------------
plotter.add_axes()              # 3D axes
plotter.show_grid()             # Optional grid for reference
plotter.enable_eye_dome_lighting()  # Makes visualization more “solid” and professional
plotter.camera_position = 'iso'     # Isometric view for nice perspective

# ------------------------------
# Interactivity
# ------------------------------
# Left-click + drag = rotate
# Right-click + drag = pan
# Scroll = zoom

# ------------------------------
# Show interactive 3D plot
# ------------------------------
plotter.show(title="3D Cancer Cell Simulation")
