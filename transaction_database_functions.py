from datetime import datetime
import os
import sqlite3

# Function to connect to the database
def connect_to_transaction_db(transaction_db):
    return sqlite3.connect(transaction_db)

# Function to create a cursor for database operations
def create_transaction_cursor(sql_connection, transaction_db, hashed_username):
    try:
        cursor = sql_connection.cursor()
        print("cursor success")
    except Exception as error:
        print(error)

    # if os.path.getsize(transaction_db) == 0:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS """ + hashed_username + """ (
            entry_num INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            profit TEXT NOT NULL,
            amount REAL NOT NULL
        );
    """)

    return cursor

class Transaction:
    def __init__(self, title, if_profit, amount):
        self.title = title
        self.if_profit = if_profit
        self.amount = amount
        self.time = datetime.now()  # Automatically set the time to the current datetime

    def get_title(self):
        return self.title

    def get_profit(self):
        return self.if_profit

    def get_amount(self):
        return self.amount

    # Not currently used for anything
    def get_time(self):
        # Return the time as a string in a readable format
        return self.time.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        return f'Title: {self.title}, Amount: {self.amount}, Time: {self.get_time()}'

def add_new_record(transaction_cursor, hashed_username):
    description = input("\nTitle of the transaction: Enter a short description\n")
    gained = input("Was this transaction a profit? (Y/N)\n")
    profit = gained.upper()
    # == 'Y'

    # Attempt to convert the amount input to a float with error handling
    while True:
        amount_input = input("Enter the amount of the transaction: Enter a decimal number\n")
        try:
            amount = float(amount_input)
            break  # Exit the loop if the conversion is successful
        except ValueError:
            print("Invalid amount. Please enter a valid decimal number.")

    transaction_cursor.execute("INSERT INTO " + hashed_username + " (description, profit, amount) VALUES (?, ?, ?)", (description, profit, amount))
    print(f'Successfully added a new transaction of {amount}.\n')

def delete_record(transaction_cursor, hashed_username):
    transaction_cursor.execute("SELECT * FROM " + hashed_username)
    length = len(transaction_cursor.fetchall())

    if length == 0:
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
    else:
        print("""***************
              All records to date:
              """)
        transaction_cursor.execute("SELECT ? FROM transactions.db WHERE type='table'", (hashed_username))
        print(transaction_cursor.fetchall())

        num_to_delete = input("Which record would you like to delete? Please enter one number: ")
        try:
            title = transaction_cursor.execute("SELECT description FROM " + hashed_username + " WHERE entry_num=?", (num_to_delete))
            transaction_cursor.execute("DELETE FROM " + hashed_username + " WHERE entry_num=?", (num_to_delete))
            print(f'Successfull deleted the transaction of {title}.\n')
        except Exception as error:
            print(error)
            return

def view_all_records(transaction_cursor, hashed_username):
    transaction_cursor.execute("SELECT * FROM " + hashed_username)
    length = len(transaction_cursor.fetchall())
    if length == 0:
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
    else:
        print("""***************
              All records to date:
              """)
        transaction_cursor.execute("SELECT * FROM " + hashed_username)
        print(transaction_cursor.fetchall())

def view_analytics(transaction_cursor, hashed_username):
    total_profit = transaction_cursor.execute("SELECT SUM(amount) FROM " + hashed_username + " WHERE profit = 'Y'")
    print(total_profit)
    total_loss = transaction_cursor.execute("SELECT SUM(amount) FROM " + hashed_username + " WHERE profit = 'N'")
    print(total_loss)
    net_balance = total_profit - total_loss

    transaction_cursor.execute("SELECT * FROM " + hashed_username)
    length = len(transaction_cursor.fetchall())

    print(f"***************\nAnalytics Summary:\n")
    print(f"Total Transactions: {length}")
    print(f"Total Profit: {total_profit}")
    print(f"Total Loss: {total_loss}")
    print(f"Net Balance: {net_balance}\n")
