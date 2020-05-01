letter={'a':'x','b':'y','c':'z','d':'a','e':'b','f':'c','g':'d','h':'e','i':'f','j':'g','k':'h','l':'i','m':'j','n':'k','o':'l','p':'m','q':'n','r':'o','s':'p','t':'q','u':'r','v':'s','w':'t','x':'u','y':'v','z':'w',
'A':'x','B':'y','C':'z','D':'a','E':'b','F':'c','G':'d','H':'e','I':'f','J':'g','K':'h','L':'i','M':'j','N':'k','O':'l','P':'m','Q':'n','R':'o','S':'p','T':'q','U':'r','V':'s','W':'t','X':'u','Y':'v','Z':'w'}
b = []
final = []
while True:
	le=input()
	if le == '-1':
		break
	b.append(le)
for i in range(len(b)):
	final.append("")
	for j in range(len(b[i])):
		if b[i][j] in letter:
			final[i]+=letter[b[i][j]]
		else:
			final[i]+=str(b[i][j])
stfin = " ".join(final)
print(stfin)