from sys import stdin
precedence = [['*','/','%'],['-','+'],['=']]
print("Enter Expression (e.g :- x = a + b)")
s = stdin.readline()
eq,s = s.split("=")
s = list(s.replace(" ",''))
operators = [[],[],[]]
ans = []
for i in s:
	if i in precedence[0]:
		operators[0].append(i)
	elif i in precedence[1]:
		operators[1].append(i)
	elif i in precedence[2]:
		operators[2].append(i)
temp = "temp"
cnt = 1
for op in operators:
	for i in op:
		ind = s.index(i)
		a = " ".join(s[ind-1:ind+2])
		ans.append(a)
		s[ind-1] = temp + str(cnt)
		cnt+=1
		del s[ind]
		del s[ind]
print()
tt = eq.strip() + " = " + s[0]
ans.append(tt)
for i in range(len(ans)):
	if "=" in  ans[i]:
		print(ans[i])
	else:
		print("temp"+str(i+1),"=",ans[i])
print()
print("Quadruples")
print("{:14} {:>12} {:>8} {:>8} {:>10}".format("Symbol Address","Operators","arg1","arg2","Result"))
for i in range(len(ans)):
	if "=" in ans[i]:
		res,op,arg1 = ans[i].split()
		print("{:>14} {:>12} {:>8} {:>8} {:>10}".format(str(i),op,arg1," ",res))
	else:
		arg1,op,arg2 = ans[i].split()
		print("{:>14} {:>12} {:>8} {:>8} {:>10}".format(str(i),op,arg1,arg2,temp+str(i)))
print("\n")
print("Triple")
print("{:14} {:>12} {:>8} {:>8}".format("Symbol Address","Operators","arg1","arg2"))
for i in range(len(ans)):
	arg1,op,arg2 = ans[i].split()
	if arg1[:4] == temp:
		arg1 = str(int(arg1[-1]) - 1)
	if arg2[:4] == temp:
		arg2 = str(int(arg2[-1] ) - 1)
	print("{:>14} {:>12} {:>8} {:>8}".format(str(i),op,arg1,arg2))
print("\n")
adr= []
print("Indirect Triples")
print("{:>14} {:>14} {:^10} {:14} {:>12} {:>8} {:>8}".format("Symbol Address","Statements","|", "Symbol Address","Operators","arg1","arg2"))
for i in range(len(ans)):
	arg1,op,arg2 = ans[i].split()
	if arg1[:4] == temp:
		arg1 = str('10')+str(int(arg1[-1]) - 1)
	if arg2[:4] == temp:
		arg2 = str('10')+str(int(arg2[-1] ) - 1)
	adr.append(str("10")+ str(i))
	print("{:>14} {:>14} {:^10} {:14} {:>12} {:>8} {:>8}".format(str(i),adr[-1],"|",str("10")+str(i),op,arg1,arg2))
