i = 1
f = 1.00
a = input()
while a != 'q':
	if float(a).is_integer():
		i *= int(a)
	else:
		f *= float(a)
	a = input()
print("%.2f\n%d"%(f,i))
if i > f:
	print("Float < Int")
elif i < f:
	print("Float > Int")
else:
	print("Float = Int")	