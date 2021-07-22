N = int(input())
seq=list(map(int, input().split( )))

ans=[-1 for i in range(N)]
stack=[]

for i in range(N):
    a=seq[-1]
    del seq[-1]
    if stack==[]:
        stack.append(a)
        continue
    while len(stack)!=0:
        b=stack[-1]
        del stack[-1]
        if a<b:
            ans[-i-1]=b
            stack.append(b)
            stack.append(a)
            break

print(*ans)
