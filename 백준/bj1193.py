X = int(input())
a=1
while True:
    X-=a
    if X<=0: break
    else: a+=1
if a%2==0:
    print(X+a, end='')
    print('/', end='')
    print(1-X)
else:
    print(1-X, end='')
    print('/', end='')
    print(X+a)
