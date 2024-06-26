import hashlib
import sqlite3
import pyotp
import qrcode
from cryptography.fernet import Fernet

# Function to connect to the database
def connect_to_account_db(user_db):
    return sqlite3.connect(user_db)

# Function to create a cursor for database operations
def create_account_cursor(sql_connection):
    try:
        cursor = sql_connection.cursor()
    except Exception as error:
        print(error)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS userdata (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            totp_secret TEXT NOT NULL,
            fernet TEXT NOT NULL
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
            username, fernet_key, success = login(cursor)
            if success == 0:
                return username, fernet_key
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

        row = cursor.fetchone()
        if row:
            secret = row[3]  # Assuming the OTP secret is stored in the fourth column
            if generate_and_verify_otp(secret):
                valid_login = True
                fernet_key = row[4]
                return username, fernet_key, 0
        else:
            print('Either the user doesn\'t exist or the credentials are invalid. Please try again.\n\n')

# Function to retrieve the user's OTP secret from the database
def get_user_secret(cursor, hashed_username):
    cursor.execute("SELECT totp_secret FROM userdata WHERE username = ?", (hashed_username,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        print("Failed to retrieve OTP secret.")
        return None

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
    fernet = (Fernet.generate_key())
    cursor.execute("INSERT INTO userdata (username, password, totp_secret, fernet) VALUES (?, ?, ?, ?)", (hashed_username, hashed_password, secret, fernet))
    sql_connection.commit()

    # Generate and display QR code
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="YourApp")
    generate_qr_code(totp_uri)

# Function to generate a QR code
def generate_qr_code(uri):
    qr = qrcode.make(uri)
    qr.save("YOUR_QR_CODE.png")
    print("QR code saved as YOUR_QR_CODE.png. Scan it with Google Authenticator.")

# Function to generate and verify OTP
def generate_and_verify_otp(secret):
    """Generate an OTP and prompt for verification."""
    totp = pyotp.TOTP(secret)
    #otp = totp.now()

    user_provided_otp = input("Enter the OTP from Google Authenticator: ")
    # Increase the verification window
    if totp.verify(user_provided_otp, valid_window=1):
        print("The OTP is valid.")
        return True
    else:
        print("The OTP is invalid.")
        return False

# Function to delete user account
def delete_account(username, sql_connection, cursor):
    delete_user = False

    while not delete_user:
        confirm = input('Are you sure you want to delete your account? (Y or N)')
        if confirm.upper() == 'Y':
            password = input('Please enter your password: ')
            hashed_username = hashlib.sha256(username.encode()).hexdigest()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (hashed_username, hashed_password))

            if cursor.fetchall():
                cursor.execute("DELETE FROM userdata WHERE username = ?", (hashed_username,))
                sql_connection.commit()
                delete_user = True
                print('User', username, 'was deleted.')
                print("Goodbye!")
                return False
            else:
                print('Either the user doesn\'t exist or the credentials are invalid. Please try again.\n\n')
        elif confirm.upper() == 'N':
            return True
        else:
            print('Invalid input. Please enter either \'Y\' or \'N\'.\n\n')
