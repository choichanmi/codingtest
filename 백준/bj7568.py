N = int(input())
infolist=[]
for i in range(N):
    infolist.append(list(map(int, input().split( ))))

ans=[1]*N
for i in range(N-1):
    for j in range(i+1,N):
        if infolist[i][0]>infolist[j][0] and infolist[i][1]>infolist[j][1]:
            ans[j]+=1
        elif infolist[i][0]<infolist[j][0] and infolist[i][1]<infolist[j][1]:
            ans[i]+=1
print(*ans)
