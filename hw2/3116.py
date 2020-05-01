NTU={'T':"Top",'H':"Hoodie",'B':"Backpack"}
key=input()
while key != '-1':
	if key in NTU:
		print(NTU[key])
	elif key == '-2':
		lkeys=list(NTU.keys())
		lkeys.sort()
		lvalues=[]
		for i in lkeys:
			lvalues.append(NTU[i])
		print("keys:",lkeys)
		print("values:",lvalues)
	elif key == '-3':
		delkey=input()
		if delkey in NTU:
			del NTU[delkey]
		else:
			print("key %s does not exist, cannot delete."%(delkey))
	else:
		print(key+' does not exist. Enter a new product category:')
		value=input()
		NTU[key]=value
	key = input()