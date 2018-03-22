theBoard = {'top-L': ' ','top-M': ' ','top-R': ' ',
			'mid-L': ' ','mid-M': ' ','mid-R': ' ',
			'low-L': ' ','low-M': ' ','low-R': ' ',}
			
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	
printBoard(theBoard)
print('-----')
print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
print('-----')
print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
print('-----')
print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])