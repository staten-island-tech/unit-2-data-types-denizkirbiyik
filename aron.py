def aron(input):
    N = input[0]
    input.remove(N)
    cur1=""
    cur2=""
    num = 0
    for i in range(N):
        cur1 = input[i]
        if(cur1!=cur2):
            num += 1
        cur2 = input[i]
    num += 1
    return num
print(aron([6, "B", "B", "B", "B", "B", "B"]))