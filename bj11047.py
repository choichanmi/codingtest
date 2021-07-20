N, K = map(int, input().split( ))
price=[]
for i in range(N):
    price.append(int(input()))

price.reverse()
num_coin=0
for p in price:
    num_coin+=K//p
    K=K%p
print(num_coin)
