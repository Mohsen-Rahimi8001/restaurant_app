import unittest
from Unittests.Models import FoodTest


def run(test_class):
    """Executes the test_class"""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def run_tests():
    """run tests on models"""
    run(FoodTest.TestFood)

if __name__ == "__main__":
    run_tests()
