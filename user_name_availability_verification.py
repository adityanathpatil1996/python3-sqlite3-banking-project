import get_present_user_names

def verify_user_name_availability():
    present_user_names_list = get_present_user_names.get_present_user_names()
    accepted_user_name = check_user_name_presence_in_the_list(present_user_names_list)
    return accepted_user_name

def check_user_name_presence_in_the_list(present_user_names_list):
    entered_user_name = input("Enter new Username: ")
    if entered_user_name in present_user_names_list:
        print("Username already exists")
        check_user_name_presence_in_the_list(present_user_names_list)
    else:
        return entered_user_name