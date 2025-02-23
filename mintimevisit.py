import math
def mintimevisit(l):
    time = 0
    for i in range(len(l)-1):
        x = max(abs(l[i][1]-l[i+1][1]),abs(l[i][0]-l[i+1][0]))
        time+=x 
    return time
print(mintimevisit( [[1,1],[3,4],[-1,0]]))  


