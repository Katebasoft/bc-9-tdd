import unittest
from factorial import Factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial(self):
        #Test for 0
        self.assertEqual(factorial(0), 1, "Should return 1")

     

if __name__ == '__main__':
    unittest.main()