import unittest
from unittest.mock import Mock
from DataBase.Sqlite import Database
from Models.Message import Message
import datetime as dt
import os



class TestMessage(unittest.TestCase):
    
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
        # Flush messages table in the database
        Database.Flush('messages')

        self.message = Message(1, 'Hello', dt.datetime(2022, 1, 1), "admin@gmail.com")

        Database.Create('messages', {
            'id': self.message.id,
            'message': self.message.message,
            'datetime': self.message.datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'admin_email': self.message.admin_email
        })


    def test_init(self):
        message = Message(1, 'Hello', dt.datetime(2022, 1, 1), "admin@gmail.com")
        self.assertIsInstance(message, Message)
        self.assertEqual(message.id, 1)
        self.assertEqual(message.message, 'Hello')
        self.assertEqual(message.datetime, dt.datetime(2022, 1, 1))
        self.assertEqual(message.admin_email, 'admin@gmail.com')

    def test_setters(self):

        with self.assertRaises(TypeError):
            self.message.message = 1

        with self.assertRaises(TypeError):
            self.message.datetime = '2020-01-01'
        
        with self.assertRaises(TypeError):
            self.message.admin_email = 1.4

        with self.assertRaises(ValueError):
            self.message.admin_email = 'admin@gmail'

        self.message.admin_email = 'admin2@gmail.com'
        self.message.message = 'Hello2'
        self.message.datetime = dt.datetime.now()

        self.assertEqual(self.message.message, 'Hello2')
        self.assertEqual(self.message.datetime, dt.datetime.now())
        self.assertEqual(self.message.admin_email, 'admin2@gmail.com')


    def test_Create(self):
        Message.Create({
            'message':'Hello2',
            'datetime':'2020-01-01 00:00:00',
            'admin_email':'admin2@gmail.com',
        })

        messages = Database.ReadAll('messages')

        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[1][0], 2)
        self.assertEqual(messages[1][1], 'Hello2')
        self.assertEqual(messages[1][2], '2020-01-01 00:00:00')
        self.assertEqual(messages[1][3], 'admin2@gmail.com')

        with self.assertRaises(KeyError):
            Message.Create({
                'message':'Hello2',
                'datetime':'2020-01-01 00:00:00',
                'admin_email':'admin@gmail.com',
                'id':1
            })
        
        with self.assertRaises(KeyError):
            Message.Create({
                'message':'Hello2',
                'datetime':'2020-01-01 00:00:00',
            })
        
        with self.assertRaises(KeyError):
            Message.Create({
                'message':'Hello2',
                'admin_email':'admin@gmail.com',
            })

        with self.assertRaises(KeyError):
            Message.Create({
                'datetime':'2020-01-01 00:00:00',
                'admin_email':'admin@gmail.com',
            })

        with self.assertRaises(TypeError):
            Message.Create({
                'message':'Hello2',
                'datetime':20220202,
                'admin_email':'admin@gmail.com',
            })

        with self.assertRaises(ValueError):
            Message.Create({
                'message':'Hello2',
                'datetime':'2020-01-01',
                'admin_email':'admin@gmail.com',
            })
        
        with self.assertRaises(ValueError):
            Message.Create({
                'message':'Hello2',
                'datetime':'2020-01-01 00:00:00',
                'admin_email':'admin@gmail',
            })
        
        with self.assertRaises(TypeError):
            Message.Create({
                'message':'Hello2',
                'datetime':'2020-01-01 00:00:00',
                'admin_email':1,
            })


    def test_GetAll(self):
        messages = Message.GetAll()

        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].id, 1)
        self.assertEqual(messages[0].message, 'Hello')
        self.assertEqual(messages[0].datetime, dt.datetime(2022, 1, 1))
        self.assertEqual(messages[0].admin_email, 'admin@gmail.com')


    def test_Get(self):
        message = Message.Get(1)

        self.assertEqual(message.id, 1)
        self.assertEqual(message.message, 'Hello')
        self.assertEqual(message.datetime, dt.datetime(2022, 1, 1))
        self.assertEqual(message.admin_email, 'admin@gmail.com')


    def test_Update(self):

        Message.Update(1, {
            'message':'Hello2',
        })

        messages = Database.Read('messages', 'id', 1)[0]

        self.assertEqual(messages[1], 'Hello2')

        with self.assertRaises(KeyError):
            Message.Update(1, {
                'message':'Hello2',
                'datetime':'2020-01-01 00:00:00',
                }
                )
        
        with self.assertRaises(KeyError):
            Message.Update(1, {
                'message':'Hello2',
                'admin_email':'admin2@gmail.com'
                }
                )

        with self.assertRaises(KeyError):
            Message.Update(1, {
                'id' : 1000,
                'message':'Hello2',
                }
                )

        with self.assertRaises(ValueError):
            Message.Update(1, {})


    def test_Delete(self):
        
        self.assertEqual(len(Database.ReadAll('messages')), 1)

        Message.Delete(1)

        messages = Database.ReadAll('messages')

        self.assertEqual(len(messages), 0)


    def test_Exists(self):

        self.assertTrue(Message.Exists(1))

        self.assertFalse(Message.Exists(2))
