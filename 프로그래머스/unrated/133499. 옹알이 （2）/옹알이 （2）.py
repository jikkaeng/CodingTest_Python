def solution(babbling):
    answer = 0
    cnt=0
    tmp=''
    li=["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in li:
            if j in i and j*2 not in i:
                cnt+=len(j)*(i.count(j))
        if len(i)==cnt:
            answer+=1
        cnt=0
    return answer