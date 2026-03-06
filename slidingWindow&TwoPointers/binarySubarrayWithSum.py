class Solution:
    def numSubarraysWithSumBrute(self, nums, goal):
        count = 0
        for i in range(len(nums)):
            sum = 0
            
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == goal:
                    count += 1
                elif sum < goal:
                    continue
                else:
                    break
                
        return count
    
    def numSubarraysWithSumBetter(self, nums, goal):
        prefix_sum_count = {0: 1}

        count = 0
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            
            # Check if (curr_sum - goal) exists in prefix map
            if (curr_sum - goal) in prefix_sum_count:
                count += prefix_sum_count[curr_sum - goal] 
            
            # Update prefix sum frequency
            prefix_sum_count[curr_sum] = prefix_sum_count.get(curr_sum, 0) + 1

        return count

            
        
    def numSubarraysWithSum(self, nums, goal):
        # Return difference between atMost(goal) and atMost(goal - 1)
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)

    def atMost(self, nums, k):
        if k < 0:
            return 0

        left = 0
        total = 0
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            # Shrink window if sum exceeds k
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            # Add number of valid subarrays ending at right
            total += (right - left + 1)

        return total

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print("Output: ", sol.numSubarraysWithSumBrute(nums, goal)) 
    print("Output: ", sol.numSubarraysWithSumBetter(nums, goal)) 
    print("Output: ", sol.numSubarraysWithSum(nums, goal)) 
    
    nums = [0, 0, 0, 0, 0, 0]
    goal = 0
    print("Output: ", sol.numSubarraysWithSumBrute(nums, goal)) 
    print("Output: ", sol.numSubarraysWithSumBetter(nums, goal)) 
    print("Output: ", sol.numSubarraysWithSum(nums, goal)) 
    
    nums = [1, 0, 0, 1, 1, 0]
    goal = 2
    print("Output: ", sol.numSubarraysWithSumBrute(nums, goal)) 
    print("Output: ", sol.numSubarraysWithSumBetter(nums, goal)) 
    print("Output: ", sol.numSubarraysWithSum(nums, goal)) 
