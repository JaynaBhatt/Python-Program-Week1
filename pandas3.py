import pandas as pd 

a = pd.Series([2,4,6,8,10],index=['A','B','C','D','E'])
b = pd.Series([1,3,5,7,9],index=['A','B','C','D','E'])

c = a.add(b)

print(c)