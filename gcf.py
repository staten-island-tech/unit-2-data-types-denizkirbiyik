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
