num1 = int(input("Enter the first value: "))
if ((num1 < 1) or (num1 > 6)):
  print("Invalid value")
  exit()

num2 = int(input("Enter the second value: "))
if ((num2 < 1) or (num2 > 6)):
  print("Invalid value")
  exit()

sum = num1 + num2

if(sum == 7 or sum == 11):
  print("Congratulations! You win!")
elif(sum == 2 or sum == 3 or sum == 12):
  print("Better luck next time.")
else:
  print(f"You have {sum} points.")

