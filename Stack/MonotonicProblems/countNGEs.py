def countNGEs(nums, indices):
    ans = []
    
    for i in indices:
        count = 0
        j = i + 1
        while j < len(nums):
            if nums[j] > nums[i]:
                count += 1
            j += 1
        
        ans.append(count)
        
    return ans

nums = [1, 2, 3, 4, 1]
indices = [0, 3]
print("output: ", countNGEs(nums, indices))
    
nums = [3, 4, 2, 7, 5, 8, 10, 6]
indices = [0, 5]
print("output: ", countNGEs(nums, indices))
    
        