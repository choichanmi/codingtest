K = int(input())
num=[]
for i in range(K):
    n=int(input())
    if n==0:
        del num[-1]
    else:
        num.append(n)
print(sum(num))
