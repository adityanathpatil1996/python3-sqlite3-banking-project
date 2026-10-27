import bcrypt

def pin_to_hash():
    entered_pin = input("Enter new PIN: ")

    entered_pin_in_bytes = entered_pin.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_pin = bcrypt.hashpw(entered_pin_in_bytes, salt)

    return hashed_pin