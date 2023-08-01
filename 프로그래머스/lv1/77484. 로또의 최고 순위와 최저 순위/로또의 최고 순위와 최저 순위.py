def solution(lottos, win_nums):
    answer = []
    cnt=lottos.count(0)
    num=0
    for i in lottos:
        if i==0:
            continue
        if i in win_nums:
            num+=1
    score={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer.append(score[cnt+num])
    answer.append(score[num])
    return answer