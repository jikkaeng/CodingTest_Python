n=int(input())
cnt=0
arr=[int(i) for i in input().split(" ")]
arr.sort()
x=int(input())
check=n
stop=n
for i in range(n):
    if arr[i]>x:
        check=i
        break
chk=check-1
for i in range(check-1):
    for j in range(chk,i,-1):
        if arr[i]+arr[j]==x:
            cnt+=1
            chk-=1
            break
print(cnt)

