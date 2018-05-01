import re
mdt,mnt,ala,mntc,mdtc,mdtp,ala_macro_binding = [],[],[],0,0,0,{}
input = open("macro.txt","r")
output = ""

class MntTuple:
    name = ""
    index = 0
    def __init__(self, s, i):
        self.name = s
        self.index = i

    def toString(self):
        s = "[" + str(self.name) + " , " + str(self.index) + "]"
        return s

def pass1():
    s = input.readline()
    while(s != ""):
        if s.upper()[:len(s)-1] == "MACRO":
            processMacroDefinition()
        s = input.readline()
    print("MDT:-")
    showMdt()

def processMacroDefinition():
    s = input.readline()
    spt = s.split()
    macro_name = spt[0]
    global mdtc,ala,mntc
    mnt.append(MntTuple(macro_name,mdtc))
    mntc+=1
    pass1Ala(s)
    x= ""
    for i in spt:
        st = i.split(",")
        if len(st)>1:
            x += st[0]
            x += ","
            x += st[1]
        else:
            x = i
            for i in range(len(x) , 12):
                x+= " "
    mdt.append(x)
    mdtc+=1
    addIntoMdt(len(ala))

def pass1Ala(s):
    temp = s.split()
    macro_name = temp[0]
    l = []
    for i in temp[1].split(','):
        x = i
        if "=" in x:
            t = x.split("=")
            x = t[0]
        l.append(x)
    ala.append(l)
    ala_macro_binding[macro_name] = len(ala_macro_binding)

def addIntoMdt(ala_number):
    global mdtc
    temp = ""
    s = ""
    l = ala[ala_number-1]
    isFirst = False
    while(s.upper() != "MEND\n"):
        isFirst = True
        s = input.readline()
        line = ""
        tm = s.split()
        temp = tm[0]
        for i in range(len(temp),12):
            temp += " "
        line += temp
        if len(tm)>1:
            st = tm[1].split(",")
            for i in st:
                temp = i
                if temp[0] == "&":
                    x = l.index(temp)
                    temp = ",#" + str(x)
                    isFirst = False
                elif not isFirst:
                    temp = "," + str(temp)
                line += temp
        mdt.append(line)
        mdtc+=1

def showMdt():
    # out = open("out_mdt.txt","w+")
    for i in mdt:
        print(i)
        # out.write(str(i))

if __name__ == '__main__':
    pass1()
