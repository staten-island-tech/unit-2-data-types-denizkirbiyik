def b1(l):
    a = l[0]
    l.remove(a)
    l.append(a)
    return l
def b2(l):
    a = l[4]
    l.remove(a)
    l.insert(0, a)
    return l
def b3(l):
    a = l[0]
    b = l[1]
    l[1] = a
    l[0] = b
    return l

def shuffle(input):
    m = []
    n = []
    list1 = ["A", "B", "C", "D", "E"]
    str1 = ""
    for i in range(int(len(input)/2)):
        m.append(input[2*i])
        n.append(input[2*i+1])
    for i in range(len(n)):
        if(m[i] == 1):
            for j in range(n[i]):
                list1 = b1(list1)
        elif(m[i] == 2):
            for j in range(n[i]):
                list1 = b2(list1)
        elif(m[i] == 3):
            for j in range(n[i]):
                list1 = b3(list1)
    for i in range(0, 4):
        str1 += (list1[i]+", ")
    str1 += list1[4]
    return str1
print(shuffle([2, 1, 3, 1, 2, 3, 4, 1]))
