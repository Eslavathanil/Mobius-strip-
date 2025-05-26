# Möbius Strip Modeling in Python 🌀

This project models a **Möbius strip** using parametric equations in Python and computes its **surface area** and **edge length** numerically. It also includes a 3D visualization using Matplotlib.

---

## 📁 Code Structure

The core logic is encapsulated in a class-based structure for clarity and modularity:

### `MobiusStrip` class:
- **`__init__(R, w, n)`**  
  Initializes the strip with:
  - `R`: Radius from center to strip midline  
  - `w`: Width of the strip  
  - `n`: Resolution of the mesh grid

- **`_generate_surface()`**  
  Uses the Möbius strip parametric equations to compute a 3D mesh of `(x, y, z)` points.

- **`compute_surface_area()`**  
  Numerically approximates the surface area by computing the magnitude of the cross product of partial derivatives (`|r_u × r_v|`) and integrating over the surface.

- **`compute_edge_length()`**  
  Calculates the length of the Möbius strip boundary by approximating arc length along the edges.

- **`plot()`**  
  Visualizes the Möbius strip using Matplotlib's 3D plotting tools.

---

## 🧮 Surface Area Approximation

- The differential area element is calculated as:

  \[
  dA = \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| \, du \, dv
  \]

- The area is computed by summing `dA` over all grid cells using `numpy`.

---

## ⚠️ Challenges

- **Numerical sensitivity**: The accuracy of area and edge computations depends on the resolution parameter `n`. A higher `n` improves precision but increases computation.
- **Non-orientability**: The Möbius strip is a one-sided surface, making direct integration tricky. However, using parametric equations with a half-twist correctly models the geometry for integration and visualization.

---

## 📷 Visualization

The `plot()` method renders the Möbius strip using a light-blue shaded surface:



---

## 📌 Requirements to Run

Install dependencies using pip:

```bash
pip install numpy matplotlib
python mobius_strip.py
