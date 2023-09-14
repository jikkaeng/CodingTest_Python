def solution(strArr):
    answer = 0
    li=[]
    cnt=0
    for i in strArr:
        li.append(len(i))
        if cnt<len(i):
            cnt=len(i)
    for i in range(cnt+1):
        if li.count(i)>answer:
            answer=li.count(i)
    return answer