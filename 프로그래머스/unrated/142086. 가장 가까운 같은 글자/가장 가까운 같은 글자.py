def solution(s):
    answer = []
    cnt=0
    for i in range(len(s)):
        for j in range(i-1,-1,-1):
            cnt+=1
            if s[i]==s[j]:
                answer.append(cnt)
                cnt=-1
                break
        if cnt!=-1:
            answer.append(-1)
        cnt=0
    return answer