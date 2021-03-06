from matplotlib import pyplot as plt
import numpy as np

def best_poly(x, y, k):
	n = len(x)

	somas = {}
	somas[0] = n
	
	for n in range(1, 2 * k + 1):
		somas[n] = sum(xi ** n for xi in x)
	
	A = []
	B = []
	for i in range(k + 1):
		row = []

		for j in range(k + 1):
			row.append(somas[i + j])
		
		A.append(row)

		if i == 0:
			B.append(sum(y))
		else:
			B.append(sum(xi ** i * yi for xi, yi in zip(x, y)))
	
	return np.linalg.solve(A, B)


x = [-1, 0, 1, 3]
y = [0, 2, 1, 2]

coeffs = best_poly(x, y, 1)

import matplotlib.pyplot as plt

def p(x, coeffs):
	return coeffs[0] + sum(ci * x ** i for i, ci in enumerate(coeffs, 1))

t = np.linspace(min(x), max(x), 200)
pt = [p(ti, coeffs) for ti in t]

plt.plot(t, pt)
plt.scatter(x, y)
plt.savefig('best_poly.png')