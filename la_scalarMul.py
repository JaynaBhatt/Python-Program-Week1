x = [[12,7,3],[4,5,6],[7,8,9]]
y = 9
z = []

z = [j * y for i in x  for j in i]
print(z)