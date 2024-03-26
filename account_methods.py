import hashlib
import os
import sqlite3
from sqlite3 import Error
import pyotp
import qrcode

# Function to connect to the database
def connect_to_db(user_db):
    return sqlite3.connect(user_db)

# Function to create a cursor for database operations
def create_cursor(sql_connection, user_db):
    try:
        cursor = sql_connection.cursor()
    except Error as error:
        print(error)

    if os.path.getsize(user_db) == 0:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS userdata (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                totp_secret VARCHAR(255) NOT NULL
            );
        """)

    return cursor

# Function to display login menu
def login_menu(sql_connection, cursor):
    cont = True

    while cont:
        print('Please select an option:\n')
        print('1) Login')
        print('2) Create an account')
        print('3) Exit')
        selection = input('Your choice: ')

        if selection == '1':
            username = login(cursor)
            if username:
                return username
        elif selection == '2':
            add_user(sql_connection, cursor)
        elif selection == '3':
            print('Goodbye.')
            cont = False
        else:
            print('Invalid selection. Please try again.\n\n')

# Function to handle user login
def login(cursor):
    valid_login = False

    print('Logging in.\n')

    while not valid_login:
        username = input('Username: ')
        password = input('Password: ')

        hashed_username = hashlib.sha256(username.encode()).hexdigest()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (hashed_username, hashed_password))

        if cursor.fetchall():
            valid_login = True
            generate_and_verify_otp(cursor, hashed_username)
            return username
        else:
            print('Either the user doesn\'t exist or the credentials are invalid. Please try again.\n\n')

# Function to add a new user
def add_user(sql_connection, cursor):
    print('Adding a new user.\n')
    username = input('Username: ')
    password = input('Password: ')
    password2 = input('Please enter password again: ')

    if password != password2:
        pw_not_equal = True
        while pw_not_equal:
            print('Passwords do not match. Please try again.')
            password = input('Password: ')
            password2 = input('Please enter password again: ')
            if password == password2:
                pw_not_equal = False

    secret = pyotp.random_base32()
    hashed_username = hashlib.sha256(username.encode()).hexdigest()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO userdata (username, password, totp_secret) VALUES (?, ?, ?)", (hashed_username, hashed_password, secret))
    sql_connection.commit()

    # Generate and display QR code
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="YourApp")
    generate_qr_code(totp_uri)

# Function to generate a QR code
def generate_qr_code(uri):
    qr = qrcode.make(uri)
    qr.save("YOUR_QR_CODE.png")
    print("QR code saved as YOUR_QR_CODE.png.png. Scan it with Google Authenticator.")

# Function to generate and verify OTP
def generate_and_verify_otp(cursor, hashed_username):
    row = cursor.execute("SELECT totp_secret FROM userdata WHERE username = ?", (hashed_username,)).fetchone()
    if row:
        secret = row[0]
        totp = pyotp.TOTP(secret)
        otp = totp.now()

        user_provided_otp = input("Enter the OTP from Google Authenticator: ")
        # Increase the verification window
        if totp.verify(user_provided_otp, valid_window=1):
            print("The OTP is valid.")
        else:
            print("The OTP is invalid.")
    else:
        print("User not found or OTP secret not set.")

# Function to delete user account
def delete_account(username, sql_connection, cursor):
    delete_user = False

    while not delete_user:
        confirm = input('Are you sure you want to delete your account? (Y or N)')
        if confirm.upper() != 'Y':
            password = input('Please enter your password: ')
            hashed_username = hashlib.sha256(username.encode()).hexdigest()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (hashed_username, hashed_password))

            if cursor.fetchall():
                cursor.execute("DELETE FROM userdata WHERE username = ?", (hashed_username,))
                sql_connection.commit()
                delete_user = True
                print('User', username, 'was deleted.\n')
            else:
                print('Either the user doesn\'t exist or the credentials are invalid. Please try again.\n\n')
        elif confirm.upper() == 'N':
            break
        else:
            print('Invalid input. Please enter either \'Y\' or \'N\'.\n\n')

# Main function
def main():
    user_db = "user_data.db"
    sql_connection = connect_to_db(user_db)
    cursor = create_cursor(sql_connection, user_db)

    # Start login menu
