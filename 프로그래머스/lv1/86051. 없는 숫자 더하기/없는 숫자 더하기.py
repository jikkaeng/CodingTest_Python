def solution(numbers):
    answer = 0
    li=[1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        li.remove(i)
    answer=sum(li)
    return answer