p = input()
place=[p[0],int(p[1])]
count=0
alplist=['a','b','c','d','e','f','g','h']
for i in range(8):
    if place[0] in alplist[i]:
        place[0]=i+1
        break
    
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
for step in steps:
    place2=[place[0]+step[0],place[1]+step[1]]
    if place2[0]>=1 and place2[0]<=8 and place2[1]>=1 and place2[1]<=8:
        count+=1
print(count)
