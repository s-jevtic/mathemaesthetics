import numpy as np
from matplotlib import pyplot as plt

print("Initializing Julia set creator...")
lsnum = 100 #number of steps
print("Array size: {0}x{0}".format(lsnum))
it = 100 #number of iterations
print("Number of iterations: {}".format(it))
xrange = [-2, 2]
yrange = [-2, 2]


def fjulia(z, it):
    print("Initializing Julia algorithm...")
    fj = np.zeros_like(z, dtype='int')
    print("Iterating...")
    for i in range(it):
        print("{}/{}:".format(i, it), end=' ')
        z = z**2 + np.abs(np.real(z)) + 1j*np.abs(np.imag(z))
        fj += (np.real(z)**2 + np.imag(z)**2 <= 4)
        print("Done", end='\r')
    return fj 

print("Creating linspaces...", end=' ')
x = np.linspace(xrange[0], xrange[1], num=lsnum)
y = np.linspace(yrange[0], yrange[1], num=lsnum)
print("Done")

print("Creating meshgrid...", end=' ')
x, y = np.meshgrid(x, y)
print("Done")

print("Creating complex space...", end=' ')
c = x + 1j*y
print("Done")

print("Creating masked array...")
mb = np.ma.masked_equal(fjulia(c, it), 0)
#masking the array because logarithms are undefined for 0
print("Masked array done")
print("Creating the logarithmic array...", end=' ')
mb_log = np.log(mb) #I used logarithms for aesthetic purposes
print("Done")
print("Unmasking array...", end=' ')
mb = np.ma.filled(mb) #unmasking the array to save it
print("Done")

#print("Saving array...", end=' ')
#np.save("./outfiles/fauxjulia1_i{0}_n{1}".format(it, lsnum), mb)
#skip this if you don't want to save the array
print("Done")

print("Plotting filled contours...", end=' ')
plt.figure(figsize=(5,5))
plt.axis('equal')
plt.contourf(x, y, mb_log, cmap='magma', levels=100)
#gives a contour plot on the (x, y) grid
print("Done")
print("Plotting the image...", end=' ')
plt.figure(figsize=(5,5))
plt.imshow(mb_log, cmap='magma', origin='lower') #just plots the values
print("Done")
#plt.imsave(
#        "./outfiles/fauxjulia1_i{0}_n{1}.png".format(it, lsnum), mb_log,
#        cmap='magma', origin='lower'
#        )
plt.show()