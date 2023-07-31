def solution(answers):
    answer = []
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    score1=0
    score2=0
    score3=0
    cnt1=0
    cnt2=0
    cnt3=0
    for i in answers:
        if i==first[cnt1]:
            score1+=1
        if i==second[cnt2]:
            score2+=1
        if i==third[cnt3]:
            score3+=1
        cnt1+=1
        cnt2+=1
        cnt3+=1
        if len(first)==cnt1:
            cnt1=0
        if len(second)==cnt2:
            cnt2=0
        if len(third)==cnt3:
            cnt3=0
    if score1==max(score1,score2,score3):
        answer.append(1)
    if score2==max(score1,score2,score3):
        answer.append(2)
    if score3==max(score1,score2,score3):
        answer.append(3)
    return answer