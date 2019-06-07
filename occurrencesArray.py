from array import array

array_num = array('i', [4,3,6,3,1,2,2,3,3])

print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))