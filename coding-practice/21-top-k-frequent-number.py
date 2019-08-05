def top_k_frequent_number(nums, k):
    num_map = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for num in nums:
        num_map[num] += 1

    return sorted(num_map, key=num_map.get, reverse=True)[:k]

def top_k_frequent_number2(nums, k): # Time O(n), Space O(6+k+2) 
    num_map = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for num in nums:
        num_map[num] += 1

    result = []
    while k > 0:
        max_freq = max_key = 0
        for key in num_map:
            if num_map[key] > max_freq:
                max_freq = num_map[key]
                max_key = key
        result.append(max_key)
        del num_map[max_key]
        k -= 1

    return result

print(top_k_frequent_number2([3,2,3,1,2,5,3,6,2,4],2))