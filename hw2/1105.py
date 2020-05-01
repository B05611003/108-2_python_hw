score=[[1,76,73,85],[2,88,84,76],[3,92,82,92],[4,82,91,85],[5,72,74,73]]
total = 0
maxavg=0
maxwho=0
avg=0
for i in score:
	print("student %s"%(i[0]))
	for j in range(3):
		print(" %d: %d"%(j+1,i[j+1]))
		total+=i[j+1]
	print(" sum: %d"%(i[1]+i[2]+i[3]))
	print(" avg: %.2f"%((i[1]+i[2]+i[3])/3))
	if (i[1]+i[2]+i[3])/3 >maxavg:
		maxavg = (i[1]+i[2]+i[3])/3
		maxwho = i[0]
print("total: %d, avg: %.2f"%(total,total/15))
print("highest avg: student %d: %.2f"%(maxwho,maxavg))
