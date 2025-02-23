def mergeIntervals(intervals):
    intervals.sort(key=lambda x:x[0])
    i=1
    if len(intervals)==1 :
        return intervals
    while i<len(intervals) :
        a=intervals[i-1]
        b=intervals[i]
        if a[1]>=b[0] :
            if a[1]>b[1] :
                intervals=intervals[:i-1]+[[a[0],a[1]]]+intervals[i+1:]
            else :
                intervals=intervals[:i-1]+[[a[0],b[1]]]+intervals[i+1:]
        else :
            i+=1
    return intervals
print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
