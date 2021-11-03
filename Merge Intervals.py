def merge(intervals):
    intervals.sort()
    result = [[]]
    result[0] = intervals[0]
        
    j = 0
    for i in intervals:
        if result[j][1] < i[0]:
            result.append(i)
            j = j + 1
        elif result[j][1] > i[1]:
            continue
        elif result[j][1] >= i[0] and result[j][1] < i[1]:
            result[j][1] = i[1]
        
    return result

a = [[1,2],[2,6],[8,10],[15,18]]
print(merge(a))
