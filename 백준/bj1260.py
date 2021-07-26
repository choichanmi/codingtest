from collections import deque
N, M, V = map(int, input().split( ))
graph=[[] for i in range(N+1)]
graphinfo=[]
for i in range(M):
    graphinfo.append(list(map(int, input().split( ))))

for i in graphinfo:
    a=i[0]
    b=i[1]
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    graph[start].sort()
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

visited=[False] * (N+1)
dfs(graph,V,visited)
print('')

visited=[False] * (N+1)
bfs(graph, V, visited)
