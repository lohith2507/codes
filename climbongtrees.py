def climbs(n):
    l,s = 1,1 
    for i in range(n-1):
        t=l
        l=l+s
        s=t
    return l
print(climbs(4))