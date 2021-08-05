N = int(input())
a=1
n=2
while True:
    if N==1:
        print(1)
        break
    if n<=N<=(n+6*a-1):
        print(a+1)
        break
    else:
        n+=6*a
        a+=1
