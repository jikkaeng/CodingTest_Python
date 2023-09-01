import sys
input=sys.stdin.readline
n=int(input())
answer=[]
for i in range(n):
    s=input().rstrip().split()
    if s[0]=='push':
        answer.append(int(s[1]))
    elif s[0]=='pop':
        if answer:
            print(answer.pop())
        else:
            print(-1)
    elif s[0]=='size':
        print(len(answer))
    elif s[0]=='empty':
        if answer:
            print(0)
        else:
            print(1)
    elif s[0]=='top':
        if answer:
            print(answer[len(answer)-1])
        else:
            print(-1)
        
