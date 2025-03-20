def substr1(s,t):
    res = 0
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)]==t:
            res = i
            break
        else:
            res=-1
    return res
print(substr1("adbutsad","sad"))