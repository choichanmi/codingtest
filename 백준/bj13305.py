N = int(input())
dlist = list(map(int, input().split( )))
plist = list(map(int, input().split( )))

sum=plist[0]*dlist[0]
price=plist[0]
for i in range(1,N-1):
    if price>plist[i]:
        price=plist[i]
    sum+=price*dlist[i]

print(sum)
