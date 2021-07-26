N = int(input())
home=[]
for i in range(N):
    home.append(list(map(int, input())))

homecount =0
homenum=set([])
#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y,num):
    #범위 벗어나면 종료
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return (False,num)
    #현재 노드를 아직 방문하지 않았다면
    if home[x][y]==1:
        home[x][y]=0
        num+=1
        #상하좌우도 재귀적으로 호출
        if dfs(x-1,y,num)[0]==True: num+=1
        if dfs(x,y-1,num)[0]==True: num+=1
        if dfs(x+1,y,num)[0]==True: num+=1
        if dfs(x,y+1,num)[0]==True: num+=1
        homenum.add(num)
        return (True, num)
    return (False,num)

#모든 노드(위치)에 대하여 확인하기

for i in range(N):
    for j in range(N):
        #현재 위치에서 DFS 수행
        num=0
        a=dfs(i,j,num)
        if a[0]==True:
            homecount+=1

print(homecount)
homenum = list(homenum)
homenum.sort()
homenum.reverse()
a=homenum[:homecount]
for i in range(homecount):
    print(a.pop())
