T = int(input())

steps=[(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y):
    #범위 벗어나면 종료
    if mapinfo[x][y]==1:
        mapinfo[x][y]=0
    for step in steps:
        current=[x+step[0], y+step[1]]
        if 0<=current[0]<N and 0<=current[1]<M:
            print(current)
            if mapinfo[current[1]][current[0]]==1:
                dfs(current[0],current[1])

for t in range(T):
    M, N, K = map(int, input().split( ))
    mapinfo=[]
    for _ in range(N):
        mapinfo.append([0 for _ in range(M)])
    for j in range(K):
        x, y = map(int, input().split( ))
        mapinfo[y][x]=1
    #모든 노드(위치)에 대하여 확인하기
    count=0
    for i in range(N):
        for j in range(M):
            if mapinfo[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)
