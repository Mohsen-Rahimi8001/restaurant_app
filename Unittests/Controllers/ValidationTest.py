import unittest
from Controllers.Validation import UserValidator

class TestUserValidator(unittest.TestCase):

    def test_nothing(self):
        """test the test"""
        pass

    def test_validate_name(self):
        self.assertFalse(UserValidator.ValidateName("hello23"))
        self.assertTrue(UserValidator.ValidateName("ben"))


    def test_validate_email(self):
        self.assertFalse(UserValidator.ValidateEmail("123"))
        self.assertFalse(UserValidator.ValidateEmail("123.com"))
        self.assertFalse(UserValidator.ValidateEmail("a@b"))
        self.assertFalse(UserValidator.ValidateEmail("a@b.c"))
        self.assertTrue(UserValidator.ValidateEmail("hello@gmail.com"))


    def test_phone_number_validation(self):
        self.assertFalse(UserValidator.ValidatePhoneNumber("091234"))
        self.assertFalse(UserValidator.ValidatePhoneNumber("123456890"))
        self.assertFalse(UserValidator.ValidatePhoneNumber("09123456a"))
        self.assertTrue(UserValidator.ValidatePhoneNumber("09123456899"))
        self.assertTrue(UserValidator.ValidatePhoneNumber("+9809123456899"))


    def test_validation_social_number(self):
        self.assertFalse(UserValidator.ValidateSocialNumber("00251111"))
        self.assertFalse(UserValidator.ValidateSocialNumber("00251a1111"))
        self.assertTrue(UserValidator.ValidateSocialNumber("0025121111"))


    def test_validation_password(self):
        self.assertFalse(UserValidator.ValidatePassword("12345678"))
        self.assertFalse(UserValidator.ValidatePassword("a2345678"))
        self.assertFalse(UserValidator.ValidatePassword("aA345678"))
        self.assertFalse(UserValidator.ValidatePassword("aA!4567"))
        self.assertTrue(UserValidator.ValidatePassword("aA!45678"))