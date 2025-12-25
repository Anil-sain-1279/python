t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s_0 = s.count('0')
    s_1 = s.count('1')
    print("0"*s_0+"1"*s_1)