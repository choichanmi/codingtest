while True:
    try:
        num=int(input())
    except EOFError:
        break
    if num==1:
        print('1')
        continue
    i=1
    count=1
    while True:
        i=i*10+1
        count+=1
        if (i%num)==0:
            print(count)
            break
