N, M = map(int, input().split( ))
nums=[]
for i in range(N):
    nums.append(list(map(int, input().split( ))))

min_nums=[]
for i in range(N):
    min_nums.append(min(nums[i]))

print(max(min_nums))
