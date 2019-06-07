x = [[12,7,3],[4 ,5,6],[7 ,8,9]]

y = [[5,8,1],[6,7,3],[4,5,9]]

z = []


z = [x[i][j] + y[i][j] for i in range(0,len(x)) for j in range(0,len(y))]
print(z)
