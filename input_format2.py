t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int,input().split())
    p = set()
    m = 0
    c = 0
    for i in a:
        if(i not in p):
            p.add(i)
            c += 1
        else:
            p.remove(i)
            c -= 1
        m = max(m,c)
    print(m)