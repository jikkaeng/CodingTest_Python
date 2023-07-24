import math
def solution(n):
    answer = -1
    if math.sqrt(n)>0 and math.sqrt(n)==int(math.sqrt(n)):
        answer=(math.sqrt(n)+1)**2
    return answer