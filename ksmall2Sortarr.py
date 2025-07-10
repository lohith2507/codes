def ksmall(l,s,k):
    p=[]
    for i in range(len(l)):
        for j in range(len(s)):
            p.append(l[i]*s[j])
    p.sort()
    print(p)
    return p[k]
print(ksmall([-4,-2,0,3],[2,4],6))