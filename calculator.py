def calculator(number1, number2, operator):
	result = 0
	if type(number1) == int or float and type(number2) == int or float and operator in ('+','-','*','/','//','**'):
		try:
			num1 = float(number1)
			num2 = float(number2)
			if operator == '+':
				result= num1 + num2
			elif operator == '-':
				result= num1 - num2
			elif operator == '*':
				result= num1 * num2
			elif operator == '/':
				result= num1 / num2
			elif operator == '//':
				result= num1 // num2	
			elif operator == '**':
				result= num1 ** num2
		except ZeroDivisionError:
			print("Can not divide by Zero")
			return False
		return result
	else:
		print('Invalid value/operator!!!')
		return False

def parse_input():
	prompt = eval("input('Enter equation: ')")
	text = prompt.split(' ')
	if len(text) == 3:
		num1 = text[0]
		num2 = text[2]
		operator = text[1]
	else:
		print('Not valid!')
		exit()
	return calculator(num1,num2,operator)

