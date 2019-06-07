x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(0,len(x)) :
 for j in range(0,len(x)) :
     y[i][j] = x[j][i]
print(y)