import unittest
from Unittests.Models import FoodTest
from Unittests.Database import SqliteTest


def run(test_class):
    """Executes the test_class"""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def run_tests():
    """run tests on models"""
    run(FoodTest.TestFood)
    run(SqliteTest.TestDataBase)

if __name__ == "__main__":
    run_tests()
