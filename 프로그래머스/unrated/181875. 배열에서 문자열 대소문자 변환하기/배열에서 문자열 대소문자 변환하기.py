def solution(strArr):
    answer = []
    s=''
    for j in range(len(strArr)):
        if j%2==0:
            answer.append(strArr[j].lower())
        else:
            answer.append(strArr[j].upper())
    return answer