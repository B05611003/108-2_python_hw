a = int(input())
left = a%12
dozen = (a-left)/12
if left == 0:
	print("%d dozen"%(dozen))
else:
	print("%d dozen and %d"%(dozen,left))
