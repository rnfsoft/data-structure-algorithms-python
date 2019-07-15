"""
Given 2 array (assume no duplicates)
is 1 array a rotation of another - return/false
same size and elements but start index is different

BigO(n) we are going through each array 2x but O(2n) = O(n) since infinite sized lists,

select an indexed position in list1 and gets its value. Find same element in list2 and 
check index for index from there

if any variation then we know its false
Getting to last item without an false means True


"""



# print(rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))