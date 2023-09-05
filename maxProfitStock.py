def masProfit(l):
    low = l[0]
    maxi = 0
    lowIndex = 0
    for i in range(len(l)):
        if l[i]<low:
            low = l[i]
        maxi = max(maxi,l[i]-low)
    return maxi 
print(masProfit([7,1,5,3,6,4]))