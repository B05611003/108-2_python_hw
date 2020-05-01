n=int(input())
b=[int(x) for x in input().split()]
maxh=max(b)
minh=min(b)
print(b.index(maxh)+1,maxh)
print(b.index(minh)+1,minh)