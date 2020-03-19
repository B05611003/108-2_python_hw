col = int(input())
row = int(input())
for i in range(col):
	for j in range(row):
		print("%d*%d=%2d"%(i+1,j+1,(i+1)*(j+1)),end = ' ')
	print("")