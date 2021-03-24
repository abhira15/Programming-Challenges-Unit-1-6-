from sys import stdin

def read_numbers():
    return int(stdin.readline())

def parties():
    days = read_numbers()
    nparties = read_numbers()
    
    return days, [read_numbers() for _ in range(nparties)]

def remove(day):
    return day%7 == 6 or day%7 == 5

def count_hartals(days, parties):

    calendar = [0 for _ in range(days)]

    for p in parties:
        current = p
        while current <= days:
            calendar[current-1] = 1
          
            current += p  

    for d in range(days):
        if remove(d):
            calendar[d] = 0
 
    return int(sum(calendar))

print("Enter number of cases :")
ncases = read_numbers()

for c in range(ncases):
    days, parties = parties()
    print(count_hartals(days, parties))