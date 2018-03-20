grid = [['.', '.', '.', '.', '.', '.'],        
		['.', 'O', 'O', '.', '.', '.'],        
		['O', 'O', 'O', 'O', '.', '.'],        
		['O', 'O', 'O', 'O', 'O', '.'],        
		['.', 'O', 'O', 'O', 'O', 'O'],        
		['O', 'O', 'O', 'O', 'O', '.'],        
		['O', 'O', 'O', 'O', '.', '.'],        
		['.', 'O', 'O', '.', '.', '.'],        
		['.', '.', '.', '.', '.', '.']]

def Character_Picture_Grid(s):
	s = [0]*len(grid[0])
	for y in range(len(grid[0])):
		s[y] = [0]*len(grid)
	for x in range(len(s)):
		for z in range(len(s[x])):
			s[x][z] = grid[z][x]

	for t in range(len(s)):
		print ' '.join(s[t])
		
Character_Picture_Grid(grid)