def sum2(l,t):
    res = []
    d = {}
    for i in range(len(l)):
        if t-l[i] in d:
            res.append(d[t-l[i]])
            res.append(i)
            return res 
        d[l[i]]=i
    return res 
print(sum2([1,2,3,4,5,6,7],13))
