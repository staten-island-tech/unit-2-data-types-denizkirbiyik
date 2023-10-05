def year_check(inp):
    inp, inp2 = [*str(inp)], {*str(inp)}
    if len(inp) == len(inp2):
        return True
    else: return False
    
def main(inp):
    i = inp+1
    while True:
        if year_check(i):
            return i
        i += 1