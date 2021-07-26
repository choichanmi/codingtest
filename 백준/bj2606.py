from collections import deque
C = int(input())
N = int(input())
graph=[[] for i in range(C+1)]
graphinfo=[]
for i in range(N):
    graphinfo.append(list(map(int, input().split( ))))
for i in graphinfo:
    a=i[0]
    b=i[1]
    graph[a].append(b)
    graph[b].append(a)

count=0
visited=[False]*(C+1)
queue=deque([1])
visited[1]=True
while queue:
    v=queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i]=True
            count+=1
print(count)
