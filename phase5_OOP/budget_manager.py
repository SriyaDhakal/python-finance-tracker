"""
Learning Goals:
- Class composition
- Managing collections
- Class methods
"""
import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d')
    
    def to_dict(self):
        return {
            'date': self.date,
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }

class BudgetManager:
    """Manages all expenses and budgets"""
    
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0
    
    def set_budget(self, amount):
        """Set monthly budget"""
        self.monthly_budget = amount
    
    def add_expense(self, amount, category, description):
        """Add a new expense"""
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        return expense
    
    def get_total_expenses(self):
        """Calculate total expenses"""
        return sum(exp.amount for exp in self.expenses)
    
    def get_remaining_budget(self):
        """Calculate remaining budget"""
        return self.monthly_budget - self.get_total_expenses()
    
    def get_expenses_by_category(self):
        """Group expenses by category"""
        categories = {}
        for exp in self.expenses:
            if exp.category in categories:
                categories[exp.category] += exp.amount
            else:
                categories[exp.category] = exp.amount
        return categories
    
    def display_summary(self):
        """Display financial summary"""
        print("\n=== Budget Summary ===")
        print(f"Monthly Budget: ${self.monthly_budget:.2f}")
        print(f"Total Spent: ${self.get_total_expenses():.2f}")
        print(f"Remaining: ${self.get_remaining_budget():.2f}")
        
        print("\nExpenses by Category:")
        for category, amount in self.get_expenses_by_category().items():
            print(f"  {category}: ${amount:.2f}")

# Usage
manager = BudgetManager()
manager.set_budget(3000)
manager.add_expense(500, "Rent", "Monthly rent")
manager.add_expense(200, "Food", "Groceries")
manager.add_expense(50, "Transport", "Gas")
manager.display_summary()
