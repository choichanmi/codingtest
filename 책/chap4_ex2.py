N = int(input())

count=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if ('3' in str(i))|('3' in str(j))|('3' in str(k)):
                count+=1
print(count)
