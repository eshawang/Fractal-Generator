from pylab import *
from numpy import NaN

def mandelbrot(C):
	z = 0
	for n in range(1, 100):
		z = z**2 + C
		if abs(z) > 2:
			return n
	return NaN

def plot():
	X = arange(-2, 0.5, 0.002)
	Y = arange(-1, 1, 0.002)
	M = zeros((len(Y), len(X)))

	for x_iter, x in enumerate(X):
		for y_iter, y in enumerate(Y):
			M[y_iter, x_iter] = mandelbrot(x + 1j * y)

	imshow(M, cmap = cm.cubehelix, extent = (X.min(), X.max(), Y.min(), Y.max()))
	show()

plot()
