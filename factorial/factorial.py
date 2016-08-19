class Factorial(object):
	def __init__(self, num):
		self.num = num

	def factorial(self):
		  fact = 1
		  if self.num < 2:
		    	return 1
		  else:
			    while self.num > 1:
			      	fact *= self.num
			      	self.num-=1
		  return fact
      

f = Factorial(0)
print(f.factorial())