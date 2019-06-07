import matplotlib.pyplot as plt

x = range(1,50)

y = [value * 3 for value in x]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(y)

plt.plot(x,y)
plt.title('X and Y line')

plt.show()

