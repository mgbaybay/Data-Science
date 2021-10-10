def fruit_list():
  fruit = []
  for i in range(len(fruits)):
    fruit.append(fruits[i][0])
  return fruit

def update_stock():
  print(fruit_list())
  fruit_choice = str(input("Which of the fruits above would you like to update? ")).capitalize()
  while fruit_choice not in fruit_list():
    fruit_choice = str(input("Which of the fruits above would you like to update? ")).capitalize()
  
  for i in range(len(fruits)):
    if (fruits[i][0].capitalize() == fruit_choice):
      fruits[i][2] += int(input(f"How many stocks of {fruit_choice} came / left? "))
      
      if (fruits[i][2] < 0):
        fruits[i][2] = 0 
      print(f"Stocks of {fruit_choice} are now updated to {fruits[i][2]}") 

def update_price():
  fruit_choice = str(input("Which of the fruits above would you like to update? ")).capitalize()
  while fruit_choice not in fruit_list():
    fruit_choice = str(input("Which of the fruits above would you like to update? ")).capitalize()
  
  for i in range(len(fruits)):
    if (fruits[i][0].capitalize() == fruit_choice):
      fruits[i][1] = float(input(f"How much does {fruit_choice} now cost? "))
      while (fruits[i][1] < 0):
        fruits[i][1] = float(input(f"How much does {fruit_choice} now cost? "))
      print(f"The price of {fruit_choice} is now Php {fruits[i][1]}") 

def add_new_stock():
  add_fruit = str(input("What is the fruit? ")).capitalize()
  while add_fruit in fruit_list():
    add_fruit = str(input("What is the fruit? ")).capitalize()

  add_price = float(input("How much does it cost? "))
  while (add_price < 0):
    add_price = float(input("How much does it cost? "))
  
  add_stock = int(input("How many stocks are there? "))
  while (add_stock < 0):
    add_stock = int(input("How many stocks are there? "))
  
  new_stock = [add_fruit, add_price, add_stock]
  fruits.append(new_stock)
  print(f"{add_stock} items of {add_fruit} worth Php {add_price} is added.")

def remove_stock():
  fruit_choice = str(input("Which fruit do you want to delete? ")).capitalize()
  while fruit_choice not in fruit_list():
    fruit_choice = str(input("Which fruit do you want to delete? ")).capitalize()
  
  for i in range(len(fruits)):
    if (fruits[i][0].capitalize() == fruit_choice):
      fruit_index = i
  del fruits[fruit_index]
  print(f"Successfully deleted {fruit_choice}.")

def total_assets():
  output = "We have {} pieces of {} at Php {} each."
  print(f"Good day, {name}. Here is the list of our stocks and prices:")
  for i in range(len(fruits)):
    print(output.format(fruits[i][2], fruits[i][0], fruits[i][1]))

def choices():
  print("\n\t1. Update stock")
  print("\t2. Update price")
  print("\t3. Add new stock")
  print("\t4. Remove existing stock")
  print("\t5. Total assets")
  print("\t6. Exit\n")
  choice = int(input("What would you like to do (Enter 1-6)? ")) 
  while (choice < 1 or choice > 6):
    choice = int(input("What would you like to do (Enter 1-6)? "))
  return choice
      
name = str(input("May I know your name? "))
fruits = [["Apple", 35.0, 10], ["Banana", 25.0, 20], ["Cantaloupe", 15.0, 30]]
total_assets()

choice = choices()
while(choice != 6):
  if (choice == 1):
    update_stock()
    choice = choices()
  elif (choice == 2):
    update_price()
    choice = choices()
  elif (choice == 3):
    add_new_stock()
    choice = choices()
  elif (choice == 4):
    remove_stock()
    choice = choices()
  elif (choice == 5):
    total_assets()
    choice = choices()

  