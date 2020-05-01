length=int(input())
index = length//2
data=input()
arr=data.split(' ')
code = (int(arr[index])+int(arr[length-1-index])+1)//2
print(code)