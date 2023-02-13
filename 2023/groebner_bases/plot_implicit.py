import numpy as np
from mayavi import mlab
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

C1 = (127/255,201/255,127/255)
C2 = (190/255,174/255,212/255)
C3 = (253/255,192/255,134/255)
C4 = (255/255, 255/255, 153/255)

if __name__ == "__main__":
    # a system of polynomial equations
    def fn1(x, y, z):
        return x**2 + y + z - 1

    def fn2(x, y, z):
        return x + y**2 + z - 1

    def fn3(x, y, z):
        return x + y + z**2 - 1

    fig = mlab.figure(size=(1024, 1024), bgcolor=(1,1,1))
    x, y, z = np.mgrid[-3:3:50j, -3:3:50j, -3:3:50j]

    values = fn1(x, y, z)
    mlab.contour3d(x, y, z, values, contours=[0], color=C1, figure=fig)

    values = fn2(x, y, z)
    mlab.contour3d(x, y, z, values, contours=[0], color=C2, figure=fig)

    values = fn3(x, y, z)
    mlab.contour3d(x, y, z, values, contours=[0], color=C3, figure=fig)

    # solutions
    x = [0, 0, 1, -1 - np.sqrt(2), np.sqrt(2) - 1]
    y = [0, 1, 0, -1 - np.sqrt(2), np.sqrt(2) - 1]
    z = [1, 0, 0, -1 - np.sqrt(2), np.sqrt(2) - 1]
    mlab.points3d(x, y, z, resolution=16, scale_factor=0.5, color=C4, figure=fig)

    f = mlab.gcf()
    f.scene._lift()
    imgmap = mlab.screenshot(mode='rgba', antialiased=True)
    mlab.close(fig)

    fig2 = plt.figure(figsize=(14, 10))
    plt.axis('off')
    plt.imsave(arr=imgmap, fname='implicit_system.png')
