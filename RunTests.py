import unittest
from Unittests.Models import FoodTest
from Unittests.Models import GiftCardTest
from Unittests.Database import SqliteTest
from Unittests.Models import RestaurantTest
from Unittests.Models import CommentTest
from Unittests.Models import UserTest
from Unittests.Models import OrderTest
from Unittests.Models import MenuTest
from Unittests.Controllers import ValidationTest
from Unittests.Controllers import AuthenticationControllerTest
from Unittests.Controllers.User import UserInfoControllerTest


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
    run(CommentTest.TestComment)
    run(UserTest.TestUser)
    run(OrderTest.TestOrder)
    run(MenuTest.TestMenu)
    run(ValidationTest.TestUserValidator)
    run(AuthenticationControllerTest.TestAuth)
    run(UserInfoControllerTest.TestUserInfo)


if __name__ == "__main__":
    run_tests()
