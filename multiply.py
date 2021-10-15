def multiply_list(list):
	"""
	calculate each element in array

	"""
	result = 1

	for n in list:
		if type(n) == int or type(n) == float:
			result *= n
		else:
			print("Invalid value!!!")
			return False
	return result

