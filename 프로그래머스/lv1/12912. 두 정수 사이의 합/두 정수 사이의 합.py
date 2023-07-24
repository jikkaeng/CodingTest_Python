def solution(a, b):
    answer = 0
    start=min(a,b)
    end=max(a,b)
    answer=sum(range(start,end+1))
    return answer