from collections import defaultdict
production = {}
non_ternimal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input("Enter number of production: "))
first_list = defaultdict(list)
def first(k,v):
    val = production[v]
    for i in val:
        vl = i[0]
        if vl in non_ternimal:
            vl = first(k,vl)
        else:
            if vl not in first_list[k]:
                first_list[k].append(vl)

for _ in range(n):
    s = input().strip().split()
    s = "".join(s)
    T , rule = s.split("->")
    rules = rule.split("|")
    production[T]=rules
# print(production)
for key, val in production.items():
    k = key
    for i in val:
        v = i[0]
        if v in non_ternimal:
            v = first(k,v)
        else:
            if v not in first_list[k]:
                first_list[k].append(v)

print("{:10}{:10}".format("TERNIMAL","FIRST"))
for key, val in first_list.items():
    print("{:^10}{:^10}".format(str(key), str(val)))
'''
OUTPUT:
Enter number of production: 4
S->ACB|CbB|Ba
A->da|BC
B->g|#
C->h|#
TERNIMAL  FIRST
    S     ['d', 'g', '#', 'h']
    A     ['d', 'g', '#']
    B     ['g', '#']
    C     ['h', '#']
'''
