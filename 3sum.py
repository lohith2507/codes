def tsum(l):
    res = []
    l.sort()  
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue  
        j, k = i + 1, len(l) - 1
        while j < k:
            total = l[i] + l[j] + l[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                res.append([l[i], l[j], l[k]])
                while j < k and l[j] == l[j + 1]:
                    j += 1  
                while j < k and l[k] == l[k - 1]:
                    k -= 1  
                j += 1
                k -= 1
    return res
print(tsum([-1, 0, 1, 2, -1, -4]))
