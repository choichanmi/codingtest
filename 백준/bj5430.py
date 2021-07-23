from collections import deque
import sys
T = int(input())
for i in range(T):
    c=list(input())
    n=int(input())
    temp=sys.stdin.readline()
    seq=temp[1:-2].split(',')
    seq=deque([int(seq[i]) for i in range(n)])
    flag=True
    for j in range(len(c)):
        if c[j]=='R':
            seq.reverse()
        elif c[j]=='D':
            if not seq:
                flag=False
                break
            else:
                seq.popleft()
    if flag==False:
        print('error')
    else:
        print(list(seq))
