def mindiffhl(l,k):
    mini = 0
    i,j=0,1 
    l.sort()
    if len(l) < k:
        return 0
    while j < len(l):
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            mini = min(mini, l[j] - l[i]) if mini != 0 else l[j] - l[i]
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    return mini if mini != 0 else 0
# Example usage:
print(mindiffhl([90],1))
print(mindiffhl([9,4,1,7],2 ))  