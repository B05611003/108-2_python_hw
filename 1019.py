a = float(input())/100
b = float(input())
bmi = b/a/a
print("%.2f"%(bmi))
if bmi >= 35:
	print("Obese Class III")
elif bmi >= 30:
	print("Obese Class II")
elif bmi >= 27:
	print("Obese Class I")
elif bmi >= 24:
	print("Overweight")
elif bmi >= 18.5:
	print("Normal")
else:
	print("Underweight")