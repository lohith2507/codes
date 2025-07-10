def findLHS(l):   
    count = {}
    for num in l:
        count[num] = count.get(num, 0) + 1
    max_length = 0
    for num in count:
        if num + 1 in count:
            max_length = max(max_length, count[num] + count[num + 1])
    return max_length
# Example usage:
print(findLHS([1,3,2,2,5,4,3,7,8,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]))
print(findLHS([1,2,3,4]))       
print(findLHS([1,1,1,1]))
print(findLHS([1,2,3,4,5,6,7,8,9,10]))