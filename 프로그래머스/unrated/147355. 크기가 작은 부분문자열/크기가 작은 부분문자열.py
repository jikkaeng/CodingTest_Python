def solution(t, p):
    answer = 0
    tmp=""
    for i in range(0,len(t)-len(p)+1):
        for j in range(len(p)):
            tmp+=t[i+j]
        if int(tmp)<=int(p):
            answer+=1
        tmp=""
    return answer