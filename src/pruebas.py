def flip(x):
    return list(map(lambda y: 1-y,x))

def flip_elements(x,positions):
    
    aux = x[:]

    for pos in positions:
        aux[pos] = 1 - aux[pos]
    
    return aux

print(flip_elements([1,1,0,0],[0,1]))