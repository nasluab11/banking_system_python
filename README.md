# banking_system_python
This Python code represents a basic banking system that allows users to create accounts, log in with a PIN, and perform various banking operations such as balance check, withdrawal, deposit, and PIN change. It supports both new and existing customers.

For new customers, the code generates a random account number and PIN, displays the account details, and guides them through the login and menu options. For existing customers, predefined account details are used for demonstration.

The code includes error handling and limits the number of login attempts. It provides a simple and functional interface for managing banking operations.


Here's an overview of the code structure and functionality:

1.The program starts by prompting the user if they are a new customer or not.

2.If the user chooses to create a new account, they are asked to enter their name and phone number. A random account number and PIN are generated for them. The account details are displayed, and the information is stored in the account_info dictionary.

3.If the user chooses not to create a new account, a pre-defined account_info dictionary is used for demonstration purposes.

4.The main functionality of the banking system is implemented through the following functions:

-balance_check: Prints the current balance.
-withdraw: Performs a withdrawal from the account balance, provided there are sufficient funds.
-deposit: Adds a specified amount to the account balance.
-pin_change: Allows the user to change their PIN by entering the current PIN and the new PIN.
-login: Prompts the user to enter their PIN and verifies it against the stored PIN in the account_info dictionary.
-main_menu: Displays the available options for the user to choose from and performs the corresponding banking operations based on their selection.


5.The program flow is controlled by the login function. If the login is successful, the user is presented with the main menu and can perform banking operations. Otherwise, access is denied.

6.The code includes appropriate error handling and input validation to ensure the program runs smoothly and handles user input correctly.
