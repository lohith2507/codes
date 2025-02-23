def lcs(l):
    l.sort()
    maxi = 0
    c = 0
    for i in range(len(l)-1):
        if (l[i+1]-l[i]==1):
            c+=1
            print(c)
            if maxi < c:
                maxi = c
                c=0
    return maxi+1
print(lcs([100,4,200,1,3,2]))
