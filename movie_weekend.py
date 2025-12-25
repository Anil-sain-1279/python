t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    b = 0
    m_lr = -1
    m_r = -1
    
    for i in range(n):
        lr = l[i]*r[i]
        if(lr>m_lr):
            m_lr = lr 
            m_r = r[i]
            b = i 
        elif(lr == m_lr):
            if(r[i]>m_r):
                m_r = r[i]
                b = i 
    print(b+1)