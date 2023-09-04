def maxSubarrySum(l):
    s=0 
    maxi=0 
    for i in range(len(l)):
        s+=l[i]
        maxi = max(s,maxi)
        if s<0:
            s=0
    return maxi 
print(maxSubarrySum([1,2,-2,-3,4,-1,-2,1,5,-1,3,-3]))