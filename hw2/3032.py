def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
k=[]
num=input()
while num != 'q':
	if(not is_number(num)):
		print("Please Enter Numbers Only")
	else:
		k.append(eval(num))
	num=input()
h=k.copy()
print(k)
k.sort()
print(k)
k.sort(reverse = True)
print(k)
print(h)


