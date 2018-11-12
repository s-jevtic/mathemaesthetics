import numpy as np
from matplotlib import pyplot as plt

def iterate(c, x, y, X, Y, it):
    z = c
    while(x <= np.real(z) <= X and y <= np.imag(z) <= Y and it > 0):
        z = z**-1 + c
        it -= 1
    return (x <= np.real(z) <= X and y <= np.imag(z) <= Y)

step = 0.01
r = -5
R = 2
i = -5
I = 5
it = 500

C = np.array(())
#C = np.append(C, [x + 1j*y for x in range(-5, 2, step) for y in range(-5, 5, step)])
'''for x in np.arange(r, R, step):
    for y in np.arange(i, I, step):
        C = np.append(C, x + 1j * y)
        print('app ' + str(x + 1j * y))
        
np.savetxt('complexw' + str(np.log10(step)) + '.txt', C, fmt=['%f%+fj'], delimiter=',')
print('done')'''

C = np.loadtxt('complexw' + str(np.log10(step)) + '.txt', dtype='complex128')
#for c in C: print(c)

#input()

mbr = np.empty(())

for c in C:
    if(iterate(c, r, i, R, I, it)):
        mbr = np.append(mbr, c)
        print('mbr ' + str(c))

print(mbr)
#np.savetxt('mandelbrot.s' + str(np.log10(step)) + 'i' + str(it) + '.txt', C, fmt=['%f %f'], delimiter=',')
        
plt.plot(np.real(mbr), np.imag(mbr), 'k.')
plt.axis('equal')
plt.show()