def insert(input):
    for i in range(1, len(input)):
        cur = input[i]
        j = i - 1    
        while j >= 0 and cur < input[j]:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = cur
    return input

def village(input):
    N = input[0]
    input.remove(N)
    input = insert(input)

