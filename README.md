# transaction-tracker
A Python project that will track a user's transactions. Users will be able to securely input and view their purchases and perform data analytics to get a better sense of their total spending within an allotted time.

# Link
https://github.com/Team-Infinite-Void/transaction-tracker

# QR Authenticator Steps

* When you create an account, the program will automatically generate a qr code for you within the project folder. You may need to refresh. Scan the qr code with the Google Authenticator app and input the code from the Google Authenticator app when attempting to login. If it is correct it will allow you to login.
  
## Currently implemented
  * Text-based menu for the user to choose what they would like to do.
    * Adding/deleting records, viewing all records, exiting the program, and delete their account.
  * User account database that displays an interactive login/create account menu.
    * Once logged in, users can interact with the main menu.
    * Stores encrypted usernames and passwords in an SQLite3 database locally
    * Provides login, add account, delete account, and menu functionality.
    * QR Authenticator that works with Google Authenticator. It sends an OTP to your phone that you need to login.

## Pending work
  * Create a transaction database using SQLite3.
  * Implement networking (currently, everything is done locally on the user's computer).
    * Authentication, database storage and access, etc.
  * Exports a Financial Report file


## Member current contributions and next steps:
  * Galen Chang
    * Created a series of functions that create and interact with an encrypted SQLite3 database locally.  Users will see a login prompt first that also gives them the option of creating their account.  Once authenticated, users can delete their account as well as access all the functionality the main menu provides.
    * Next step will be to implement the transaction database using SQLite3.

  * Josiah Kila
    * I added the remaining functions to the menu to view Analytics. I also added a timestamp feature to track when someone makes a transaction. Additonaly, I added a filtering system so the user cannot input incorrect data.
   
    * Assignment 3: I added further security by adding a qr code generator and using Google Authenticator to generate an OTP for users trying to login. If this was a real transaction tracker with important information such as bank info and account records, this would be an extra barrier for any hacker.

  * Chris Dang

  * Michelle Ho
    * I have created the text-based menu and will work on an option to perform data analytics on the recorded transactions. This includes The total sum of expense savings for a given period. That also means including a date-time functionality for each record.
