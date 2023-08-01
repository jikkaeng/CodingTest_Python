def solution(dartResult):
    answer = 0
    li=[]
    cnt=0
    check=0
    for i in range(len(dartResult)):
        if not dartResult[i].isdigit():
            if dartResult[i]=='D':
                li[cnt]=li[cnt]**2
            elif dartResult[i]=='T':
                li[cnt]=li[cnt]**3
            elif dartResult[i]=='*':
                cnt-=1
                li[cnt]*=2
                if cnt!=0:
                    li[cnt-1]*=2
            elif dartResult[i]=='#':
                cnt-=1
                li[cnt]*=-1
            cnt+=1
            if check==1:
                check=0
        else:
            if check==1:
                li[cnt]=int(str(li[cnt])+dartResult[i])
                check=0
            else:
                li.append(int(dartResult[i]))
                check=1
    for i in li:
        answer+=i
    return answer