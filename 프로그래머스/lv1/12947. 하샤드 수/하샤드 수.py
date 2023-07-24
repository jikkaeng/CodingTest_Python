def solution(x):
    answer = True
    cnt=0
    for i in str(x):
        cnt+=int(i)
    if x%cnt!=0:
        answer=False
    return answer