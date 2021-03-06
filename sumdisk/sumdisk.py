import numpy as np
from matplotlib import pyplot as plt, colors

lsnum = 1000 #array resolution
it = 100 #number of iterations

x, y = np.meshgrid(*(np.linspace(-1, 1, num=lsnum),)*2)

z = x + 1j*y

def zetasum(n, field):
    _sum = np.zeros_like(field)
    for i in range(it):
        _sum += z**(i)**n
    return _sum

def arg(z):
    return np.where(np.angle(z) < 0, 2*np.pi+np.angle(z), np.angle(z))

def gethsv(z):
    hue = arg(z)/(np.pi*2)
#    saturation = np.ones_like(z, dtype=float)
    saturation = 1 - np.floor(2*np.exp(-100*(np.abs(z)-1)**2))
    value = np.exp(-np.abs(z))
    return np.array((hue, saturation, value), dtype=float)

def getrgb(z):
    return colors.hsv_to_rgb(np.moveaxis(gethsv(z), 0, 2))
fig, [img, cnt] = plt.subplots(nrows=2, figsize=(10, 20))
img.imshow(getrgb(zetasum(2, z)), origin='lower')
cnt.contourf(
        x, y,
        np.log(np.ma.masked_where(
                np.abs(z) >= 1, np.abs(zetasum(2, z)), copy=False
                )),
        levels=100, cmap='gray'
        )
cnt.set_xlabel('Real part')
cnt.set_ylabel('Imaginary part')
cnt.set_aspect('equal', 'box')
plt.show()