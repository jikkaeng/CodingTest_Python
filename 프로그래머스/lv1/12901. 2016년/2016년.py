def solution(a, b):
    answer = ''
    cnt=0
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    cnt=sum(month[:a-1])
    cnt%=7
    cnt+=b
    cnt%=7
    answer=day[cnt]
    return answer