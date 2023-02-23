import numpy as np
from mayavi import mlab
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

C1 = (127 / 255, 201 / 255, 127 / 255)
C2 = (190 / 255, 174 / 255, 212 / 255)
C3 = (253 / 255, 192 / 255, 134 / 255)
C4 = (255 / 255, 255 / 255, 153 / 255)


def cone(x, y, z):
    return z**2 - x**2 - y**2


def plane(x, y, z):
    return x + z


def cubic(x, y, z):
    return x**3 + y**2 - z**2


def clebsch_cubic(x, y, z):
    return (
        81 * (x**3 + y**3 + z**3)
        - 189
        * (x**2 * y + x**2 * z + y**2 * x + y**2 * z + z**2 * x + z**2 * y)
        + 54 * (x * y * z)
        + 126 * (x * y + x * z + y * z)
        - 9 * (x**2 + y**2 + z**2)
        - 9 * (x + y + z)
        + 1
    )


def make_contour(x, y, z, vals, fname):
    fig = mlab.figure(size=(1024, 1024), bgcolor=(1, 1, 1))
    mlab.contour3d(x, y, z, vals, contours=[0], color=C1, figure=fig)

    f = mlab.gcf()
    f.scene._lift()
    imgmap = mlab.screenshot(mode="rgba", antialiased=True)
    mlab.close(fig)

    fig1 = plt.figure(figsize=(14, 10))
    plt.axis("off")
    plt.imsave(arr=imgmap, fname=fname)
    return


if __name__ == "__main__":
    x, y, z = np.mgrid[-3:3:50j, -3:3:50j, -3:3:50j]

    plane_vals = plane(x, y, z)
    make_contour(x, y, z, plane_vals, "plane.png")

    cone_vals = cone(x, y, z)
    make_contour(x, y, z, cone_vals, "cone.png")

    cubic_vals = cubic(x, y, z)
    make_contour(x, y, z, cubic_vals, "cubic.png")

    clebsch_cubic_vals = clebsch_cubic(x, y, z)
    make_contour(x, y, z, clebsch_cubic, "clebsch_cubic.png")
