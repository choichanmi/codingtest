import sys
T = int(input())
for i in range(T):
    c=input()
    n=int(input())
    temp=sys.stdin.readline()
    seq=temp[1:-2].split(',')
    flag=True
    left=True
    if n==0: seq=[]
    if len(seq)<c.count('D'): flag=False
    for cc in c:
        if cc=='R':
            left=not left
        elif cc=='D':
            if left:
                p=0
            else:
                p=-1
            if not seq:
                flag=False
                break
            else:
                seq.pop(p)
    if flag==False:
        print('error')
    else:
        if left: print('['+','.join(seq)+']')
        else: print('['+','.join(reversed(seq))+']')
