import hashlib
from account_database_functions import connect_to_account_db, delete_account
from account_database_functions import create_account_cursor
from account_database_functions import login_menu
from transaction_database_functions import add_new_record
from transaction_database_functions import connect_to_transaction_db
from transaction_database_functions import create_transaction_cursor
from transaction_database_functions import delete_record
from transaction_database_functions import view_all_records
from transaction_database_functions import view_analytics

# Program execution starts here.
def main():
    # Set the database names
    account_database = 'userdatabase.db'
    transaction_database = 'transactions.db'
    print("vars success")

    # Connect to the databases
    account_sql_connection = connect_to_account_db(account_database)
    transaction_sql_connection = connect_to_transaction_db(transaction_database)
    print("database connection success")

    # Create SQL cursor to traverse the SQL databases
    account_cursor = create_account_cursor(account_sql_connection)
    print("account cursor success")

    # Attempt to login
    username, fernet_key = login_menu(account_sql_connection, account_cursor)
    hashed_username = hashlib.sha256(username.encode()).hexdigest()
    transaction_cursor = create_transaction_cursor(transaction_sql_connection)

    cont = True
    while cont:
        print(f'Logged in as {username}\n')
        choice = input("""***************
1. Add new record
2. Delete a record
3. View all records
4. View Analytics
5. Delete your account
6. Exit
Your choice: """)
        
        if choice == "1":
            add_new_record(transaction_sql_connection, transaction_cursor, hashed_username, fernet_key)
        elif choice == "2":
            delete_record(transaction_cursor, hashed_username, fernet_key)
        elif choice == "3":
            view_all_records(transaction_cursor, hashed_username, fernet_key)
        elif choice == "4":
            view_analytics(transaction_cursor, hashed_username, fernet_key)
        elif choice == "5":
            test = delete_account(username, account_sql_connection, account_cursor)
            print(test)
            if not test:
                cont = False
                break
        elif choice == "6":
            print("You chose to exit, goodbye!")
            cont = False
            break
        else:
            print("That was an invalid input. Please enter 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()
