import unittest
from unittest.mock import Mock
from DataBase.Sqlite import Database
from Models.Food import Food
import os


class TestFood(unittest.TestCase):
    
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
        # Flush foods table in the database
        Database.Flush('foods')

    def test_init(self):
        food = Food(1, 'Pizza', 1, 120, 150, 'bluh bluh', 'American', '1-2-3-4')
        self.assertIsInstance(food, Food)
        self.assertEqual(food.id, 1)
        self.assertEqual(food.title, 'Pizza')
        self.assertEqual(food.stock, 1)
        self.assertEqual(food.fixed_price, 120)
        self.assertEqual(food.sale_price, 150)
        self.assertEqual(food.description, 'bluh bluh')
        self.assertEqual(food.category, 'American')
        self.assertEqual(food.materials, '1-2-3-4')
        self.assertTrue(os.path.samefile(food.image, os.path.abspath(r'.\Resources\Images\food_default.png')))
        
    def test_setters(self):
        food = Food(1, 'Pizza', 1, 150, 120, 'bluh bluh', 'American', '1-2-3-4')

        with self.assertRaises(TypeError):
            food.stock = 1.
        
        with self.assertRaises(ValueError):
            food.stock = -1

        with self.assertRaises(TypeError):
            food.fixed_price = '120'

        with self.assertRaises(ValueError):
            food.fixed_price = -120

        with self.assertRaises(TypeError):
            food.sale_price = 150.4

        with self.assertRaises(ValueError):
            food.sale_price = -150
        
        with self.assertRaises(FileNotFoundError):
            food.image = 'bluh bluh'
        
        with self.assertRaises(TypeError):
            food.image = 1.5

        self.assertTrue(os.path.samefile(food.image, os.path.abspath(r'.\Resources\Images\food_default.png')))

    def test_Create(self):
        Food.Create({'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        self.assertTrue(Food(*Database.Read('foods', 'title', 'Pizza0')[0]), Food(1, 'Pizza', 1, 120, 150, 'bluh bluh', 'American', '1-2-3-4', r'.\Resources\Images\food_default.png'))

        # check errors
        # no title
        with self.assertRaises(KeyError):
            Food.Create({'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})

        # wrong stock
        with self.assertRaises(ValueError):
            Food.Create({'title': 'Pizza0', 'stock': -1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong stock
        with self.assertRaises(TypeError):
            Food.Create({'title': 'Pizza0', 'stock': 1.5, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # no fixed price
        with self.assertRaises(KeyError):
            Food.Create({'title': 'Pizza0', 'stock': 1, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong fixed price
        with self.assertRaises(ValueError):
            Food.Create({'title': 'Pizza0', 'stock': 1, 'fixed_price': -120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong fixed price
        with self.assertRaises(TypeError):
            Food.Create({'title': 'Pizza0', 'stock': 1, 'fixed_price': '120', 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})

        # no sale price
        with self.assertRaises(KeyError):
            Food.Create({'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong sale price
        with self.assertRaises(ValueError):
            Food.Create({'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'sale_price': -150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong sale price
        with self.assertRaises(TypeError):
            Food.Create({'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'sale_price': '150', 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})


    def test_Get(self):
        Database.Create('foods', {'id':1, 'title': 'Pizza', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image': r'.\Resources\Images\food_default.png'})
        food = Food.Get(1)

        self.assertEqual(food, Food(1, 'Pizza', 1, 120, 150, 'bluh bluh', 'American', '1-2-3-4', image=r'.\Resources\Images\food_default.png'))
        self.assertIsNone(Food.Get(2))

    def test_Update(self):
        Database.Create('foods', {'id':1, 'title': 'Pizza', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image': r'.\Resources\Images\food_default.png'})
        
        # check if update works propertly (including check for image update) (if dirty data is given for image, image doesn't change)
        Food.Update(1, {'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image':'bluh bluh'})
        food = Food.Get(1)
        self.assertEqual(food, Food(1, 'Pizza0', 1, 120, 150, 'bluh bluh', 'American', '1-2-3-4', image=r'.\Resources\Images\food_default.png'))

        # check for errors
        # wrong stock (value)
        with self.assertRaises(ValueError):
            Food.Update(1, {'title': 'Pizza0', 'stock': -1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong stock (type)
        with self.assertRaises(TypeError):
            Food.Update(1, {'title': 'Pizza0', 'stock': 1.5, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong fixed price (value)
        with self.assertRaises(ValueError):
            Food.Update(1, {'title': 'Pizza0', 'stock': 1, 'fixed_price': -120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})

        # wrong fixed price (type)
        with self.assertRaises(TypeError):
            Food.Update(1, {'title': 'Pizza0', 'stock': 1, 'fixed_price': '120', 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong sale price (value)
        with self.assertRaises(ValueError):
            Food.Update(1, {'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'sale_price': -150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})
        
        # wrong sale price (type)
        with self.assertRaises(TypeError):
            Food.Update(1, {'title': 'Pizza0', 'stock': 1, 'fixed_price': 120, 'sale_price': '150', 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4'})

    def test_Delete(self):
        Database.Create('foods', {'id':1, 'title': 'Pizza', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image': r'.\Resources\Images\food_default.png'})
        Food.Delete(1)
        self.assertIsNone(Food.Get(1))

    def test_GetAll(self):
        Database.Create('foods', {'id':1, 'title': 'Pizza', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image': r'.\Resources\Images\food_default.png'})
        Database.Create('foods', {'id':2, 'title': 'Pizza', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image': r'.\Resources\Images\food_default.png'})
        Database.Create('foods', {'id':3, 'title': 'Pizza', 'stock': 1, 'fixed_price': 120, 'sale_price': 150, 'description': 'bluh bluh', 'category': 'American', 'materials': '1-2-3-4', 'image': r'.\Resources\Images\food_default.png'})
        foods = Food.GetAll()
        self.assertEqual(foods, [Food(i, 'Pizza', 1, 120, 150, 'bluh bluh', 'American', '1-2-3-4', image=r'.\Resources\Images\food_default.png') for i in range(1, 4)])
