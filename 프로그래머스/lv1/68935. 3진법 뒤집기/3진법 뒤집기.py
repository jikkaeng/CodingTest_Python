def solution(n):
    answer = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    answer=int(rev_base,3)
    return answer
