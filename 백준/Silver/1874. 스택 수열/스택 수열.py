import sys
input=sys.stdin.readline
n=int(input())
answer=[]
answer2=[]
s=int(input())
tmp=s
check=0
for i in range(s):
    answer.append(i+1)
    answer2.append("+")
answer.pop()
answer2.append("-")
for i in range(n-1):
    s=int(input())
    if tmp<s:
        for j in range(tmp+1,s+1):
            answer.append(j)
            answer2.append("+")
        answer.pop()
        answer2.append("-")
        tmp=s
    else:
        if answer.pop()==s:
            answer2.append("-")
        else:
            print("NO")
            check=1
            break
if check==0:
    for i in answer2:
        print(i)
            
        
