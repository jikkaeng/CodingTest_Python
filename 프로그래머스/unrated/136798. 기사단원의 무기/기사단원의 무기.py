def solution(number, limit, power):
    answer = 0
    li=[]
    cnt=0
    for i in range(1,number+1):
        for j in range(1, int(i ** (0.5)) + 1):
            if i % j == 0:
                cnt+=1
                if j != i // j:
                    cnt+=1
        li.append(cnt)
        cnt=0
    for i in range(len(li)):
        if li[i] >limit:
            li[i]=power
        answer+=li[i]
    return answer