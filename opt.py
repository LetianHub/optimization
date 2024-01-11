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
x_grad = x_0
step_size = 1
KMaxIter = 400
iter = 0
x_grad_array = np.array([])
while True:
  iter = iter + 1
  grad = dy(x_grad) 
  x_grad_new = x_grad - step_size * grad
  if y(x_grad_new) >= y(x_grad) or iter > KMaxIter:
    break
  else:
    x_grad = x_grad_new
  x_grad_array = np.append(x_grad_array, x_grad)
print(iter)

# newton-type (2nd order)
x_newton = x_0
tolerance = 0.1
KMaxIter = 400
iter = 0
x_newton_array = np.array([])
while True:
  iter = iter + 1
  x_newton_new = x_newton - dy(x_newton) / ddy(x_newton)
  if np.abs(x_newton_new - x_newton) < tolerance or iter > KMaxIter:
    break
  else:
    x_newton = x_newton_new
  x_newton_array = np.append(x_newton_array, x_newton)
print(iter)


fig1, ax1 = plt.subplots()
ax1.plot(X, y(X))
ax1.plot(x_grad, y(x_grad), marker='o', linestyle='', markersize=5, markerfacecolor='red', markeredgewidth=2)
ax1.plot(x_grad_array[:-1], y(x_grad_array[:-1]), marker='o', linestyle='', markersize=5, markerfacecolor='magenta', markeredgewidth=2)
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.set_title('GD')
ax1.grid(True)

fig2, ax2 = plt.subplots()
ax2.plot(X, y(X))
ax2.plot(x_newton, y(x_newton), marker='o', linestyle='', markersize=5, markerfacecolor='green', markeredgewidth=2)
ax2.plot(x_newton_array[:-1], y(x_newton_array[:-1]), marker='o', linestyle='', markersize=5, markerfacecolor='magenta', markeredgewidth=2)
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_title('Newton')
ax2.grid(True)

plt.show()

