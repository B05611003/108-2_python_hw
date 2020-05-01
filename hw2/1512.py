N,K = [int(x) for x in input().split()]
data = [int(x) for x in input().split()]
total = 0
for i in data:
	if i >= K:
		total+=i//K*K
print(total)

