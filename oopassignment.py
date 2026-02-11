# Task 1 ; create the class

# Create a class called student with the following  attributes; fullname,course ,age, feespaid



#Task 2 :create Multiple objects
#Create at least 3 student objects from the class with different values and display the same info


class Student:

    def __init__(self,fullname,course,age, feespaid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.feespaid = feespaid

    def study(self):
        print("Student is studying")

    def eat(self):
        print("Student is eating")

student1 = Student("Makena","DataScience",20,69000)
print(student1.fullname,student1.course,student1.age,student1.feespaid)

student2 = Student("Pierre","MIT",26,100000)
print(student2.fullname,student2.course,student2.age,student2.feespaid)

student3 = Student("Jodie","CyberSecurity",18,90990)
print(student3.fullname,student3.course,student3.age,student3.feespaid)