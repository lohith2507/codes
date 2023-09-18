def largestNumber(l):
    def large(a,b):
        if int(str(a)+str(b)) > int(str(b)+str(a)):
            return True
        else:
            return False
    for i in range(len(l)):
        for j in range(i,len(l)):
            if large(l[i],l[j]):
                pass 
            else:
                l[i],l[j]=l[j],l[i]
    return str(int("".join(map(str,l))))
print(largestNumber([3,30,34,5,9]))