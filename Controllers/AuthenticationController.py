from Controllers.Validation import UserValidator
from Lib.Messages import Messages
from Models.User import User
import bcrypt



class Auth:


    CurrentUserId = False
    AdminRole = 2

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
        return User.SearchByEmail(email)



    @staticmethod
    def SignUp(data : dict):

        #input validation
        if not Auth.ValidateSignUpData(data):
            return False

        #check for previous signup
        if Auth.CheckForPreviousSignUp(data["email"]):
            Messages.push(Messages.Type.ERROR, "an account with this email address already exists")
            return False

        #hash password
        data["password"] = Auth.HashPassword(data["password"])

        #add user to data base
        return User.Create(data)


    @staticmethod
    def Login(data : dict) -> bool:

        """input validation"""
        if not Auth.ValidateLoginData(data):
            return False

        #check if account exists
        if not Auth.CheckForPreviousSignUp(data["email"]):
            Messages.push(Messages.Type.ERROR, "account does not exists")
            return False

        #get user
        user = User.GetUserByEmail(data["email"])

        #check for match password
        if not Auth.CheckPasswordMatch(data["password"], user.password):
            Messages.push(Messages.Type.ERROR, "wrong password")
            return False

        Auth.CurrentUserId = user.id
        return True


    @staticmethod
    def IsUserLoggedIN():
        return bool(Auth.CurrentUserId)

    @staticmethod
    def ValidateLoginData(data : dict) -> bool:

        return UserValidator.ValidateEmail(data["email"]) and UserValidator.ValidatePassword(data["password"], justNotEmpty = True)


    @staticmethod
    def LogOut():
        if Auth.IsUserLoggedIN():
            Auth.CurrentUserId = False
            return True
        return False


    @staticmethod
    def GetUser() -> User:
        """ returns logged in user object """

        if not Auth.IsUserLoggedIN():
            return False

        return User.Get(Auth.CurrentUserId)


    @staticmethod
    def CheckAdminCredentials() -> bool:
        """returns true if logged in user is admin"""

        if not Auth.IsUserLoggedIN():
            return False

        return Auth.GetUser().role == Auth.AdminRole

