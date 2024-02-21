import hashlib
import sqlite3
from sqlite3 import Error
import os.path

def check_if_db_exists(user_db):
    if os.path.isfile(user_db):
        return True
    else:
        return False


#https://www.sqlitetutorial.net/sqlite-python/creating-database/
def connect_to_db(user_db):
    # sqlite3.connect creates the database if it does not exist.
    return sqlite3.connect(user_db)
    
def create_cursor(sql_connection, user_db):
    try:
        cursor = sql_connection.cursor()
    except Error as error:
        print(error)
    finally:
        if os.path.getsize(user_db) != 0:
            print('exists')
            return cursor
            #return sql_connection.cursor()
        else:    
            # https://www.youtube.com/watch?v=3NEzo3CfbPg by NeuralNine
            #cursor = sql_connection.cursor()
            print('did not exist')
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS userdata (
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                );
            """)
            return cursor

def login_menu(sql_connection, cursor):
    cont = True

    while cont == True:
        print('Please select an option:\n')
        print('1) Login')
        print('2) Create an account')
        print('3) Exit')
        selection = input('Your choice: ')

        if selection == '1':
            # Pass username to menu() in menu.py
            return (login(cursor))
        elif selection == '2':
            add_user(sql_connection, cursor)
        elif selection == '3':
            print('Goodbye.')
            cont == False
            break
        else:
            print('Invalid selection.  Please try again.\n\n')

# https://www.youtube.com/watch?v=3NEzo3CfbPg by NeuralNine
def login(cursor):
    valid_login = False

    print('Logging in.\n')

    while valid_login == False:
        username = input('Username: ')
        password = input('Password: ')
    
        hashed_username = hashlib.sha256(username.encode()).hexdigest()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (hashed_username, hashed_password))

        if cursor.fetchall():
            valid_login = True
        else:
            print('Either the user doesn\'t exist or the credentials are invalid.  Please try again.\n\n')

    return username
            
# https://www.youtube.com/watch?v=3NEzo3CfbPg by NeuralNine
def add_user(sql_connection, cursor):
    print('Adding a new user.\n')
    username = input('Username: ')
    password = input('Password: ')
    password2 = input('Please enter password again: ')

    if password != password2:
        pw_not_equal = True
        while pw_not_equal:
            print('Passwords do not match.  Please try again.')
            password = input('Password: ')
            password2 = input('Please enter password again: ')
            if password == password2:
                pw_not_equal = False
    
    hashed_username = hashlib.sha256(username.encode()).hexdigest()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (hashed_username, hashed_password))
    sql_connection.commit()

# https://www.youtube.com/watch?v=3NEzo3CfbPg by NeuralNine
def remove_user(username, sql_connection, cursor):
    delete_user = False

    while delete_user == False:
        confirm = input('Are you sure you want to delete your account? (Y or N)')
        if confirm.upper() != 'Y':
            password = input('Please enter your password: ')
            hashed_username = hashlib.sha256(username.encode()).hexdigest()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (hashed_username, hashed_password))

            if cursor.fetchall():
                cursor.execute("DELETE FROM userdata (username, password) VALUES (?, ?)", (hashed_username, hashed_password))
                sql_connection.commit()
                delete_user = True
                print('User %a was deleted.\n', username)
            else:
                print('Either the user doesn\'t exist or the credentials are invalid.  Please try again.\n\n')
        elif confirm.upper() == 'N':
            break
        else:
            print('Invalid input.  Please enter either \'Y\' or \'N\'.\n\n')