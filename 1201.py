a = input()
b = a.split(' ')
n = float(b[0])
m = float(b[1])

x = (4*n - m)/2
y = (m - 2*n)/2
if x.is_integer() and y.is_integer() and x > 0 and y > 0:
	print("YES")
	print("%d %d"%(x,y))
else:
	print("NO")