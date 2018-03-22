import random 
a1 = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')
for a2 in range(1,7):
	print('take a guess')
	guess = int(input())
	if guess < a1:
		print('your guess is too low')
	elif guess > a1:\
		print('your guess is too hight')
	else:
		break 
if guess == a1:
	print('Good job! you guessed my  number '+ str(a2) +' guesses!')
else:
	print('Nope, the number i was thinking of was ' +str(a1))