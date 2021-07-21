N, M = map(int, input().split( ))
aa=list(map(int, input().split( )))
place=[aa[0],aa[1]]
d=aa[2] #0:북, 1:동, 2:남. 3:서
mapinfo=[]
for i in range(N):
    mapinfo.append(list(map(int, input().split( ))))
mapinfo[place[0]][place[1]]=1 #현재 위치 방문 처리
steps = [(-1,0),(0,1),(1,0),(0,-1)]
count=1
turn_time=0
while True:
    d=(d+3)%4 #왼쪽으로 회전
    current_place=[place[0]+steps[d][0],place[1]+steps[d][1]]
    #이동가능한 경우
    if mapinfo[current_place[0]][current_place[1]]==0:
        mapinfo[current_place[0]][current_place[1]]=1
        place=current_place
        count+=1
        turn_time=0
        continue
    #이동불가능한 경우
    else:
        turn_time+=1
    #네 방향 모두 이동불가능한 경우
    if turn_time==4:
        current_place=[place[0]-steps[d][0],place[1]-steps[d][1]]
        if mapinfo[current_place[0]][current_place[1]]==0:
            place=current_place
        else:
            break
        turn_time=0

print(count)
