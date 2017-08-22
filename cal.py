start = "0"
goal = -120
moves = 4

def rev(expr):
    expr = str(eval(expr))
    # print('v',expr)
    if '.' in expr and eval(expr) != float(int(eval(expr))) :
        return '0'
    expr = str((int)(eval(expr)))
    negFlag = False
    if expr[0] == '-':
        expr = expr[1:]
        negFlag = True
    s = ''
    for i in range(len(expr)):
        s += (expr[len(expr) - i - 1])
    s = s.strip('0')
    if not s:
        s = '0'
    # print(s)
    if negFlag:
        s = '-'+(s)
    # print(s)
    return s

def insert(num):
    def fun(exprStr):
        return str(int(eval(exprStr))) + str(int(num)) if int(eval(exprStr)) != 0 else str(num)
    return fun

def getPre(exprStr):
    # print(str(eval(exprStr)))
    if len(str(eval(exprStr))) <= 1 or (eval(exprStr) > -10 and eval(exprStr) <= 0):
        return '0'
    return str(eval(exprStr))[:-1]

def neg(expr):
    expr = '-' + str(eval(expr))
    return expr

def changeNum(numF, numT):
    def fun(exprStr):
        # print(int(eval(exprStr)), end=' ')
        if eval(exprStr) != float(int(eval(exprStr))):
            return
        exprStr = str(int(eval(exprStr)))
        for i in range(len(exprStr)):
            if exprStr[i] == str(numF):
                exprStr = exprStr[:i] + str(numT) + exprStr[i+1:]
        exprStr = exprStr.strip('0')
        if exprStr == '.':
            return '0'
        # print(exprStr.strip('0'))
        return exprStr.strip('0')
    return fun

opeartors = []
opestrs = []

def sq(expr):
    return str(eval(expr) ** 2)


ans = []


def dfs(exprStr, moves, goal, ansstr):
    # print(ansstr + ' ===> ', exprStr, eval(exprStr))
    # try:
    #     eval(exprStr)
    #     print(repr(exprStr))
    # except TypeError as e:
    #     print(repr(exprStr))
    try:
        eval(exprStr)
    except:
        return
    if (eval(exprStr) == goal):
        ans.append(ansstr)
        return
    if moves == 0:
        return 
    else :
        for j in range(len(opeartors)):
            i = opeartors[j]
            if isinstance(i, str):
                newStr = '(' + exprStr + ')' + i
            else:
                newStr = i(exprStr)
            nansstr  = ansstr + opestrs[j] + ' '
            dfs(newStr, moves - 1, goal, nansstr)

def inp():
    global start, moves, goal, opeartors, opestrs
    start = input("start num:")
    moves = int(input("steps:"))
    goal = int(input("goal:"))
    n = int(input("ope nums:"))
    for i in range(n):
        o = input()
        if o == 'neg':
            opeartors.append(neg)
            opestrs.append('+/-')
        elif o[0] == 'i':
            ins = int(o[1:])
            opeartors.append(insert(ins))
            opestrs.append(str(ins))
        elif o == 'sq':
            opeartors.append(sq)
            opestrs.append("x^2")
        elif o == '<<':
            opeartors.append(getPre)
            opestrs.append("<<")
        elif o == 'rev':
            opeartors.append(rev)
            opestrs.append("Rev")
        elif o == 'ch':
            f = int(input())
            t = int(input())
            fun = changeNum(f,t)
            opeartors.append(fun)
            opestrs.append(str(f)+'=>'+str(t))
        else :
            opeartors.append(o)
            opestrs.append(o)

inp()
# print(start)
dfs(start, moves, goal, "")
for i in ans:
    print(i)

        