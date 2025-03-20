def isHappy(n):
    r=0
    if n==1:
        return True
    else:
        for i in range(len(str(n))):
            temp=n
            temp=temp%(10**(i+1))
            r+=temp**2
        print(r)
        return isHappy(r)
print(isHappy(19))