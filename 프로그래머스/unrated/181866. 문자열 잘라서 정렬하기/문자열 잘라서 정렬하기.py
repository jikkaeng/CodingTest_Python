def solution(myString):
    answer2 = myString.split('x')
    answer=[]
    answer2.sort()
    for i in answer2:
        if i !="":
            answer.append(i)
    return answer