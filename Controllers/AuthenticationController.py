from Controllers.Validation import UserValidator
from Lib.Messages import Messages
from Models.User import User
import bcrypt



class Auth:

    @staticmethod
    def HashPassword(password) -> str:
        return bcrypt.hashpw(password, bcrypt.gensalt(12))


    @staticmethod
    def SignUp(data):

        #input validation

        valid = UserValidator.ValidateName(data["first_name"], "First Name")
        valid &= UserValidator.ValidateName(data["last_name"], "Last Name")
        valid &= UserValidator.ValidateEmail(data["email"])
        valid &= UserValidator.ValidatePhoneNumber(data["phone_number"])
        valid &= UserValidator.ValidateSocialNumber(data["social_number"])
        valid &= UserValidator.ValidatePassword(data["password"])
        valid &= UserValidator.ValidatePasswordVerification(data["password"], data["password_verification"])

        if not valid:
            return False

        #check for previous signup
        if User.SearchByEmail(data["email"]):
            Messages.push(Messages.Type.ERROR, "an account with this email address already exists")
            return False


        #hash password
        data["password"] = Auth.HashPassword(data["password"])

        return User.Create(data)





    @staticmethod
    def GetUser() -> User:
        """ returns logged in user object """
        pass


    @staticmethod
    def CheckAdminCredentials() -> bool:
        """returns true if logged in user is admin"""
        return True