"""

Common Elements in Two Sorted Arrays
return the common elements (as an array) between two sorted arrays of integers(ascending order)
Example: The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] are [1, 4, 9]

"""

# def common_elements(a,b):
#     p1 = 0
#     p2 = 0

#     result = []
#     count = 0
#     while p1 < len(a) and p2 < len(b):
        
#         if a[p1] == b[p2]:
#             result.append(a[p1])
#             p1 +=1
#             p2 +=2

#         elif a[p1] > b[p2]:
#             p2 += 1

#         else:
#             p1 += 1
#         count += 1
    
#     print(count)
#     return result

def common_elements(a, b):
    # count = 0
    # result = []
    # for x in a:
    #     for y in b:
    #         if x == y:
    #             result.append(x)
    #         else:
    #             continue
    #         count += 1
    # print(count)
    # return result

    return [x for x in a for y in b if x == y]
print(common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]))