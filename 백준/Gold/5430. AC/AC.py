import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
q=deque()
cnt=0
for i in range(t):
    go=0
    p=input().rstrip()
    n=int(input())
    q=deque(input().rstrip()[1:-1].split(','))
    for j in p:
        if j=='R' and q:
            cnt+=1
        elif j=='D':
            if q:
                if q[0]=='':
                    print('error')
                    go=1
                    break
                if cnt%2==1:
                    q.pop()
                else:
                    q.popleft()
            else:
                print('error')
                go=1
                break
    if go==0:
        if cnt%2==1:
            q.reverse()
        print('['+','.join(q)+']')
    q.clear()
    cnt=0
