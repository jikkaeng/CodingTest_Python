def solution(n, arr1, arr2):
    answer = []
    a=0
    b=0
    s=[' ']*n
    map1=[[0]*n for i in range(n)]
    for i,j in zip(arr1,arr2):
        a=bin(i)[2:]
        b=bin(j)[2:]
        a = "{0:0>{n}}".format(a, n=n)
        b="{0:0>{n}}".format(b, n=n)
        for z in range(n):
            if a[z]=='1':
                s[z]='#'
            if b[z]=='1':
                s[z]='#'
        res=''.join(k for k in s)
        answer.append(res)
        s=[' ']*n
    return answer