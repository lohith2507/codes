def bomb(l,k):
    res=[]
    if k==0:
        return [0]*len(l)
    if k>0:
        while len(l)>k:
            res.append(max(l[:k]))
            l=l[k:]
        res.append(max(l))
    else:   
        while len(l)>abs(k):
            res.append(min(l[:abs(k)]))
            l=l[abs(k):]
        res.append(min(l))  
    return res