p = input()
place=[p[0],int(p[1])]
count=0
alplist=['a','b','c','d','e','f','g','h']
for i in range(8):
    if place[0] in alplist[i]:
        place[0]=i+1
        break

if place[0]+2<=8:
    if place[1]+1<=8:
        count+=1
    if place[1]-1>=1:
        count+=1
if place[0]-2>=1:
    if place[1]+1<=8:
        count+=1
    if place[1]-1>=1:
        count+=1
if place[1]+2<=8:
    if place[0]+1<=8:
        count+=1
    if place[0]-1>=1:
        count+=1
if place[1]-2>=1:
    if place[0]+1<=8:
        count+=1
    if place[0]-1>=1:
        count+=1
print(count)
