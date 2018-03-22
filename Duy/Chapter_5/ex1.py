birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}

while True:
	print('Enter your name:(Blank to quit)')
	name = input()
	if name == '':
		break
	if name in birthdays:
		print(birthdays[name] +' is a birthday of ' + name)
	else:
		print('I do not have a birthday information for ' +name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('birthday database update')