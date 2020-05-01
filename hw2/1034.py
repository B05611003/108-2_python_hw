a=[None]*5
for i in range(5):
	a[i]=input()
for i in range(5):
	print(a[i],end='')
	print('\t',end='')
	for j in range(int(a[i])):
		print('*',end='')
	print()