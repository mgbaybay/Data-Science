lines = int(input("Enter amount of lines: "))

for i in range(lines, 0, -1):
  print("* " * i)  

#for diamond pattern
for i in range(lines+1):
  print(" " * (lines-i), "* " * (i))
for i in range(lines-1, -1, -1):
  print(" " * (lines-i), "* " * (i))
  