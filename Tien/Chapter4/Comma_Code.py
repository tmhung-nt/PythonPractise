spam = ['apples', 'bananas', 'tofu', 'cats']

def Comma_Code(sp):
	n = len(sp)
	sp[n-1] = 'and ' +sp[n-1]
	str1 = ', '.join(sp)
	print str1
	
Comma_Code(spam)
