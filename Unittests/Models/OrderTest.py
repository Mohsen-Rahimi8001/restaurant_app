import unittest
from unittest.mock import Mock
from DataBase.Sqlite import Database
from Models.Order import Order
from Models.Food import Food
import json
import os
import datetime

class TestOrder(unittest.TestCase):

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
        # Flush orders table in the database
        Database.Flush('orders')
        Database.Flush('foods')

    data = {
        "foods" : list(),
        "date" : "1-1-1",
        "paid" : False,
        "reference_number" : "123456789",
        "delivered" : False,
        "user_id" : 1,
        "account_number" : "",
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

    # test the test class
    def test_nothing(self):
        pass

    def test_create(self):
        data1 = TestOrder.data.copy()
        id = Order.Create(data1)
        self.assertTrue(Order.Exists(id))


    def test_double_create(self):

        id = Order.Create(TestOrder.data)
        self.assertTrue(Order.Exists(id))

        data1 = TestOrder.data.copy()
        id1 = Order.Create(data1)
        self.assertTrue(Order.Exists(id1))

    def test_create_with_missing_col(self):

        missing_data = TestOrder.data.copy()
        missing_data.pop("date")

        with self.assertRaises(Exception):
            id = Order.Create(missing_data)


    def test_create_with_wrong_datatype(self):

        data1 = TestOrder.data.copy()
        data1["date"] = datetime.datetime.now()

        with self.assertRaises(Exception):
            id = Order.Create(data1)


    def test_get(self):

        data1 = TestOrder.data.copy()
        id = Order.Create(data1)

        order = Order.Get(id)


    def test_get_invalid_id(self):

        with self.assertRaises(Exception):
            order = Order.Get(223)


    def test_get_values(self):

        data1 = TestOrder.data.copy()
        data1["foods"] = [1,2,3]
        id = Order.Create(data1)

        order : Order = Order.Get(id)

        self.assertEqual(order.id , id)
        self.assertEqual(order.foods , data1["foods"])
        self.assertEqual(order.date , data1["date"])
        self.assertEqual(order.paid , False)
        self.assertEqual(order.reference_number , "")
        self.assertEqual(order.user_id , data1["user_id"])
        self.assertEqual(order.delivered , False)
        self.assertEqual(order.account_number, "")


    def test_get_all(self):

        data1 = TestOrder.data.copy()
        data1["foods"] = [1, 2, 3]

        Order.Create(data1)
        Order.Create(data1)
        Order.Create(data1)
        Order.Create(data1)

        orders = Order.GetAll()

        self.assertEqual(len(orders), 4)

        for order in orders:
            self.assertEqual(order.foods, data1["foods"])
            self.assertEqual(order.date, data1["date"])
            self.assertEqual(order.paid, False)
            self.assertEqual(order.reference_number, "")
            self.assertEqual(order.user_id, data1["user_id"])
            self.assertEqual(order.delivered, False)
            self.assertEqual(order.account_number, "")



    def test_delete(self):

        data1 = TestOrder.data.copy()
        data1["foods"] = [1, 2, 3]

        id = Order.Create(data1)

        Order.Delete(id)

        self.assertEqual(Order.Exists(id), False)


    def test_delete_invalid_id(self):

        with self.assertRaises(Exception):
            Order.Delete(23)


    def test_update(self):

        data1 = TestOrder.data.copy()
        id = Order.Create(data1)

        data2 = dict()
        data2["paid"] = True
        data2["foods"] = [1, 2, 3]
        data2["delivered"] = False

        Order.Update(id, data2)

        order = Order.Get(id)

        self.assertEqual(order.id, id)
        self.assertEqual(order.foods, data2["foods"])
        self.assertEqual(order.paid, data2["paid"])
        self.assertEqual(order.delivered, data2["delivered"])


    def test_add_food_by_id(self):

        data1 = TestOrder.data.copy()
        id = Order.Create(data1)

        foodData1 = TestOrder.foodData.copy()
        foodId = Food.Create(foodData1)

        order = Order.Get(id)

        order.addFood(foodId)

        self.assertEqual(order.foods, [foodId,])

        order = Order.Get(id)
        self.assertEqual(order.foods, [foodId,])


    def test_add_food_by_object(self):

        data1 = TestOrder.data.copy()
        id = Order.Create(data1)

        foodData1 = TestOrder.foodData.copy()
        foodId = Food.Create(foodData1)

        order = Order.Get(id)
        food = Food.Get(foodId)

        order.addFood(food)
        order.addFood(food)

        self.assertEqual(order.foods, [foodId, foodId])

        order = Order.Get(id)
        self.assertEqual(order.foods, [foodId, foodId])


    def test_remove_food(self):

        data1 = TestOrder.data.copy()
        id = Order.Create(data1)

        foodData1 = TestOrder.foodData.copy()
        foodId = Food.Create(foodData1)

        order = Order.Get(id)
        food = Food.Get(foodId)

        order.addFood(food)
        order.addFood(foodId)
        order.addFood(foodId)

        #remove by object
        order.removeFood(food)

        self.assertEqual(order.foods, [foodId, foodId])

        # remove by id
        order.removeFood(foodId)

        order = Order.Get(id)
        self.assertEqual(order.foods, [foodId,])


    def test_get_foods(self):

        data1 = TestOrder.data.copy()
        id = Order.Create(data1)

        foodData1 = TestOrder.foodData.copy()
        foodId = Food.Create(foodData1)

        order = Order.Get(id)

        order.addFood(foodId)
        order.addFood(foodId)
        order.addFood(foodId)
        order.addFood(foodId)

        foods = order.getFoods()

        self.assertEqual(len(foods),4)
        for food in foods:
            self.assertTrue(food, Food)
            self.assertTrue(Food.Exists(food.id))

