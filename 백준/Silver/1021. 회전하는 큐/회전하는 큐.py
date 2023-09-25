import sys
from collections import deque
input=sys.stdin.readline
n=list(map(int,input().split()))
q=deque([i for i in range(1,n[0]+1)])
k=list(map(int,input().split()))
idx=0
cnt=0
for i in k:
    idx=q.index(i)+1
    if len(q)//2>=idx-1:
        while q[0]!=i:
            q.append(q.popleft())
            cnt+=1
        q.popleft()
    else:
        while q[0]!=i:
            q.appendleft(q.pop())
            cnt+=1
        q.popleft()
print(cnt)