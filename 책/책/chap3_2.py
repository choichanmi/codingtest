N, M, K = map(int, input().split( ))
nlist=list(map(int, input().split( )))

nlist.sort()
n1=nlist[-1]
n2=nlist[-2]
if n1==n2:
    sum=n1*M
else:
    a=M//(K+1)
    sum=n1*(M-a)+n2*a

print(sum)
