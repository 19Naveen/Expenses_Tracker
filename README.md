
# Expense Tracker

## Overview
Expense Tracker is a simple Python application that allows users to manage their daily expenses. It utilizes SQLite to store data, with features such as adding, viewing, and deleting expenses. The application is implemented using Object-Oriented Programming (OOP) principles.

## Features
- Add new expenses with details such as name, category, price, description, and date
- Display all expenses
- Delete expenses based on a unique identifier (`exp_id`)
- Validate the date format (`YYYY-MM-DD`) before adding an expense
- Supports auto-incrementing `exp_id` for each new expense

## Technologies Used
- **Python 3.x**: The programming language used
- **SQLite3**: The database used to store expense data
- **OOP (Object-Oriented Programming)**: The design paradigm used for code structure

## Installation
To use this application, you need to have Python and SQLite installed.

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Adding an Expense
To add a new expense, call the `add_expense` method with the following parameters:

```python
tracker.add_expense(
    u_id=1,
    name="Lunch",
    date="2024-12-29",
    price=20.50,
    category="Food",
    description="Lunch at restaurant"
)
```

Parameters:
- `u_id`: Unique ID of the user (if applicable)
- `name`: Name of the expense item
- `date`: The date of the expense in YYYY-MM-DD format
- `price`: The price of the expense item
- `category`: The category of the expense
- `description`: Optional description of the expense

### Displaying Expenses
To display all the expenses stored in the database:

```python
tracker.display_expense()
```

### Deleting an Expense
To delete an expense based on its `exp_id`:

```python
tracker.delete_expenses(expense_id=1)
```

### Validating Date
To validate if a date is in the correct format (YYYY-MM-DD):

```python
validate_date("2024-12-29")  # Returns True if the date is valid, else False
```

## Project Structure
```
Expense_Tracker/
│
├── main.py                # Main application file
├── oop.py                # Contains the expense class and methods
├── tools.py              # Helper functions like date validation
├── requirements.txt      # List of dependencies
└── README.md            # Project documentation
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[NaveenkumarD] - [naveenkumar19082004.com]
[RajasriSneha] - [scrajasrisneha@gmail.com.com]