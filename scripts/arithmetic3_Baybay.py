num1 = float(input("Enter the first value: "))
num2 = float(input("Enter the second value: "))

print("Select an operation:" + "\n1) Addition" + "\n2) Subtraction" + "\n3) Multiplication" + "\n4) Division\n") 

operation_num = int(input("Enter choice: "))

if (operation_num == 1):
  print(f"The sum of {num1} and {num2} is {num1 + num2}")
elif (operation_num == 2):
  print(f"The difference of {num1} and {num2} is {num1 - num2}")  
elif (operation_num == 3):
  print(f"The product of {num1} and {num2} is {num1 * num2}")
elif (operation_num == 4):
  print(f"The quotient of {num1} and {num2} is {num1 / num2}")
else:
  print("Invalid choice. Please try again")