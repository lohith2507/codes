def countGoodSubstrings(s):
    c=0
    for i in range(len(s)-3+1):
        print(s[i:i+3],set(list(s[i:i+3])))
        if len(s[i:i+3]) == len(set(list(s[i:i+3]))):
            c+=1 
    return c
# Example usage:
print(countGoodSubstrings("xyzzaz"))  # Output: 1   
print(countGoodSubstrings("aababcabc"))  # Output: 4
