#A simple python calculator program

#when the program runs, it prompts the user to enter first no., operator and second no. Based on the operator entered
# it should provide the correct output

# Simple Python Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
     result = num1 / num2
     print("Result:", result)

else:
    print("Invalid operator. Please use +, -, *, or /.")

