import unittest
from unittest.mock import Mock
from Models.Restaurant import Restaurant
import os
import json


class TestRestaurant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # mock json file
        Restaurant.GetJsonAddress = Mock(return_value="test.json")
    
    @classmethod
    def tearDownClass(cls):
        # remove mock json file
        if os.path.exists("test.json"):
            os.remove("test.json")
    
    def setUp(self):
        self.restaurant = Restaurant("testName", "testManager", "test@test.com", 'testType', 'testDescription', '09123456789', 'testRegion', 'testAddress')

    def test_init(self):
        # check if the object is created
        self.assertIsNotNone(self.restaurant)
        # check if the object has the correct properties
        self.assertEqual(self.restaurant.restaurantName, "testName")
        self.assertEqual(self.restaurant.managerName, "testManager")
        self.assertEqual(self.restaurant.managerEmail, "test@test.com")
        self.assertEqual(self.restaurant.type, "testType")
        self.assertEqual(self.restaurant.description, "testDescription")
        self.assertEqual(self.restaurant.phone, "09123456789")
        self.assertEqual(self.restaurant.region, "testRegion")
        self.assertEqual(self.restaurant.address, "testAddress")

    def test_setters(self):

        # check if the setters work
        self.restaurant.restaurantName = "newName"
        self.assertEqual(self.restaurant.restaurantName, "newName")
        
        self.restaurant.managerName = "newManager"
        self.assertEqual(self.restaurant.managerName, "newManager")
        
        self.restaurant.managerEmail = "mohsen_rahimi@somewhere.somthing"
        self.assertEqual(self.restaurant.managerEmail, "mohsen_rahimi@somewhere.somthing")
        
        self.restaurant.type = "newType"
        self.assertEqual(self.restaurant.type, "newType")
        
        self.restaurant.description = "newDescription"
        self.assertEqual(self.restaurant.description, "newDescription")

        self.restaurant.phone = "00989123456789"
        self.assertEqual(self.restaurant.phone, "00989123456789")
        
        self.restaurant.phone = "9123456789"
        self.assertEqual(self.restaurant.phone, "9123456789")

        self.restaurant.phone = "+9809123456789"
        self.assertEqual(self.restaurant.phone, "+9809123456789")

        self.restaurant.region = "newRegion"
        self.assertEqual(self.restaurant.region, "newRegion")
        
        self.restaurant.address = "newAddress"
        self.assertEqual(self.restaurant.address, "newAddress")


        # wrong type for restaurantName
        with self.assertRaises(TypeError):
            self.restaurant.restaurantName = 123

        # wrong type for managerName
        with self.assertRaises(TypeError):
            self.restaurant.managerName = 123

        # wrong type for managerEmail
        with self.assertRaises(TypeError):
            self.restaurant.managerEmail = 123

        # wrong pattern of email
        with self.assertRaises(ValueError):
            self.restaurant.managerEmail = "test@test"
        
        # wrong pattern of email
        with self.assertRaises(ValueError):
            self.restaurant.managerEmail = "test@test.asdf_"

        # wrong type for type
        with self.assertRaises(TypeError):
            self.restaurant.type = 123
        
        # wrong type for description
        with self.assertRaises(TypeError):
            self.restaurant.description = 123
        
        # wrong type for phone
        with self.assertRaises(TypeError):
            self.restaurant.phone = 123
        
        # wrong pattern of phone
        with self.assertRaises(ValueError):
            self.restaurant.phone = "091234567890"

        # wrong patter of phone
        with self.assertRaises(ValueError):
            self.restaurant.phone = "098123456789"
        
        # wrong type for region
        with self.assertRaises(TypeError):
            self.restaurant.region = 123
        
        # wrong type for address
        with self.assertRaises(TypeError):
            self.restaurant.address = 123        

    def test_SaveToJson(self):
        # check if the function works
        self.restaurant.SaveToJson()

        # check if the file is created
        self.assertTrue(os.path.exists("test.json"))

        # check if the file has the correct content
        with open("test.json", "r") as f:
            data = json.load(f)
            self.assertEqual(data["_restaurantName"], "testName")
            self.assertEqual(data["_managerName"], "testManager")
            self.assertEqual(data["_managerEmail"], "test@test.com")
            self.assertEqual(data["_type"], "testType")
            self.assertEqual(data["_description"], "testDescription")
            self.assertEqual(data["_phone"], "09123456789")
            self.assertEqual(data["_region"], "testRegion")
            self.assertEqual(data["_address"], "testAddress")

    def test_LoadFromJson(self):
        # create json file and push data in it.
        with open("test.json", "w") as f:
            json.dump(
                {"_restaurantName": "testName",
                "_managerName": "testManager",
                "_managerEmail": "test@test.com",
                "_type": "testType",
                "_description": "testDescription",
                "_phone": "09123456789",
                "_region": "testRegion",
                "_address": "testAddress"}, f)
        
        # check if the function works
        new_restaurant = Restaurant.LoadFromJson()
        
        # check if the object is created
        self.assertIsNotNone(new_restaurant)
        
        # check if the object has the correct properties
        self.assertEqual(new_restaurant.restaurantName, "testName")
        self.assertEqual(new_restaurant.managerName, "testManager")
        self.assertEqual(new_restaurant.managerEmail, "test@test.com")
        self.assertEqual(new_restaurant.type, "testType")
        self.assertEqual(new_restaurant.description, "testDescription")
        self.assertEqual(new_restaurant.phone, "09123456789")
        self.assertEqual(new_restaurant.region, "testRegion")
        self.assertEqual(new_restaurant.address, "testAddress")
