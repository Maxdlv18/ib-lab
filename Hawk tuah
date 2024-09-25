import random

type = input("Are you a Student, Teacher, or Staff? ")

fullName = input("What is your full name: ")
password = input("What is your password: ")
print("")

attempts = 0
while attempts < 3:
  checkFullName = input("Enter your full name: ")
  checkPassword = input("Enter your password: ")
  
  if checkFullName == fullName and checkPassword == password:
    break
  else:
    attempts = attempts + 1
    print("Wrong name or password, try again.")

print("")
if type == "Student":
  studentFirstName = input("Enter your first name: ")
  studentLastName = input("Enter your last name: ")
  studentAge = int(input("Enter your age: "))
  studentGrade = int(input("Enter your grade level (number): "))
  
  studentID = random.randint(100, 999)
  studentUsername = (studentFirstName + studentLastName[0] + studentLastName[len(studentLastName)-1] + "_" + str(studentID))
  print("This your new username: " + studentUsername)
  print("This your new student ID: " + str(studentID))
  
  studentClasses = []
  
  class1 = input("Pick a class: Math 11, English 11, USA History, Reading, Computer Science, Biology, Chemistry, Engineering, Philisophy, and PE. ")
  class2 = input("Pick a another class: ")
  class3 = input("Pick a another class: ")
  class4 = input("Pick a another class: ")
  class6 = input("Pick a another class: ")
  class7 = input("Pick a another class: ") 
  
  studentClasses.append(class1)
  studentClasses.append(class2)
  studentClasses.append(class3)
  studentClasses.append(class4)
  studentClasses.append(class5)
  studentClasses.append(class6)
  studentClasses.append(class7)
  
  printStudentInfo()
  
def printStudentInfo():
  print("")
  print("Students full name: " + studentFirstName + " " + studentLastName)
  print("Students age: " + str(studentAge))
  print("Students grade level: " + str(studentGrade))
  print("Students ID: " + str(studentID))
  print("Students username: " + studentUsername)
  print("These are you classes: " + studentClasses)


#Objectives:
#• Request for Teacher data like names, age, etc..
#• Dynamically assign a Teacher ID number for each newly created student.
#• At registration, dynamically create a teacher username that consists of the
#first letter of their first name, followed by their last name, and their Teacher
#ID.
#• E.g. For Teacher called Emmanuel Guzman and a generated ID of 0123 the
#username will be: EGuzman_0123.
#• You can produce a different way to generate a teacher username with their
#information
#• Define a function to print all teacher information in an organized manner.
#• Create a function to display all the courses taught by this teacher.
#• Create a function to display each student from a selected course from this
#teacher.

print("")
if type == "Teacher":
  teacherFirstName = input("Enter your first name: ")
  teacherLastName = input("Enter your last name: ")
  teacherAge = int(input("Enter your age: "))
  teacherCourse = int(input("What course do you teach: English, Spanish, Biology, or Math 11"))
  
  teacherID = random.randint(100, 999)
  teacherUsername = (teacherFirstName[0] + teacherLastName + "_" + str(teacherID))
  print("This your new username: " + teacherUsername)
  print("This your new teacher ID: " + str(teacherID))
  
  englishStudents = ["John Jones", "Oscar James", "Vannessa Williams", "Kanye West"]
  spanishStudents = ["Hank Mill", "Oscar Brown" "Blake Will", "Joe Sue" ]
  biologyStudents = ["Zablon Mulugeta", "Jackson Kwug", "Maximus De La Vega"]
  math11Students = ["Mark Edwards", "Carol James", "Aaron Hawk", "Taylor Chang"]
  
  printTeacherInfo()  
  
def printTeacherInfo():
  print("")
  print("Teachers full name: " + teacherFirstName + " " + teacherLastName)
  print("Teacher age: " + str(teacherAge))
  print("Teacher subjects: " + str(teacherSubject))
  print("Teacher ID: " + str(teacherID))
  print("Teacher username: " + teacherUsername)
  print("This is your course: " + teacherCourse)
  
  if teacherCourse == "English":
    print("These are you students: " + englishStudents)
  elif teacherCourse == "Spanish":
    print("These are you students: " + spanishStudents)
  elif teacherCourse == "Biology":
    print("These are you students: " + biologyStudents)
  elif teacherCourse == "Math 11":
    print("These are you students: " + math11Students)
  else:
    print("That is not a class option") 
