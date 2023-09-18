def lengthOfLongestSubstring(s):
    d={}
    l = 0
    res=0
    for i in range(len(s)):
        if s[i] in d:
            l = max(d[s[i]]+1,l)
        d[s[i]]=i 
        res = max(res,i-l+1)
    return res 
print(lengthOfLongestSubstring("pwwkew"))
