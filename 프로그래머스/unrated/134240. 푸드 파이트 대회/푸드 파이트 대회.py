def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i]%2!=0:
            answer+=(str(i)*((food[i]-1)//2))
        else:
            answer+=(str(i)*(food[i]//2))
    li=sorted(list(answer))
    answer=""
    for i in li:
        answer+=i
    answer+="0"
    li.sort(reverse=True)
    for i in li:
        answer+=i
    return answer