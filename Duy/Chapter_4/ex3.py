bien = ['duy','tien','trinh','sang']
while True:
	print('nhap ten ban cua ban: ')
	name = input()
	if name not in bien:
		print('ban khong co nguoi ban ten: ' + name )
	else:
		print(name + ' la ban cua ban' )