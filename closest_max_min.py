lst = list(map(int, input().split()))
def  minMax(lst):
    minval = float('inf')
    maxval = float('-inf')
    for ele in lst:
        if ele > maxval:
            maxval = ele
        if ele < minval:
            minval = ele
    minval_Idx = -1
    maxval_Idx = -1
    min_len = len(lst) + 1
    for i in range(0, len(lst)):
        if lst[i] == minval:
            minval_Idx = i
            if maxval_Idx >= 0:
               min_len = min(min_len, minval_Idx - maxval_Idx + 1)
        elif(lst[i] == maxval):
             maxval_Idx = i
             if minval_Idx >= 0:
                min_len = min(min_len, maxval_Idx - minval_Idx + 1)
    return min_len
print(minMax([1, 3, 2]))
print(minMax([2, 6, 1, 6, 9]))
print(minMax(lst))
