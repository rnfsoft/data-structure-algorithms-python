# https://www.daleseo.com/sort-quick/

# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return

#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)

#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low

#     return sort(0, len(arr) - 1)

# print(quick_sort([1, 5, 4, 3, 2, 7])

    