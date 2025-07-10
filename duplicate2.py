def dup2(l, k):
    seen = set()
    for i, num in enumerate(l):
        if num in seen:
            return True
        seen.add(num)
        if i >= k:
            seen.remove(l[i - k])
    return False

print(dup2([1,2,3,1],3))  
print(dup2([1,0,1,1],1))     
print(dup2([1,2,3,1,2,3],2))  

            
