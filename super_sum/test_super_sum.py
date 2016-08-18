import unittest

from super_sum import super_sum

class MySuperSum(unittest.TestCase):

	def setUp(self):
			self.numbers = [10,5,7,8,90,60]

	def test_super_sum(self):
		'''
		Test for the super sum
		'''
		self.assertEqual(super_sum(10, 5, 6, 9),30, "wrong answer")
		self.assertEqual(super_sum([10, 5], 5),20, "wrong answer")
		self.assertEqual(super_sum([5, 6], [4, 5], 10),30, "wrong answer")
		self.assertEqual(super_sum(0,2,[-9,2,1]))

	def test_non_numbers(self):
		'''
		When strings are passed
		'''
		self.assertEqual(super_sum('a', 'a'), 0, "Should return 0")

	def test_empty(self):
		'''When empty string is passed'''
		self.assertEqual(super_sum(''), 0, "Should return 0")

	def test_big_sum(self):
		self.assertEqual(super_sum(1000,9), "sum too big", "Should return sum too big")

	def test_small_sum(self):
		self.assertEqual(super_sum(0,0), "sum too small", "Should return sum too small")

if __name__ == '__main__':
	unittest.main()


