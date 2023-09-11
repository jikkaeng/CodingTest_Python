def solution(todo_list, finished):
    answer = []
    for i,j in zip(todo_list,finished):
        if j==False:
            answer.append(i)
    return answer