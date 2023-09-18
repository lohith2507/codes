height = [0,1,0,2,1,0,1,3,2,1,2,1]
def trappingWater(l):
    count=0
    leftArray = []
    rightArray = []
    leftMax = l[0]
    rightMax = l[len(l)-1]
    for i in range(len(l)):
        leftMax = max(leftMax,l[i])
        leftArray.append(leftMax)
        rightMax = max(rightMax,l[len(l)-i-1])
        rightArray.append(rightMax)
    rightArray = rightArray[::-1]
    for i in range(len(l)):
        if min(rightArray[i],leftArray[i])-l[i]>0:
            count += min(rightArray[i],leftArray[i])-l[i]
    return count
print(trappingWater(height))