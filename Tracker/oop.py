from datetime import datetime
import sqlite3

#OOP
class expense:
    def __init__(self):
        self.conn = sqlite3.connect("expense.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.create_index()

    def add_expense(self,u_id, name, date, price, description="",  category='Daily Expense'):
        query = """
                    INSERT INTO expenses(u_id, name, category, date, price, description)
                    VALUES(?, ?, ?, ?, ?, ?);
                """
        self.cursor.execute(query, (u_id, name, category, date, price, description))
        self.conn.commit()

    def display_expense(self):
        query = "SELECT * FROM expenses;"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for records in data:
            print(records)

    def create_table(self):
        query = """
                    CREATE TABLE IF NOT EXISTS expenses(
                    exp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    u_id INTEGER,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL, 
                    date TEXT NOT NULL, 
                    price REAL NOT NULL, 
                    description TEXT NOT NULL);
                """
        self.cursor.execute(query)

    def create_index(self):
        query = "CREATE INDEX IF NOT EXISTS idx_category ON expenses(category);"
        self.cursor.execute(query)
        query = "CREATE INDEX IF NOT EXISTS idx_u_id ON expenses(u_id);"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_expenses(self,expense_id):
        query = """
                    DELETE FROM expenses
                    WHERE exp_id = ?;
                """
        self.cursor.execute(query, (expense_id,))
        self.conn.commit()

    def close_conn(self):
        self.conn.close()

    