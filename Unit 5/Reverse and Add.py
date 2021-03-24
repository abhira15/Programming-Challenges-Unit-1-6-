
T = int(input())
for _ in range(T):
    a = int(input())
    cnt = 0
    while True:
        k = str(a)
        if k == k[::-1]:
            break
        else:
            m = int(k[::-1])
            a += m
            cnt += 1
    print(cnt, a)
    
