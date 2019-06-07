import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randn(200)
y = np.random.randn(200)

plt.scatter(x,y,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()