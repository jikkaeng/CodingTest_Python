li=[]
for i in range(7):
    a=int(input())
    if a%2!=0:
        li.append(a)
if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)