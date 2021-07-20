N=int(input())
time_list=[]
for i in range(N):
    time_list.append(list(map(int, input().split( ))))
time_list.sort()

ans=0
for j in range(N-1):
    ans_list=[]
    ans_list.append(time_list[j])
    for i in range(j+1,N):
        if time_list[i][0]>=ans_list[-1][1]:
            ans_list.append(time_list[i])
    ans=max(ans, len(ans_list))
print(ans)
