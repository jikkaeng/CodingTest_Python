def solution(num_list):
    answer = []
    num_list.sort()
    answer.extend(num_list[5:])
    return answer