t = int(input())
for _ in range(t):
    n = int(input())
    result = [0] * n
    l, r = 1, n
    
    for i in range(n - 1, -1, -1):
        if i % 2 == 0:
            result[i] = r
            r -= 1
        else:
            result[i] = l
            l += 1

    print(*result)
