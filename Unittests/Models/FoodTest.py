import unittest
from Models.Food import Food


class TestFood(unittest.TestCase):
        
    def test_init(self):
        food = Food(1, 'Pizza', 1, 150, 120, 'bluh bluh', 'American', '1-2-3-4')
        self.assertIsInstance(food, Food)
        self.assertEqual(food.id, 1)
        self.assertEqual(food.title, 'Pizza')
        self.assertEqual(food.stock, 1)
        self.assertEqual(food.fixed_price, 120)
        self.assertEqual(food.sale_price, 150)
        self.assertEqual(food.description, 'bluh bluh')
        self.assertEqual(food.category, 'American')
        self.assertEqual(food.materials, '1-2-3-4')
        self.assertEqual(food.image, r'.\Resources\Images\food_default.png')
        
    def test_setters(self):
        food = Food(1, 'Pizza', 1, 150, 120, 'bluh bluh', 'American', '1-2-3-4')

        with self.assertRaises(TypeError):
            food.stock = 1.
        
        with self.assertRaises(TypeError):
            food.fixed_price = '120'

        with self.assertRaises(TypeError):
            food.sale_price = 150.4
        
        with self.assertRaises(FileNotFoundError):
            food.image = 'bluh bluh'
