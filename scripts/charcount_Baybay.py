input = str(input("Enter string: "))
char_count = {}

for i in input:
  keys = char_count.keys()
  if i in keys:
    char_count[i] += 1
  else:
    char_count[i] = 1
print(char_count)