N= input()
l=len(N)
num=[i*9*(10**(i-1)) for i in range(1, 10)]
num.insert(0,0)
ans=sum(num[:l])+l*(int(N)-(10**(l-1))+1)
print(ans)
