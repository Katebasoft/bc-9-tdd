import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial(self):
        #Test for 0
        self.assertEqual(factorial(0), 1, "Should return 1")

    def test_factorial(self):
        self.assertEqual(factorial(3), 6, "Wrong Answer")

    def test_empty(self):
        self.assertEqual(factorial(''), 0, "Wrong Answer")

    def test_empty(self):
        self.assertEqual(factorial(100),"Doesn't allow big numbers")

     

if __name__ == '__main__':
    unittest.main()