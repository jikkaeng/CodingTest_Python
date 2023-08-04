def solution(my_string, overwrite_string, s):
    answer = ''
    if s+len(overwrite_string)>len(my_string):
        answer=my_string[:s]+overwrite_string
    else:
        answer=my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
    return answer