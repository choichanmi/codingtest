from collections import deque
T = int(input())
for i in range(T):
    ans=[]
    N, M = map(int, input().split( ))
    temp=list(map(int, input().split( )))
    info=deque([])
    for j in range(N):
        info.append((j,temp[j]))
    while len(info)>0:
        flag=False
        for k in range(1,len(info)):
            if info[0][1]<info[k][1]:
                info.append(info.popleft())
                flag=True
                break
        if flag:
            continue
        else:
            ans.append(info.popleft())
    for j in range(N):
        if ans[j][0]==M:
            print(j+1)
            break
