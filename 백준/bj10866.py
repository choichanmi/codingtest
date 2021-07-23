import sys
from collections import deque

deque1=deque([])
N = int(sys.stdin.readline())
for i in range(N):
    c=sys.stdin.readline().split()
    if c[0] == 'push_front':
        deque1.appendleft(c[1])
    elif c[0] == 'push_back':
        deque1.append(c[1])
    elif c[0] == 'pop_front':
        if not deque1:
            print(-1)
        else:
            print(deque1.popleft())
    elif c[0] == 'pop_back':
        if not deque1:
            print(-1)
        else:
            print(deque1.pop())
    elif c[0] == 'size':
        print(len(deque1))
    elif c[0] == 'empty':
        if not deque1:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if not deque1:
            print(-1)
        else:
            print(deque1[0])
    elif c[0] == 'back':
        if not deque1:
            print(-1)
        else:
            print(deque1[-1])
