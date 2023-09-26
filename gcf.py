'''
def factor(x):
    y = []
    for i in range(1, x):
        if(x % i == 0):
            y.append(i)
    return y
def gcf(x, y):
    xfactors = factor(x)
    yfactors = factor(y)
    for i in range(1, len(xfactors)):
        for j in range(1, len(yfactors)):
            if(xfactors[-i] == yfactors[-j]):
                return xfactors[-i]
'''
def gcf(x, y):
    if x > y: b = x
    else: b = y
    for z in range(1, b):
        if x % z == 0:
            if y % z == 0:
                a = z
    return a
print(gcf(100,50))