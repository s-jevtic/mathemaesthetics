import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

echo = 1

def cprint(p, *args, **kwargs):
    if echo >= p:
        print(*args, **kwargs)

cprint(1, "Initializing Mandelbrot set creator...")
lsnum = 500 #number of steps
cprint(1, "Array size: {0}x{0}".format(lsnum))
it = 100 #number of iterations
cprint(1, "Number of iterations: {}".format(it))
fnum = 1200 #number of frames
cprint(1, "Number of frames: {}".format(fnum))
xrange = [-3, 3]
yrange = [-2, 4]
center = (xrange[0] + xrange[1])/2 + (yrange[0] + yrange[1])*0.5j
cprint(1, "Center: {}".format(center))

def zoom(f, xr, yr):
    dx = (xr[1] - xr[0])/2
    dy = (yr[1] - yr[0])/2
    dx /= f
    dy /= f
    xr = [np.real(center) - dx, np.real(center) + dx]
    yr = [np.imag(center) - dy, np.imag(center) + dy]
    return xr, yr

def mandelbrot(field, it):
    cprint(2, "Initializing Mandelbrot algorithm...")
    z = np.zeros_like(field, dtype='complex')
    mb = np.zeros_like(field, dtype='int')
    cprint(2, "Iterating...")
    for i in range(it):
        cprint(2, "{}/{}:".format(i, it), end=' ')
        z = z**2 + field
        mb += (np.real(z)**2 + np.imag(z)**2 <= 4)
        cprint(2, "Done", end='\r')
    return mb 

frames = []
f = plt.figure(frameon=False)
plt.set_cmap('magma')
plt.axis('off')

cprint(1, "Creating frames...")
for i in range(fnum):
    cprint(1, "{}/{}:".format(i, fnum), end=' ')
    xrange, yrange = zoom(1.03725, xrange, yrange)
    cprint(2, "Creating linspaces...", end=' ')
    x = np.linspace(xrange[0], xrange[1], num=lsnum)
    y = np.linspace(yrange[0], yrange[1], num=lsnum)
    cprint(2, "Done")
    
    cprint(2, "Creating meshgrid...", end=' ')
    x, y = np.meshgrid(x, y)
    cprint(2, "Done")
    
    cprint(2, "Creating complex space...", end=' ')
    c = x + 1j*y
    cprint(2, "Done")
    
    cprint(2, "Creating masked array...")
    mb = np.ma.masked_equal(mandelbrot(c, it),0)
    #masking the array because logarithms are undefined for 0
    cprint(2, "Masked array done")
    cprint(2, "Creating the logarithmic array...", end=' ')
    mb_log = np.log(mb) - 1 #I used logarithms for aesthetic purposes
    cprint(2, "Done")
    #cprint(2, "Unmasking array...", end=' ')
    #mb = np.ma.filled(mb) #unmasking the array to save it
    #cprint(2, "Done")
    cprint(2, "Plotting the image...", end=' ')
    #plt.figure(frameon=False)
    #plt.axis('off')
    frames.append([plt.imshow(mb, animated=True)])
    cprint(2, "Done")
    cprint(1, "Done", end= '\r')
ani = animation.ArtistAnimation(f, frames, 33, repeat_delay=1000)
#ani.save("./outfiles/mbanim_i{}_n{}_f{}_c{}.mp4")
plt.show()