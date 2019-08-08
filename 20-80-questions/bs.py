def BS(arr, x): 
    l = 0
    r = len(arr) - 1
    while l <= r: 
        mid = int(l + (r - l)/2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1


print(BS([ 2, 3, 4, 10, 40] , 50))