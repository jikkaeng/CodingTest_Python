def solution(s):
    answer = True
    p=s.count('p')
    y=s.count('y')
    p+=s.count('P')
    y+=s.count('Y')
    if p!=y:
        answer=False
    return answer