def total_assets():
  output = "We have {} pieces of {} at {} each."
  print(f"Good day, {name}. Here is the list of our stocks and prices:")
  for i in range(len(fruits)):
    print(output.format(fruits[i][2], fruits[i][0], fruits[i][1]))

def update_stock():
  fruit_choice = str(input("Which of the fruits above would you like to update? "))
  new_stock = int(input(f"How many stocks of {fruit_choice} came / left? "))
  for i in range(len(fruits)):
    if (fruits[i][0] == fruit_choice):
      fruits[i][2] = new_stock  
  print(f"Stocks of {fruit_choice} are now updated to {new_stock}") 

def update_price():
  fruit_choice = str(input("Which of the fruits above would you like to update? "))
  new_price = int(input(f"How much does {fruit_choice} now cost? "))
  for i in range(len(fruits)):
    if (fruits[0][i] == fruit_choice):
      fruits[i][1] = new_price  
  print(f"The price of {fruit_choice} is now {new_price}") 

def add_new_stock():
  add_fruit = str("What is the fruit? ")
  add_price = float("How much does it cost? ")
  add_stock = int("How many stocks are there? ")
  new_stock = (add_fruit, add_price, add_stock)
  fruits.append(new_stock)
  print(f"{add_stock} items of {add_fruit} worth Php{add_price} is added.")

def remove_stock():
  remove_fruit = str(input("Which fruit do you want to delete? "))
  for i in range(len(fruits)):
    # match_fruit = fruits[i][0]
    print(fruits[i][0])
    print(fruits[i])
    if (fruits[i][0] == remove_fruit):
      del fruits[i]
  print(f"Successfully deleted {remove_fruit}.")
  total_assets()

def choices():
  print("\n\t1. Update stock")
  print("\t2. Update price")
  print("\t3. Add new stock")
  print("\t4. Remove existing stock")
  print("\t5. Total assets")
  print("\t6. Exit")
  num_choice = int(input("\nWhat would you like to do (Enter 1-6)? "))
  return num_choice

name = str(input("May I know your name? "))
fruits = [("Apples", 35.0, 10), ("Banana", 25.0, 20), ("Cantaloupe", 15.0, 30)]

total_assets()
choice = choices()
if (choice != 6):
  if (choice == 1):
    update_stock()
  elif (choice == 2):
    update_price()
  elif (choice == 3):
    add_new_stock()
  elif (choice == 4):
    remove_stock()
  elif (choice == 5):
    total_assets()

else:
  exit()
# choice = {
#   "1": update_stock(),
#   "2": update_price(),
#   "3": add_new_stock(),
#   "4": remove_stock(),
#   "5": total_assets(),
#   "6": exit()
# }

# choice[choices()]()



# output = "We have {} pieces of {} at {} each."

# print(f"\nGood day, {name}. Here is the list of our stocks and prices:")
# for i in range(len(fruits)):
#   print(output.format(fruits[1][i], fruits[0][i], fruits[2][i]))
# print("\n\t1. Update stock\t2. Update price\t3. Add new stock\t4. Remove existing stock\t5. Total assets\t6. Exit")

# num_choice = int(input("\nWhat would you like to do (Enter 1-6)? "))

# while (num_choice < 1 and num_choice > 6):
#   num_choice = int(input("\nWhat would you like to do (Enter 1-6)? "))
# else:
#   print(f"{fruits[0]}") 
#   fruit_choice = str(input("Which of the fruits above would you like to update? "))
#   if (fruits[0][i].upper() == fruit_choice.upper()):


# # def update_price():
# #   fruit_price = [35.0, 25.0, 15.0]  
# #   return

# name = str(input("May I know your name? "))
# # fruit_name = ["Apples", "Banana", "Cantaloupe"]
# # fruit_stock = [10, 20, 30]
# # fruit_price = [35.0, 25.0, 15.0]
# # fruits = map(fruit_stock, fruit_name, fruit_price)
# # fruits = [(10, "Apples", 35.0), (20, "Banana", 25.0), (30, "Cantaloupe", 15.0)]
# fruits = [("Apples", "Banana", "Cantaloupe"), (10, 20, 30), (35.0, 25.0, 15.0)]
# output = "We have {} pieces of {} at {} each."

# print(f"\nGood day, {name}. Here is the list of our stocks and prices:")
# for i in range(len(fruits)):
#   # print(output.format(fruits[i][0], fruits[i][1], fruits[i][2]))
#   print(output.format(fruits[1][i], fruits[0][i], fruits[2][i]))
# print("\n\t1. Update stock")
# print("\t2. Update price")

# num_choice = int(input("\nWhat would you like to do (Enter 1-2)? "))

# while (num_choice != 1 and num_choice != 2):
#   num_choice = int(input("\nWhat would you like to do (Enter 1-2)? "))
# else:
#   print(f"{fruits[0]}")
#   fruit_choice = str(input("Which of the fruits above would you like to update? "))
#   new_price = int(input(f"How much does {fruit_choice} now cost? "))
#   print(f"The price of {fruit_choice} is now {new_price}")