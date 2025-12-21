# Variables for personal finance
income = 5000  # Integer
expense = 2500.50  # Float
category = "Groceries"  # String
is_paid = True  # Boolean

# Display the variables
print("Income:", income)
print("Expense:", expense)
print("Category:", category)
print("Is Paid:", is_paid)

# Type conversion
income_str = "6000"
income_num = int(income_str)
print(f"Converted income: ${income_num}")

# Calculate and display savings
savings = income - expense
print("Savings:", savings)  # Update and display expense
expense = 3000.75
print("Updated Expense:", expense)
print("Updated Savings:", income - expense)         