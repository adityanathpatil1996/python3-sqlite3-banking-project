import database_creation
import registration
import login

database_creation.create_database()

option = input("Choose one of the following :"
"1.Login"
"2.Register")

if option == "1":
    login.login()

else:
    registration.register()