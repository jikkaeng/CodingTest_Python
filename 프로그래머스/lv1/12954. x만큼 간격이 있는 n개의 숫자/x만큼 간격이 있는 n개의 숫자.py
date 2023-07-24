def solution(x, n):
    answer = []
    cnt=0
    for i in range(n):
        cnt+=x
        answer.append(cnt)
    return answer