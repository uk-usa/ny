from collections import defaultdict
firstSets = {}
followSets = {}
EPSILON = "#"
terminal = []
non_terminal = []
def buildFirstSets(grammar):
    firstSets = {}
    buildSet(firstOf)

def firstOf(symbol):
    # print(firstSets[symbol])
    keys_list = firstSets.keys()
    if symbol in keys_list :
        return firstSets[symbol]

    first = firstSets[symbol] = {}

    if (isTerminal(symbol)):
        first[symbol] = True
        return firstSets[symbol]

    productionsForSymbol = getProductionsForSymbol(symbol)
    for k in productionsForSymbol:
        production = getRHS(productionsForSymbol[k])

        for i in production:
            productionSymbol = i

            if productionSymbol == EPSILON:
                first[EPSILON] = True
                break

            firstOfNonTerminal = firstOf(productionSymbol)
            first_keys_list = firstOfNonTerminal.keys()
            if EPSILON not in first_keys_list:
                merge(first, firstOfNonTerminal,None)
                break

            merge(first, firstOfNonTerminal, [EPSILON])
    return first

def getProductionsForSymbol(symbol):
    productionsForSymbol = {}
    for k in grammar:
        if grammar[k][0] == symbol:
            productionsForSymbol[k] = grammar[k]
    return productionsForSymbol

def getLHS(production):
    p = production.replace(" ","").split("->")
    return p[0]

def getRHS(production):
    p = production.replace(" ","").split("->")
    return p[1]

def buildFollowSets(grammar):
    followSets = {}
    buildSet(followOf)

def followOf(symbol):
    keys_list = followSets.keys()
    if symbol in keys_list :
        return followSets[symbol]

    follow = followSets[symbol] = {}

    if symbol == START_SYMBOL:
        follow['$'] = True

    productionsWithSymbol = getProductionsWithSymbol(symbol)
    for k in productionsWithSymbol:
        production = productionsWithSymbol[k]

        RHS = getRHS(production)

        symbolIndex = RHS.index(symbol)
        followIndex = symbolIndex + 1

        while(True):
            if followIndex == len(RHS):
                LHS = getLHS(production)
                if LHS != symbol :
                    merge(follow, followOf(LHS),None)
                break
            followSymbol = RHS[(followIndex)]
            firstOfFollow = firstOf(followSymbol)
            first_keys_list = firstOfFollow.keys()
            if EPSILON not in first_keys_list:
                merge(follow, firstOfFollow, None)
                break
            merge(follow, firstOfFollow, [EPSILON])
            followIndex += 1
    return follow

def buildSet(builder):
    for k in grammar:
        builder(grammar[k][0])


def getProductionsWithSymbol(symbol):
    productionsWithSymbol = {}
    for k in grammar:
        production = grammar[k]
        RHS = getRHS(production)
        if symbol in RHS:
            productionsWithSymbol[k] = production
    return productionsWithSymbol


def isTerminal(symbol):
    return symbol  not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def merge(to, from1, exclude):
    if not exclude:
        exclude = []
    for k in from1:
        if k not in exclude:
            to[k] = from1[k]



grammar = {}

count = 1
n = int(input("Enter the number of production: "))
for i in range(n):
    s = input().strip()
    s = s.replace(" ","")
    non_terminal.append(s[0])
    for T in s[3:]:
        if T not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ|" and T not in terminal:
            if T == EPSILON :
                if "$" not in terminal:
                    terminal.append("$")
            else:
                terminal.append(T)
    if "|" in s:
        key = s[0:3]
        st = s.split("|")
        grammar[count] = st[0]
        count+=1
        for j in st[1:]:
            grammar[count] = key + j
            count+=1
    else:
        grammar[count] = s
        count += 1

predictive_table = []
for i in range(len(non_terminal) + 1):
    map = []
    for j in range(len(terminal) + 1):
        if i == 0 and j == 0:
            map.append(None)
        elif i == 0 and j > 0:
            map.append(terminal[j-1])
        elif j == 0 and i > 0:
            map.append(non_terminal[i-1])
        else:
            map.append("")
    predictive_table.append(map)


START_SYMBOL = input("Enter start symbol: ")
print()
buildFirstSets(grammar)
# print("First")
# for i,val in firstSets.items():
#     if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         continue
#     print(i,end="\t")
#     for k in val.keys():
#         print(k, end=", ")
#     print()

buildFollowSets(grammar)
print("Follow")
for i,val in followSets.items():
    print(i,end="\t")
    for k in val.keys():
        print(k, end=", ")
    print()

# rules = defaultdict(list)
# for i , val in grammar.items():
#     s = val.split("->")
#     st = s[1].split("|")
#     for i in  st:
#         rules[s[0]].append(i)
# for NT in non_terminal:
#     firsts = firstSets[NT]
#     for fi in firsts:
#         ind_i = non_terminal.index(NT) + 1
#         if fi == EPSILON:
#             follows = followSets[NT]
#             for fol in follows:
#                 ind_j = terminal.index(fol) + 1
#                 ans = NT + " -> " + "#"
#                 predictive_table[ind_i][ind_j] += (ans + ",")
#         else:
#             ind_j = terminal.index(fi) + 1
#             ans = ""
#             for rl in rules[NT]:
#                 if fi in rl:
#                     ans = rl
#                     break
#             ans = rules[NT][0] if ans == "" else ans
#             ans = NT +" -> " + ans
#             predictive_table[ind_i][ind_j] += (ans + ",")
#
# print("\nParser Table")
# for i in predictive_table:
#     for j in i:
#         print("{:^12}".format(str(j)),end=" ")
#     print()
