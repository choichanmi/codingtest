A, B, V = map(int, input().split( ))
temp1=(V-A)//(A-B)
temp2=(V-A)/(A-B)
if temp1==temp2: print(temp1+1)
else: print(temp1+2)
