def b1(l):
    n = []
    n.append(l[1])
    n.append(l[2])
    n.append(l[3])
    n.append(l[4])
    n.append(l[0])
    print(n)
    print(1)
    return l
def b2(l):
    n = []
    n.append(l[4])
    n.append(l[0])
    n.append(l[1])
    n.append(l[2])
    n.append(l[3])
    print(n)
    print(2)
    return n
def b3(l):
    n = []
    n.append(l[1])
    n.append(l[0])
    n.append(l[2])
    n.append(l[3])
    n.append(l[4])
    print(n)
    print(3)
    return n

def shuffle(input):
    m = []
    n = []
    list1 = ["A", "B", "C", "D", "E"]
    str1 = ""
    for i in range(int(len(input)/2)):
        m.append(input[i])
        n.append(input[i+1])
    for i in range(len(n)):
        if(m[i] == 1):
            for j in range(n[i]):
                b1(list1)
        elif(m[i] == 2):
            for j in range(n[i]):
                b2(list1)
        elif(m[i] == 3):
            for j in range(n[i]):
                b3(list1)
    for i in range(4):
        str1 += (list1[i]+", ")
    str1 += list1[4]
    return str1
print(shuffle([2, 1, 3, 1, 2, 3, 4, 1]))