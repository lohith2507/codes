def mergeIntervals(l):
    l.sort(key=lambda x:x[0])
    i=1
    if len(l)==1 :
        return l
    while i<len(l) :
        a=l[i-1]
        b=l[i]
        if a[1]>=b[0] :
            if a[1]>b[1] :
                l=l[:i-1]+[[a[0],a[1]]]+l[i+1:]
            else :
                l=l[:i-1]+[[a[0],b[1]]]+l[i+1:]
        else :
            i+=1
    return l
print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
