def factor(x):
    y = []
    for i in range(1, x):
        if(x % i == 0):
            y.append(i)
    return y
print(factor(120))