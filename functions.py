#Functions/Methods - A block of code used to perform a task

# 1. Standard - library/ Inbuilt functions - already exists

y = max(56, 67, 345, 213, 5666, 6788, 2344)
print(y)

x = min(18, 24, 6589, 745, 8453, 5)
print(x)

# 2. User-Defined Functions
def school():
    print("eMobilis")
school()  #Calling a function


 #Parameters/Variables
 #Arguments/Values
def multiply(x, y):
    print(x * y)

multiply(14, 78)
multiply(10, 38)

#Python program to display details of 5 employees at emobilis
#Use a user-defined function with the help of parameters and arguments

#Details -Fullname ,Position,age, gender

print()

def employee(fullname, position, age, gender):
    print(fullname, position, age, gender)

employee("Kukan Pierre", "Lecturer", 28, "Male")
employee("Elani Kubai", "Student liason", 32, "Female")
employee("Jedida King'ori", "Managing Director", 46, "Female")
employee("Leon Okok", "Lecturer", 25, "Male")
employee("Willstacy Kagundu", "Lecturer", 36 , "Female")



