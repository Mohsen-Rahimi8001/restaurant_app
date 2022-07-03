from Controllers.Validation import UserValidator
from Lib.Messages import Messages
from Models.User import User
import bcrypt



class Auth:

    @staticmethod
    def HashPassword(password) -> str:
        return  bcrypt.hashpw(password, bcrypt.gensalt(1))


    @staticmethod
    def CheckPasswordMatch(password : str, hashed : str) -> bool:
        return  bcrypt.checkpw(password, hashed)


    @staticmethod
    def ValidateSignUpData(data : dict) -> bool:
        """sign up input validation"""

        valid = UserValidator.ValidateName(data["first_name"], "First Name")
        valid &= UserValidator.ValidateName(data["last_name"], "Last Name")
        valid &= UserValidator.ValidateEmail(data["email"])
        valid &= UserValidator.ValidatePhoneNumber(data["phone_number"])
        valid &= UserValidator.ValidateSocialNumber(data["social_number"])
        valid &= UserValidator.ValidatePassword(data["password"])
        valid &= UserValidator.ValidatePasswordVerification(data["password"], data["password_verification"])

        data.pop("password_verification")

        return valid


    @staticmethod
    def CheckForPreviousSignUp(email : str) -> bool:
        """check if there is an account with same email in database or not"""

        if User.SearchByEmail(email):
            Messages.push(Messages.Type.ERROR, "an account with this email address already exists")
            return True

        return False


    @staticmethod
    def SignUp(data : dict):

        #input validation
        if not Auth.ValidateSignUpData(data):
            return False

        #check for previous signup
        if Auth.CheckForPreviousSignUp(data["email"]):
            return False

        #hash password
        data["password"] = Auth.HashPassword(data["password"])

        #add user to data base
        return User.Create(data)



    @staticmethod
    def GetUser() -> User:
        """ returns logged in user object """
        pass


    @staticmethod
    def CheckAdminCredentials() -> bool:
        """returns true if logged in user is admin"""
        return True