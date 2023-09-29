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
