N = int(input())
ans=0

for i in range(N):
    num=str(i)
    a=[int(num[j]) for j in range(len(num))]
    s=i+sum(a)
    if s==N:
        ans=i
        break
print(ans)
