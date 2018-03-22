chuoi = []
print('nhap gia tri cua chuoi: ')
while True:
	gtri = input()
	chuoi.append(gtri)
	chuoi.sort()
	if gtri == '':
		chuoi.remove('')
		break
print(chuoi)