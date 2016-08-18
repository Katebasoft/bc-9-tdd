def super_sum(*argv):
	sum_numbers = 0
	for arg in argv:
		if type(arg) == list:
			for num in arg:
				sum_numbers += num
		elif type(arg) == str:
			return 0
		else:
			sum_numbers += arg
			

	if sum_numbers > 1000:
		return "sum too big"
	elif sum_numbers == 0:
		return "sum too small"
	return sum_numbers


#print super_sum(10, 5, 6, 9)




