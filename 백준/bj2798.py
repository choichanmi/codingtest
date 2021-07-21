from itertools import combinations

N, M = map(int, input().split( ))
numlist=list(map(int, input().split( )))
ans=0
for c in combinations(numlist,3):
    temp=sum(c)
    if temp<=M and temp>ans:
        ans=temp
print(ans)
