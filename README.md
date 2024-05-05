# transaction-tracker
A Python project that will track a user's transactions. Users will be able to securely input and view their purchases and perform data analytics to get a better sense of their total spending within an allotted time.

## Progress (Feb 21)
* **User Interaction Menu:** Text-based menu allowing users to navigate various functionalities.
* **User Account Database:** Features an interactive login and account creation menu.

## Progress (Mar 28)
* **QR Authenticator:** Integration with Google Authenticator for two-factor authentication during login.
* **SQLite3 Transaction Database:** Utilizes SQLite3 to store user data and transaction records securely.
* **Improved Functions:** Ongoing refinements to existing functionalities for better performance and usability.
* **Code Organization:** Reorganized `.py` files for better clarity and maintainability, such as moving account-related functions to `account_database_functions.py`.

## Progress (Apr 11)
* **Improved Functions:** Ongoing refinements to existing functionalities for better performance and usability.
* **Error Handling:** Addition of more robust error handling.
* **Code Organization:** Ongoing reorganization of functions and general code style.
* **Fuzz Testing:** Verified that application handles random input.
* **John The Ripper Testing:** Tested security of database encryption algorithm.
* **SQL Injection Testing:** Verified application is not vulnerable to SQL injection attacks.

## Link to Repository
[Transaction Tracker GitHub Repository](https://github.com/Team-Infinite-Void/transaction-tracker)

## Currently Implemented Features
* **User Interaction Menu:** Text-based menu allowing users to navigate various functionalities.
  * Add/delete records, view all records, exit program, delete account.
* **User Account Database:** Features an interactive login and account creation menu.
  * Encrypted usernames and passwords stored in a local SQLite3 database.
  * Includes functionalities for login, account creation, account deletion, and main menu access.
* **Transactions Database:** Interact with transaction records through a dedicated menu.
  * Transactions are stored in cleartext in an SQLite3 database, named after the user's hashed account name.
  * Supports adding, deleting, viewing all transactions, and viewing transaction analytics.
* **QR Authenticator:** Upon creating an account, the program automatically generates a QR code within the project folder.
  * Refresh the folder view to see the QR code.
  * Scan the QR code with the Google Authenticator app and input the provided code during login for enhanced security.

## Pending Work (Feb 21)
* **Transaction Database:** Create a transaction database using SQLite3.
* **Networking Implementation:** Transition from local storage to networked database interactions for enhanced security and accessibility.

## Pending Work (Mar 28)
* **Networking Implementation:** Transition from local storage to networked database interactions for enhanced security and accessibility.
* **Financial Report Exporting:** Development of functionality to export comprehensive financial reports.
* **Function Improvements:**
  * Enhance the analytics features, which are currently facing bugs in integration with SQLite3.
  * Implement hashing for all entries in the transaction database to secure data further.

## Pending Work (Apr 11)
* **Networking Implementation:** Transition from local storage to networked database interactions for enhanced security and accessibility.
* **Financial Report Exporting:** Development of functionality to export comprehensive financial reports.
* **Function Improvements:**
  * Enhance the analytics features, which are currently facing bugs in integration with SQLite3.
  * Implement hashing for all entries in the transaction database to secure data further.
  * Add complexity requirements to username and password.

## Member Contributions and Next Steps
### **Galen Chang:**
  * **Feb 21**
    * **Work Done:** Implemented encrypted SQLite3 database functionalities for user account management.
    * **Current and Next Steps:** Implement transaction database using SQLite3.

  * **Mar 28**
    * **Work Done:** Implemented cleartext SQLite3 database functionalities for transaction management.
    * **Current and Next Steps:** Encrypt the transaction database and debug analytics function.

  * **Apr 11**
    * **Work Done:** Tested password cracking tool "John The Ripper" against encrypted user account database.
    * **Current and Next Steps:** Encrypt the transaction database, debug analytics function, and implement username and password complexity requirements.

### **Josiah Kila:**
  * **Feb 21**
    * **Work Done:** Added transaction timestamping, analytics functions, and data input validation systems.
    * **Current and Next Steps:** Refinement of analytics and input validation.

  * **Mar 28**
    * **Work Done:** Enhance the security model by refining the QR code generator and OTP validation systems to protect sensitive user data.
    * **Current and Next Steps:** Research additional security measures we could add.

  * **Apr 11**
    * **Work Done:** Conducted fuzzing tests to ensure application handles unexepcted input.
    * **Current and Next Steps:** Research additional security measures we could add and code refinement.

### **Chris Dang:**
  * **Feb 21**
    * **Work Done:** Conducted tests to ensure currently implemented functions worked as expected.
    * **Current and Next Steps:** Research additional security measures we could add.

  * **Mar 28**
    * **Work Done:** Conducted a Risk Assessment and verification methods and how solutions were executed.
    * **Current and Next Steps:** Continue to enhance our project documentation and risk assessment strategies.

  * **Apr 11**
    * **Work Done:** Assisted in testing hacks against our application.
    * **Current and Next Steps:** Continue to enhance our project documentation and risk assessment strategies.

### **Michelle Ho:**
  * **Feb 21**
    * **Work Done:** Developed the initial text-based user interaction menu and data analytics functionalities.
    * **Current and Next Steps:** Refinement of UI menu and analytics functions.

  * **Mar 28**
    * **Work Done:** Further refined code so functions were optimized and UI was enhanced to be more user friendly.
    * **Current and Next Steps:** Continue to refine code and consider additional security measures.

  * **Apr 11**
    * **Work Done:** Conducted SQL injection attacks to test security of application databases.
    * **Current and Next Steps:** Expand the data analytics options to include comprehensive expense tracking and reporting, integrating date-time functionality for each transaction record.

# Part IV: Final Wrap-Up and Documentation

## Division of Labor

- **Galen Chang**: Implemented and tested all database encryption and ensured all data is securely handled.
- **Josiah Kila**: Led the testing phase, ensuring all functionalities meet the performance standards.
- **Chris Dang**: Managed the compilation of project documentation and was responsible for the final submission requirements.
- **Michelle Ho**: Oversaw the deployment of the final version and updated the project's Wiki page with the latest information.

## Technical Notes

### Specifications for Use
- **Operating System**: Compatible with Windows 10 and newer.
- **Python Version**: Requires Python 3.8 or higher.
- **Dependencies**: All dependencies are listed in the `requirements.txt` file.

### Installation Instructions
1. Clone the repository:
git clone https://github.com/Team-Infinite-Void/transaction-tracker

2. Install the required packages:
pip install -r requirements.txt

3. Run the application:
python transaction_tracker.py

## Developer Reflections

Looking back on our journey through the development of the Transaction Tracker, our team has encountered a range of emotions from exhilaration to frustration. Here are some key takeaways:

### Achievements
- **Robust Security Features**: Implementing QR-based two-factor authentication was a milestone that enhanced the security of our application significantly.
- **Dynamic Data Analysis Tools**: Developing complex data analytics functionalities that provide users with meaningful insights into their spending habits.
- **Implementation of Encryption Tools**: Utilized encryption tools to ensure data at rest is secure and protected.

### Challenges
- **Cross-Platform Compatibility**: Ensuring the application runs smoothly across different operating systems remains a challenge.
- **Performance Optimization**: Balancing complex features with optimal performance was particularly challenging during the initial phases.

### Surprises
- The adaptability of the team to unexpected technical challenges and the innovative solutions that were brainstormed during those times.

### Disappointments
- **Limited User Testing**: Due to time constraints, extensive user testing was not feasible, which could have provided more insights into user experience improvements.

### Disclaimers/Caveats
- The application is optimized for educational and demonstration purposes and may require modifications for commercial deployment.

## Important Links

- **Online Repository**: [Transaction Tracker GitHub Repository](https://github.com/Team-Infinite-Void/transaction-tracker)
- **Final Project Documentation**: [Project Documentation File](https://github.com/Team-Infinite-Void/transaction-tracker/blob/main/DOCUMENTATION.md)
- **Release Version of the Program**: [Release Version](https://github.com/Team-Infinite-Void/transaction-tracker/releases)
- **Wiki Page**: [Project Wiki](https://github.com/Team-Infinite-Void/transaction-tracker/wiki/Transaction-Tracker)
- **License**: [License](https://github.com/Team-Infinite-Void/transaction-tracker/blob/main/LICENSE.txt)
