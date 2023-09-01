import sys
input=sys.stdin.readline
n=int(input())
answer=[]
for i in range(n):
    k=int(input())
    if k==0 and answer:
        answer.pop()
    else:
        answer.append(k)
print(sum(answer))
