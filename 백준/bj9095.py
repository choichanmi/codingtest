def case(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return case(n-1)+case(n-2)+case(n-3)

T=int(input())
for i in range(T):
    n=int(input())
    print(case(n))
