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



# Application Loop
while userOption != "6":

  # Prompt the user to select an option
  print()
  displayMenu()
  userOption = input("Select an Option: ")

  # Perform selected option
  # If option 1 selected, prompt them to enter a student name
  if userOption == "1":
    studentName = input("Enter student name: ")
    students[studentName] = []
    print(f"{studentName} added!")
    print(students)

  # If option 2 selected, prompt them to enter a student to remove
  if userOption == "2":
    studentName = input("Enter student name: ")
    if studentName in students:
      students.pop(studentName)

    else: 
      print(f"{studentName} not in dictionary!")

  # if they select 3, add a grade to a student
  if userOption == "3":
    
    # prompt user to enter a student name
    studentName = input("Enter student name: ")
    
    if studentName in students:
      for key,value in students.items():
        value.append(getNumberGradeFromUser())
        print(f"Added {value[0]} to {key}'s quizzes")
      
        
      
    
    
    