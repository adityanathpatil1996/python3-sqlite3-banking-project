import bcrypt
import logged_in

def verify_credentials(credentials_tuples_list):
    entered_user_name = input("Enter your Username: ")
    entered_pin = input("Enter PIN: ")
    entered_pin_in_byte = entered_pin.encode("utf-8")

    is_user_name_verified = False
    is_pin_verified =False
    
    for credentials_tuple in credentials_tuples_list:
        if entered_user_name == credentials_tuple[0]:
            is_user_name_verified = True
            pin_in_database_in_hash = credentials_tuple[1]
            break

    if is_user_name_verified:
        is_pin_verified = bcrypt.checkpw(entered_pin_in_byte, pin_in_database_in_hash)

    if is_pin_verified == True:
        logged_in.logged_in(entered_user_name)

    else:
        verify_credentials(credentials_tuples_list)