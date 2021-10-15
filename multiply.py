def multiply_list(list):
	result = 1

	for n in list:
		if type(n) == int or type(n) == float:
			result *= n
		else:
			print("Invalid value!!!")
			return False
	return result

print(multiply_list([1,2,3]))
