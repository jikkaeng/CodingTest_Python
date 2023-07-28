def solution(s):
    answer = 0
    li=['zero','one','two','three','four','five','six','seven','eight','nine']
    cnt=0
    for i in li:
        s=s.replace(i,str(cnt))
        cnt+=1
    answer=int(s)
    return answer