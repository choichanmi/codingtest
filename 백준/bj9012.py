T = int(input())
lists=[]
for i in range(T):
    lists.append(list(input()))


for i in range(T):
    stack=[]
    result='YES'
    for j in range(len(lists[i])):
        if lists[i][j] in '(':
            stack.append(lists[i][j])
        else:
            if len(stack)==0:
                result='NO'
                break
            else:
                if stack[-1] in '(':
                    del stack[-1]
    if len(stack)!=0:
        result='NO'
    
    print(result)
