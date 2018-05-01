import string as st
s = input("Enter Expression :-\n")
s = s.replace(" ","")
identifier = st.ascii_lowercase + st.ascii_uppercase
digit = st.digits
operators = "+-*/~!%^&="
idt = []
dgt = []
op = []
for i in s:
	if i in identifier:
		idt.append(i)
	if i in digit:
		dgt.append(i)
	if i in operators:
		op.append(i)
print("There are {} identifiers in {}".format(len(idt),s))
print("\n".join(idt))
print("There are {} digit in {}".format(len(dgt), s))
print("\n".join(dgt))
print("There are {} operators in {}".format(len(op),s))
print("\n".join(op))
'''
OUTPUT:
Enter Expression :-
x = a + b * c / e + 9
There are 5 identifiers in x=a+b*c/e+9
x
a
b
c
e
There are 1 digit in x=a+b*c/e+9
9
There are 5 operators in x=a+b*c/e+9
=
+
*
/
+
'''
