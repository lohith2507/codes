def minkcolors(s,k):
    mini = k
    for i in range(len(s)-k+1):
        print(s[i:i+k])
        if s[i:i+k].count("B") ==len(s[i:i+k]):
            return 0 
        elif s[i:i+k].count("W")<mini:
            print(s[i:i+k].count("B"),s[i:i+k])
            mini = k-s[i:i+k].count("B")
    return mini 
print(minkcolors("BWWWBB",6))
            
