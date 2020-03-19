score = int(input())
if score not in range(1,101):
	print("input out of range")
elif score >= 90:
	print("%.1f\n%s"%(4.3,'A+'))
elif score >= 85:
	print("%.1f\n%s"%(4.0,'A'))
elif score >= 80:
	print("%.1f\n%s"%(3.7,'A-'))
elif score >= 77:
	print("%.1f\n%s"%(3.3,'B+'))
elif score >= 73:
	print("%.1f\n%s"%(3.0,'B'))
elif score >= 70:
	print("%.1f\n%s"%(2.7,'B-'))
elif score >= 67:
	print("%.1f\n%s"%(2.3,'C+'))
elif score >= 63:
	print("%.1f\n%s"%(2.0,'C'))
elif score >= 60:
	print("%.1f\n%s"%(1.7,'C-'))
else:
	print("%d\n%s"%(0,'F'))
