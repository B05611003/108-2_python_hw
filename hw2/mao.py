a=input()
b=input()
c=a.split()
d=b.split()
sum=0
for i in range(0,len(d)):
    if int(d[i])>=int(c[1]):
        sum=sum+(int(d[i])//(int(c[1]))*int(c[1]))
 
print(sum)