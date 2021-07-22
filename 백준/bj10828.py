N = int(input())
command=[]
for i in range(N):
    command.append(list(input().split()))

def push(stack,X):
    stack.append(X)

def pop(stack):
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top(stack):
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])

stack1=[]
for c in command:
        if c[0] in 'push':
            push(stack1,c[1])
        elif c[0] in 'pop':
                pop(stack1)
        elif c[0] in 'size':
                size(stack1)
        elif c[0] in 'empty':
                empty(stack1)
        elif c[0] in 'top':
                top(stack1)
