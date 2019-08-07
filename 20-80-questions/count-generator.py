# https://www.geeksforgeeks.org/find-the-number-of-elements-greater-than-k-in-a-sorted-array/
def count_generator(arr, n, k):

    l = 0
    r = n - 1

    left_greater = n

    while (l <= r):
        m = int(l + (r - l) / 2) 
        if (arr[m] > k):
            left_greater = m
            r = m - 1
        else:
            l = m + 1

    return (n - left_greater)


arr = [3, 3, 4, 7, 7, 7, 11, 13, 13] 
n = len(arr) 
k = 7

print(count_generator(arr, n, k)) 