import random

def randomNum2():
    z = random.randint(-10,10)
    return z

def polynomialgen():
    x1, x2 = randomNum2(), randomNum2()
    
    a = 1
    b = -x1 - x2
    c = x1*x2

    r = random.randint(-5,5)

    if r != 0:
        a, b, c = a*r, b*r, c*r

    print(x1,x2)
    QuadraticEquation = "{}x^2 + {}x + {}"
    printed = QuadraticEquation.format(a,b,c)
    return x1, x2, printed

print(polynomialgen())
