def params(s):
    c=0
    l=[-1]
    for i in range(len(s)):
        if s[i] == "(":
            l.append(i)
        else:
            l.pop()
            if len(l)==0:
                l.append(i)
            else:
                c=max(c,i-l[-1])
    return c
               

