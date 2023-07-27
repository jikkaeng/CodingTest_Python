def solution(s):
    answer = ''
    arr=s.split(" ")
    for i in arr:
        cnt=1
        for j in i:
            if cnt==1:
                answer+=j.upper()
            else:
                answer+=j.lower()
            cnt*=-1
        answer+=" "
    answer=answer[:-1]
    return answer