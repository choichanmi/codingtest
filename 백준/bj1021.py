from collections import deque
N, M = map(int, input().split( ))
target=list(map(int, input().split( )))
seq=deque([i+1 for i in range(N)])
count=0
for i in range(M):
    if seq[0]==target[i]:
        seq.popleft()
        continue
    indx=0
    for j in range(len(seq)):
        if seq[j]==target[i]:
            indx=j
            break
    if indx>len(seq)-indx:
        seq.rotate(len(seq)-indx)
        count+=len(seq)-indx
        seq.popleft()
    elif indx<len(seq)-indx:
        seq.rotate(-indx)
        count+=indx
        seq.popleft()
    elif indx==len(seq)-indx:
        seq.rotate(-indx)
        count+=indx
        seq.popleft()
print(count)
