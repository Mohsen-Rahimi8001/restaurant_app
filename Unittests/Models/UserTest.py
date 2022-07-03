import unittest
from unittest.mock import Mock
from DataBase.Sqlite import Database
from Models.User import User
from Models.Order import Order
from Models.Food import Food
import os


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # mock the database
        Database.GetDatabasePath = Mock(return_value='test.db')
        Database.Initialize()


    @classmethod
    def tearDownClass(cls):
        # delete the database
        if os.path.exists('test.db'):
            os.remove('test.db')

    data = {
        "first_name" : "fname",
        "last_name" : "lname",
        "email" : "email@gmail.com",
        "phone_number" : "09123456789",
        "social_number" : "0025111111",
        "image" : "image.png",
        "password" : "12345678",
        "role" : 1,
        "orders" : [],
        "cart" : [],
    }

    #test the test class
    def test_nothing(self):
        pass


