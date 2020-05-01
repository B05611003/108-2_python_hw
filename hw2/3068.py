di={'P':"Pikachu",'M':"Mickey Mouse",'H':"Hello kitty"}
key=input()

while key != '-1':
	if key in di:
		print(di[key])
	else:
		print(key+" does not exist. Enter a new one:")
		add=input()
		di[key]=add
	key=input()

