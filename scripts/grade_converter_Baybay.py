name = str(input("What is the student's name? "))
grade = float(input(f"What is {name}'s grade? "))

#Grade to letter grade conversion
if (grade >= 97 and grade <= 100):
  letter_grade = "A+"
elif (grade >= 94 and grade < 97):
  letter_grade = "A"
elif (grade >= 91 and grade < 94):
  letter_grade = "A-"
elif (grade >= 88 and grade < 91):
  letter_grade = "B+"
elif (grade >= 85 and grade < 88):
  letter_grade = "B"
elif (grade >= 80 and grade < 85):
  letter_grade = "B-"
elif (grade >= 75 and grade < 80):
  letter_grade = "C"
elif (grade >= 70 and grade < 75):
  letter_grade = "D"
elif (grade >= 0 and grade < 70):
  letter_grade = "F"
else:
  letter_grade = "Invalid range"

#Print passed or failed and grade
if (grade >= 75 and grade <= 100):
  print(f"{name} passed and has a grade of {letter_grade}")
elif (grade >= 0 and grade < 75):
  print(f"{name} failed and has a grade of {letter_grade}")
else:
  print(f"{letter_grade}. Enter grade between 0 to 100.")
