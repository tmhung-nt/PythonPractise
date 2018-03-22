def	collatz(number):
	if number%2 == 0:
		result = number // 2
		print(str(number) + ' // 2 = ' + str(result))
	else:
		result = 3 * number + 1
		print('3 * ' + str(number) + ' + 1 = ' + str(result))
		
print('Please! Enter number: ')
collatz(int(input()))

	
	
