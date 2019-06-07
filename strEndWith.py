strng = input("Please Enter string = ")

strng1 = len(strng)
findIng = strng.rfind("ing")

if strng1 < 3:
 print(strng)
elif findIng > -1 :
    print(strng + "ly")
else :
    print(strng + "ing")