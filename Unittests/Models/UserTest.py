import unittest
from Unittests.Test import Test
from unittest.mock import Mock
from DataBase.Sqlite import Database
from Models.User import User
from Models.User import User
from Models.Food import Food
import os
import datetime


class TestUser(Test):

    def setUp(self):
        # Flush users table in the database
        Database.Flush('users')
        Database.Flush('foods')

    data = {
        "first_name" : "john",
        "last_name" : "doe",
        "email" : "email@gmail.com",
        "phone_number" : "09123456789",
        "social_number" : "0025111111",
        "image" : "image.png",
        "password" : "12345678",
        "role" : 1,
        "orders" : [],
        "cart" : [],
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
        data1 = TestUser.data.copy()
        id = User.Create(data1)
        self.assertTrue(User.Exists(id))


    def test_double_create(self):

        id = User.Create(TestUser.data)
        self.assertTrue(User.Exists(id))

        data1 = TestUser.data.copy()
        id1 = User.Create(data1)
        self.assertTrue(User.Exists(id1))


    def test_create_with_missing_col(self):

        missing_data = TestUser.data.copy()
        missing_data.pop("email")

        with self.assertRaises(Exception):
            id = User.Create(missing_data)


    def test_create_with_wrong_datatype(self):

        data1 = TestUser.data.copy()
        data1["email"] = datetime.datetime.now()

        with self.assertRaises(Exception):
            id = User.Create(data1)

    
    def test_get(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        user = User.Get(id)

        self.assertTrue(isinstance(user, User))


    def test_get_invalid_id(self):

        with self.assertRaises(Exception):
            user = User.Get(223)


    def test_get_values(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        user : User = User.Get(id)

        self.assertEqual(user.id , id)
        self.assertEqual(user.first_name , data1["first_name"])
        self.assertEqual(user.last_name , data1["last_name"])
        self.assertEqual(user.email , data1["email"])
        self.assertEqual(user.phone_number , data1["phone_number"])
        self.assertEqual(user.social_number , data1["social_number"])
        self.assertEqual(user.image , data1["image"])
        self.assertEqual(user.password , data1["password"])
        self.assertEqual(user.role , data1["role"])
        self.assertEqual(user.orders , [])
        self.assertEqual(user.cart , [])

    
    def test_get_all(self):

        data1 = TestUser.data.copy()

        User.Create(data1)
        User.Create(data1)
        User.Create(data1)
        User.Create(data1)

        users = User.GetAll()

        self.assertEqual(len(users), 4)

        for user in users:
            self.assertEqual(user.first_name, data1["first_name"])
            self.assertEqual(user.last_name, data1["last_name"])
            self.assertEqual(user.email, data1["email"])
            self.assertEqual(user.phone_number, data1["phone_number"])
            self.assertEqual(user.social_number, data1["social_number"])
            self.assertEqual(user.image, data1["image"])
            self.assertEqual(user.password, data1["password"])
            self.assertEqual(user.role, data1["role"])
            self.assertEqual(user.orders, [])
            self.assertEqual(user.cart, [])


    def test_delete(self):

        data1 = TestUser.data.copy()

        id = User.Create(data1)

        User.Delete(id)

        self.assertEqual(User.Exists(id), False)


    def test_delete_invalid_id(self):

        with self.assertRaises(Exception):
            User.Delete(23)


    def test_update(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        data2 = dict()
        data2["role"] = 2
        data2["cart"] = [1, 2, 3]
        data2["orders"] = [4, 5, 6]
        data2["email"] = "user@yahoo.com"

        User.Update(id, data2)

        user = User.Get(id)

        self.assertEqual(user.id, id)
        self.assertEqual(user.role, 1)
        self.assertEqual(user.cart, data2["cart"])
        self.assertEqual(user.orders, data2["orders"])
        self.assertEqual(user.email, data2["email"])


    def test_search_by_email(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        self.assertTrue(User.SearchByEmail("email@gmail.com"))
        self.assertFalse(User.SearchByEmail("user@yahoo.com"))


    def test_get_user_by_email(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        userById = User.Get(id)
        userByEmail = User.GetUserByEmail(data1["email"])

        self.assertEqual(userById.first_name, userByEmail.first_name)
        self.assertEqual(userById.last_name, userByEmail.last_name)
        self.assertEqual(userById.email, userByEmail.email)
        self.assertEqual(userById.phone_number, userByEmail.phone_number)
        self.assertEqual(userById.social_number, userByEmail.social_number)
        self.assertEqual(userById.password, userByEmail.password)
        self.assertEqual(userById.image, userByEmail.image)
        self.assertEqual(userById.orders, userByEmail.orders)
        self.assertEqual(userById.cart, userByEmail.cart)



    def test_add_food_to_cart_by_id(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        foodData1 = TestUser.foodData.copy()
        foodId = Food.Create(foodData1)

        user = User.Get(id)

        user.addFoodToCart(foodId)

        self.assertEqual(user.cart, [foodId,])

        user = User.Get(id)
        self.assertEqual(user.cart, [foodId,])


    def test_add_food_to_cart_by_object(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        foodData1 = TestUser.foodData.copy()
        foodId = Food.Create(foodData1)

        user = User.Get(id)
        food = Food.Get(foodId)

        user.addFoodToCart(food)
        user.addFoodToCart(food)

        self.assertEqual(user.cart, [foodId, foodId])

        user = User.Get(id)
        self.assertEqual(user.cart, [foodId, foodId])


    def test_remove_food_from_cart(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        foodData1 = TestUser.foodData.copy()
        foodId = Food.Create(foodData1)

        user = User.Get(id)
        food = Food.Get(foodId)

        user.addFoodToCart(food)
        user.addFoodToCart(foodId)
        user.addFoodToCart(foodId)

        #remove by object
        user.removeFoodFromCart(food)

        self.assertEqual(user.cart, [foodId, foodId])

        # remove by id
        user.removeFoodFromCart(foodId)

        user = User.Get(id)
        self.assertEqual(user.cart, [foodId,])


    def test_get_foods(self):

        data1 = TestUser.data.copy()
        id = User.Create(data1)

        foodData1 = TestUser.foodData.copy()
        foodId = Food.Create(foodData1)

        user = User.Get(id)

        user.addFoodToCart(foodId)
        user.addFoodToCart(foodId)
        user.addFoodToCart(foodId)
        user.addFoodToCart(foodId)

        foods = user.getCartFoods()

        self.assertEqual(len(foods),4)
        for food in foods:
            self.assertTrue(food, Food)
            self.assertTrue(Food.Exists(food.id))

