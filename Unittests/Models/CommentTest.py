import unittest
from Models.Food import Food
from Models.User import User
from unittest.mock import Mock
from Models.Comment import Comment
from DataBase.Sqlite import Database
import os


class TestComment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # delete the database if it exists
        if os.path.exists('test.db'):
            os.remove('test.db')

        # Create a mock database path
        Database.GetDatabasePath = Mock(return_value='test.db')
        # init the database
        Database.Initialize()

        # Create User 1
        User.Create({
            'id': 1,
            'first_name': 'TestName', 
            'last_name': 'last_name', 
            'email': 'test@test.com', 
            'phone_number': '091234567890', 
            'social_number':'123456789', 
            'password':'testPassword',
        })

        # Create User 2
        User.Create({
            'id': 2,
            'first_name': 'TestName', 
            'last_name': 'last_name', 
            'email': 'test@test.com', 
            'phone_number': '091234567890', 
            'social_number':'123456789', 
            'password':'testPassword',
        })

        # Create Food 1
        Food.Create({
            'id':1,
            'title':'TestFood',
            'stock':1,
            'fixed_price':100,
            'sale_price':150,
            'description':'TestDescription',
            'category':'TestCategory',
            'materials':'TestMaterials',
            'image':'TestImage',
        })

        # Create Food 2
        Food.Create({
            'id':2,
            'title':'TestFood',
            'stock':1,
            'fixed_price':100,
            'sale_price':150,
            'description':'TestDescription',
            'category':'TestCategory',
            'materials':'TestMaterials',
            'image':'TestImage',
        })

    @classmethod
    def tearDownClass(cls):
        # Delete the mocked database file
        if os.path.exists('test.db'):
            os.remove('test.db')

    def setUp(self):
        # Create a new comment object
        self.comment = Comment(1, 'test', '2020-01-01 22:10:30', 1, 2)

        # Create a new comment row in the database
        Database.Create(
            'comments', {
                'id': 1,
                'comment': 'test',
                'datetime': '2020-01-01 22:10:30',
                'user_id': 1,
                'food_id': 2,
                })

    def tearDown(self):
        # Flush mocked database
        Database.Flush('comments')

    def test_Init(self):
        # Check that the comment is correct
        self.assertEqual(self.comment.comment, 'test')
        self.assertEqual(self.comment.datetime, '2020-01-01 22:10:30')
        self.assertEqual(self.comment.user_id, 1)
        self.assertEqual(self.comment.food_id, 2)

    def test_setters(self):
        # food_id (wrong type)
        with self.assertRaises(TypeError):
            self.comment.food_id = 'test'
        
        # food_id (wrong value)
        with self.assertRaises(ValueError):
            self.comment.food_id = -1
        
        # food_id (not found)
        with self.assertRaises(KeyError):
            self.comment.food_id = 3 # consider food with id 3 doesn't exist

        # user_id (wrong type)
        with self.assertRaises(TypeError):
            self.comment.user_id = 'test'

        # user_id (wrong value)
        with self.assertRaises(ValueError):
            self.comment.user_id = -1

        # user_id (not found)
        with self.assertRaises(KeyError):
            self.comment.user_id = 3 # consider user with id 3 doesn't exist
        
        # comment (wrong type)
        with self.assertRaises(TypeError):
            self.comment.comment = 1

        # wrong datetime (type)
        with self.assertRaises(TypeError):
            self.comment.datetime = 20201010

        # datetime (wrong pattern)
        with self.assertRaises(ValueError):
            self.comment.datetime = '2020-01-01'
        
        # datetime (wrong pattern)
        with self.assertRaises(ValueError):
            self.comment.datetime = '2020-01-01_22:10:30'

        # correct info
        self.comment.comment = 'test2'
        self.comment.datetime = '2020-01-02 00:10:30'
        self.comment.user_id = 2
        self.comment.food_id = 1

        # asserts 
        self.assertEqual(self.comment.comment, 'test2')
        self.assertEqual(self.comment.datetime, '2020-01-02 00:10:30')
        self.assertEqual(self.comment.user_id, 2)
        self.assertEqual(self.comment.food_id, 1)

    def test_Create(self):

        # Create a new comment
        Comment.Create({
            'comment' : 'test',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 1,
            'food_id' : 2,
        })

        # Check if the comment is created
        fetched_data = Database.Read('comments', 'id', 1)
        self.assertEqual(len(fetched_data), 1)

        fetched_data = fetched_data[0]

        # Check if the comment is correct
        self.assertEqual(fetched_data[0], 1)
        self.assertEqual(fetched_data[1], 'test')
        self.assertEqual(fetched_data[2], '2020-01-01 22:10:30')
        self.assertEqual(fetched_data[3], 1)

        # check errors might happen
        
        # id (can't be specified)
        with self.assertRaises(RuntimeError):
            Comment.Create({
                'id' : 1,
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 1,
                'food_id' : 2,
            })
        
        # comment (Not entered)
        with self.assertRaises(KeyError):
            Comment.Create({
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 1,
                'food_id' : 2,
            })

        # datetime (Not entered)
        with self.assertRaises(KeyError):
            Comment.Create({
                'comment' : 'test',
                'user_id' : 1,
                'food_id' : 2,
            })

        # datetime (wrong format)
        with self.assertRaises(ValueError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01_22:10:30',
                'user_id' : 1,
                'food_id' : 2,
            })

        # datetime (wrong type)
        with self.assertRaises(TypeError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : 20200101,
                'user_id' : 1,
                'food_id' : 2,
            })

        # user_id (Not entered)
        with self.assertRaises(KeyError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'food_id' : 2,
            })
        
        # user_id (Not exists)
        with self.assertRaises(KeyError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 3,
                'food_id' : 2,
            })

        # user_id (wrong type)
        with self.assertRaises(TypeError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 'test',
                'food_id' : 2,
            })

        # user_id (wrong value)
        with self.assertRaises(ValueError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : -1,
                'food_id' : 2,
            })

        # food_id (Not entered)
        with self.assertRaises(KeyError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 1,
            })

        # food_id (Not exists)
        with self.assertRaises(KeyError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 1,
                'food_id' : 3,
            })
        
        # food_id (wrong type)
        with self.assertRaises(TypeError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 1,
                'food_id' : 'test',
            })
        
        # food_id (wrong value)
        with self.assertRaises(ValueError):
            Comment.Create({
                'comment' : 'test',
                'datetime' : '2020-01-01 22:10:30',
                'user_id' : 1,
                'food_id' : -1,
            })
        
    def test_Get(self):
        # fetch the comment created in setUp
        fetched_data = Comment.Get(1)

        self.assertIsNotNone(fetched_data)

        # check if the comment is correct
        self.assertEqual(fetched_data.id, 1)
        self.assertEqual(fetched_data.comment, 'test')
        self.assertEqual(fetched_data.datetime, '2020-01-01 22:10:30')
        self.assertEqual(fetched_data.user_id, 1)
        self.assertEqual(fetched_data.food_id, 2)

    def test_GetAll(self):
        # Create a new comment
        Database.Create('comments', {
            'id' : 2,
            'comment' : 'test2',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 1,
            'food_id' : 2,
        })

        # fetch all comments
        fetched_data = Comment.GetAll()

        self.assertListEqual(fetched_data, [
            Comment(1, 'test', '2020-01-01 22:10:30', 1, 2), 
            Comment(2, 'test2', '2020-01-01 22:10:30', 1, 2),
        ])

    def test_GetAllByFood(self):
        # Create two new comments
        Database.Create('comments', {
            'id' : 2,
            'comment' : 'test2',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 1,
            'food_id' : 2,
        })

        Database.Create('comments', {
            'id' : 3,
            'comment' : 'test3',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 1,
            'food_id' : 1,
        })

        # fetch all comments
        fetched_data = Comment.GetAllByFood(2)

        self.assertListEqual(fetched_data, [
            Comment(1, 'test', '2020-01-01 22:10:30', 1, 2), 
            Comment(2, 'test2', '2020-01-01 22:10:30', 1, 2),
        ])

    def test_GetAllByUser(self):
        # Create two new comments
        Database.Create('comments', {
            'id' : 2,
            'comment' : 'test2',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 2,
            'food_id' : 2,
        })

        Database.Create('comments', {
            'id' : 3,
            'comment' : 'test3',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 1,
            'food_id' : 1,
        })

        # fetch all comments
        fetched_data = Comment.GetAllByUser(1)
        
        self.assertListEqual(fetched_data, [
            Comment(1, 'test', '2020-01-01 22:10:30', 1, 2),
            Comment(3, 'test3', '2020-01-01 22:10:30', 1, 1),
        ])

    def test_GetAllByDate(self):
        # Create two new comments
        Database.Create('comments', {
            'id' : 2,
            'comment' : 'test2',
            'datetime' : '2020-01-02 22:10:00',
            'user_id' : 1,
            'food_id' : 1,
        })

        Database.Create('comments', {
            'id' : 3,
            'comment' : 'test3',
            'datetime' : '2020-01-01 22:10:30',
            'user_id' : 2,
            'food_id' : 1,
        })

        # fetch all comments
        fetched_data = Comment.GetAllByDate('2020-01-01')

        self.assertListEqual(fetched_data, [
            Comment(1, 'test', '2020-01-01 22:10:30', 1, 2),
            Comment(3, 'test3', '2020-01-01 22:10:30', 2, 1),
        ])

    def test_GetAllByDateRange(self):
        # Create two new comments
        Database.Create('comments', {
            'id' : 2,
            'comment' : 'test2',
            'datetime' : '2020-01-03 22:10:00',
            'user_id' : 1,
            'food_id' : 1,
        })

        Database.Create('comments', {
            'id' : 3,
            'comment' : 'test3',
            'datetime' : '2020-01-02 22:10:30',
            'user_id' : 2,
            'food_id' : 1,
        })

        # fetch all comments
        fetched_data = Comment.GetAllByDateRange('2020-01-01', '2020-01-03')

        self.assertListEqual(fetched_data, [
            Comment(1, 'test', '2020-01-01 22:10:30', 1, 2),
            Comment(3, 'test3', '2020-01-02 22:10:30', 2, 1),
        ])

    def test_Delete(self):
        # Delete the comment created in setUp
        Comment.Delete(1)

        # Check if the comment is deleted
        self.assertEqual(Database.ReadAll('comments'), [])

    def test_Update(self):
        # Update the comment created in setUp
        Comment.Update(1, {
            'comment' : 'newTest',
            'datetime' : '2020-01-01 00:00:00',
            'user_id' : 1,
            'food_id' : 1,
        })

        # Check if the comment is updated
        self.assertEqual(Database.Read('comments', 'id', 1), [
            (1, 'newTest', '2020-01-01 00:00:00', 1, 1),
        ])

        # check errors might happen

        # new datetime (wrong type)
        with self.assertRaises(TypeError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : 20200101,
                'user_id' : 1,
                'food_id' : 1,
            })

        # new datetime (wrong pattern)
        with self.assertRaises(ValueError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01_00-00-00',
                'user_id' : 1,
                'food_id' : 1,
            })

        # new user_id (wrong type)
        with self.assertRaises(TypeError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01 00:00:00',
                'user_id' : '1',
                'food_id' : 1,
            })
        
        # new user_id (wrong value)
        with self.assertRaises(ValueError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01 00:00:00',
                'user_id' : -1,
                'food_id' : 1,
            })

        # new user_id (not exists)
        with self.assertRaises(KeyError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01 00:00:00',
                'user_id' : 3,
                'food_id' : 1,
            })

        # new food_id (wrong type)
        with self.assertRaises(TypeError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01 00:00:00',
                'user_id' : 1,
                'food_id' : '1',
            })
        
        # new food_id (wrong value)
        with self.assertRaises(ValueError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01 00:00:00',
                'user_id' : 1,
                'food_id' : -1,
            })
        
        # new food_id (not exists)
        with self.assertRaises(KeyError):
            Comment.Update(1, {
                'comment' : 'newTest',
                'datetime' : '2020-01-01 00:00:00',
                'user_id' : 1,
                'food_id' : 3,
            })
