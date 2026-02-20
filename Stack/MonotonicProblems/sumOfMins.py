def findSumSubarrayMins(nums):
    '''
    Initialize a variable to hold the total sum, starting from 0
    Start a loop to fix the starting index of the subarray
    Initialize a variable to keep track of the minimum element in the current subarray
    Use an inner loop to extend the subarray to the right
    Update the minimum element as the subarray grows
    Add the current minimum to the total sum
    Repeat this process for all possible subarrays
    Return the total sum after all subarrays are processed
    '''
    n = len(nums)

    mod = int(1e9 + 7)

    total_sum = 0
    
    for i in range(n):
        
        mini = nums[i]

        for j in range(i, n):
            mini = min(nums[j], mini)

            total_sum = (total_sum + mini) % mod
        
    return total_sum

if __name__ == "__main__":
   arr = [3, 1, 2, 5]
   print("Output: ", findSumSubarrayMins(arr))