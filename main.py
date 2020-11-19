import matplotlib
import rasterio
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from rasterio.plot import show
import matplotlib.pyplot as plt
from matplotlib import cm
import os
from rasterio.windows import WindowMethodsMixin, Window
from rasterio.enums import Resampling
# import georasters as gr
import numpy as np

matplotlib.use('Qt5Agg')


def house():
    fp = 'DHMVIIDSMRAS1m_k13.tif'
    img = rasterio.open(fp)
    # show(img)
    array = img.read()
    array = array[0, 6300:6400, 3900:4000]
    show(array)
    print(array.shape)
    print(type(img))
    return array


def cord():
    array = house()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(0, 99, 1)
    Y = np.arange(0, 99, 1)
    X, Y = np.meshgrid(X, Y)
    Z = array[X, Y]
    #print(Z)
    #print(array)
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


cord()
