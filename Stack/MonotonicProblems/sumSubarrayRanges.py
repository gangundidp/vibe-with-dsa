def sumSubarrayRanges(nums):
    n = len(nums)
    total_sum = 0
    
    for i in range(n):
        start = nums[i]
        for j in range(i, n):
            end = nums[j]
            
            total_sum += abs(start - end)
        
    return total_sum

nums = [1, 2, 3]
print("Output: ", sumSubarrayRanges(nums))