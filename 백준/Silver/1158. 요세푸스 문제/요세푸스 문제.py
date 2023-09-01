import sys
input = sys.stdin.readline
n,m=map(int,input().rstrip().split())
li=list(range(1,n+1))
answer=[]
k=0
while li:
    k+=(m-1)
    if k>=len(li):
        k=k%len(li)
    answer.append(li.pop(k))
print("<{}>".format(', '.join(map(str, answer))))
