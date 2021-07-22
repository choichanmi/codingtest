N, M = map(int, input().split( ))
state=[]
for i in range(N):
    state.append(input())
case=[]
for i in range(N-7):
    for j in range(M-7):
        a=[]
        for k in range(i,i+8):
            a.append(state[k][j:j+8])
        case.append(a)

def check(case):
    count1=0
    count2=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if case[i][j] in 'B':
                    count1+=1
                else:
                    count2+=1
            else:
                if case[i][j] in 'W':
                    count1+=1
                else:
                    count2+=1
    return min(count1,count2)

count=[]
for i in range(len(case)):
    count.append(check(case[i]))
print(min(count))
