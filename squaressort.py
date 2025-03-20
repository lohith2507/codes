def squaresort(l):
    lo = 0
    r = len(l)-1
    res = []
    while lo<=r:
        if abs(l[lo])>abs(l[r]):
            res.append(l[lo]**2)
            lo+=1
        else:
            res.append(l[r]**2)
            r-=1
    res.reverse()
    return res
print(squaresort([-4,-1,0,3,10]))