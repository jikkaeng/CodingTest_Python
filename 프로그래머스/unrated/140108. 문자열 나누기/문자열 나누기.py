def solution(s):
    answer = 0
    x=s[0]
    cnt_x=0
    cnt_y=0
    cnt=0
    for i in s:
        if i==x:
            cnt_x+=1
        else:
            cnt_y+=1
        if cnt_x==cnt_y:
            answer+=1
            if(cnt+1<len(s)):
                x=s[cnt+1]
        cnt+=1
    if cnt_x!=cnt_y:
        answer+=1
    return answer