guess = 0
ans = int(input())
maxra = 100
minra = 1
while ans != guess:
	print("%d < ? < %d"%(minra,maxra))
	guess = int(input())
	if guess <= minra or guess >= maxra:
		print("out of range")
		continue
	if guess < ans:
		minra = guess
		print("wrong answer, guess larger")
	elif guess > ans:
		maxra = guess
		print("wrong answer, guess smaller")
print("bingo answer is %d"%(ans))