def solution(arr):
    answer = []
    tmp=-1
    for i in arr:
        if tmp!=i:
            answer.append(i)
            tmp=i
    return answer