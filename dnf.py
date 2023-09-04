l = [0,1,1,0,1,2,1,2,1,1,1,1,0]
def sort012(l):
    low = 0
    mid = 0
    high = len(l)-1
    for i in range(len(l)):
        if l[mid]==0:
            l[low],l[mid] = l[mid],l[low]
            low+=1
            mid+=1 
        elif l[mid]==1:
            mid+=1 
        else:
            l[high],l[mid] = l[mid],l[high]
            high-=1 
    return l
print(sort012(l))
