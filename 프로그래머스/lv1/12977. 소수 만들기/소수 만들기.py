def solution(nums):
    answer = 0
    check=0
    for i in range(0,len(nums)-2):
        for k in range(i+1,len(nums)-1):
            for z in range(k+1,len(nums)):
                num=nums[i]+nums[k]+nums[z]
                for j in range(2,num):
                    if num%j==0:
                        check=1
                        break
                if check==0:
                    answer+=1
                check=0
    return answer