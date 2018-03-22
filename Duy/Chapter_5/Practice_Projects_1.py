Inventory = {'rope': 1, 'torch': 6,'gold coin': 42,'dagger': 1, 'arrow': 12}

def  displayInventory(Inventory):
	print('Inventory: ')
	item = 0
	for k,v in Inventory.items():
		print(str(v)+' '+ k)
		item = item + v 
	print('Total number of item: ' + str(item))
	
displayInventory(Inventory)