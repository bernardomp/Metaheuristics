

with open("input/inputs.txt","r") as f:

    test_cases = int(next(f).split(" ")[0])
    
    
    next(f)
    elements, capacity = map(int,next(f).split(" "))

    values = list(map(float,next(f).split(" ")))
    if len(values) > elements:
        print("Number of values greater than expected") 

    weights = list(map(float,next(f).split(" ")))
    if len(weights) > elements:
        print("Number of weights greater than expected") 



print(test_cases)
print(elements,capacity)
print(values)
print(weights)