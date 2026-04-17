# This file handles saving and loading expenses from a file.
# Keeping file I/O here means the rest of the program never has
# to worry about *how* data is stored -- only that it is.

import json
import os
from models import Expense

# The name of the file where expenses will be saved.
DATA_FILE = "expenses.json"


def load_expenses():
    """
    Read expenses from the data file and return them as a list of Expense objects.
    If the file doesn't exist yet, return an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        raw_list = json.load(file)

    expenses = []
    for item in raw_list:
        expense = Expense(
            date=item["date"],
            category=item["category"],
            description=item["description"],
            amount=item["amount"]
        )
        expenses.append(expense)

    return expenses


def save_expenses(expenses):
    """
    Write a list of Expense objects to the data file.
    Each Expense is converted to a plain dictionary first,
    because JSON doesn't know how to serialize custom objects.
    """
    raw_list = []
    for expense in expenses:
        item = {
            "date": expense.date,
            "category": expense.category,
            "description": expense.description,
            "amount": expense.amount
        }
        raw_list.append(item)

    with open(DATA_FILE, "w") as file:
        json.dump(raw_list, file, indent=2)
