a = float(input())
b = float(input())
c = input()
if c == '+':
	print("%.2f + %.2f = %.2f"%(a,b,a+b))
elif c == '-':
	print("%.2f - %.2f = %.2f"%(a,b,a-b))
elif c == '*':
	print("%.2f * %.2f = %.2f"%(a,b,a*b))
else:
	print("%.2f / %.2f = %.2f"%(a,b,a/b))

