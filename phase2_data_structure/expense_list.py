"""
Learning Goals:
- Lists for storing multiple expenses
- Dictionaries for structured data
- Looping through data
- List methods (append, remove, etc.)
"""

# List to store expense dictionaries
expenses = []

def view_expenses():
    """View all expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\n" + "="*60)
    print(" ALL EXPENSES ".center(60))
    print("="*60)
    
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ${exp['amount']:7.2f} - {exp['category']:12} - {exp['date']}")
        total += exp['amount']
    
    print("="*60)
    print(f"TOTAL: ${total:.2f}")

def expense_summary_by_category():
    """Summarize expenses by category."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    summary = {}
    for exp in expenses:
        category = exp['category']
        amount = exp['amount']
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    
    print("\n" + "="*50)
    print(" EXPENSE SUMMARY BY CATEGORY ".center(50))
    print("="*50)
    
    for category, total in sorted(summary.items()):
        print(f"{category:20} ${total:10.2f}")
    
    print("="*50)
    print(f"{'TOTAL':20} ${sum(summary.values()):10.2f}")

def main():
    """Main function to run the expense tracker."""
    print("="*60)
    print(" EXPENSE TRACKER ".center(60))
    print("="*60)
    
    while True:
        print("\n--- MENU ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Summary by Category")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter expense amount: $"))
                category = input("Enter expense category: ")
                date = input("Enter expense date (YYYY-MM-DD): ")
                add_expense(amount, category, date)
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")
        
        elif choice == '2':
            view_expenses()
        
        elif choice == '3':
            expense_summary_by_category()
        
        elif choice == '4':
            print("\n" + "="*60)
            print("Thank you for using Expense Tracker!".center(60))
            print("Keep tracking your finances! 💰".center(60))
            print("="*60)
            break
        
        else:
            print("❌ Invalid choice. Please choose 1-4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()