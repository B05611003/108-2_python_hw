a = input()
b = a.split()
cur = 20

if(int(b[0])%2 == 0):
	for i in range(1,int(b[0])+1):
		if i == 1:
			continue
		elif i%2 == 1:
			cur -= int(b[2])
		else:
			cur += int(b[1])
else:
	for i in range(1,int(b[0])+1):
		if i%2 == 1:
			cur += int(b[1])
		else:
			cur -= int(b[2])
print(cur)