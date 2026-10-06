# Made By Ricky L. 

def count(list, value):
    fIndex = findstart(list, value)
    if fIndex == -1:
        return 0
    return findend(list, value)-fIndex+1


def findstart(list, value):
    lo, hi = 0, len(list)-1
    result = -1
    while lo <= hi:
        mid = (lo+hi)//2
        if list[mid] == value:
            result = mid
            hi = mid-1
        elif list[mid] > value:
            hi = mid-1
        else:
            lo = mid+1

    return result


def findend(list, value):
    lo, hi = 0, len(list)-1
    result = -1
    while lo <= hi:
        mid = (lo+hi)//2
        if list[mid] == value:
            result = mid
            lo = mid+1
        elif list[mid] > value:
            hi = mid-1
        else:
            lo = mid+1

    return result
