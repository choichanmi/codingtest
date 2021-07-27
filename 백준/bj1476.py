from collections import deque
E, S, M = map(int, input().split( ))
i=1
e=deque([i for i in range(1,16)])
s=deque([i for i in range(1,29)])
m=deque([i for i in range(1,20)])
while True:
    if E==1 and S==1 and M==1:
        print(1)
        break
    i+=1
    e.append(e.popleft())
    s.append(s.popleft())
    m.append(m.popleft())
    if e[0]==E and s[0]==S and m[0]==M:
        print(i)
        break
