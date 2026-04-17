# This file is responsible for summarizing and displaying expense data.
# It takes a list of Expense objects and produces useful output.
# Notice it doesn't know anything about files or user input -- just reporting.


def print_all_expenses(expenses):
    """Print every expense in the list."""
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print()
    print(f"  {'DATE':<12}  {'CATEGORY':<15}  {'AMOUNT':>9}  {'DESCRIPTION'}")
    print("  " + "-" * 65)
    for expense in expenses:
        expense.display()
    print()


def print_total(expenses):
    """Print the total amount spent across all expenses."""
    if len(expenses) == 0:
        print("No expenses to total.")
        return

    total = 0.0
    for expense in expenses:
        total = total + expense.amount

    print(f"\n  Total spent: ${total:.2f}\n")


def print_by_category(expenses):
    """
    Print a breakdown of spending grouped by category.
    We build a dictionary where each key is a category name
    and each value is the running total for that category.
    """
    if len(expenses) == 0:
        print("No expenses to summarize.")
        return

    # Build a dictionary of category totals
    category_totals = {}
    for expense in expenses:
        category = expense.category

        if category not in category_totals:
            category_totals[category] = 0.0

        category_totals[category] = category_totals[category] + expense.amount

    # Display the results
    print()
    print("  Spending by category:")
    print("  " + "-" * 30)
    for category in category_totals:
        total = category_totals[category]
        print(f"  {category:<20}  ${total:>7.2f}")
    print()
