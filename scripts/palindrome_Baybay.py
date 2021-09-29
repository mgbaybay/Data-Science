# Answer 1: Input with special characters

text = str(input("Enter text: "))

if (len(text) != 0):
  new_text = ''.join(filter(str.isalnum, text)) 
  new_text = new_text.lower()
  if (new_text == new_text[::-1]):
    print("True")
  else:
    print("False")
else:
  print("Please enter text.")


#Answer 2: Simple input only, no special characters
# text = str(input("Enter text: "))

# if (len(text) != 0):
#   new_text1 = text.replace(" ", "")
#   new_text1 = new_text1.lower()
#   if (new_text1 == new_text1[::-1]):
#     print("True")
#   else:
#     print("False")
# else:
#   print("Please enter text.")

