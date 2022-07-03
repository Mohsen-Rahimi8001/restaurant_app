from Unittests.Test import Test
from Controllers.AuthenticationController import Auth
from Models.User import User
from DataBase.Sqlite import Database


class TestAuth(Test):

    validData = {

        "first_name": "user",
        "last_name": "user",
        "email": "user@gmail.com",
        "phone_number": "09123456789",
        "social_number": "0025111111",
        "password": "aA!12345678",
        "password_verification": "aA!12345678"
    }


    def setUp(self):
        # Flush users in the database
        Database.Flush('users')
        Auth.LogOut()


    def test_for_previous_signup(self):

        data = {
            "first_name": "user",
            "last_name": "useri",
            "email": "user@gmail.com",
            "phone_number": "09123456789",
            "social_number": "0025111111",
            "password": "aA!12345678",
        }

        User.Create(data)

        self.assertTrue(Auth.CheckForPreviousSignUp("user@gmail.com"))
        self.assertFalse(Auth.CheckForPreviousSignUp("user@yahoo.com"))


    def test_signup(self):

        #case of invalid data tested in validation tests
        data = TestAuth.validData.copy()

        id = Auth.SignUp(data)

        self.assertTrue(User.Exists(id))

        user = User.Get(id)

        self.assertEqual(user.id, id)
        self.assertEqual(user.first_name, data["first_name"])
        self.assertEqual(user.last_name, data["last_name"])
        self.assertEqual(user.email, data["email"])
        self.assertEqual(user.phone_number, data["phone_number"])
        self.assertEqual(user.social_number, data["social_number"])
        self.assertTrue(Auth.CheckPasswordMatch("aA!12345678", user.password))


    def test_login(self):

        data = TestAuth.validData.copy()
        Auth.SignUp(data)

        loginData = {
            "email" : "user@gmail.com",
            "password" : "aA!12345678"
        }

        result = Auth.Login(loginData)

        self.assertTrue(result)
        self.assertTrue(Auth.IsUserLoggedIN())


    def test_login_with_account_that_does_not_exists(self):
        loginData = {
            "email": "user@gmail.com",
            "password": "aA!12345678"
        }

        result = Auth.Login(loginData)

        self.assertFalse(result)
        self.assertFalse(Auth.IsUserLoggedIN())


    def test_login_with_wrong_password(self):
        data = TestAuth.validData.copy()
        Auth.SignUp(data)

        loginData = {
            "email": "user@gmail.com",
            "password": "aA!1678"
        }

        result = Auth.Login(loginData)

        self.assertFalse(result)
        self.assertFalse(Auth.IsUserLoggedIN())


    def test_logout(self):
        data = TestAuth.validData.copy()
        Auth.SignUp(data)

        loginData = {
            "email": "user@gmail.com",
            "password": "aA!12345678"
        }

        Auth.Login(loginData)

        Auth.LogOut()

        self.assertFalse(Auth.CurrentUserId)
        self.assertFalse(Auth.IsUserLoggedIN())