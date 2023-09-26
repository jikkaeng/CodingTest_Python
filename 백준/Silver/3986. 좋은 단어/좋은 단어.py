import sys
input=sys.stdin.readline
n=int(input().rstrip())
cnt=0
for i in range(n):
    s=list(input().rstrip())
    li=[]
    for j in s:
        if li:
            if j==li[-1]:
                li.pop()
            else:
                li.append(j)
        else:
            li.append(j)
    if not li:
        cnt+=1
print(cnt)
        
        
