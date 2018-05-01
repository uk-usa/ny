prg = open("3input.txt","r")
loc = []
label = []
lc = 0
bval=0
base=""
print("Program:-")
s = prg.readline().strip()
while(s != ""):
    print(s)
    st = s.split()
  
    if len(st) == 2:
        if st[1] == "START":
            label.append(st[0])
            loc.append(lc)
        b = st[0][-1].upper()
        if b == "R":
            lc += 2
        elif (b == "L") or (b == "A") or (b == "T"):
            lc += 4
    if len(st) >= 3:
        label.append(st[0])
        loc.append(lc)
        b = st[1].upper()
        c = st[2].upper()
        if (b == "DC") or (b == "DS"):
            if "H" in c:
                lc += 2
            elif "F" in c:
                lc += 4
            elif "D" in c:
                lc += 8
    if len(st)==2:
       
        if st[0]=="using":
            
            y=st[1].split(",")
            base=y[1]
            x=y[0]
            if x=="*":
                break;
            else:
                k=x.split("+")
                for i in range(0,len(label)):
                    if label[i]==k[0]:
                        bval=loc[i]+int(k[1])
    s = prg.readline().strip()
prg.close()

print("\nBase Table")
print("{:10} {:10}".format("BASE NO", "CONTENTS"))
print("{:10} {:>5}".format(base,bval))
