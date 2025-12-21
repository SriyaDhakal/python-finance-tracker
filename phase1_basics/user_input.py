
"""
Learning Goals:
- Getting user input
- String formatting
- Basic calculations
"""

# Get user input for income and expense
print("=== Simple Budget Calculator ===\n")

# Get user input (always returns string)
name = input("What's your name? ")
print(f"Hello, {name}!")
income_input = input("enter your monthly income: $")

# Convert input strings to float
income=float(income_input) #if there is a decimal part in the income convert to float and assign to income
rent = float(input("Enter your rent: $"))
groceries = float(input("Enter grocery expenses: $"))
utilities = float(input("Enter utilities: $"))
entertainment = float(input("Enter entertainment: $"))

# Calculate totals
total_expenses = rent + groceries + utilities + entertainment
remaining = income - total_expenses
savings_percentage = (remaining / income) * 100
print(f"\nThank you, {name}! Here is your budget summary:")

#calculate savings
savings = income - total_expenses
print(f"Based on the income and expenses you provided:")
print(f"- Monthly Income: ${income}")
print(f"- Monthly Expenses: ${total_expenses}")
print(f"- Monthly Savings: ${savings}\n")  

# Conditional check
if remaining > 0:
    print("✓ You're saving money!")
elif remaining == 0:
    print("⚠ You're breaking even.")
else:
    print("✗ You're overspending!")
