#Class is a blueprint of an object
#Object is an instance of a class
class Employee:
    #Attributes/Variables
    name = "John"
    age = 35
    gender = "Male"
    salary = 80000.00


    #Behaviour/Function
    def eat(self):
        print("Employee eats")

employee1 = Employee() #Creating an object
print(employee1.name)



employee2 = Employee()
employee3 = Employee()