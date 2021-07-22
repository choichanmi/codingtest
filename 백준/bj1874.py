n = int(input())
numlist=[]
for i in range(n):
    numlist.append(int(input()))

num=[i for i in range(1,n+1)]
stack=[]
p=0
a=0
check=0
ans=[]
flag=True
for i in range(n):
    if numlist[i]>a:
        p=a
        a=numlist[i]
        for j in range(a-p):
            stack.append(num[0])
            del num[0]
            ans.append('+')
    else:
        check+=1
    if stack[-1]==numlist[i]:
        ans.append('-')
        del stack[-1]
    else:
        check+=1
    if check==2:
        print('NO')
        flag=False
        break
    else:
        check=0
if flag==True:
    for i in range(len(ans)):
        print(ans[i])
