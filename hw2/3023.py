k=[]
num=int(input())
while num != -1:
	k.append(num)
	num=int(input())
print(k)
k.sort()
print(k)
total = 0
for i in k:
	if i>30:
		total+=i
print(total)