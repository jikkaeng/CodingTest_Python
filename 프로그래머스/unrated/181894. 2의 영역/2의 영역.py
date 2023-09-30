def solution(arr):
    answer = []
    li=[]
    end=0
    if arr.count(2)==0:
        answer.append(-1)
    else:
        arr.reverse()
        end=len(arr)-arr.index(2)
        arr.reverse()
        answer=arr[arr.index(2):end]
    return answer