def solution(phone_number):
    s=phone_number[len(phone_number)-4:len(phone_number)]
    answer = ('*'*(len(phone_number)-4))+s
    return answer