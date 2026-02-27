class Solution:
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
    print("Output: ", sol.numSubarraysWithSum(nums, goal)) 
