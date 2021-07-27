N = list(input())
M = int(input())
if M!=0:
    broken=list(map(int, inut().split( )))
target=100

def check(N,broken):
    for i in range(len(broken)):
        if broken[i] in N:
            return True #부서진 버튼 있음
    return False #부서진 버튼 없음
count=0
if N==target:
    print(count)
else:
    while check(N, broken):
        
