import numpy as np
import matplotlib.pyplot as plt

# construct the function
start = -5
stop = 5
step = 0.1

X = np.arange(start, stop + step, step)
y = lambda x: 1 / (1 + np.exp(-x**2)) + (2 * x + 1)**2 / 200 
dy = lambda x: 2 * np.exp(-x**2) * x / (np.exp(-x**2) + 1)**2 + 1 / 50 * (2 * x + 1)
ddy = lambda x: (-4 * np.exp(-x**2) * x**2 + 2 * np.exp(-x**2)) / (np.exp(-x**2) + 1)**2 + \
                 8 * np.exp(-2*x**2) * x**2 / (np.exp(-x**2) + 1)**3 + \
                 1 / 25

# Initial value
x_0 = -4
# gradient descent (1st order)
x = x_0
step_size = 0.2
KMaxIter = 400
iter = 0
while True:
  iter = iter + 1
  grad = dy(x) 
  x_new = x - step_size * grad
  if y(x_new) >= y(x) or iter > KMaxIter:
    break
  else:
    x = x_new
print(iter)
# newton-type (2nd order)


plt.plot(X, y(X))
plt.plot(x, y(x), marker='o', linestyle='', markersize=10, markerfacecolor='red', markeredgewidth=2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Optimization')
plt.grid(True)
plt.show()


