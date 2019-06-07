x = [[12,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]

z = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,len(x)) :
    for j in range(0,len(y)) :
        for k in range(0,len(y)) :
         z[i][j] += x[i][k] * y[k][j]
print(z)
    