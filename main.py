# *** simple calculator ***

print("\n******** Select an operations ********")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divide")

operation = input()

a = int(input("Enter the first number : "))
b = int(input("Enter the second number :"))

if operation == "1":
    Add = a+b
    print(f"Add:{Add}")

elif operation == "2":
    Subtract = a-b
    print(f"Subtract: {Subtract}")

elif operation == "3":
    Multiplication = a*b
    print(f"Multiplication: {Multiplication}")

elif operation == "4":
    Divide = a/b
    print(f"Divide: {Divide}")

else:
    print("Enter  a valid operation")
