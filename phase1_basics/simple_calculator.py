"""
Learning Goals:
- Conditionals (if/elif/else)
- Loops (while)
- User interaction
"""

def simple_calculator():
    print("=== Finance Calculator ===")

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Calculate  Percentage")
        print("4. CALCULATE SAVINGS RATE")
        print("5. Exit")

        print("Enter the number of the operation you want to perform:")
        choice = input() #Get user input for choice of operation this is one method to get user input

        #The other method for user input
        #choice = int(input("Enter the number for which operation you want to perform: "))

        if choice == '5':
            print("Exiitng the calculator , goodbye!")
            break
        

        if choice == '1':
            print("\n--- ADD TWO NUMBERS ---")
            num1 = float(input("Enter First number:"))
            num2 = float(input("Enter Second number:")) 
            print(f"{num1 + num2}")

        elif choice == '2':
            print("\n--- SUBTRACT TWO NUMBERS ---")
            num1 = float(input("Enter First number:"))
            num2 = float(input("Enter Second number:"))
            print(f"{num1 - num2}")

        elif choice == '3':
            print("\n--- CALCULATE PERCENTAGE ---")
            num1 = float(input("Enter First number:"))
            num2 = float(input("Enter Second number:"))
            print(f"{(num1 / num2) * 100}%")

        elif choice == '4':
            print("\n--- CALCULATE SAVINGS RATE ---")
            income = float(input("Monthly income: $"))
            expenses = float(input("Monthly expenses: $"))
            if income != 0:
                savings_rate = ((income - expenses) / income) * 100
                print(f"Savings Rate: {savings_rate}%")
            if expenses != 0:
                print(f"{income / expenses * 100}%")    
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please try again.")  