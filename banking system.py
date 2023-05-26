import sys
import random

print("--------------ABC bank--------------")

choice = input("Are you a new customer? (yes/no): ")

if choice.lower() == 'yes':
    input("Press enter to create a new account")

    name = input("Enter your name: ")
    phone_num = input("Enter your phone number: ")
    account_num = random.randint(1000000000, 9999999999)
    pin = random.randint(1000, 9999)
    print("Hi", name, "Welcome to ABC BANK")
    print("Account details")
    print("------------------")
    print("Name:", name)
    print("Mobile number:", phone_num)
    print("Account number:", account_num)
    print("Your PIN number is:", pin)
    print("------------------")

    account_info = {
        'Name': name,
        'Mobile number': phone_num,
        'Account number': account_num,
        'PIN': pin
    }

    balance = 0

    def balance_check():
        global balance
        print("---------------------------")
        print("Your balance is $", balance)
        print("---------------------------")

    def withdraw(amount):
        global balance
        if amount > balance:
            print("---------------------------")
            print("Insufficient funds")
            print("---------------------------")
        else:
            balance -= amount
            print("---------------------------")
            print("Withdrawal successful")
            print("---------------------------")
            choice = input("Do you want to know your current balance? (yes/no): ")
            if choice.lower() == 'yes':
                balance_check()

    def deposit(amount):
        global balance
        balance += amount
        print("---------------------------")
        print("Amount $", amount, "is deposited successfully")
        print("Your current balance is: $", balance)
        print("---------------------------")

    def pin_change():
        global pin
        current_pin = int(input("Enter your current PIN: "))
        if current_pin != pin:
            print("Wrong PIN. Please try again.")
            return
        new_pin = int(input("Enter your new PIN: "))
        pin = new_pin
        print("Your new PIN is", pin)
        print("PIN changed successfully")

    def login():
        i = 0
        while i <= 2:
            password = int(input("Enter your 4-digit PIN: "))
            if password == pin:
                print("HI,", name)
                return True
            else:
                print("Wrong PIN! Please try again.")
                i += 1
                if i == 2:
                    print("Last chance to enter the correct PIN.")
                elif i == 3:
                    print("Access denied... Try again later.")
                    sys.exit()


    def main_menu():
        while True:
            print("---------------------------")
            print("1. Balance check")
            print("2. Withdrawal")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Exit")
            print("---------------------------")

            choice = int(input("Choose an option: "))
            if choice == 1:
                balance_check()
            elif choice == 2:
                amount = float(input("Enter the amount: $"))
                withdraw(amount)
            elif choice == 3:
                amount = float(input("Please enter the deposit amount: $"))
                deposit(amount)
            elif choice == 4:
                pin_change()
            elif choice == 5:
                print("Thank you for using ABC bank")
                sys.exit()
            else:
                print("Invalid selection")

    # Main program flow
    logged_in = login()
    if logged_in:
        print("---------------------------")
        print("Login successful!")
        print("Welcome to ABC Bank,", name)
        print("---------------------------")
        main_menu()
    else:
        print("Access denied... Try again later.")

elif choice.lower() == 'no':
    account_info = {
        'Name': 'naslu ab',
        'Mobile number': '7994641998',
        'Account number': '1234567890',
        'PIN': '1234'
    }

    balance = 0

    def balance_check():
        global balance
        print("---------------------------")
        print("Your balance is $", balance)
        print("---------------------------")

    def withdraw(amount):
        global balance
        if amount > balance:
            print("---------------------------")
            print("Insufficient funds")
            print("---------------------------")
        else:
            balance -= amount
            print("---------------------------")
            print("Withdrawal successful")
            print("---------------------------")
            choice = input("Do you want to know your current balance? (yes/no): ")
            if choice.lower() == 'yes':
                balance_check()

    def deposit(amount):
        global balance
        balance += amount
        print("---------------------------")
        print("Amount $", amount, "is deposited successfully")
        print("Your current balance is: $", balance)
        print("---------------------------")

    def pin_change():
        global account_info
        current_pin = input("Enter your current PIN: ")
        if current_pin != account_info['PIN']:
            print("Wrong PIN. Please try again.")
            return
        new_pin = input("Enter your new PIN: ")
        account_info['PIN'] = new_pin
        print("Your new PIN is", new_pin)
        print("PIN changed successfully")

    def login():
        global account_info
        i = 0
        while i <= 2:
            password = input("Enter your 4-digit PIN: ")
            if password == account_info['PIN']:
                print("HI,", account_info['Name'])
                return True
            else:
                print("Wrong PIN! Please try again.")
                i += 1
                if i == 2:
                    print("Last chance to enter the correct PIN.")
                elif i == 3:
                    print("Access denied... Try again later.")
                    sys.exit()


    def main_menu():
        while True:
            print("---------------------------")
            print("1. Balance check")
            print("2. Withdrawal")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Exit")
            print("---------------------------")

            choice = int(input("Choose an option: "))
            if choice == 1:
                balance_check()
            elif choice == 2:
                amount = float(input("Enter the amount: $"))
                withdraw(amount)
            elif choice == 3:
                amount = float(input("Please enter the deposit amount: $"))
                deposit(amount)
            elif choice == 4:
                pin_change()
            elif choice == 5:
                print("Thank you for using ABC bank")
                sys.exit()
            else:
                print("Invalid selection")

    # Main program flow
    logged_in = login()
    if logged_in:
        print("---------------------------")
        print("Login successful!")
        print("Welcome to ABC Bank,", account_info['Name'])
        print("---------------------------")
        main_menu()
    else:
        print("Access denied... Try again later.")

else:
    print("Invalid choice. Please try again.")

