def	collatz(number):
	try:
		number = int(number)
		if number%2 == 0:
			result = number // 2
			print(str(number) + ' // 2 = ' + str(result))
		else:
			result = 3 * number + 1
			print('3 * ' + str(number) + ' + 1 = ' + str(result))
	except ValueError:
		print('You must enter an interger!')
n = raw_input('Please! Enter number:')
collatz(n)
