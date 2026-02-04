age = 18  #Integer
length = 45.6  #Float
greeting ="Hello there"  #String
hasFeathers = True #Boolean - if value is true or false

#Data Structures- Multiple values stored in one variable
fruits = ["Banana", "Mango", "Pineapple"]  # List - Ordered and Changeable -different datatypes
courses = ["MIT", "DataScience", "Cybersecurity"] #Array -Similar datatypes
cars = ("Mercedes", "Ford", "Porsche", "Toyota") #Tuple and Unchangeable
countries = {"Austrailia", "Canada", "India"} #Set -Unordered and unchangeable
student ={
    "firstname" :  "Elani",
    "course" : "MIT" ,
    "age" : 20 ,
    "nationality" : "Kenyan" ,
    "gender" : "Female"
} #Dictionary - Key value pair

print(age)
print("The length is", length)
print(fruits)
print(countries)
print(student)
print(student["nationality"])

#Typecasting - Converting one data type to another
print(float(age))
print(int(length))