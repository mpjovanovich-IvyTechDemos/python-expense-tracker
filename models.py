# This file defines what an "Expense" looks like.
# Think of it as a blueprint for the data we want to store.

# A dataclass is a convenient way to create a class that mainly holds data.
# It automatically gives us __init__, __repr__, and other useful methods.
from dataclasses import dataclass


@dataclass
class Expense:
    """Represents a single expense entry."""

    date: str        # Date as a string, e.g. "2024-06-15"
    category: str    # e.g. "Food", "Transport", "Entertainment"
    description: str # e.g. "Lunch at campus cafe"
    amount: float    # e.g. 12.50

    def display(self):
        """Print this expense in a readable format."""
        print(f"  {self.date}  |  {self.category:<15}  |  ${self.amount:>7.2f}  |  {self.description}")
