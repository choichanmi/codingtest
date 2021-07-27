m, n = map(int, input().split( ))

def Prime(N):
    if N==1:
        return False
    else:
        for i in range(2,int(N**(1/2))+1):
            if N%i==0:
                return False
        return True

for i in range(m, n+1):
    if Prime(i):
        print(i)
