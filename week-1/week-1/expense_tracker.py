expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def view_expenses():
    for e in expenses:
        print(f"{e['category']}: ${e['amount']}")

def total_expenses():
    total = sum(e['amount'] for e in expenses)
    print(f"Total: ${total}")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(amount, category)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
