t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    a = sorted(a)
    if(a[0]==a[1] and a[2]==a[3]):
        print("yes")
    else:
        print("no")