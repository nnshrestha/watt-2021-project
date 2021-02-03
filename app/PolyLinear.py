import random

def randomNum3():
    z = random.randint(-20,20)
    return z

def noZeros(m):
    if m == 0:
        m += 1
    return m

def lineargen1():
    m, b = randomNum3(), randomNum3()
    m = noZeros(m)
    LinearEquation = "y = {}x + {}"
    printedEquation = LinearEquation.format(m,b)

    # Answer #
    xInter = round(-b/m,2)
    return xInter, printedEquation

def lineargen2():
    y1, m, x1 = randomNum3(), randomNum3(), randomNum3()
    m = noZeros(m)
    LinearEquation = "(y - {}) = {}(x - {})"
    printedEquation = LinearEquation.format(y1,m,x1)

    # Answer #
    yInter = round((-x1*m) + y1,2)
    xInter = round((-y1 + m*x1)/m, 2)

    return yInter, xInter, printedEquation

def lineargen3():
    A, B, C = randomNum3(), randomNum3(), randomNum3()
    A = noZeros(A)
    LinearEquation = "{}x + {}y = {}"
    printedEquation = LinearEquation.format(A,B,C)

    # Answer # 
    yInter = round(C/B, 2)
    xInter = round(C/A, 2)

    return yInter, xInter, printedEquation

####

def linearPicker():
    t = random.randint(1,3)
    if t == 1:
        print("1")
        return lineargen1()
    elif t == 2:
        print("2")
        return lineargen2()
    else:
        print("3")
        return lineargen3()

print(linearPicker())