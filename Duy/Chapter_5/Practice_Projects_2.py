dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = {'rope': 1, 'torch': 6,'gold coin': 42,'dagger': 1, 'arrow': 12}

def  displayInventory(Inventory):
	print('Inventory: ')
	item = 0
	for k,v in Inventory.items():
		print(str(v)+' '+ k)
		item = item + v 
	print('Total number of item: ' + str(item))
	
#displayInventory(stuff) 

def addToInventory(Inventory,addedItems):
	for i in range(len(addedItems)):
		Inventory.setdefault(addedItems[i],0)
		Inventory[addedItems[i]] = Inventory[addedItems[i]] + 1
	return Inventory
	
	
inv = {'gold coin' : 42, 'rope': 1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)