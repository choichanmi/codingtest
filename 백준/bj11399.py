N = int(input())
time_list=list(map(int, input().split( )))

time_list.sort()
sum=0
for i in range(N):
    sum+=time_list[i]*(N-i)
print(sum)
