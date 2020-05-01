goal = input().lower()
book=[]
while True:
	a=input()
	if a == 'q':
		break
	book.append(a)
if goal in book:
	print("Yes",book.index(goal)+1)
else:
	print("No",len(book))


	