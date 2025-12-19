from account import Account
from current_account import CurrentAccount
from savings_account import SavingsAccount
from user import User


accounts : list[Account] = []  #storing multiple types of accounts in a polymorphic way (savings, current accounts)
users : list[User]= []


def find_user(user_id):
    for usr in users:
        if usr.get_nic() == user_id:
            return usr
    return None

def list_users():
    for usr in users:
        print(f"""
            username - {usr.get_name()}
            contact - {usr.get_contact()}
            Nic - {usr.get_nic()}
                    
            """)

def find_account(account_num):
    for account in accounts:
        if account.account_no == account_num:
            return account

    return None


def list_accounts():
    for acc in accounts:
        print(f"""
                Account No - {acc.account_no}
                Balance - {acc.balance}
                """)

def get_float(message):
    while True:
        value = input(message)

        if value.strip() == "":
            print("Value cannot be empty")
            continue

        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")


while True:
    print("""
================= Baning System ========================

            1- press 1 to create a user
            2- press 2 to create an account
            3- press 3 to list all users
            4- press 4 to list all accounts
            5- press 5 to deposit money
            6- press 6 to withdraw money
            7- press 7 to check account balance
            8- press 8 to add interest (savings only)
            9- press 9 to add cheque id
            10-press 0 to exit 
========================================================
     """)

    try:

        choice = int(input("Enter choice: "))

    except ValueError:
        print("Invalid input! please enter a number.")
        continue


    if choice == 1:
        nic = input("Enter NIC No: ")
        if find_user(nic):
            print("user already exists!")
            continue

        name = input("Enter Name:")
        contact = int(input("Enter Contact No: "))

        user = User(nic, name, contact)
        users.append(user)

    elif choice == 2:
        account_no = input("Enter Account No: ")
        if find_account(account_no):
            print("Account already exists!")
            continue

        balance = get_float("Enter Balance: ")
        branch = input("Enter Branch: ")
        user_nic = input("Enter User NIC: ")

        user = find_user(user_nic)

        if user is not None:
            account_type = input("Enter Account Type -> Savings/Current: ").lower()

            if account_type == "savings":
                atm_card_no = input("Enter Card No: ")
                savings_account = SavingsAccount(account_no, balance, branch, user, atm_card_no)

                accounts.append(savings_account)

            if account_type == "current":
                cheque_id = int(input("Enter cheque id: "))
                current_account = CurrentAccount(account_no, balance, branch, user,  [cheque_id])

                accounts.append(current_account)


    elif choice == 3:
        list_users()

    elif choice == 4:
        list_accounts()

    elif choice == 5:
        account_number = input("Enter Account number to deposit money: ")
        user_account = find_account(account_number)

        if user_account is not None:
            try:
                amount = float(input("Enter deposit amount: "))
                user_account.deposit(amount)
                print("Deposit successful!")

            except Exception as e:
                print(e)

        else:
            print("Account Not found!")

    elif choice == 6:
        account_number = input("Enter Account number to withdraw money: ")
        user_account = find_account(account_number)

        if not user_account:
            print("Account Not found!")
            continue

        try:
            amount = float(input("Enter withdrawal amount: "))
            user_account.withdrawal(amount)
            print("Withdrawal successful!")

        except Exception as e:
            print(e)

    elif choice == 7:
        account_number = input("Enter Account number to check balance: ")
        user_account = find_account(account_number)

        if user_account:
            print(f"Current balance: {user_account.check_balance()}")

        else:
            print(f"Account not found!")

    elif choice == 8:
        account_number = input("Enter Account number to add interest: ")
        user_account = find_account(account_number)

        if isinstance(user_account, SavingsAccount):
            user_account.add_interest()
            print("Interest added successfully")

        else:
            print("This is not savings account!")

    elif choice == 9:
        account_number = input("Enter Account number to add cheque id: ")
        user_account = find_account(account_number)

        if isinstance(user_account, CurrentAccount):
            cheque_id = input("Enter cheque id: ")

            if user_account.search_cheque_id(cheque_id):
                print("Cheque ID already exists for this account!")


            else:
                user_account.add_cheque_id(cheque_id)
                print("Cheque ID added successfully!")

        else:
            print("This is not a current account!")

    elif choice == 0:
        print("Exiting... Thank You!")

    else:
        print("Invalid choice. Please try again.")





