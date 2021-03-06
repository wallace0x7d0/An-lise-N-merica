from matplotlib import pyplot as plt
import numpy as np

def best_line(x, y):
	n = len(x)	

	sum_x = sum(x)
	sum_x2 = sum(xi ** 2 for xi in x)
	sum_y = sum(y)
	sum_xy = sum(xi * yi for xi, yi in zip(x, y))

	A = [[n, sum_x], [sum_x, sum_x2]]
	B = [sum_y, sum_xy]

	return np.linalg.solve(A, B)

x = [-1, 0, 1, 3]
y = [0, 2, 1, 2]

a0, a1 = best_line(x, y)
print(a0)
print(a1)

import matplotlib.pyplot as plt

def p(x, a0, a1):
	return a0 + a1 * x

t = np.linspace(min(x), max(x), 200)
pt = [p(ti, a0, a1) for ti in t]
plt.plot(t, pt)
plt.scatter(x, y)
plt.savefig('best_line.png')