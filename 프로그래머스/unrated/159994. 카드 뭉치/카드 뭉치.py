def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if i in cards1:
            if cards1.index(i)!=0:
                return "No"
            cards1.remove(i)
        elif i in cards2:
            if cards2.index(i)!=0:
                return "No"
            cards2.remove(i)
        else:
            return "No"
    return answer