def zermat(l):
    r=[]
    c=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 0:
                r.append(i)
                c.append(j)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i in r or j in c:
                    l[i][j]=0 
    print(l)
zermat([[1,1,1],[1,0,1],[1,1,1]])
