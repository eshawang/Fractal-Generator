from pylab import *
from numpy import NaN

def julia(C):
	X = arange(-1.5, 1.5, 0.002)
	Y = arange(-1.5, 1.5, 0.002)
	M = zeros((len(Y), len(X)))

	for x_iter, x in enumerate(X):
		for y_iter, y in enumerate(Y):
			z = x + 1j * y
			pixel = NaN
			for n in range(1, 300):
				z = z**2 + C
				if abs(z) > 2:
					pixel = n
					break

			M[y_iter, x_iter] = pixel

	imshow(M, cmap = cm.cubehelix, extent = (X.min(), X.max(), Y.min(), Y.max()))
	show()

julia(-0.7 + 0.27015j)
