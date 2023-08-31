import sys
input = sys.stdin.readline
s = list(input().rstrip())
right=[]
m=int(input())
for i in range(m):
    call=input().rstrip().split(' ')
    if call[0]=='P':
        s.append(call[1])
    elif call[0]=='L' and s:
        right.append(s.pop())
    elif call[0]=='D' and right:
        s.append(right.pop())
    elif call[0]=='B' and s:
        s.pop()
answer=s+right[::-1]
print("".join(answer))
