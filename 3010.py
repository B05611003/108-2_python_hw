def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
a = int(input())
if is_prime(a):
	print("%d is prime"%(a))
else:
	print("%d is not prime"%(a))