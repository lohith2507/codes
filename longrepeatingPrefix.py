def preCheck(l):
    if len(l)==1:
        return l[0]
    l.sort()
    res=""
    for i in range(len(l[0])):
        for j in range(len(l)-1):
            if l[j][i]!=l[j+1][i]:
                return res 
        res+=l[j][i]
    return res
print(preCheck(["flower","flow","flowght"]))