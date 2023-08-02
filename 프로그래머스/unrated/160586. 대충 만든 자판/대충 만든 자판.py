def solution(keymap, targets):
    answer = []
    tmp=101
    tmp2=0
    num=0
    for i in targets:
        for j in i:
            for k in keymap:
                if j in k:
                    if k.index(j)<tmp:
                        tmp=k.index(j)
            if tmp==101:
                num=-1
                break
            num+=(tmp+1)
            tmp=101
        answer.append(num)
        num=0
        tmp=101
    return answer