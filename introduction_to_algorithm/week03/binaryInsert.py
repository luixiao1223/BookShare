"""
#有序数列存在
def binaryInsert(series,a):
    low = 0
    high = len(series) - 1
    m = (low + high)//2
    while low < high:
        if series[m] > a:
            high = m - 1
        elif series[m] < a:
            low = m + 1
        else:
            high = m
        m = (low + high)//2
    series.insert(high+1,a)

l = sorted([2,4,7,3,9,1,5,6,9])
binaryInsert(l,5)
print(l)
"""



# 有序数列不存在
def binaryInsert(series, a):
    for i in range(0, len(series)):
        low = 0
        high = len(a) - 1
        m = (low + high) // 2
        while low <= high:
            if a[m] > series[i]:
                high = m - 1
            elif a[m] < series[i]:
                low = m + 1
            else:
                high = m
            m = (low + high) // 2
        if len(a) != 1:
            a.insert(high + 1, series[i])
        else:
            if a[0] > series[i]:
                a.insert(0, series[i])
            else:
                a.insert(1, series[i])


a = []
l = [2, 4, 7, 3, 10, 1, 5, 6, 9]
binaryInsert(l, a)
print(a)
