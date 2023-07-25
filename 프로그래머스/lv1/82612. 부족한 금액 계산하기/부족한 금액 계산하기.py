def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        money-=price*i
    if money<0:
        answer=money*-1
    return answer