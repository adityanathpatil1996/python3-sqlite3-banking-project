import login_interface

def withdraw(user_balance):
    requested_amount = float(input("Enter the amount you want to withdraw: "))

    if requested_amount > user_balance:
        print("Insufficient Funds")

    else:
        user_balance -= user_balance - requested_amount

    login_interface.login_interface(user_balance)