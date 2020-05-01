a=input()
if a.isdigit():
	print(a+" is a number.")
elif a.isupper():
	print(a+" is a capital letter.")
elif a.islower():
	print(a+" is a lowercase letter.")
	print("swap to capital letter "+a.upper()+".")
else:
	print(a+" is a punctuation.")