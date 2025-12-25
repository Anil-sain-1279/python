t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if(a==b):
        print("YES")
    elif(b/2>=a):
        print("YES")
    else:
        print("NO")