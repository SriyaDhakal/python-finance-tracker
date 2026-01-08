"""
Learning Goals:
- Creating reusable functions
- Parameters and return values
- Function documentation (docstrings)
- Default parameters
"""

def calculate_savings(income, expenses):
    """
    Calculate monthly savings.

    Args:
        income (float): Monthly income
        expenses (float): Monthly expenses

    Returns:
        float: Amount saved
    """
    savings = income - expenses
    return savings


def calculate_savings_rate(income, expenses):
    """
    Calculate savings rate as a percentage.
    """
    savings = calculate_savings(income, expenses)
    return (savings / income) * 100 if income != 0 else 0


def format_currency(amount):
    """
    Format number as currency.
    """
    return f"${amount:,.2f}"


def get_financial_advice(savings_rate):
    """
    Provide financial advice based on savings rate.
    """
    if savings_rate >= 20:
        return "Excellent! You're saving a significant portion of your income."
    elif 10 <= savings_rate < 20:
        return "Good job! Consider increasing your savings rate."
    elif 0 < savings_rate < 10:
        return "You're saving, but there's room for improvement."
    else:
        return "You need to review your expenses and find ways to save."


def main():
    print("=== Personal Finance Calculator ===\n")

    income = float(input("Monthly income: $"))
    rent = float(input("Rent: $"))
    food = float(input("Food: $"))
    transport = float(input("Transport: $"))
    other = float(input("Other expenses: $"))

    total_expenses = rent + food + transport + other
    savings = calculate_savings(income, total_expenses)
    rate = calculate_savings_rate(income, total_expenses)

    print("\n--- Financial Summary ---")
    print(f"Income: {format_currency(income)}")
    print(f"Expenses: {format_currency(total_expenses)}")
    print(f"Savings: {format_currency(savings)}")
    print(f"Savings Rate: {rate:.1f}%")
    print(f"\nAdvice: {get_financial_advice(rate)}")


if __name__ == "__main__":
    main()
