import numpy as np
from matplotlib import pyplot as plt, colors
import math

lsnum = 1000  # array resolution

it = 1000  # number of iterations

x, y = np.meshgrid(*(np.linspace(-1, 1, num=lsnum),)*2)

z = x + 1j*y


def zetasum(n, field):
    _sum = np.zeros_like(field)
    for i in range(it):
        _sum += z**i**n
    return _sum


def ogf(f, field):
    _sum = np.zeros_like(field)
    for i in range(it):
        _sum += z**i * f(i)
        print(i, end='')
        print('\r', end='')
    return _sum


def phi(n):
    gcds = np.array([math.gcd(n, i) for i in range(n)])
    return np.count_nonzero(gcds == 1)


def f(n):
    try:
        return n**-2
    except ZeroDivisionError:
        return 0


def arg(z):
    return np.where(np.angle(z) < 0, 2*np.pi+np.angle(z), np.angle(z))


def getHSV(z):
    hue = arg(z)/(np.pi*2)
#    saturation = np.ones_like(z, dtype=float)
    saturation = 1 - np.floor(2*np.exp(-100*(np.abs(z)-1)**2))
    value = np.exp(-np.abs(z))
    return np.array((hue, saturation, value), dtype=float)


def getRGB(z):
    return colors.hsv_to_rgb(np.moveaxis(getHSV(z), 0, 2))


def getHSVPhase(z):
    hue = arg(z)/(np.pi*2)
    saturation = np.ones_like(hue)
    value = np.ones_like(hue)
    return np.array((hue, saturation, value), dtype=float)


def getRGBPhase(z):
    return colors.hsv_to_rgb(np.moveaxis(getHSVPhase(z), 0, 2))


Z = ogf(phi, z)
fig, [img, cnt, phs] = plt.subplots(nrows=3, figsize=(10, 20))

img.imshow(getRGB(Z), origin='lower')
img.set_title("Domain coloring")

cnt.contourf(
        x, y,
        np.log(np.ma.masked_where(
                np.abs(z) >= 1, np.abs(Z), copy=False
                )),
        levels=100, cmap='gray'
        )
cnt.set_title("Contours")
cnt.set_xlabel('Real part')
cnt.set_ylabel('Imaginary part')
cnt.set_aspect('equal', 'box')

phs.imshow(getRGBPhase(Z), origin='lower')
phs.set_title("Phase plot")

plt.show()
