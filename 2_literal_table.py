prg = open("program.asm","r")
loc = []
label = []
lc = 0
print("Program:-")
s = prg.readline().strip()
while(s != ""):
    print(s)
    st = s.split()
    if len(st) == 2:
        b = st[0][-1].upper()
        if b == "R":
            lc += 2
        elif (b == "L") or (b == "A") or (b == "T"):
            lc += 4
    if len(st) >= 3:
        b = st[1].upper()
        c = st[2].upper()
        if (b == "DC") or (b == "DS"):
            if "H" in c:
                lc += 2
            elif "F" in c:
                lc += 4
            elif "D" in c:
                lc += 8
        if '=' in c:
            label.append(c)
            loc.append(lc)
    s = prg.readline().strip()
prg.close()
print("\nLiteral Table")
print("{:10} {:10}".format("LITERAL", "VALUE"))
for i in range(len(loc)):
    print("{:10} {:>5}".format(label[i], loc[i]))
