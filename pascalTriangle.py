def fact(n):
    if n<=0:
        return 1 
    else:
        return n*fact(n-1)
def nCr(n,r):
    return fact(n)//(fact(n-r)*fact(r))
def pascalTriangle(n):
    for i in range(n):
        for k in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(nCr(i,j),end=" ")
        print(" ")
pascalTriangle(5)