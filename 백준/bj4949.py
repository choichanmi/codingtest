contents=[]
while True:
    a=input()
    if len(a)==1 and a in '.':
        break
    contents.append(a)
content=[]
for i in range(len(contents)):
    b=[]
    for j in range(len(contents[i])):
        if contents[i][j] in ['(',')','[',']']:
            b.append(contents[i][j])
    content.append(b)

for i in range(len(content)):
    stack=[]
    result='yes'
    for j in range(len(content[i])):
        if content[i][j] in ['(','[']:
            stack.append(content[i][j])
        elif content[i][j] in [')',']']:
            if len(stack)==0:
                result='no'
                break
            elif content[i][j] in ')':
                if stack[-1] in '(':
                    del stack[-1]
                else:
                    result='no'
                    break
            elif content[i][j] in ']':
                if stack[-1] in '[':
                    del stack[-1]
                else:
                    result='no'
                    break
    if len(stack)!=0:
        result='no'
    
    print(result)
