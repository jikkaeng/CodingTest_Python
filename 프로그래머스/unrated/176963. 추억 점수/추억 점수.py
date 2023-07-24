def solution(name, yearning, photo):
    answer = []
    a={}
    cnt=0
    for i in range(len(name)):
        a[name[i]]=yearning[i]
    for i in range(len(photo)):
        for j in photo[i]:
            cnt+=a.get(j,0)
        answer.append(cnt)
        cnt=0
    return answer