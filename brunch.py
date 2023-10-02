def brunch(input):
    cost = input[0]
    people = input[-1]
    y1 = people*input[1]
    y2 = people*input[2]
    y3 = people*input[3]
    y4 = people*input[4]
    funding = y1 * 12 + y2 * 10 + y3 * 7 + y4 * 5
    if(funding/2 < cost):
        return "YES"
    else:
        return "NO"
def final(input):
    f = []
    for i in range(10):
        f.append(brunch(input[0][6*i], input[0][6*i+1], input[0][6*i+2], input[0][6*i+3], input[0][6*i+4], input[0][6*i+5]))
    return f