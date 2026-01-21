"""
Learning Goals:
- Reading and writing JSON files
- Persistent data storage
- File operations
- Error handling basics
"""

import json
import os
from _datetime import datetime

Data_FILE = "expenses_data.json"

def load_expenses():
    """Load expenses from a JSON file."""
    if not os.path.exists(Data_FILE):
        return []
    with open(Data_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
        