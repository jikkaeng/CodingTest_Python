def solution(N, stages):
    answer = []
    li=[]
    cnt=0
    score=[0]*N
    for i in range(N):
        li.append(stages.count(i+1))
    if N+1 in stages:
        cnt+=stages.count(N+1)
    for i in range(N-1,-1,-1):
        cnt+=li[i]
        if cnt!=0:
            score[i]=li[i]/cnt
    for i in range(N):
        answer.append(score.index(max(score))+1)
        score[score.index(max(score))]=-1
    return answer