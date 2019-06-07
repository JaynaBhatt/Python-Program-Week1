import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x,y,s=70,facecolor='none',edgecolor='green')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()