n = int(input("Enter Number Of lines:-"))
inputProgram = []
print("ENTER INPUT PROGRAM")
for _ in range(n):
    a = list(input().strip().split())
    inputProgram.append(a)
print()
initLoc = int(input("Enter the Initial Address Loaction:-"))
print()
print("OUTPUT PROGRAM:-")
for i in range(len(inputProgram)):
    absloc = int(inputProgram[i][0]) + initLoc
    print("\n"+str(absloc)+" "+inputProgram[i][1],end=" ")
    chr = inputProgram[i][1].upper()
    if chr == "L" or chr == "A" or chr == "ST":
        print(inputProgram[i][2],end=" ")
        no = inputProgram[i][3]
        ind = no.index("(")
        ansloc = int(no[:ind]) + initLoc
        print(str(ansloc) + no[ind:],end=" ")
print()
""" OUTPUT
Enter Number Of lines:- 6
ENTER INPUT PROGRAM
0 L 1, 16(0,15)
4 A 1, 12(0,15)
8 ST 1, 20(0,15)
12 4
16 5
20 -

Enter the Initial Address Loaction:-530

OUTPUT PROGRAM:-

530 L 1, 546(0,15)
534 A 1, 542(0,15)
538 ST 1, 550(0,15)
542 4
546 5
550 -
"""
