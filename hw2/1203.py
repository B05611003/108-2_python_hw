a=int(input())
b=[]
yn={'yes':0,'no':0,'ns':0}
for i in range(a):
	b.append(input())
for i in b:
	if i.isupper():
		yn['no']+=1
	elif i.islower():
		yn['yes']+=1
	else:
		yn['ns']+=1
print("%d %d %d"%(yn['yes'],yn['no'],yn['ns']))




