T = int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())
    flag=False
    while x<=M*N:
        if x%N==y%N:
            print(x)
            flag=True
            break
        x+=M
    if flag==False:
        print(-1)
