import numpy as np
import matplotlib.pyplot as plt

# Define the function for the saddle surface
def saddle_function(x, y):
    return x**2 - y**2

# Create a meshgrid of x and y values
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calculate the z values
Z = saddle_function(X, Y)

# Parameterize the intersection curve
radius = 1
theta = np.linspace(0, 2*np.pi, 100)
x_c = radius * np.cos(theta) + 0.5
y_c = radius * np.sin(theta) + 0.2
z_c = x_c * x_c - y_c * y_c

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.5)

# Plot the intersection curve
ax.plot(x_c, y_c, z_c, label='Intersection Curve', color='red', linewidth=2)


# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Saddle Surface')

plt.show()
