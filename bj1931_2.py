N=int(input())
time_list=[]
for i in range(N):
    time_list.append(list(map(int, input().split( ))))
time_list.sort()
time_list.sort(key=lambda x:x[1])

ans_list=[]
ans_list.append(time_list[0])
for i in range(1, N):
    if time_list[i][0]>=ans_list[-1][1]:
        ans_list.append(time_list[i])
        
print(len(ans_list))
