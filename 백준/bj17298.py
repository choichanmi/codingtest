N = int(input())
seq=list(map(int, input().split( )))

ans=[-1 for i in range(N)]
stack=[]

for i in range(N):
    while len(stack)!=0 and stack[-1][0]<seq[i]:
        a,inx = stack[-1]
        del stack[-1]
        ans[inx]=seq[i]
    stack.append([seq[i],i])

print(*ans)
