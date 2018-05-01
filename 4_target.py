from collections import defaultdict
lables=[]
lc=[0]
lables
pseudo=["start","using","END","DC","DS"]
my_dict={'A':4,'L':4,'ST':4,'start':0,'using':0,'DS':4,'DC':4}
st_dict={}
mne=["A","L","ST"]
lm=[4,4,4]
lcarray=[]
lit_dict={}
lc=0
mot=[]
pot=[]
lit_dict = defaultdict(list)
with open("4input.txt","r") as my_file:
    for line in my_file:
        
       # print(line)
        strt=line.split(' ')
        strt[-1] = strt[-1].strip()
        
        y=strt[len(strt)-1]
        
        if "," in y:
            s1=y.split(',')
            
            lit_dict[s1[0]].append(s1[1])
        if(strt[0].isalpha()):
 
            lables.append(strt[0])
            
            if ((strt[1] in pseudo)and ( strt[1] not in pot)):
                pot.append(strt[1])
            if (strt[1] in pseudo):
                if strt[1] in my_dict:
                    lcarray.append(lc)
                    st_dict[strt[0]]=lc
                    lc=lc+my_dict[strt[1]]
                    
                                           
 
                
            if (strt[1] in mne)and (strt[1] not in mot):
                mot.append(strt[1])
                if strt[1] in my_dict:
 
                    lcarray.append(lc)
                    st_dict[strt[0]]=lc
                    lc=lc+my_dict[strt[1]]
 
        elif(strt[0]==''):
            #print(strt.index('using'))
            x=strt[len(max(lables,key=len))+1]
            if (x in pseudo) and (x not in pot):
                pot.append(x)
                if x in my_dict:
                    lcarray.append(lc)
                    lc=lc+my_dict[x]
                
            if (x in mne) and (x not in mot):
                mot.append(x)
                if x in my_dict:
                    lcarray.append(lc)
                    lc=lc+my_dict[x]
 
a=len(max(mot,key=len))
b=len(max(pot,key=len))
c=len(min(mot,key=len))
d=int(len(min(pot,key=len)))
print(st_dict)
print(lit_dict)
'''print("lables:")           
for s in lables:
    print(s)'''
print("-"*20) 
print(" MOT :")
print("opcode |   length")
for s in mot:
    x=12
    if(len(s)==c):
        x=12+(a-c)
    print(s,end=' '*x)
    if s in my_dict:
        print( str(my_dict[s]),end=' '*x)
    print()
print("-"*20) 
print("POT:")
print("opcode     |     length")

for s in pot:
    x=12
    if(len(s)==d):
        x=12+(b-d)
    print(s,end=' '*x)
    if s in my_dict:
        print( "P"+str(s).upper(),end=' '*x)
    print()
    
print("-"*20) 
'''print("lc:")
for s in lcarray:
    print(s)'''
    
print("-"*20) 
print("symbol table:")
print("symbol    |     value")

for s in st_dict:
    x=12
    print(s,end=' '*x)
    if s in st_dict:
        print(st_dict[s],end=' '*x)
    print()
print("-"*20)    
flag=False    
print(lit_dict)
print("-"*20)   
print("code after pass 2:")
print("-"*20)
print(" ADDRESS |     SYMBOL |     STATEMENT  ")
i=0
with open("4_target.txt","r") as my_file:
    for line in my_file:
        strt=line.split(' ')
        strt[-1] = strt[-1].strip()
        y=strt[len(strt)-1]
        if "," in y:
            s1=y.split(',')
        if(i<len(lcarray)):
            for s in mot:
                if s in strt:
                    print(lcarray[i],end=" "*4)
                    print(s+" "*7+"1",end=" "*10)
                    flag=True
                    
                    for a in st_dict:
                        if a in s1:
                            print(st_dict[a])
            if(flag==False):
                print(lcarray[i])
                 
        else:
            break;
        i=i+1
        flag=False



        
