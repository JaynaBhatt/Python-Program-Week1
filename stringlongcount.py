strng = input("Please Enter string = ")
longest = 0

for x in strng.split() :
  if len(x) > longest:
      longest = len(x)
      longest_word = x

print("The longest word is", longest_word, "with length", len(longest_word))

