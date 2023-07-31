def solution(n):
    answer = 0
    '''
    check=0
    for i in range(2,n+1):
        for j in range(2,int(i**(0.5))+1):
            if i%j==0:
                check=1
                break
        if check!=1:
            answer+=1
        check=0
    '''
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    answer=sieve.count(True)-2
    return answer