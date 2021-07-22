from collections import deque
N, M = map(int, input().split( ))
miro=[]
for i in range(N):
    miro.append(list(map(int, input())))

steps=[(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for step in steps:
            current=[x+step[0],y+step[1]]
            #미로 공간 벗어난 경우 무시
            if current[0]<0 or current[1]<0 or current[0]>=N or current[1]>=M:
                continue
            #벽인 경우 무시
            if miro[current[0]][current[1]]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if miro[current[0]][current[1]]==1:
                miro[current[0]][current[1]]=miro[x][y]+1
                queue.append((current[0],current[1]))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return miro[N-1][M-1]
print(bfs(0,0))
