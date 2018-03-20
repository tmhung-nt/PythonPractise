tableData = [['apples', 'oranges', 'cherries', 'banana'],              
			 ['Alice', 'Bob', 'Carol', 'David'],              
			 ['dogs', 'cats', 'moose', 'goose']]
			 
def printTable(st):
	size = 0
	colWidths = [0] * len(st)
	for x in range(len(st)):
		size_old = 0
		for y in st[x]:
			size = len(y)
			if size > size_old:
				size_old = size
		colWidths[x] = size_old 
	for j in range(len(st[0])):
		for x in range(len(st)):	
			print str(st[x][j]).rjust(colWidths[x],' '),
		print	
printTable(tableData)
