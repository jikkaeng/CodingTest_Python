def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if len(cards1)>0 and i == cards1[0]:
            cards1.remove(i)
        elif len(cards2)>0 and i == cards2[0]:
            cards2.remove(i)
        else:
            return "No"
    return answer