import unittest
from Unittests.Models import FoodTest
from Unittests.Models import GiftCardTest
from Unittests.Database import SqliteTest
from Unittests.Models import RestaurantTest


def run(test_class):
    """Executes the test_class"""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def run_tests():
    """run tests"""
    run(FoodTest.TestFood)
    run(SqliteTest.TestDataBase)
    run(GiftCardTest.TestGiftCard)
    run(RestaurantTest.TestRestaurant)


if __name__ == "__main__":
    run_tests()
