print("==============================")
print("       PYTHON CALCULATOR")
print("==============================")
print("Welcome to Calculator 2.0!")


# Mathematical Functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

history = []
total_calculations = 0
symbols = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/"
}
# Main Calculator Loop
while True:

    print("\nSelect an Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("\nEnter your choice (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select 1-4.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)


        elif choice == "4":

            result = divide(num1, num2)

        print("\nResult:", result)
        history.append(f"{num1} {symbols[choice]} {num2} = {result}")
        total_calculations += 1


    except ValueError:
        print("Error: Please enter valid numbers.")

    again = input("\nCalculate again? (yes/no/history/clear): ").strip().lower()

    if again == "history":
        print("\n===== CALCULATION HISTORY =====")

        if history:
            for item in history:
                print(item)
            print("Total calculations:", total_calculations)
        else:
            print("No calculations yet.")


    elif again == "clear":
        history.clear()
        print("Calculation history cleared!")

    elif again != "yes":
        print("Thank you for using Calculator!")
        break
