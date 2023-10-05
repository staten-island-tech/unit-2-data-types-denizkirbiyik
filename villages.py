def insert(inp):
    for i in range(1, len(inp)):
        cur = inp[i]
        j = i - 1    
        while j >= 0 and cur < inp[j]:
            inp[j + 1] = inp[j]
            j -= 1
        inp[j + 1] = cur
    return inp

def village(inp):
    N = inp[0]
    inp.remove(N)
    inp = insert(inp)
    distances = []
    for i in range(N-2):
        distances.append((inp[i+2]-inp[i])/2)
    distances = insert(distances)
    return distances[0]
