import unittest
from unittest.mock import Mock, patch
from Models.GiftCard import GiftCard
from DataBase.Sqlite import Database
import datetime as dt
import os


class TestGiftCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Mock the Database"""
        Database.GetDatabasePath = Mock(return_value='test.db')
        Database.Initialize()
    
    @classmethod
    def tearDownClass(cls):
        """Delete the test db"""
        os.remove('test.db')

    def test_init(self):
        with patch('Models.GiftCard.GiftCard.GetDefaultCode', return_value='123456789'):
            start_date = dt.datetime.strftime(dt.datetime.now() + dt.timedelta(days=1), "%Y-%m-%d")
            expiration_date = dt.datetime.strftime(dt.datetime.now() + dt.timedelta(days=2), "%Y-%m-%d")
            gc = GiftCard(1, start_date, expiration_date)
            self.assertEqual(gc.id, 1)
            self.assertEqual(gc.code, '123456789')
            self.assertEqual(gc.start_date, dt.datetime.strptime(start_date, '%Y-%m-%d'))
            self.assertEqual(gc.expiration_date, dt.datetime.strptime(expiration_date, '%Y-%m-%d'))

    def test_setters(self):
        """Check for error raises in setters"""
        gc = GiftCard(2, '2029-01-01', '2029-01-02', '123456')

        with self.assertRaises(TypeError):
            gc.code = 1
        
        with self.assertRaises(ValueError):
            gc.start_date = '2020-01-01'

        with self.assertRaises(ValueError):
            gc.expiration_date = '2028-01-01'

        with self.assertRaises(ValueError):
            gc.start_date = '2029,01,01'
        
        with self.assertRaises(ValueError):
            gc.expiration_date = '2029,01,02'
