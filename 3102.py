def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
a = int(input())
for j in range(2,a):
	if is_prime(j):
		print("%d is prime"%(j))