def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def percentage(x, y):
    return (x * y) / 100

def power(x, y):
    return x ** y

def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def display_menu():
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Percentage (%)")
    print("6. Power (^)")
    print("7. Floor Division (//)")
    print("0. Exit")

while True:
    display_menu()
    choice = input("Enter choice (0-7): ")

    if choice == '0':
        print("Exiting calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Invalid input. Please enter a valid choice.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Please enter numeric values.")
        continue
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", percentage(num1, num2), "%")
    elif choice == '6':
        print("Result:", power(num1, num2))
    elif choice == '7':
        print("Result:", floor_division(num1, num2))
