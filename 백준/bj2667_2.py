N= int(input())
home=[]
for i in range(N):
    home.append(list(map(int, input())))
visited=[[0]*N for i in range(N)]

steps=[(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y,c): #c번째 단지
    visited[x][y]=1
    global nums
    #아파트가 있으면 숫자를 세어줍니다.
    if home[x][y]==1:
        home[i][j]=c 
        nums+=1
    #해당 위치에서 좌/우/위/아래 방향의 좌표를 확인하여 dfs 적용
    for step in steps:
        current=[x+step[0], y+step[1]]
        if 0<=current[0]<N and 0<=current[1]<N:
            if visited[current[0]][current[1]]==0 and home[current[0]][current[1]]==1:
                dfs(current[0],current[1],c)
count=1
homecount=[]
nums=0
for i in range(N):
    for j in range(N):
        if home[i][j]==1 and visited[i][j]==0:
            dfs(i,j,count)
            homecount.append(nums)
            nums=0
            count+=1

print(len(homecount))
for n in sorted(homecount):
    print(n)
