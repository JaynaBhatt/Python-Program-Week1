strExample = "www.google.com"
dict = {}

for n in strExample:
  keys = dict.keys()
  if n in keys:
    dict[n] += 1
  else:
    dict[n] = 1

print(dict)