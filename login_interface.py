import withdraw
import deposit
import update_user_balance_in_database

def login_interface(user_name, user_balance):

    option = input("Choose one of the following: " \
        "1.Withdrawl" \
        "2.Deposit" \
        "3.Check Balance"
        "4.Exit")

    if option == "1":
        withdraw.withdraw(user_balance)

    elif option == "2":
        deposit.deposit(user_balance)

    elif option == "3":
        print(user_balance)
        login_interface(user_balance)

    elif option == "4":
        update_user_balance_in_database.update_user_balance_in_database(user_name, user_balance)

    else:
        print("Invalid Choice")
        login_interface(user_balance)