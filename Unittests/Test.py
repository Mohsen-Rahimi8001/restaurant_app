import unittest
from unittest.mock import Mock
from DataBase.Sqlite import Database
import os


class Test(unittest.TestCase):

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


    def setUp(self):
        # Flush tables in the database

        Database.Flush('users')
        Database.Flush('foods')
        Database.Flush('orders')
        Database.Flush('menus')
        Database.Flush('gift_cards')
        Database.Flush('comments')