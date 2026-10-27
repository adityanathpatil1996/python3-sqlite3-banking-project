import user_name_availability_verification
import convert_pin_to_hash
import user
import add_new_user_to_database

def register():
    accepted_user_name = user_name_availability_verification.verify_user_name_availability()

    full_name = input("Enter you Full Name: ")

    hashed_pin = convert_pin_to_hash()

    new_user = user.User(accepted_user_name, full_name, hashed_pin)

    add_new_user_to_database.add_new_user_to_database(new_user)