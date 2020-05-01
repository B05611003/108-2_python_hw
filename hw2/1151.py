a=[]
num=int(input())
while num!=-1:
	a.append(num)
	num=int(input())
size=len(a)
for i in range(size):
	print(a[size-1-i])
	for j in range(a[size-1-i]	):
		print()
print("--------------------")
