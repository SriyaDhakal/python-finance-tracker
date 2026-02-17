"""
Learning Goals:
- Creating classes
- Instance methods
- __init__ constructor
- __str__ representation
"""

class Expense:
    def __init__(self, name, amount, category, description): # This method initializes the object's state
        self.name = name
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self): # This method defines what "print(person_object)" will output
        return f"{self.name}: ${self.amount:.2f} ({self.category}) - {self.description}"
    
    def to_dict(self):
        """Convert to dictionary for JSON"""
        return {
            'date': self.date,
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }

# Usage example
expense1 = Expense("Groceries", 50.00, "Food", "Weekly grocery shopping")
expense2 = Expense("Gas", 30.00, "Transport", "Fuel for the car")


print(expense1)
print(expense2)
