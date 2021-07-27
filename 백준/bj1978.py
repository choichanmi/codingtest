N=int(input())
numlist=list(map(int, input().split( )))

def Divisor(N):
    ans=[]
    for i in range(1,N+1):
        if N%i==0:
            ans.append(i)
    return ans

count=0
for i in range(N):
    a=divisor(numlist[i])
    if len(a)==2:
        count+=1
print(count)
