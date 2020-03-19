a = int(input())
num ={1:'壹',2:'貳',3:'參',4:'肆',5:'伍',6:'陸',7:'柒',8:'捌',9:'玖',0:''}
ten_thousand = num[int((a/10000))%10]
thousand = num[int((a/1000))%10]
hundred = num[int((a/100))%10]
ten = num[int((a/10))%10]
one = num[a%10]

if a not in range(1,100000):
	print("out of range")
else:
	if(ten_thousand!=''):
		ten_thousand+='萬'
	if(thousand!=''):
		thousand+='仟'
	if(hundred!=''):
		hundred+='佰'
	if(ten!=''):
		ten+='拾'
	print("%s%s%s%s%s元整"%(ten_thousand,thousand,hundred,ten,one))
