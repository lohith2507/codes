def hamming(n):
    c=0
    while (n>=1):
        if (n %2==0):
            n=n/2
        else:
            n=(n-1)/2
            c+=1
    return c
print(hamming(128))