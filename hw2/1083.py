a=int(input())
b=[]
maxx=0
code=""
total=0
for i in range(a):
	s=input()
	b.append(s.upper())
for i in b:
	total=0
	for j in i:
		total+=(ord(j)-64)
	print(i,"= %d"%(total))
	if total>maxx:
		code=i
		maxx=total
print("%s is the key."%(code))



