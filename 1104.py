twenty = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
large_n = ["","thousand","million"]
def numbertowords(num):
	if num == 0:
		return "zero"
	res = ""
	for i in range(len(large_n)):
		if num % 1000 != 0:
			res = transfer(num%1000) + large_n[i] + " " + res
		num /= 1000
	return res.strip()

def transfer(num):
	if num == 0:
		return ""
	elif num < 20:
		return twenty[num] + " "
	elif num < 100:
		return tens[int(num)/10] + " " + transfer(num%10)
	else:
		return twenty[int(num)/100] + " hundred " + transfer(num%100)
a = int(input())
if a not in range(1,10000000):
	print("out of range")
elif a == 1:
	print("one dollar")
else:
	print(numbertowords(a))
