################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

################ Main Program ################
userOption = ""
students = {}

from statistics import mean

# Application Loop
while userOption != "6":

  # Prompt the user to select an option
  print()
  displayMenu()
  userOption = input("Select an Option: ")

  # Perform selected option
  # If option 1 selected, prompt them to enter a student name
  if userOption == "1":
    studentName1 = input("Enter student name: ")
    students[studentName1] = []
    print(f"{studentName1} added!")
    print(students)

  # If option 2 selected, prompt them to enter a student to remove
  if userOption == "2":
    studentName2 = input("Enter student name: ")
    if studentName2 in students:
      students.pop(studentName2)
      print(f"{studentName2} was removed!")

    else: 
      print(f"{studentName2} not in dictionary!")

  # If they select 3, add a grade to a student
  if userOption == "3":
    
    # prompt user to enter a student name
    studentName3 = input("Enter student name: ")
    
    if studentName3 in students:
      grade = getNumberGradeFromUser()
      students[studentName3].append(grade)
      print(f"Added {grade} to {studentName3} 's quizzes")

  # List a student's Quiz grades
  if userOption == "4":
    studentName4 = input("Enter student name: ")
    print(f"{studentName4}'s Quizzes: ")
    for grade in students[studentName4]:
      print(grade)

  # Display a students letter grade
  if userOption == "5":

    # Prompt user to enter name
    studentName5 = input("Enter student name: ")

    # use the mean function to get the average of all the grades the student has
    avg = mean(students[studentName5])

    # print out the corresponding letter grade
    if(avg > 89):
      print(f"{studentName5}'s current grade is an A")
    elif(avg > 79):
      print(f"{studentName5}'s current grade is an B")
    elif(avg > 69):
      print(f"{studentName5}'s current grade is an C")
    elif(avg > 59):
      print(f"{studentName5}'s current grade is an D")
    elif(avg > 49):
      print(f"{studentName5}'s current grade is an E")
    else:
      print(f"{studentName5} has Failed") 
      
      
      
      
      