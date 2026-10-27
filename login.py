import verify_credentials
import get_credentials_list_from_database

def login():

    credentials_tuples_list = get_credentials_list_from_database.get_credentials_list_from_database()
    has_been_verified = verify_credentials.verify_credentials(credentials_tuples_list)