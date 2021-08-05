N, M = map(int, input().split())
num=[]
for i in range(N):
    num.append(list(map(int, input().split())))

ans=0
for i in range(N-1):
    for j in range(M-1):
        summ=num[i][j]+num[i][j+1]+num[i+1][j]+num[i+1][j+1]
        if summ>ans: ans=summ
for i in range(N):
    for j in range(M-3):
        summ=sum(num[i][j:j+4])
        if summ>ans: ans=summ
for j in range(M):
    for i in range(N-3):
        summ=num[i][j]+num[i+1][j]+num[i+2][j]+num[i+3][j]
        if summ>ans: ans=summ
for i in range(N-2):
    for j in range(M-1):
        summ=num[i][j]+num[i+1][j]+num[i+2][j]+num[i+2][j+1]
        if summ>ans: ans=summ
        summ=num[i][j+1]+num[i+1][j+1]+num[i+2][j+1]+num[i+2][j]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i+1][j]+num[i+1][j+1]+num[i+2][j+1]
        if summ>ans: ans=summ
        summ=num[i][j+1]+num[i+1][j+1]+num[i+1][j]+num[i+2][j]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i+1][j]+num[i+2][j]+num[i+1][j+1]
        if summ>ans: ans=summ
        summ=num[i][j+1]+num[i+1][j+1]+num[i+2][j+1]+num[i+1][j]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i][j+1]+num[i+1][j+1]+num[i+2][j+1]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i][j+1]+num[i+1][j]+num[i+2][j]
        if summ>ans: ans=summ
for i in range(N-1):
    for j in range(M-2):
        summ=num[i][j]+num[i+1][j]+num[i][j+1]+num[i][j+2]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i+1][j]+num[i+1][j+1]+num[i+1][j+2]
        if summ>ans: ans=summ
        summ=num[i+1][j]+num[i+1][j+1]+num[i][j+1]+num[i][j+2]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i][j+1]+num[i+1][j+1]+num[i+1][j+2]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i][j+1]+num[i][j+2]+num[i+1][j+1]
        if summ>ans: ans=summ
        summ=num[i+1][j]+num[i+1][j+1]+num[i+1][j+2]+num[i][j+1]
        if summ>ans: ans=summ
        summ=num[i][j]+num[i][j+1]+num[i][j+2]+num[i+1][j+2]
        if summ>ans: ans=summ
        summ=num[i][j+2]+num[i+1][j]+num[i+1][j+1]+num[i+1][j+2]
        if summ>ans: ans=summ
        
print(ans)
