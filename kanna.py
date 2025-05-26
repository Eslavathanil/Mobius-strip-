import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=100):
        """
        Initialize a Möbius strip with:
        R: Radius from center to middle of strip
        w: Width of the strip
        n: Resolution (number of divisions along u and v)
        """
        self.R = R
        self.w = w
        self.n = n
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._generate_surface()

    def _generate_surface(self):
        """
        Generate the mesh grid for the Möbius strip using parametric equations.
        """
        u = self.u
        v = self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        """
        Approximate the surface area using the differential surface element.
        |r_u x r_v| du dv
        """
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        # Derivatives
        dx_du = np.gradient(self.x, axis=1) / du
        dx_dv = np.gradient(self.x, axis=0) / dv
        dy_du = np.gradient(self.y, axis=1) / du
        dy_dv = np.gradient(self.y, axis=0) / dv
        dz_du = np.gradient(self.z, axis=1) / du
        dz_dv = np.gradient(self.z, axis=0) / dv

        # Cross product of partial derivatives
        cross_x = dy_du * dz_dv - dz_du * dy_dv
        cross_y = dz_du * dx_dv - dx_du * dz_dv
        cross_z = dx_du * dy_dv - dy_du * dx_dv

        dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        surface_area = np.sum(dA) * du * dv
        return surface_area

    def compute_edge_length(self):
        """
        Compute the length of the Möbius strip edge (around u with v fixed at ±w/2).
        """
        u = np.linspace(0, 2 * np.pi, self.n)
        v = self.w / 2

        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)

        # Arc length calculation along u
        dx = np.gradient(x)
        dy = np.gradient(y)
        dz = np.gradient(z)
        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        edge_length = np.sum(ds)
        return edge_length

    def plot(self):
        """
        Visualize the Möbius strip using Matplotlib 3D plotting.
        """
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, color='lightblue', edgecolor='k', alpha=0.8)
        ax.set_title("Möbius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()


# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.4, n=200)
    
    print("Surface Area ≈", round(mobius.compute_surface_area(), 4))
    print("Edge Length ≈", round(mobius.compute_edge_length(), 4))

    mobius.plot()
