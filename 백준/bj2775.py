T = int(input())
num=[[i+1 for i in range(14)]]
for i in range(14):
    a=[]
    for j in range(14):
        a.append(sum(num[i][:(j+1)]))
    num.append(a)
for i in range(T):
    k=int(input())
    n=int(input())
    print(num[k][n-1])
