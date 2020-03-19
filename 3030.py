import math
a = float(input())
b = math.sqrt(a) * 10
print("Original: %.2f"%(a))
print("Adjusted: %.2f(+%.0f)"%(b,b-a))

