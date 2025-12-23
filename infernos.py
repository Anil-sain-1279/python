t = int(input())

for _ in range(t):
    n, x = map(int,input().split())
    h = list(map(int,input().split()))

    s = 0
    for i in range(len(h)):
        s += (h[i] + x - 1) // x

    m = max(h)

    print(min(s,m))
