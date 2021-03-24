avg = 0
total = 0
sum = 0

n = int(input())

l1 = []
l2 = []

for i in range(0,n):
    l1.append(float(input()))
    sum+=l1[i]
avg = sum/n

def diff(i,j):
    if(i>j) :
        return i-j
    else :
        return j-i
    
for i in range(0,n) :
    difference = round(diff(l1[i] , avg),3)
    if difference in l2 :
        continue
    else:
        l2.append(difference)

for i in l2:
    total += i
print(total)
    