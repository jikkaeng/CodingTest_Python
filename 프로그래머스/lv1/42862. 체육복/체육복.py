def solution(n, lost, reserve):
    n-=len(lost)
    lost.sort()
    li=[]
    for i in reserve:
        if i in lost:
            lost.remove(i)
            n+=1
        else:
            li.append(i)
    for i in lost:
        if i-1 in li:
            n+=1
            li.remove(i-1)
        elif i+1 in li:
            n+=1
            li.remove(i+1)
    return n