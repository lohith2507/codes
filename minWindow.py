def minWindow(s,t):
    x=s
    minLen = []
    ls=s
    if len(t)>len(s):
        return ""
    else:
        for i in range(len(s)):
            for j in range(i,len(s)):
                c=0
                for k in range(len(t)):
                    if t[k] in s[i:j+1]:
                        c+=1 
                if len(t)==c:
                    print(s[i:j+1])
                    if len(s[i:j+1])<len(x):
                        x=s[i:j+1]
                        minLen.append(x)
    for i in range(len(minLen)):
        if (len(minLen[i]))<len(ls):
            ls = minLen[i]
    return ls
print(minWindow("a","b"))