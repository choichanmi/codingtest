N = int(input())
nums=list(map(int, input().split( )))
nums.sort()
if N==1:
    print(nums[0]**2)
else:
    print(nums[0]*nums[-1])
