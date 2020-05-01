change = {'1':"I",'7':"T",'3':"E",'5':"S",'4':"A",'0':"O"}
a = input()
b = ""
for i in range(len(a)):
	if a[i] in change:
		b+=change[a[i]]
	else:
		b+=(a[i])
print(b)