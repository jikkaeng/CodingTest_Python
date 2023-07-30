def solution(k, score):
    answer = [score[0]]
    tmp=[score[0]]
    if k>len(score):
        for i in range(1,len(score)):
            tmp.append(score[i])
            answer.append(min(tmp))
    else:         
        for i in range(1,k):
            tmp.append(score[i])
            answer.append(min(tmp))
    for i in range(k,len(score)):
        if score[i]>min(tmp):
            tmp[tmp.index(min(tmp))]=score[i]
        answer.append(min(tmp))
    return answer