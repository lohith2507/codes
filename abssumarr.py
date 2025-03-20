def abssum(l):
    def kadane(l):
        s=0 
        maxi=0 
        for i in range(len(l)):
            s+=l[i]
            maxi = max(s,maxi)
            if s<0:
                s=0
        return maxi
    s = [-x for x in l]
    x = kadane(l)
    y = kadane(s)
    return max(x,y)
print(abssum([2,-5,1,-4,3,-2]))
