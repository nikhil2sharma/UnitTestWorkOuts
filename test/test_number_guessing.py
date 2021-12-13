import unittest
from unittest import result
from unittest.main import main
from number_guessinggame import GuessingGame
class NumberGuessingTestClass(unittest.TestCase):
    """
    This class will be used to test number guessing game method
    """

    def test_expect_to_be_in_validrange(self):
        """
        Lets test the number guessing game and ensure value is in the range of 0 to 100
        """
        result1=GuessingGame()
        self.assertIn(result1,range(0,101))
        print('Second')
        self.assertTrue(
            0<result1<100,
            msg="UnitTestFail"
       )

if __name__ == '__main__':
    unittest.main(verbosity=2)