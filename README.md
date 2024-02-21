# transaction-tracker
A Python project that will track a user's transactions. Users will be able to securely input and view their purchases and perform data analytics to get a better sense of their total spending within an allotted time.

## Currently implemented
  * Text-based menu for the user to choose what they would like to do.<br />
    * Adding/deleting records, viewing all records, exiting the program, and delete their account.<br />
  * User account database that displays an interactive login/create account menu.<br />
    * Once logged in, users can interact with the main menu.<br />
    * Stores encrypted usernames and passwords in an SQLite3 database locally.<br />
    * Provides login, add account, delete account, and menu functionality.

## Pending work
  * Create a transaction database using SQLite3<br />
  * Implement networking (currently, everything is done locally on the user's computer)<br />
    * Authentication, database storage and access, etc.


## Member current contributions and next steps:
  * Galen Chang
    * Created a series of functions that create and interact with an encrypted SQLite3 database locally.  Users will see a login prompt first that also gives them the option of creating their account.  Once authenticated, users can delete their account as well as access all the functionality the main menu provides.
    * Next step will be to implement the transaction database using SQLite3.

  * Josiah Kila

  * Chris Dang

  * Michelle Ho
    * I have created the text-based menu and will work on an option to perform data analytics on the recorded transactions. This includes The total sum of expense savings for a given period. That also means including a date-time functionality for each record.
