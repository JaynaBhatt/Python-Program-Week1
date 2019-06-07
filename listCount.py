
list1 = ['abc','xyz','aba','121']
count = 0
for x in list1:
    if len(x) > 1 and x[0] == x[-1]:
        count = count + 1
        print(x)