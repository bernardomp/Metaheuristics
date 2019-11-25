from functools import reduce
import random

def shake(x,k,N):
    
    neighbourhood_structure = N[k]
    
    neighbours = list(neighbourhood_structure(x=x))

    return random.choice(neighbourhood_structure)

def neighbourhood_change_sequential(x,x_prime, k,eval_sol):

    if eval_sol(x)<eval_sol(x_prime):
        x = x_prime 
        k=1
    else:
        k+=1

def reducedVNS(x,k_max,N):

    for i in range(1):
        k = 1
        while k<k_max:
            x_prime = shake(x,k,N)
            neighbourhood_change_sequential(x,x_prime,k)


def hamming_distance(x=None,distance=1):
    neighbours = set()

    level = hamming_distance_one(x)
    neighbours.update(level)

    while(distance>1):
        level = list(map(hamming_distance_one,level))
        level = reduce(lambda x,y: x+y, level)

        neighbours.update(level)
        distance-=1
    
    neighbours.discard(x)

    return neighbours


def hamming_distance_one(x):
    
    neighbours = []

    char = None
    for i in range(0,len(x)):

        if x[i] == '0':
            char='1'
        else:
            char='0'
        
        neighbours.append(x[:i] + char + x[i+1:])
    
    return neighbours
        