import numpy as np 

a = np.ones([5,5])
print("origional array")
print(a)
a[1:-1,1:-1] = 0
print("New output = \n" , a)


  