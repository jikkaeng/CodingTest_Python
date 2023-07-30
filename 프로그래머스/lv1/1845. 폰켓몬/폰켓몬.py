def solution(nums):
    answer = 0
    li=[]
    for i in nums:
        if i not in li:
            li.append(i)
    if len(li)>len(nums)/2:
        answer=len(nums)/2
    else:
        answer=len(li)
    return answer