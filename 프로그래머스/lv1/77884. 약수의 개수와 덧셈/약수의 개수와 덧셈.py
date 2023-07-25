def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt=0
        n=1
        while n*n<=i:
            if n*n==i:
                cnt+=1
            elif i%n==0:
                cnt+=2
            n+=1
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
    return answer
