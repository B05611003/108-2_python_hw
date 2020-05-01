def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

total = 0.0
while True:
	n = input()
	if n =='q':
		break
	if is_number(n):
		total+=(float(n)%1)
print("%.2f"%(total))

