import os 


print ("\033[92m")
os.system("clear")
os.system("figlet -w 1200 ==== NS HACK ==== ")

print ("")
print ("--------------------- author :  NS HACK ---------------------------")
print ("-------------------- TOOL NAME : calculator ------------------------")
print (" ")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

def calculator():


    print("Welcome to the Calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter your choice (1-4): ")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        print("The result of addition is:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("The result of subtraction is:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("The result of multiplication is:", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("The result of division is:", result)
    else:
        print("Invalid choice. Please try again.")


calculator()
