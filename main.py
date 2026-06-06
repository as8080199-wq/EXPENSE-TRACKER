expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append({
            "item": item,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        print("\n--- Expenses ---")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(f"{expense['item']} - ₹{expense['amount']}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\nTotal Expenses: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")