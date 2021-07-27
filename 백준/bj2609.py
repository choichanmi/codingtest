a, b = map(int, input().split( ))

def divisor(N):
    ans=[]
    for i in range(1,N+1):
        if N%i==0:
            ans.append(i)
    return ans

alist=divisor(a)
blist=divisor(b)
nums=[]
for i in range(len(alist)):
    for j in range(len(blist)):
        if alist[i]==blist[j]:
            nums.append(alist[i])
ans1=max(nums)
print(ans1)
print(ans1*(a//ans1)*(b//ans1))
