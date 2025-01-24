def rev(s):
    l = s.split()[::-1]
    r = ""
    for i in range(len(l)):
        r+=l[i]+" "
    return r.strip()
print(rev("a good   example"))