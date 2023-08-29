s=input()
arr=[]
for i in range(97,123):
    arr.append(s.count(chr(i)))
for i in arr:
    print(i,end=" ")
