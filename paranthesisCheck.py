def paraCheck(s):
    if len(s)%2!=0:
        return False 
    d = {"(":")","[":"]","{":"}"}
    res = []
    for i in s:
        if i in d.keys():
            res.append(i)
        else:
            if res == []:
                return False 
            x = res.pop()
            if i!=d[x]:
                return False 
    return res == []
print(paraCheck("()(){"))
