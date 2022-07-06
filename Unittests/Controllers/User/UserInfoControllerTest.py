from Unittests.Test import Test
from Controllers.AuthenticationController import Auth
from Models.User import User
from DataBase.Sqlite import Database
from Controllers.User.UserInfoController import UserInfo


class TestUserInfo(Test):

    signupData = {
        "first_name": "user",
        "last_name": "user",
        "email": "user@gmail.com",
        "phone_number": "09123456789",
        "social_number": "0025111111",
        "password": "aA!12345678",
        "password_verification": "aA!12345678"
    }

    data = {
        "first_name": "useruser",
        "last_name": "user",
        "email": "user2@gmail.com",
        "phone_number": "09123456789",
        "social_number": "0025111111",
        "password": "aA!12345678",
        "new_password": "aA!123456789",
        "image" : ""
    }

    def test_edit_data(self):

        data = TestUserInfo.signupData.copy()
        id = Auth.SignUp(data)

        Auth.CurrentUserId = id

        editData = TestUserInfo.data.copy()
        UserInfo.Edit(editData)

        user = Auth.GetUser()

        self.assertEqual(user.first_name, editData["first_name"])
        self.assertEqual(user.last_name, editData["last_name"])
        self.assertEqual(user.email, editData["email"])
        self.assertEqual(user.phone_number, editData["phone_number"])
        self.assertEqual(user.social_number, editData["social_number"])
        self.assertEqual(user.password, editData["new_password"])


