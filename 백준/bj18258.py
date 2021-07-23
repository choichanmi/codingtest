import sys
from collections import deque

queue1=deque([])
N = int(sys.stdin.readline())
for i in range(N):
    c=sys.stdin.readline().split()
    if c[0] == 'push':
        queue1.append(c[1])
    elif c[0] == 'pop':
        if not queue1:
            print(-1)
        else:
            print(queue1.popleft())
    elif c[0] == 'size':
        print(len(queue1))
    elif c[0] == 'empty':
        if not queue1:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if not queue1:
            print(-1)
        else:
            print(queue1[0])
    elif c[0] == 'back':
        if not queue1:
            print(-1)
        else:
            print(queue1[-1])
