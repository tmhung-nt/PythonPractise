catname = []
while True:
	print('Enter name of cat ' +str(len(catname)+1)+'(or enter nothing to stop):')
	name = input()
	if name =='':
		break
	catname = catname + [name]
print('the cat name are:')
for name in catname:
	print(name)