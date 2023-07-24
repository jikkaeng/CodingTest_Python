def solution(n):
    answer = ""
    n=str(n)
    li=[]
    for i in n:
        li.append(i)
    li=sorted(li,reverse=True)
    for i in li:
        answer+=i
    answer=int(answer)
    return answer