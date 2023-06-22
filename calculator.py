def addition (x , y):
    return x+ y 

def subtraction (a, b) :
    return a - b

def multiplication( first, second):
    return first*second

def division (x, y):
    return x/y

number1 = int(input("Enter your first number: ", ))
number2= int(input("Enter your second number: ", ))

print("Addition: ", addition(number1, number2))
print("Subtraction: ", subtraction(number1, number2))
print("Multiplication: ", multiplication(number1, number2))
print("Divison: ", round(division(number1, number2),3))