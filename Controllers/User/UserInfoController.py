from Controllers.Validation import UserValidator
from Lib.Messages import Messages
from Models.User import User
from Controllers.AuthenticationController import Auth
from Lib.Image import Image

class UserInfo:



    @staticmethod
    def ValidateEditDate(data : dict) -> None:
        """validate input data"""

        if not UserValidator.ValidateName(data["first_name"], "First Name"):
            data.pop("first_name")

        if not UserValidator.ValidateName(data["last_name"], "Last Name"):
            data.pop("last_name")

        if not UserValidator.ValidatePhoneNumber(data["phone_number"]):
            data.pop("phone_number")

        if not UserValidator.ValidateSocialNumber(data["social_number"]):
            data.pop("social_number")

        if not UserValidator.ValidateEmail(data["email"]):
            data.pop("email")


    @staticmethod
    def PopOldData(user : User, data : dict) -> None:
        """remove old data"""

        if "first_name" in data:
            if user.first_name == data["first_name"]:
                data.pop("first_name")

        if "last_name" in data:
            if user.last_name == data["last_name"]:
                data.pop("last_name")

        if "phone_number" in data:
            if user.phone_number == data["phone_number"]:
                data.pop("phone_number")

        if "social_number" in data:
            if user.social_number == data["social_number"]:
                data.pop("social_number")

        if "email" in data:
            if user.email == data["email"]:
                data.pop("email")


    @staticmethod
    def CheckForNewImage(data : dict):
        """check if user has uploaded new photo or not"""

        if data["image"]:
            Image.GetFromDirectory(data["image"])
        else:
            data.pop("image")


    @staticmethod
    def CheckForNewPassword(user : User, data : dict):
        """check if user has interred new password"""

        if data["password"]:

            if data["password"] != user.password:
                Messages.push(Messages.Type.ERROR, "wrong password")
                data.pop("password")
            else:

                if not UserValidator.ValidatePassword(data["new_password"], "New Password"):
                    data.pop("password")

                else:
                    data["password"] = data["new_password"]

        else:

            if data["new_password"]:
                Messages.push(Messages.Type.ERROR, "you must Inter current password to change password")
                data.pop("password")

            else:
                data.pop("password")

        data.pop("new_password")


    @staticmethod
    def Edit(editData : dict) -> None:
        """update user data"""

        data = editData.copy()

        #validate input
        UserInfo.ValidateEditDate(data)

        user = Auth.GetUser()

        #remove old values from update data
        UserInfo.PopOldData(user, data)

        #handel new image
        UserInfo.CheckForNewImage(data)

        #change password
        UserInfo.CheckForNewPassword(user, data)

        if len(data) > 0:
            User.Update(user.id, data)








