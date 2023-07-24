def solution(park, routes):
    answer = []
    x=0
    height=len(park)
    width=len(park[0])
    for i in park:
        if i.find('S')!=-1:
            y=i.find('S')
            break
        x+=1
    for i in routes:
        check=0
        if i[0]=='E':
            if y+int(i[2])<width:
                for j in range(int(i[2])):
                    if park[x][y+j+1]=='X':
                        check=1
                        break
                if check==0:
                    y+=int(i[2])
        elif i[0]=='W':
            if y-int(i[2])>=0:
                for j in range(int(i[2])):
                    if park[x][y-(j+1)]=='X':
                        check=1
                        break
                if check==0:
                    y-=int(i[2])
        elif i[0]=='N':
            if x-int(i[2])>=0:
                for j in range(int(i[2])):
                    if park[x-(j+1)][y]=='X':
                        check=1
                        break
                if check==0:
                    x-=int(i[2])
        elif i[0]=='S':
            if x+int(i[2])<height:
                for j in range(int(i[2])):
                    if park[x+j+1][y]=='X':
                        check=1
                        break
                if check==0:
                    x+=int(i[2])
        print(x,y)
    answer.append(x)
    answer.append(y)
    return answer