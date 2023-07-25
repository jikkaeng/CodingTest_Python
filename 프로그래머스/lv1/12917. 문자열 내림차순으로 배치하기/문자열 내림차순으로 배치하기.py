def solution(s):
    s=list(s)
    answer=''
    s.sort(reverse=True)
    for i in s:
        answer+=i
    return answer