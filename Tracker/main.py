from datetime import datetime
from oop import expense
from Tools import date, validate_date


user_id = int(input("Enter new user ID: "))
exp = expense()

while True:
    print("Expense Tracker App")
    print("---------------------")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete expenses")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Expense name:")
        category = input("Enter category: ")
        while True:
            date = input("Enter a valid date (YYYY-MM-DD): ")
            if validate_date(date):
                break 
            else:
                print(f"The date '{date}' is invalid. Please try again.")

        price = float(input("Enter price: "))
        description = input("Enter Description")
        exp.add_expense(u_id=user_id, name=name, category=category, date=date, price=price, description=description)
        print("Expense added successfully!")
        
    elif choice == 2:
        exp.display_expense()
    elif choice == 3:
        expense_id = int(input('Enter Expense ID:'))
        exp.delete_expenses(expense_id)
    elif choice == 4:
        exp.close_conn()
        break
    else:
        "Invalid option"
        