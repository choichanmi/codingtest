N = int(input())
move = list(input().split( ))

low=1
column=1
for i in range(len(move)):
    if move[i]=='R':
        if column+1<=N:
            column+=1
    elif move[i]=='L':
        if column-1>=1:
            column-=1
    elif move[i]=='U':
        if low-1>=1:
            low-=1
    elif move[i]=='D':
        if low+1<=N:
            low+=1
print(low, column)
