import numpy as np
import matplotlib.pyplot as plt

# construct the function
start = -5
stop = 5
step = 0.1

x = np.arange(start, stop + step, step)
y = 1 / (1 + np.exp(-x**2)) + (2 * x + 1)**2 / 200 

# gradient descent (1st order)

# newton-type (2nd order)



plt.plot(x, y)
plt.show()

