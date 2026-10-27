import get_user_balance_from_database
import login_interface

def logged_in(logged_in_user_name):
    logged_in_user_balance = get_user_balance_from_database.get_user_balance_from_database()
    login_interface.login_interface(logged_in_user_name, logged_in_user_balance)