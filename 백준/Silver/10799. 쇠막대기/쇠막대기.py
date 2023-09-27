import sys
input=sys.stdin.readline
n=input().rstrip()
li=[]
cnt=0
for i in range(len(n)):
    if n[i]=='(':
        li.append(i)
    elif n[i]==')':
        if n[i-1]=='(':
            li.pop()
            cnt+=len(li)
        else:
            li.pop()
            cnt+=1
print(cnt)
            
                

        
        
