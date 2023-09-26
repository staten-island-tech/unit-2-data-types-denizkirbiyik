def short(N, input):
    newList = []
    for i in range(N):
        if(input[i]!=input[i+1]):
            newList.append(input[i+1])
    return newList

def aron(input):
    N = input[0]
    clone = []
    for i in range(1, len(input)):
        clone.append(input[i])
    clone.append(None)
    print(clone)
    if(len(clone)!=len(set(clone))):
        clone = short(len(clone)-1, clone)
    return len(clone)
        
print(aron([3, "C", "Z", "P"]))