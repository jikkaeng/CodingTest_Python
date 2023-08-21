def solution(my_string, m, c):
    answer = ''
    mok=len(my_string)//m
    for i in range(mok):
        answer+=my_string[i*m+c-1]
    return answer