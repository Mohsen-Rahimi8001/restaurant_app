from DataBase.Sqlite import Database
from Controllers.AuthenticationController import Auth



class Initialize:

    @staticmethod
    def Run():
        """run app init methods"""

        #init database tables
        Database.Initialize()

        #add default admin
        Defaults.SignUpDefaultAdmin()







class Defaults:


    @staticmethod
    def SignUpDefaultAdmin(data = False):
        """add a default admin to users database"""

        #set sample data
        if not data:
            data = {
                "first_name": "admin",
                "last_name": "admin",
                "email": "admin@gmail.com",
                "phone_number": "09123456789",
                "social_number": "1111111111",
                "password": "aA!12345678",
                "password_verification": "aA!12345678",
                "role" : 2,
                "image" : r".\Resources\Images\user_default.png"
            }

        if not Auth.CheckForPreviousSignUp(data["email"]):
            Auth.SignUp(data)
