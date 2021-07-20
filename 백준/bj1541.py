eq=input().split('-')
ans=0
for i in eq[0].split('+'):
    ans+=int(i)

for i in range(1, len(eq)):
    for j in eq[i].split('+'):
        ans-=int(j)
print(ans)
