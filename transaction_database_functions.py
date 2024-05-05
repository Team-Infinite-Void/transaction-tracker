import sqlite3
from cryptography.fernet import Fernet

# Function to connect to the database
def connect_to_transaction_db(transaction_db):
    return sqlite3.connect(transaction_db)

# Function to create a cursor for database operations
def create_transaction_cursor(sql_connection):
    try:
        cursor = sql_connection.cursor()
        print("cursor success")
    except Exception as error:
        print(error)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            entry INTEGER PRIMARY KEY,
            user TEXT NOT NULL,
            description TEXT NOT NULL,
            profit TEXT NOT NULL,
            amount TEXT NOT NULL
        );
    """)

    return cursor

def add_new_record(transaction_sql_connection, transaction_cursor, hashed_username, fernet_key):
    description = input("\nTitle of the transaction: Enter a short description\n")
    gained = input("Was this transaction a profit? (Y/N)\n")
    profit = gained.upper()

    # Attempt to convert the amount input to a float with error handling
    while True:
        amount_input = input("Enter the amount of the transaction: Enter a decimal number\n")
        try:
            amount = float(amount_input) # Ensure amount is a valid float
            amount = str(amount)
            break  
        except ValueError:
            print("Invalid amount. Please enter a valid decimal number.")

    # Encrypt the values that will be stored in the database
    fernet = Fernet(fernet_key)
    encrypted_description = fernet.encrypt(bytes(description, 'utf-8'))
    encrypted_profit = fernet.encrypt(bytes(profit, 'utf-8'))
    encrypted_amount = fernet.encrypt(bytes(amount, 'utf-8'))

    transaction_cursor.execute("INSERT INTO transactions (user, description, profit, amount) VALUES (?, ?, ?, ?)",
        (hashed_username, encrypted_description, encrypted_profit, encrypted_amount)
    )
    transaction_sql_connection.commit()
    print(f'Successfully added a new transaction of {amount}.\n')

def delete_record(transaction_cursor, hashed_username, fernet_key):
    transaction_cursor.execute("SELECT * FROM transactions WHERE user=?", (hashed_username,))
    length = len(transaction_cursor.fetchall())
    fernet = Fernet(fernet_key)

    if length == 0:
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
    else:
        print("""***************
              All records to date:
              """)

        transaction_cursor.execute("SELECT * FROM transactions WHERE user=?", (hashed_username,))

        for row in transaction_cursor:
            print(str(row[0]) + ": " + fernet.decrypt(row[2]).decode() + "     " + fernet.decrypt(row[3]).decode() + "     " + fernet.decrypt(row[4]).decode())

        num_to_delete = input("Which record would you like to delete? Please enter one number: ")
        try:
            transaction_cursor.execute("DELETE FROM transactions WHERE entry=?", (num_to_delete))
        except Exception as error:
            print(error)
            return

def view_all_records(transaction_cursor, hashed_username, fernet_key):
    fernet = Fernet(fernet_key)

    transaction_cursor.execute("SELECT * FROM transactions WHERE user=?", (hashed_username,))
    length = len(transaction_cursor.fetchall())
    if length == 0:
        print("No records in the database. Create a new record by selecting '1' in the main menu.\n")
    else:
        print("""***************
              All records to date:
              """)
        transaction_cursor.execute("SELECT * FROM transactions WHERE user=?", (hashed_username,))

        for row in transaction_cursor:
            print(fernet.decrypt(row[2]).decode() + "     " + fernet.decrypt(row[3]).decode() + "     " + fernet.decrypt(row[4]).decode())

def view_analytics(transaction_cursor, hashed_username, fernet_key):
    fernet = Fernet(fernet_key)
    total_profit = 0
    total_loss = 0
    net_balance = 0

    transaction_cursor.execute("SELECT * FROM transactions WHERE user=?", (hashed_username,))

    for row in transaction_cursor:
        if fernet.decrypt(row[3]).decode() == "Y":
            total_profit += float(fernet.decrypt(row[4]))
        elif fernet.decrypt(row[3]).decode() == "N":
            total_loss += float(fernet.decrypt(row[4]))
        else:
            print("Error getting amount.")
    net_balance = total_profit - total_loss

    transaction_cursor.execute("SELECT * FROM transactions WHERE user=?", (hashed_username,))
    length = len(transaction_cursor.fetchall())

    print(f"***************\nAnalytics Summary:\n")
    print(f"Total Transactions: {length}")
    print(f"Total Profit: {total_profit}")
    print(f"Total Loss: {total_loss}")
    print(f"Net Balance: {net_balance}\n")
