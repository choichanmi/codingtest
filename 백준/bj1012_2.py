T = int(input())
steps=[(-1,0),(1,0),(0,-1),(0,1)]
def bfs(x,y):
    queue=[[x,y]]
    while queue:
        a,b=queue[0][0], queue[0][1]
        del queue[0]
        for step in steps:
            current=[a+step[0],b+step[1]]
            if 0<=current[0]<N and 0<=current[1]<M and mapinfo[current[0]][current[1]]==1:
                mapinfo[current[0]][current[1]]=0
                queue.append([current[0],current[1]])

for i in range(T):
    M, N, K = map(int, input().split( ))
    mapinfo=[[0]*M for _ in range(N)]
    count=0
    for j in range(K):
        a,b = map(int, input().split( ))
        mapinfo[b][a]=1
    for k in range(N):
        for l in range(M):
            if mapinfo[k][l]==1:
                bfs(k,l)
                mapinfo[k][l]=0
                count+=1
    print(count)
