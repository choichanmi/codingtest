#희망채널
N = int(input())
#고장난 버튼수
M = int(input())
#0-9까지 버튼을 가지고 있는 리모컨
remote = {str(i) for i in range(10)}

if M>0:
    #고장난 버튼을 리모컨에서 제거
    remote -=set(map(str, input().split( )))

#현재 보고 있는 채널
current_channel = 100
#현재 보고 있는 채널에서 보고자 하는 채널까지 +- 버튼을 통해 이동했을때 버튼을 눌러야하는 횟수
min_count=abs(current_channel-N)
#100만 채널까지 순회
for channel in range(1000000):
    #현재 순회중인 채널의 각 자릿수 순회
    for j in range(len(str(channel))):
        #현재 자릿수가 누를 수 없는 버튼이라면 해당 채널은 패스
        if str(channel)[j] not in remote:
            break
        #마지막 자릿수까지 모두 사용가능한 버튼이라면
        elif len(str(channel))-1 ==j:
            #채널 번호 누른 횟수(len(str(channel)))와
            #채널번호에서 희망채널까지 +-눌러야하는 횟수를 더해서
            #이전에 구한 최저횟수보다 적다면 최저횟수로 지정한다.
            min_count = min(min_count, abs(channel-N)+len(str(channel)))
print(min_count)
