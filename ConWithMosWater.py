def contwithmoswat(h):
    maxArea = 0
    for i in range(len(h)):
        for j in range(len(h)):
            maxArea = max(maxArea, min(h[i],h[j])*(i-1))
    return maxArea
print(contwithmoswat([1,8,6,2,5,4,8,3,7]))

        
