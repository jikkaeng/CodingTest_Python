def solution(array, commands):
    answer = []
    li=[]
    for i in commands:
        li=sorted(array[i[0]-1:i[1]])
        answer.append(li[i[2]-1])
    return answer