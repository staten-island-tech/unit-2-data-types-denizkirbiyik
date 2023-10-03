def brunch(input):
    cost = input[0]
    people = input[-1]
    y1 = people*input[1] - (people*input[1] % 1)
    y2 = people*input[2] - (people*input[2] % 1)
    y3 = people*input[3] - (people*input[3] % 1)
    y4 = people*input[4] - (people*input[4] % 1)
    extra = (people*input[1] % 1) + (people*input[2] % 1) + (people*input[3] % 1) + (people*input[4] % 1)
    print(extra)
    m = max([(people*input[1] % 1), (people*input[2] % 1), (people*input[3] % 1), (people*input[4] % 1)])
    if(m == (people*input[1] % 1)):
        y1 += extra
    elif(m == (people*input[2] % 1)): 
        y2 += extra
    elif(m == (people*input[3] % 1)): 
        y3 += extra
    elif(m == (people*input[4] % 1)): 
        y4 += extra
    funding = y1 * 12 + y2 * 10 + y3 * 7 + y4 * 5
    if(funding/2 < cost):
        return "YES"
    else:
        return "NO"
def final(input):
    f = []
    for i in range(10):
        f.append(brunch(input[6*i], input[6*i+1], input[6*i+2], input[6*i+3], input[6*i+4], input[6*i+5]))
    return f
print(brunch([5727, 0.1, 0.15, 0.4, 0.35, 477]))