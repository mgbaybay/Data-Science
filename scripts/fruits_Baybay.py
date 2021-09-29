name = str(input("Input name: "))
fruits = [(1, "Apples", 50, 20), (2, "Oranges", 40, 35), (3, "Bananas", 30, 40)]
output = "{}) {} - Php {} | {} pieces left (only {} pieces available)"

print("\nWhat would you like to buy?")
print(output.format(fruits[0][0], fruits[0][1], fruits[0][2], fruits[0][3], fruits[0][3]))
print(output.format(fruits[1][0], fruits[1][1], fruits[1][2], fruits[1][3], fruits[1][3]))
print(output.format(fruits[2][0], fruits[2][1], fruits[2][2], fruits[2][3], fruits[2][3]))

choice = int(input("\nEnter choice: "))

if (choice <= 3 and choice >= 1):
  quantity = int(input(f"How many pieces would you like to buy of {fruits[choice-1][1]}? "))
  total = fruits[choice-1][2] * quantity

  if (quantity < 0 or quantity > fruits[choice-1][3]):
    print("Invalid quantity")
  else:
    print(f"Your total bill for {quantity} items is Php {total}.00")

else:
  print("Invalid choice")
