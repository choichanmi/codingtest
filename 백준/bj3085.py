N = int(input())
candy=[]
candy=[list(map(str, input())) for _ in range(N)]

def check(candy):
    count=0
    for i in range(N):
        count_row=1
        count_col=1
        for j in range(N-1):
            if candy[i][j]==candy[i][j+1]:
                count_row+=1
            else:
                count = max(count, count_row)
                count_row=1
            if candy[j][i]==candy[j+1][i]:
                count_col+=1
            else:
                count=max(count, count_col)
                count_col=1
        count=max(count, count_row, count_col)
    return count

ans=0
for i in range(N):
    for j in range(N-1):
        if candy[i][j]!=candy[i][j+1]:
            temp=candy[i][j]
            candy[i][j]=candy[i][j+1]
            candy[i][j+1]=temp

            ans=max(ans, check(candy))

            temp=candy[i][j]
            candy[i][j]=candy[i][j+1]
            candy[i][j+1]=temp

        if candy[j][i]!=candy[j+1][i]:
            temp=candy[j][i]
            candy[j][i]=candy[j+1][i]
            candy[j+1][i]=temp

            ans=max(ans, check(candy))

            temp=candy[j][i]
            candy[j][i]=candy[j+1][i]
            candy[j+1][i]=temp

print(ans)
