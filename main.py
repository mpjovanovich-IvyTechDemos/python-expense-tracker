# This is the entry point for the expense tracker.
# It shows the menu, collects user input, and calls functions
# from the other modules to do the actual work.

from datetime import date
from models import Expense
from storage import load_expenses, save_expenses
from reports import print_all_expenses, print_total, print_by_category


def get_menu_choice():
    """Display the main menu and return the user's choice."""
    print("=" * 40)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("  1. Add an expense")
    print("  2. View all expenses")
    print("  3. View total spent")
    print("  4. View spending by category")
    print("  5. Delete an expense")
    print("  6. Quit")
    print("=" * 40)
    choice = input("Enter your choice (1-6): ")
    return choice


def add_expense(expenses):
    """
    Ask the user for expense details, create an Expense object,
    add it to the list, and save to disk.
    """
    print("\n-- Add New Expense --")

    # Default the date to today, but let the user override it
    today = str(date.today())
    entered_date = input(f"Date (press Enter for today, {today}): ")
    if entered_date.strip() == "":
        entered_date = today

    category = input("Category (e.g. Food, Transport, Bills): ").strip()
    description = input("Description: ").strip()

    # Keep asking until we get a valid number
    while True:
        amount_text = input("Amount: $")
        try:
            amount = float(amount_text)
            break
        except ValueError:
            print("  Please enter a valid number (e.g. 12.50)")

    new_expense = Expense(
        date=entered_date,
        category=category,
        description=description,
        amount=amount
    )

    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"\n  Expense added and saved!\n")


def delete_expense(expenses):
    """
    Show a numbered list of expenses and let the user pick one to delete.
    """
    if len(expenses) == 0:
        print("No expenses to delete.\n")
        return

    print("\n-- Delete an Expense --")
    for i in range(len(expenses)):
        expense = expenses[i]
        print(f"  {i + 1}. {expense.date}  {expense.category:<15}  ${expense.amount:.2f}  {expense.description}")

    print()
    choice_text = input("Enter the number of the expense to delete (or 0 to cancel): ")

    try:
        choice = int(choice_text)
    except ValueError:
        print("  Invalid input, returning to menu.\n")
        return

    if choice == 0:
        print("  Cancelled.\n")
        return

    if choice < 1 or choice > len(expenses):
        print("  Number out of range, returning to menu.\n")
        return

    # Lists are 0-indexed, but we showed the user 1-indexed numbers
    removed = expenses.pop(choice - 1)
    save_expenses(expenses)
    print(f"\n  Deleted: {removed.description} (${removed.amount:.2f})\n")


def main():
    """
    The main loop. Load expenses once at startup, then keep showing
    the menu until the user chooses to quit.
    """
    expenses = load_expenses()

    while True:
        choice = get_menu_choice()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            print_all_expenses(expenses)
        elif choice == "3":
            print_total(expenses)
        elif choice == "4":
            print_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("\nGoodbye!\n")
            break
        else:
            print("\n  Invalid choice, please enter a number from 1 to 6.\n")


# This is the standard Python idiom for "run main() only if this file
# is executed directly, not if it's imported by another file."
if __name__ == "__main__":
    main()
