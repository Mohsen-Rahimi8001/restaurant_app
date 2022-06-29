import unittest
from unittest.mock import Mock, patch
from Models.GiftCard import GiftCard
from DataBase.Sqlite import Database
import datetime as dt
import os


class TestGiftCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Mock the Database functionalities
        Database.GetDatabasePath = Mock(return_value='test.db')
        Database.Initialize()
    
    @classmethod
    def tearDownClass(cls):
        # Delete the test db
        os.remove('test.db')

    def setUp(self):
        Database.DeleteAll('gift_cards') # deletes all rows of the gift_cards table

    def test_init(self):
        with patch('Models.GiftCard.GiftCard.GetDefaultCode', return_value='123456789'):
            start_date = dt.datetime.strftime(dt.datetime.now() + dt.timedelta(days=1), "%Y-%m-%d")
            expiration_date = dt.datetime.strftime(dt.datetime.now() + dt.timedelta(days=2), "%Y-%m-%d")
            gc = GiftCard(1, start_date, expiration_date, 10)
            self.assertEqual(gc.id, 1)
            self.assertEqual(gc.code, '123456789')
            self.assertEqual(gc.start_date, dt.datetime.strptime(start_date, '%Y-%m-%d'))
            self.assertEqual(gc.expiration_date, dt.datetime.strptime(expiration_date, '%Y-%m-%d'))
            self.assertEqual(gc.amount, 10)

    def test_setters(self):
        gc = GiftCard(2, '2029-01-01', '2029-01-02', 10, '123456')

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

        with self.assertRaises(TypeError):
            gc.amount = '10'
        
        with self.assertRaises(ValueError):
            gc.amount = -10
        
        with self.assertRaises(ValueError):
            gc.amount = 101

    def test_Create(self):
        # Add a new gift card
        Database.Create('gift_cards', {'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': '123456', 'amount': 10})
        
        # try add a gift card with the same code
        with self.assertRaises(ValueError):
            GiftCard.Create({'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': '123456', 'amount': 10})
        
        # check errors might happen
        # wrong start_date
        with self.assertRaises(ValueError):
            GiftCard.Create({'start_date': '2020-01-01', 'expiration_date': '2029-01-02', 'code': '2589', 'amount': 10})
        
        # wrong expiration_date
        with self.assertRaises(ValueError):
            GiftCard.Create({'start_date': '2029-01-01', 'expiration_date': '2020-01-02', 'code': '2589', 'amount': 10})

        # wrong amount
        with self.assertRaises(ValueError):
            GiftCard.Create({'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': '2589', 'amount': -10})
        
        # wrong amount
        with self.assertRaises(ValueError):
            GiftCard.Create({'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': '2589', 'amount': 101})
        
        # wrong amount
        with self.assertRaises(TypeError):
            GiftCard.Create({'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': '2589', 'amount': '10'})

        GiftCard.Create({'id':15, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': '123457', 'amount': 10})
        self.assertTrue(Database.Exists('gift_cards', 'id', 15))

    def test_Get(self):
        Database.Create(
            'gift_cards',
            {'id':10, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_get', 'amount': 10}
            )
        gc = GiftCard.Get(10)
        self.assertEqual(gc, GiftCard(10, '2029-01-01', '2029-01-02', 10, 'test_get'))

    def test_GetAll(self):
        Database.Create('gift_cards', {'id':1, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_get_all', 'amount': 10})
        Database.Create('gift_cards', {'id':2, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_get_all2', 'amount': 12})
        gc = GiftCard.GetAll()
        self.assertEqual(gc, [GiftCard(1, '2029-01-01', '2029-01-02', 10, 'test_get_all'), GiftCard(2, '2029-01-01', '2029-01-02', 10, 'test_get_all2')])

    def test_GetByKey(self):
        Database.Create('gift_cards', {'id':1, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_get_by_code', 'amount': 10})
        Database.Create('gift_cards', {'id':2, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_get_by_code2', 'amount': 12})
        Database.Create('gift_cards', {'id':3, 'start_date': '2029-01-02', 'expiration_date': '2029-01-02', 'code': 'test_get_by_code3', 'amount': 13})
        gc = GiftCard.GetByKey('start_date', '2029-01-01')
        self.assertEqual(gc, [GiftCard(1, '2029-01-01', '2029-01-02', 10, 'test_get_by_code'), GiftCard(2, '2029-01-01', '2029-01-02', 12, 'test_get_by_code2')])

    def test_Update(self):
        # create a row
        Database.Create('gift_cards', {'id':1, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_update', 'amount': 10})
        # update the row
        GiftCard.Update(1, {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2', 'amount': 12})
        
        # check if the row was updated
        gc = GiftCard.Get(1)
        self.assertEqual(gc, GiftCard(1, '2029-01-01', '2029-02-02', 12, 'test_update2'))

        # check errors might happen

        with self.assertRaises(ValueError):
            GiftCard.Update(1, {'start_date': '1-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2'})
        
        with self.assertRaises(ValueError):
            GiftCard.Update(1, {'start_date': '2029-01-01', 'expiration_date': '2028-02-02', 'code': 'test_update2'})

        with self.assertRaises(ValueError):
            GiftCard.Update(-1, {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2'})
        
        with self.assertRaises(TypeError):
            GiftCard.Update(1, {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 1})
        
        with self.assertRaises(ValueError):
            GiftCard.Update('1', {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2'})

        with self.assertRaises(ValueError):
            GiftCard.Update(1, {'id' : 2, 'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2'})

        with self.assertRaises(ValueError):
            GiftCard.Update(1, {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2', 'amount': -10})
        
        with self.assertRaises(ValueError):
            GiftCard.Update(1, {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2', 'amount': 101})
        
        with self.assertRaises(TypeError):
            GiftCard.Update(1, {'start_date': '2029-01-01', 'expiration_date': '2029-02-02', 'code': 'test_update2', 'amount': '10'})

    def test_DeleteExpiredGiftCards(self):
        Database.Create('gift_cards', {'id':1, 'start_date': '2029-01-01', 'expiration_date': '2029-01-02', 'code': 'test_delete_expired_gift_cards', 'amount': 10})
        Database.Create('gift_cards', {'id':2, 'start_date': '2019-01-01', 'expiration_date': '2020-01-02', 'code': 'test_delete_expired_gift_cards2', 'amount': 12})
        
        GiftCard.DeleteExpiredGiftCards()
        
        gc = GiftCard.GetAll()
        self.assertListEqual(gc, [GiftCard(1, '2029-01-01', '2029-01-02', 10, 'test_delete_expired_gift_cards')])
