def solution(num_list):
    answer = 0
    x=1
    su=0
    for i in num_list:
        x*=i
        su+=i
    if x<(su**2):
        answer=1
    return answer