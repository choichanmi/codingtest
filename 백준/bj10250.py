T= int(input())
for i in range(T):
    H, W, N = map(int, input().split( ))
    q=N//H+1
    r=N%H
    if r==0:
        r=H
        q-=1
    if q<10: q='0'+str(q)
    else: q=str(q)
    
    print(str(r)+q)
