# Import the modules with math functions and plotting options
import numpy as np
from matplotlib import pyplot as plt
import sys

# Define functions
x = np.arange(0.0, 2, 0.1)
y = np.cos(2*np.pi*x)
y1 = np.sin(2*np.pi*x)

# Plot
plt.plot(x, y, label='Coseno')
plt.plot(x,y1, label='Seno')
plt.plot
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
