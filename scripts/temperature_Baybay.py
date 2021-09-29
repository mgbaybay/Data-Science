def to_celsius():
  converted_temp = (temp - 32) / 1.8
  converted_unit = "C"
  print(f"{temp} {temp_unit} is equal to {converted_temp} {converted_unit}")

def to_fahrenheit():
  converted_temp = temp * 1.8 + 32
  converted_unit = "F"
  print(f"{temp} {temp_unit} is equal to {converted_temp} {converted_unit}")

temp = float(input("Enter temperature value: "))
temp_unit = str(input("Enter unit (either F or C): ")).upper()

while (temp_unit != 'C' and temp_unit != 'F'):
  temp_unit = str(input("Enter unit (either F or C): ")).upper()
else:
  if (temp_unit == "C"):
    to_fahrenheit()
  else:
    to_celsius()


  