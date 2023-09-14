def factor(x):
    y = []
    for i in range(1, x):
        if(x % i == 0):
            y.append(i)
    return y
def gcf(x, y):
    xfactors = factor(x)
    yfactors = factor(y)
    xlen = len(xfactors)
    ylen = len(yfactors)
    for i in range(1, xlen):
        for j in range(1, ylen):
            if(xfactors[-i] == yfactors[-j]):
                return xfactors[-i]
