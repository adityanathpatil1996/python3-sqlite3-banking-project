import login_interface

def deposit(user_balance):
    amount_to_deposit = float(input("Enter the amount that you want to deposit: "))
    user_balance += amount_to_deposit
    login_interface.login_interface(user_balance)