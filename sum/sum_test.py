import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):

	def setUp(self):
			self.numbers = [10,5,7,8,90,60]

	def test_sum_of_numbers(self):
		'''
		Test sum of digits/numbers
		'''
		result = my_sum(5,10)
		self.assertEqual(result, 15)
		self.assertEqual(my_sum(0.5,1.2),1.7)
		self.assertEqual(my_sum(-9,2), -7)

	def test_non_numbers(self):
		'''
		Assert throwing of exceptions when it's a non-number
		'''
		self.assertEqual(my_sum('a', 'a'), "You didn't pass numbers")

if __name__ == '__main__':
	unittest.main()



