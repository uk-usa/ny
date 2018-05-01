n = int(input("Enter the line of code:-"))
code = []
print("Enter your Code")
for i in range(n):
    s = input().strip()
    s = s.split()
    s = "".join(s)
    code.append(s)
opt = []
for i in range(n):
    s = code[i].split("=")
    if s[1].strip() not in opt:
        opt.append(s[1].strip())

print("\nOUTPUT CODE")
for i in range(len(opt)):
    s = list(opt[i])
    s = " ".join(s)
    print("temp" + str(i+1) + " = " + s)
