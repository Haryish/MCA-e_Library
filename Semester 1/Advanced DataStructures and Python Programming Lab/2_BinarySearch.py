def binarySearch(ar, start_index, r, srch):
    if r >= start_index:
        mid = start_index + (r-start_index)//2
        if ar[mid] == srch:
            return mid
        elif ar[mid] > srch:
            return binarySearch(ar, start_index, mid-1,srch)
        else:
            return binarySearch(ar, mid+1, r, srch)
    else:
        return -1
    
ar = [0,1,2,3,23]
srch = 23
output = binarySearch(ar, 0, len(ar), srch)
if output != -1:
    print("given element position is %d"%output)
else:
    print("Element does not exist in array")