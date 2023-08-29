import math
a=input()
max_cnt=0
for i in range(0,10):
    if i==6 or i==9:
        if a.count("6")!=0 and a.count("9")!=0:
            cnt=min(a.count("6"),a.count("9"))+math.ceil((max(a.count("6"),a.count("9"))-min(a.count("6"),a.count("9")))/2)
        else:
            cnt=math.ceil((a.count("6")+a.count("9"))/2)
        if max_cnt<cnt:
            max_cnt=cnt
    else:
        if max_cnt<a.count(str(i)):
            max_cnt=a.count(str(i))
print(max_cnt)

