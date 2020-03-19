a = input()
b = a.split(' ')
tar = int(b[0])
cur = int(b[1])
count = 0
while tar != cur:
	if cur < tar:
		cur += 5
		count += 1
	else:
		cur -= 2
		count +=1
print(count)