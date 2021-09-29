even_numbers = []
odd_numbers = []
by_five = []
by_five_sum = 0
even_numbers_sum = 0
odd_numbers_sum = 0

for i in range(100, 501, +1):
  if (i % 5 == 0):
    by_five.append(i)
  if (i % 2 == 0):
    even_numbers.append(i)
  else:
    odd_numbers.append(i)  
  
for i in range(len(odd_numbers)):
  odd_numbers_sum += odd_numbers[i]

for i in range(len(by_five)):
  by_five_sum += by_five[i]

for i in range(len(even_numbers)):
  even_numbers_sum += even_numbers[i]

print(by_five_sum)
print(even_numbers_sum)
print(odd_numbers_sum)
print(even_numbers_sum / len(even_numbers))
