import statistics

def Vito(n, arr):
        arr.sort()
        d = 0
        mid = statistics.mean(arr)
        
        for a in arr:
            d += abs(a - mid)
            
        return int(d)


cases = int(input())
for i in range(cases):
    arr = list(map(int, input().split()))
    print(Vito(arr[0], arr[1:]))