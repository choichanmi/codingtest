from collections import deque
N, K = map(int, input().split( ))
queue=deque([i+1 for i in range(N)])
ans=[]
while len(queue)>0:
    for i in range(K-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())
print('<',end='')
print(*ans,sep=', ',end='')
print('>')
