a = int(input())
for i in range(a):
	for j in range(a):
		if a-i-1 <= j:
			print("*",end = '') 
		else:
			print(" ",end = '') 
	print('')

