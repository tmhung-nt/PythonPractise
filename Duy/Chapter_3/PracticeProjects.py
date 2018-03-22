def collatz(a):
	if a%2 == 0:
		return a/2
	else:
		return 3*a+1
		
print('Enter number:')
while True:
	a = int(input())
	a1 = collatz(a)
	print(int(a1))