import sys
input = sys.stdin.readline
n=int(input())
answer=[]
right=[]
left=[]
for i in range(n):
    s=list(input().rstrip())
    for j in s:
        if j=='<' and left:
            right.append(left.pop())
        elif j=='>' and right:
            left.append(right.pop())
        elif j=='-' and left:
            left.pop()
        elif j!='<' and j!='>' and j!='-':
            left.append(j)
    answer.append("".join(left+right[::-1]))
    left.clear()
    right.clear()
for i in answer:
    print(i)
