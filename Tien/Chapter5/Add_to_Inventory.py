def displayInventory(inventory):    
	print("Inventory:")    
	item_total = 0    
	for k, v in inventory.items():        
		print(str(v) + ' ' + k)        
		item_total += v    
	print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):    
	
	for j in range(len(addedItems)):
		for i, v in inventory.items():
			if str(addedItems[j]) in str(i):
				v += 1
				inventory[i] = v
				break
			else:
				inventory[str(addedItems[j])]=1
	return inventory
				
	
inv = {'gold coin': 42, 'rope': 1} 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
inv = addToInventory(inv, dragonLoot) 
displayInventory(inv)