n=int(input())
a={}
ma=0
for i in range(n):
	h,k=[x for x in input().split()]
	if h in a:
		a[h]+=int(k)
	else:
		a[h]=int(k)
for i in a:
	if a[i]>ma:
		ma=a[i]
		ite = i
print(ite,a[ite])
