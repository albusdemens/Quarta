# Import the modules with the math functions and the plotting options
# We need
import numpy as np
from matplotlib import pyplot as plt
import sys

# Two ways to plot the tangent
x = np.arange(0.0, 2, 0.1)
#y = (np.sin(2*np.pi*x)) / (np.cos(2*np.pi*x))
y1 = np.tan(2*np.pi*x)

# Set the range of the axes
plt.axis([-2*np.pi, 2*np.pi, -2, 2])
# Include a title
plt.title('y = tan(x)')

#plt.plot(x,y)
plt.plot(x,y1)
plt.show()
