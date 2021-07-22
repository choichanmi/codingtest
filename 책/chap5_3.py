N, M = map(int, input().split( ))
ice=[]
for i in range(N):
    ice.append(list(map(int, input().split( ))))
#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #범위 벗어나면 종료
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if ice[x][y]==0:
        ice[x][y]=1
        #상하좌우도 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result =0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if dfs(i,j)==True:
            result+=1

print(result)
