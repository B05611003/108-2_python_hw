a = input()
if a != '1' and a != '2':
	print("roll error")
	exit(0)
b = int(input())
if b not in range(0,101):
	print("score error")
else:
	if (a == '1' and b >= 60) or (a == '2' and b >= 70):
		print("pass")
	else:
		print("fail")

