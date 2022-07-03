import unittest
from unittest.mock import Mock
from DataBase.Sqlite import Database
from Models.Food import Food
from Models.Menu import Menu
import os
import datetime


class TestMenu(unittest.TestCase):

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
        # Flush menu table in the database
        Database.Flush('menus')
        Database.Flush('foods')

    data = {
        "title" : "menu",
        "foods" : [],
        "date" : "1-1-1"
    }

    foodData = {
        'title': 'Pizza0',
        'stock': 2,
        'fixed_price': 120,
        'sale_price': 150,
        'description': 'a b c',
        'category': 'American',
        'materials': '1-2-3-4'
    }


    #test the test class
    def test_nothing(self):
        pass
    
    def test_create(self):
        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)
        self.assertTrue(Menu.Exists(id))


    def test_double_create(self):

        id = Menu.Create(TestMenu.data)
        self.assertTrue(Menu.Exists(id))

        data1 = TestMenu.data.copy()
        id1 = Menu.Create(data1)
        self.assertTrue(Menu.Exists(id1))

    def test_create_with_missing_col(self):

        missing_data = TestMenu.data.copy()
        missing_data.pop("date")

        with self.assertRaises(Exception):
            id = Menu.Create(missing_data)


    def test_create_with_wrong_datatype(self):

        data1 = TestMenu.data.copy()
        data1["date"] = datetime.datetime.now()

        with self.assertRaises(Exception):
            id = Menu.Create(data1)


    def test_get(self):

        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)

        menu = Menu.Get(id)

        self.assertTrue(isinstance(menu, Menu))


    def test_get_invalid_id(self):

        with self.assertRaises(Exception):
            menu = Menu.Get(223)


    def test_get_values(self):

        data1 = TestMenu.data.copy()
        data1["foods"] = [1,2,3]
        id = Menu.Create(data1)

        menu : Menu = Menu.Get(id)

        self.assertEqual(menu.id , id)
        self.assertEqual(menu.foods , data1["foods"])
        self.assertEqual(menu.title , data1["title"])
        self.assertEqual(menu.date , data1["date"])



    def test_get_all(self):

        data1 = TestMenu.data.copy()
        data1["foods"] = [1, 2, 3]

        Menu.Create(data1)
        Menu.Create(data1)
        Menu.Create(data1)
        Menu.Create(data1)

        menus = Menu.GetAll()

        self.assertEqual(len(menus), 4)

        for menu in menus:
            self.assertEqual(menu.foods, data1["foods"])
            self.assertEqual(menu.title, data1["title"])
            self.assertEqual(menu.date, data1["date"])



    def test_delete(self):

        data1 = TestMenu.data.copy()
        data1["foods"] = [1, 2, 3]

        id = Menu.Create(data1)

        Menu.Delete(id)

        self.assertEqual(Menu.Exists(id), False)


    def test_delete_invalid_id(self):

        with self.assertRaises(Exception):
            Menu.Delete(23)


    def test_update(self):

        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)

        data2 = dict()
        data2["title"] = "sunday"
        data2["foods"] = [1, 2, 3]

        Menu.Update(id, data2)

        menu = Menu.Get(id)

        self.assertEqual(menu.id, id)
        self.assertEqual(menu.foods, data2["foods"])
        self.assertEqual(menu.title, data2["title"])


    def test_add_food_by_id(self):

        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)

        foodData1 = TestMenu.foodData.copy()
        foodId = Food.Create(foodData1)

        menu = Menu.Get(id)

        menu.addFood(foodId)

        self.assertEqual(menu.foods, [foodId,])

        menu = Menu.Get(id)
        self.assertEqual(menu.foods, [foodId,])


    def test_add_food_by_object(self):

        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)

        foodData1 = TestMenu.foodData.copy()
        foodId = Food.Create(foodData1)

        menu = Menu.Get(id)
        food = Food.Get(foodId)

        menu.addFood(food)
        menu.addFood(food)

        self.assertEqual(menu.foods, [foodId, foodId])

        menu = Menu.Get(id)
        self.assertEqual(menu.foods, [foodId, foodId])


    def test_remove_food(self):

        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)

        foodData1 = TestMenu.foodData.copy()
        foodId = Food.Create(foodData1)

        menu = Menu.Get(id)
        food = Food.Get(foodId)

        menu.addFood(food)
        menu.addFood(foodId)
        menu.addFood(foodId)

        #remove by object
        menu.removeFood(food)

        self.assertEqual(menu.foods, [foodId, foodId])

        # remove by id
        menu.removeFood(foodId)

        menu = Menu.Get(id)
        self.assertEqual(menu.foods, [foodId,])


    def test_get_foods(self):

        data1 = TestMenu.data.copy()
        id = Menu.Create(data1)

        foodData1 = TestMenu.foodData.copy()
        foodId = Food.Create(foodData1)

        menu = Menu.Get(id)

        menu.addFood(foodId)
        menu.addFood(foodId)
        menu.addFood(foodId)
        menu.addFood(foodId)

        foods = menu.getFoods()

        self.assertEqual(len(foods),4)
        for food in foods:
            self.assertTrue(food, Food)
            self.assertTrue(Food.Exists(food.id))
    