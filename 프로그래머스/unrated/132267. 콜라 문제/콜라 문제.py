def solution(a, b, n):
    answer = 0
    nmg=0
    while n>=a:
        nmg=n%a
        n=n//a
        answer+=(n*b)
        n=n*b+nmg
    return answer