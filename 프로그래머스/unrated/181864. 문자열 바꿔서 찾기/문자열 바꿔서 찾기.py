def solution(myString, pat):
    answer = 0
    myString=myString.replace('A','b')
    myString=myString.replace('B','A')
    myString=myString.upper()
    if pat in myString:
        answer=1
    return answer