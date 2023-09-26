import sys
from collections import deque
input=sys.stdin.readline
while True:
    s=input().rstrip()
    check=True
    if s=='.':
        break
    li=[]
    for i in s:
        if i=='(' or i=='[':
            li.append(i)
        elif i==')':
            if li:
                if li.pop()!='(':
                    print('no')
                    check=False
                    break
            else:
                print('no')
                check=False
                break
        elif i==']':
            if li:
                if li.pop()!='[':
                    print('no')
                    check=False
                    break
            else:
                print('no')
                check=False
                break
    if check:
        if li:
            print('no')
        else:
            print('yes')
