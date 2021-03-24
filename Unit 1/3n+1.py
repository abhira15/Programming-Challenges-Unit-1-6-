def contra(k) :    
    count = 0
    while k != 1 :
        if k%2 == 0 :
            k = k/2
            
            count=count+1
            
        else :
            k = 3*k+1
            
            count=count+1
    c = count + 1
    return c
# main code 
i= int(input("Enter the value for i : "))
j = int(input("Enter the value for j : "))
l = list()
# i to j
for n in range( i , j+1 ) :
    r = contra(n)
    l.append(r)
print(i,j,max(l))
    
    

            