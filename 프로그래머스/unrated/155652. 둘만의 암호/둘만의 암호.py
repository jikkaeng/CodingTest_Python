def solution(s, skip, index):
    answer = ''
    li=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in skip:
        li.remove(i)
    for i in s:
        if li.index(i)+index>=len(li):
            answer+=li[(li.index(i)+index)%len(li)]
        else:
            answer+=li[li.index(i)+index]
    return answer