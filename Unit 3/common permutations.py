from collections import Counter


def cp(a, b):
    
    for k, v in zip(a, b):
        some = (Counter(a) & Counter(b)).keys()
        sort = sorted(some)
    
    cp = "".join(sort)
    
    return cp


while(True):
    first = input()
    if first == "" :
        break
    second = input()
    
    print(cp(first, second))
    

    
    


    
    
    
    

    
    

    