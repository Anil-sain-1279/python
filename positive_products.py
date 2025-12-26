t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    apos = 0
    aneg = 0
    for i in range(n):
        if(a[i]<0):
            aneg += 1
        elif(a[i]>0):
            apos += 1
    
    p = (apos*(apos-1))//2
    n = (aneg*(aneg-1))//2
    
    print(n+p)